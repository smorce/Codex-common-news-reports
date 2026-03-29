#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional

import torch
from fast_bunkai import FastBunkai
from transformers import AutoModelForTokenClassification, AutoTokenizer


@dataclass
class SentenceSpan:
    text: str
    start: int
    end: int
    separator_score: float = 0.0


class FastBunkaiChonkyChunker:
    """
    セマンティックチャンキングを行うためのクラス。
    FastBunkai で文分割し、Chonky の separator 予測で
    文同士を意味的にまとまったチャンクへ束ねる。

    入力テキストはデフォルトで normalize_newlines により
    改行・連続空行をある程度整える（chunk / debug の前に適用）。
    """

    def __init__(
        self,
        model_name: str = "mirth/chonky_mmbert_small_multilingual_1",
        threshold: float = 0.55,
        max_length: int = 1024,
        stride: int = 128,
        min_sentences_per_chunk: int = 1,
        max_chunk_tokens: Optional[int] = None,
        device: Optional[str] = None,
        normalize_input: bool = True,
        max_consecutive_blank_lines: int = 1,
        strip_line_trailing_spaces: bool = True,
        merge_soft_linebreaks: bool = False,
        normalize_chunk_output: bool = False,
    ) -> None:
        self.model_name = model_name
        self.threshold = threshold
        self.max_length = max_length
        self.stride = stride
        self.min_sentences_per_chunk = min_sentences_per_chunk
        self.max_chunk_tokens = max_chunk_tokens
        self.normalize_input = normalize_input
        self.max_consecutive_blank_lines = max_consecutive_blank_lines
        self.strip_line_trailing_spaces = strip_line_trailing_spaces
        self.merge_soft_linebreaks = merge_soft_linebreaks
        self.normalize_chunk_output = normalize_chunk_output

        self.device = device or self._detect_device()

        self.bunkai = FastBunkai()
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            model_max_length=max_length,
        )
        if not getattr(self.tokenizer, "is_fast", False):
            raise RuntimeError(
                "offset_mapping が必要なので fast tokenizer が必要です。"
            )

        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

        # label2id はモデル側設定を優先。無ければ model card の定義にフォールバック
        label2id = getattr(self.model.config, "label2id", {}) or {}
        self.separator_label_id = label2id.get("separator", 1)

    @staticmethod
    def _detect_device() -> str:
        if torch.cuda.is_available():
            return "cuda"
        if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
            return "mps"
        return "cpu"

    @staticmethod
    def _collapse_long_newline_runs(text: str, max_consecutive_blank_lines: int) -> str:
        """
        連続する \\n を上限に合わせて短くする。
        max_consecutive_blank_lines=n のとき、段落あいだの「空行」は n 行までなので、
        \\n の連続は最大 n+1 個まで（n=0 なら改行は1つにまとめる）。
        """
        if max_consecutive_blank_lines <= 0:
            return re.sub(r"\n{2,}", "\n", text)
        limit = max_consecutive_blank_lines + 2
        replacement = "\n" * (max_consecutive_blank_lines + 1)
        return re.sub(rf"\n{{{limit},}}", replacement, text)

    @staticmethod
    def normalize_newlines(
        text: str,
        *,
        max_consecutive_blank_lines: int = 1,
        strip_line_trailing_spaces: bool = True,
        merge_soft_linebreaks: bool = False,
    ) -> str:
        """
        改行・空白をある程度そろえる。
        - CRLF / 単独 CR を LF に
        - 行末の空白を除去（任意）
        - 連続する空行を max_consecutive_blank_lines 回までに抑える（空白・タブのみの行も空行扱い）
        - 改行の長い連続は _collapse_long_newline_runs で再度抑える（行分割の取りこぼし対策）
        - merge_soft_linebreaks: 段落区切り（空行）以外の単独改行を空白に置換（コピペの折り返し対策）
        """
        if not text:
            return ""
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = text.replace("\u2028", "\n").replace("\u2029", "\n")
        lines = text.split("\n")
        # 空白・タブのみの行も空行として数える（連続空行の圧縮が途切れないようにする）
        if strip_line_trailing_spaces:
            lines = [ln.rstrip() for ln in lines]
        normalized_lines: List[str] = []
        for ln in lines:
            if not ln.strip():
                normalized_lines.append("")
            else:
                normalized_lines.append(ln)

        max_blank = max(0, max_consecutive_blank_lines)
        out: List[str] = []
        blank_streak = 0
        for ln in normalized_lines:
            if ln == "":
                blank_streak += 1
                if blank_streak <= max_blank:
                    out.append("")
            else:
                blank_streak = 0
                out.append(ln)

        while out and out[0] == "":
            out.pop(0)
        while out and out[-1] == "":
            out.pop()

        text = "\n".join(out)
        # 行単位処理で取りこぼした「改行の連続」をまとめて抑える（max_blank=n なら \n を最大 n+1 連続まで）
        text = FastBunkaiChonkyChunker._collapse_long_newline_runs(
            text, max_consecutive_blank_lines
        )
        if merge_soft_linebreaks:
            text = re.sub(r"(?<=[^\n])\n(?=[^\n])", " ", text)
        return text

    def _maybe_normalize(self, text: str) -> str:
        if not self.normalize_input:
            return text
        return self.normalize_newlines(
            text,
            max_consecutive_blank_lines=self.max_consecutive_blank_lines,
            strip_line_trailing_spaces=self.strip_line_trailing_spaces,
            merge_soft_linebreaks=self.merge_soft_linebreaks,
        )

    def _maybe_normalize_chunk(self, chunk: str) -> str:
        if not self.normalize_chunk_output:
            return chunk
        return self.normalize_newlines(
            chunk,
            max_consecutive_blank_lines=self.max_consecutive_blank_lines,
            strip_line_trailing_spaces=self.strip_line_trailing_spaces,
            merge_soft_linebreaks=self.merge_soft_linebreaks,
        )

    def split_sentences(self, text: str) -> List[SentenceSpan]:
        """
        FastBunkai が返す各文を、元テキスト中の char span に対応付ける。
        """
        raw_sentences = [s for s in self.bunkai(text) if s and s.strip()]
        if not raw_sentences:
            stripped = text.strip()
            return [SentenceSpan(stripped, 0, len(text))] if stripped else []

        spans: List[SentenceSpan] = []
        cursor = 0

        for sent in raw_sentences:
            idx = text.find(sent, cursor)
            if idx == -1:
                raise ValueError(
                    f"文の位置合わせに失敗しました: {sent!r}\n"
                    "FastBunkai の出力と元文字列の対応が取れません。"
                )
            start = idx
            end = idx + len(sent)
            spans.append(SentenceSpan(text=sent, start=start, end=end))
            cursor = end

        return spans

    def _token_separator_scores(self, text: str) -> List[Tuple[int, int, float]]:
        """
        元テキスト上の各 token span に対して separator 確率を返す。
        長文は stride 付きでスライディングウィンドウ推論する。
        """
        encoded = self.tokenizer(
            text,
            truncation=True,
            max_length=self.max_length,
            stride=self.stride,
            return_overflowing_tokens=True,
            return_offsets_mapping=True,
            return_special_tokens_mask=True,
        )

        # overlap した token span は max で集約
        span2score: Dict[Tuple[int, int], float] = {}

        with torch.no_grad():
            num_windows = len(encoded["input_ids"])
            for i in range(num_windows):
                input_ids = torch.tensor(
                    [encoded["input_ids"][i]], dtype=torch.long, device=self.device
                )
                attention_mask = torch.tensor(
                    [encoded["attention_mask"][i]], dtype=torch.long, device=self.device
                )

                logits = self.model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                ).logits[0]  # [seq_len, num_labels]

                probs = torch.softmax(logits, dim=-1)[:, self.separator_label_id]
                probs = probs.detach().cpu().tolist()

                offsets = encoded["offset_mapping"][i]
                special_mask = encoded["special_tokens_mask"][i]

                for (start, end), is_special, prob in zip(offsets, special_mask, probs):
                    if is_special or start == end:
                        continue
                    key = (start, end)
                    prev = span2score.get(key, 0.0)
                    if prob > prev:
                        span2score[key] = float(prob)

        return [(s, e, p) for (s, e), p in span2score.items()]

    def _attach_sentence_scores(self, text: str, sentences: List[SentenceSpan]) -> List[SentenceSpan]:
        """
        各 sentence に対して、
        その sentence 内にある token の separator 最大確率を割り当てる。
        """
        token_scores = self._token_separator_scores(text)

        for sent in sentences:
            sent.separator_score = max(
                (
                    score
                    for tok_start, tok_end, score in token_scores
                    if tok_start < sent.end and tok_end > sent.start
                ),
                default=0.0,
            )
        return sentences

    def _sentence_token_counts(self, text: str, sentences: List[SentenceSpan]) -> List[int]:
        """
        max_chunk_tokens 用の概算 token 数。
        """
        token_scores = self._token_separator_scores(text)
        counts = []
        for sent in sentences:
            n = sum(
                1
                for tok_start, tok_end, _ in token_scores
                if tok_start < sent.end and tok_end > sent.start
            )
            counts.append(max(n, 1))
        return counts

    def chunk(self, text: str) -> List[str]:
        text = self._maybe_normalize(text)
        sentences = self.split_sentences(text)
        if not sentences:
            return []

        sentences = self._attach_sentence_scores(text, sentences)
        sentence_token_counts = self._sentence_token_counts(text, sentences)

        chunks: List[str] = []

        chunk_start = sentences[0].start
        chunk_sent_count = 0
        chunk_token_count = 0

        for i, sent in enumerate(sentences):
            chunk_sent_count += 1
            chunk_token_count += sentence_token_counts[i]

            is_last = i == len(sentences) - 1
            if is_last:
                continue

            score_based_split = (
                sent.separator_score >= self.threshold
                and chunk_sent_count >= self.min_sentences_per_chunk
            )

            size_based_split = False
            if self.max_chunk_tokens is not None and chunk_token_count >= self.max_chunk_tokens:
                size_based_split = True

            if score_based_split or size_based_split:
                chunk_text = self._maybe_normalize_chunk(
                    text[chunk_start:sent.end].strip()
                )
                if chunk_text:
                    chunks.append(chunk_text)

                chunk_start = sentences[i + 1].start
                chunk_sent_count = 0
                chunk_token_count = 0

        # tail
        tail_text = self._maybe_normalize_chunk(
            text[chunk_start:sentences[-1].end].strip()
        )
        if tail_text:
            chunks.append(tail_text)

        return chunks

    def debug(self, text: str) -> List[dict]:
        """
        文ごとの separator_score を確認したいとき用。
        """
        text = self._maybe_normalize(text)
        sentences = self.split_sentences(text)
        sentences = self._attach_sentence_scores(text, sentences)
        return [
            {
                "sentence": s.text,
                "start": s.start,
                "end": s.end,
                "separator_score": round(s.separator_score, 4),
            }
            for s in sentences
        ]


