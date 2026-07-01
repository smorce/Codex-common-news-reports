# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-07-01T09:00:00+09:00
- Articles: 3

## I generated a research podcast using Claude Opus and it embarrassed every NotebookLM episode I'd saved
- Date: 2026-06-18T07:00:00-04:00

### Executive Summary
- NotebookLM の Audio Overview は、資料に基づく個人化ポッドキャストとして便利だが、長く使うと構成や掛け合いが定型化して聞こえる。
- 筆者は単調さの主因を、脚本を生成する基盤モデルの文体やリズムにあると見ている。
- Open Notebook はセルフホスト型の NotebookLM 代替で、言語モデル、埋め込みモデル、音声合成モデルを利用者が選べる。
- 実験では Claude Opus 4.8 を脚本生成に使い、OpenAI の text-embedding-3-small と tts-1 を周辺処理に組み合わせた。
- 80ページの博士論文を素材に、4セグメント構成、31行の対話、20分の音声エピソードが生成された。
- 生成時間は約18分で、脚本自体は約2分、残りは主に音声レンダリングだった。
- 結果は NotebookLM より詳細で予測しにくく、専門家らしい掘り下げがあると評価されている。
- 一方で Docker、API キー、モデル設定が必要で、手軽さでは NotebookLM に劣る。
- 費用は 20 分のエピソード 1 本で約 0.82 ドルであり、無料ではないが品質改善の対価として筆者は妥当と見ている。

### Key Findings
- NotebookLM の音声概要は、反復利用で構成や言い回しの定型化が目立つ。 [^]
  - Footnote: 記事では、毎回似た構成、ホスト間の同じ応答、同じような転換句や締め方が現れると説明している。
- NotebookLM では脚本を作るモデルを利用者が選べないため、文体の単調さを根本的に変えにくい。 [^]
  - Footnote: 筆者は問題を基盤モデルの「個性」に絞り込み、NotebookLM は Gemini を使い、モデル選択肢を提供しないと述べている。
- Open Notebook はローカル実行可能なオープンソース代替で、プライバシー面と柔軟性が強みになる。 [^]
  - Footnote: 記事では Docker で自分のマシン上に立ち上げ、PDF、リンク、テキスト、YouTube、PowerPoint などを扱えると説明している。
- Open Notebook は処理段階ごとにモデルを選択できる。 [^]
  - Footnote: 言語モデル、埋め込みモデル、TTS モデルを選べ、Anthropic、OpenAI、Google、xAI などの API キーやローカル LLM を利用できると記載されている。
- 実験構成では Claude が思考と脚本を担い、OpenAI が埋め込みと音声合成を担った。 [^]
  - Footnote: 筆者は Claude Opus 4.8、OpenAI text-embedding-3-small、OpenAI tts-1 の組み合わせを使ったと説明している。
- 生成プロセスはアウトライン、脚本、音声化の段階に分かれていた。 [^]
  - Footnote: Opus が4セグメントのアウトラインを作り、31行の対話に展開し、その後 tts-1 が各行を音声化して結合したとある。
- 20分のエピソード生成に約18分かかり、遅延の主因は音声レンダリングだった。 [^]
  - Footnote: 記事では脚本生成は約2分で、残り16分は Open Notebook が音声を逐次バッチ処理した時間だと説明している。
- 費用は 1 本あたり約 0.82 ドルで、無料利用にはローカルモデルとローカル TTS が必要になる。 [^]
  - Footnote: Anthropic クレジットが0.68ドル、OpenAI TTS が0.14ドル、合計約0.82ドルだったと記載されている。

### References
- https://www.makeuseof.com/generated-a-research-podcast-using-claude-opus-embarrassed-every-notebooklm-episode/

## Leanstral 1.5 - Mistral AI | Mistral Docs
- Date: 2026-06-30T00:00:00+00:00

### Executive Summary
- Leanstral 1.5 は Mistral AI のモデルカードで公開された Lean 4 向けの形式証明エンジニアリングモデルである。
- 用途は自動定理証明と自動形式化に最適化されている。
- モデルは総パラメータ 1190 億、アクティブパラメータ 65 億と示されている。
- 提供名は labs-leanstral-1-5 で、Labs 系モデルとして扱われている。
- コンテキスト長は 256k と記載されており、長い証明文脈や仕様を扱う用途を想定している。
- 価格は 0 ドルと表示され、モデルカード上では無料利用可能な位置づけになっている。
- 対応機能一覧には Chat Completions、Function Calling、Agents & Conversations、Structured Outputs などが並ぶ。
- ドキュメント上の公開日は 2026 年 6 月 30 日である。

### Key Findings
- Leanstral 1.5 は Lean 4 の形式証明作業に特化した更新版モデルである。 [^]
  - Footnote: モデルカードには、Lean 4 formal proof engineering model として、自動定理証明と自動形式化向けに最適化されたと書かれている。
- モデル規模は総 119B パラメータ、アクティブ 6.5B パラメータである。 [^]
  - Footnote: 本文冒頭に 119B total parameters, 6.5B active と明記されている。
- API でのモデル識別子は labs-leanstral-1-5 である。 [^]
  - Footnote: モデルカードの概要欄に labs-leanstral-1-5 と表示されている。
- コンテキスト長は 256k で、大きな形式化作業に向いた仕様である。 [^]
  - Footnote: 性能欄の CONTEXT に 256k と表示されている。
- 価格欄は 0 ドルである。 [^]
  - Footnote: モデルカードの PRICE 欄に $0 と表示されている。
- Chat Completions と Function Calling に対応する。 [^]
  - Footnote: Features には Chat Completions /v1/chat/completions と Function Calling /v1/chat/completions が列挙されている。
- Agents & Conversations や Structured Outputs など、エージェント的な利用や構造化出力にも対応する。 [^]
  - Footnote: Features には Agents & Conversations、Built-In Tools、Structured Outputs、Predicted Outputs、Prefix などが並んでいる。
- 公開日は 2026 年 6 月 30 日である。 [^]
  - Footnote: ページ上部に June 30, 2026 と表示されている。

### References
- https://docs.mistral.ai/models/model-cards/leanstral-1-5-26-06

## From Brain Waves to Words: Brain2Qwerty Offers a New Path to Communication Without Surgery
- Date: 2026-06-29T00:00:00+00:00

### Executive Summary
- Meta は非侵襲の脳活動記録から文章を復元する Brain2Qwerty v2 を発表した。
- この研究は、外科的インプラントなしで脳活動をテキストへ復号する方向の進展として位置づけられている。
- Brain2Qwerty v2 はリアルタイム文復号が可能なエンドツーエンドパイプラインとして説明されている。
- 学習には 9 名のボランティアから約 22,000 文、各 10 時間の MEG 記録が使われた。
- 手作業で設計した神経イベント検出ではなく、生の脳信号から直接復号する深層学習方式を採用している。
- 大規模言語モデルを神経データで微調整し、ノイズの多い記録と一貫した言語の間を意味的文脈で補っている。
- v2 は単語精度 61% を達成し、他の非侵襲手法の 8% から大きく改善した。
- 最良の参加者では単語精度 78% に達し、半数超の文が 1 語以下の誤りで復号された。
- Meta はコードとデータ公開を通じ、神経科学と医療応用の研究加速を狙っている。

### Key Findings
- Brain2Qwerty v2 は手術不要の脳活動テキスト復号を目指す研究の最新版である。 [^]
  - Footnote: Meta は前年の v1 に続き、外科的インプラントなしで脳活動をテキストに復号する次段階として v2 を紹介している。
- v2 は非侵襲記録からリアルタイムに文を復号する高性能エンドツーエンドパイプラインとされる。 [^]
  - Footnote: 記事では highest-performing end-to-end pipeline capable of real-time sentence decoding from non-invasive brain recordings と説明されている。
- 研究は、意思疎通を妨げる脳損傷を持つ人々への応用可能性を意識している。 [^]
  - Footnote: Meta は、コミュニケーションを妨げる脳病変に苦しむ数百万人に違いを生む可能性があると述べている。
- 学習データは 9 名、約 22,000 文、各 10 時間の MEG 記録から構成された。 [^]
  - Footnote: 記事には nine volunteer participants、approximately 22,000 sentences、each recorded for 10 hours、MEG device と記載されている。
- 復号は手作業の特徴抽出ではなく、生の脳信号を直接扱う深層学習で行われた。 [^]
  - Footnote: Instead of relying on hand-crafted pipelines、end-to-end deep learning to decode directly from raw brain signals と説明されている。
- LLM の微調整により、ノイズの多い脳記録と自然言語の意味文脈を接続している。 [^]
  - Footnote: Fine-tuning large language models on neural data allows the system to leverage semantic context と説明されている。
- v2 の単語精度は 61% で、他の非侵襲手法の 8% から大きく改善した。 [^]
  - Footnote: The result として 61% word accuracy、other non-invasive methods の 8% word accuracy と比較されている。
- 最良の参加者では単語精度 78% を達成した。 [^]
  - Footnote: best participant では 78% word accuracy、半数超の文が one word error or less と記載されている。
- データ量を増やすことで、外科的手法との差をさらに縮められる可能性が示唆されている。 [^]
  - Footnote: decoding accuracy improves log-linearly with data volume とし、data scaling alone で性能差を狭められる可能性があると説明している。

### References
- https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication/