if __name__ == "__main__":

    text = """「自分は見た目がいい」と思っている従業員は職場で発言しやすいという研究結果

教室や職場の人間関係について考えている時、「見た目がいい人の方が発言権が強いのではないか」と感じたことがあるかもしれません。韓国の研究では、自分の容姿に自信を持っている従業員は職場で積極的に発言し、アイデアを共有する可能性が高いという研究結果が示されました。

I'm attractive, so i speak up: a moderated-mediation model of self-perceived attractiveness, perceived impact, and voice | Current Psychology | Springer Nature Link
https://link.springer.com/article/10.1007/s12144-025-08537-w

Employees who feel attractive are more likely to share ideas at work
https://www.psypost.org/employees-who-feel-attractive-are-more-likely-to-share-ideas-at-work/

これまでの研究では、外見的な魅力が昇進や収入などの点で有利に働くことが示唆されています。しかし、自分の外見に対する認識が、職場においてどのような心理的作用をもたらすのかという点は、あまり研究されてこなかったとのこと。

現代社会の職場は人に見られる機会が多く、絶え間ない他者との交流が求められます。そのため、韓国・ソウル大学の博士課程に在籍するリ・ヒョンジョン氏らの研究チームは、自分の外見を魅力的だと思うかどうかが、心理的なリソースとして機能するのかどうかを調べることにしました。

ヒョンジョン氏は、「私たちは『単に自分が魅力的だと感じるだけで、職場で発言しやすくなるのだろうか？』という、シンプルながらも興味深い疑問から始めました」「韓国では、外見は特に強い社会的意味合いを持ちます。この分野で研究を行う人間として、私たちはこうした力学が日常生活においていかに顕著であり、重大な影響を及ぼし得るのかを頻繁に目にしています」と述べています。

研究チームは今回の研究で、従業員が自分の外見を魅力的だと思うことが、組織心理学者らが「Employee voice(従業員の声)」と呼ぶものにつながるかどうかを調べました。従業員の声とは、組織改善を目的としたアイデア・提案・懸念を自発的に表明することを指します。職場で意見を述べることには潜在的なリスクがあるため、一般に従業員は自分の意見が尊重されるかどうかを慎重に検討し、意見を共有するかどうかを決定します。



研究チームは、韓国の正社員153人を対象にアンケート調査を行いました。被験者は製造業・小売業・情報技術といったさまざまな分野で働いており、男性が44％、平均年齢は39歳であり、大多数が大学の学位を取得していました。

アンケートに伴うバイアスを排除するため、被験者は2段階のアンケートを実施しました。1つ目のアンケートでは、従業員に対して自分の身体的魅力を評価してもらった上で、「instrumentality(外見の媒介性)」に関する質問に答えてもらいました。外見の媒介性とは、「身体的魅力は社会で成功するために役立つ社会的価値として機能する」という信念を表す言葉です。



1つ目のアンケートから1週間後、被験者は自身の影響力を評価する2つ目のアンケートに答えました。ここでは「自分の意見が有意義な変化をもたらし、他者から真剣に受け止められていると思うか」といった質問が投げかけられたほか、「従業員の声」をどれほどの頻度で発信しているのかも問われました。

データを分析した結果、被験者が自分の外見を魅力的だと評価することが、職場での発言意欲を高めていることがわかりました。つまり、自分の外見を高評価している人ほど職場での影響力も強いと感じており、その結果として積極的な提案や抑止的な声を発信する可能性が高まったということです。



しかし、この傾向はすべての被験者に当てはまるわけではなく、外見の高評価が発言意欲につながるのは、外見の媒介性を重視している従業員に限られました。外見が社会的成功においてあまり重要ではないと考えている従業員は、外見の評価が自分の影響力やアイデアを共有する意欲にあまり関係していませんでした。



リ氏は心理学系メディアのPsyPostに、「自分の容姿を魅力的だと評価する人は、職場でより自信を持って提案する傾向があります。しかし、この傾向はすべての人に同じように当てはまるわけではありません」「重要なのは容姿そのものではなく、容姿が影響力をもたらすという信念であり、それが人々の影響力への自信を高め、発言する可能性を高めるのです」とコメントしました。

今回の研究で興味深い点として、外見の評価と発言の意欲との関係性は男女ともに見られたということが挙げられます。これまでの心理学研究では、一般に女性では男性よりも外見の社会的価値が大きいと示されてきたため、この結果は意外だったとのこと。



研究チームは今回の研究結果について、「出世のためには身だしなみを整えるための時間と資金が必要だ」と読み取るべきではなく、むしろ「職場が意図せずに個人の影響力を外見と結びつけてしまっている」ことを浮き彫りにしていると主張。リ氏は、「私たちの研究は、成功するためには外見にもっと投資するべきだと示唆しているわけではありません」「より根本的な問題は、個人がいかにして外見を良くするかではなく、職場がどうやって自信や影響力が意図せず外見と結びつかないようにするかということです」と述べました。"""

    chunker = FastBunkaiChonkyChunker(
        threshold=0.55,              # 日本語では要調整
        min_sentences_per_chunk=1,
        max_chunk_tokens=300,        # RAG 用なら上限を持たせると扱いやすい
    )

    print("=== sentence scores ===")
    for row in chunker.debug(text):
        print(f"{row['separator_score']:.4f}\t{row['sentence']}")

    print("\n=== chunks ===")
    for i, chunk in enumerate(chunker.chunk(text), 1):
        print(f"[chunk {i}] {chunk}")
