# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-21T09:04:54+09:00
- Articles: 3

## 「Unsloth Studio」を試す
- Date: 2026-03-20T23:10:00+09:00

### Executive Summary
- Unsloth StudioはLLMの学習・実行向けのオープンソースWeb UIとして紹介されている。
- Mac/Windows/Linuxでローカル実行でき、Dockerなどでも利用可能とされる。
- VRAM 70%削減と学習2倍速で500+モデル対応という性能面を強調。
- GGUFやビジョン/音声/埋め込みなど多様なモデル形式に対応。
- PDF/CSV/DOCXから自動でデータセット化する機能がある。
- サンドボックスでコード実行し回答検証できる点で信頼性向上を狙う。
- Unsloth Studioと既存のUnsloth Coreはライセンスが異なると整理。

### Key Findings
- ローカル実行のクロスプラットフォーム対応が明記されている。 [^]
  - Footnote: 「Mac、Windows、Linux環境でローカルにモデルを実行可能」
- VRAM削減と学習高速化、対応モデル数の主張がある。 [^]
  - Footnote: 「VRAM使用量を70%削減しながら、500種類以上のモデルを2倍の速度で学習可能」
- GGUFやビジョン/音声/埋め込みなど多様な形式をサポートするとされる。 [^]
  - Footnote: 「GGUF形式をはじめ、ビジョンモデル、音声モデル、埋め込みモデルなど多様なモデル形式に対応」
- PDF/CSV/DOCXから自動でデータセット作成できる点が強調されている。 [^]
  - Footnote: 「PDF、CSV、DOCXファイルから自動的にデータセットを作成」
- サンドボックス内でコード実行し、回答の検証に使えるとしている。 [^]
  - Footnote: 「LLMがサンドボックス内でコードやプログラムを実行できる…回答の検証が可能」
- StudioとCoreでライセンスが異なると明記されている。 [^]
  - Footnote: 「Unsloth Studio: AGPL-3.0」「Unsloth Core: Apache-2.0」

### References
- https://zenn.dev/kun432/scraps/571c5ab6af50a8
- https://github.com/unslothai/unsloth
- https://unsloth.ai/docs/new/studio

## LiveKit "Adaptive interruption handling"
- Date: 2026-03-20T02:35:00+09:00

### Executive Summary
- LiveKitのAdaptive Interruption Handlingは音声エージェントの割り込み判定改善を狙う。
- VADが相槌やノイズで誤停止する問題を課題として提示。
- 専用の音声モデルを訓練し、本当の割り込みとノイズを区別する。
- 最初の数百ミリ秒の波形を見て判定する仕組みを説明。
- CNN+音声エンコーダで話し始めの特徴を捉えるとされる。
- ベンチマークで高いprecision/recallや検出速度改善を主張。
- LiveKit Agentsの最新版ではデフォルト有効でCloudでも使える。

### Key Findings
- VADは相槌やくしゃみなどで誤停止する課題があると述べている。 [^]
  - Footnote: 「VADは感度が高すぎます — 笑い声、『うんうん』、あるいは、くしゃみで、エージェントが止まってしまうべきではありません。」
- 適応型割り込み処理のためのオーディオモデルを訓練したと記載。 [^]
  - Footnote: 「適応型割り込み処理（adaptive interruption handling）のためのオーディオモデルを訓練しました。」
- 最初の数百ミリ秒の波形をチェックして割り込みか否か判断する。 [^]
  - Footnote: 「モデルが『最初の数百ミリ秒』の波形をチェックする。」
- ベンチマークとして500ms重なりで86% precision/100% recallを提示。 [^]
  - Footnote: 「86% precision / 100% recall（500ms 重なったスピーチで）」
- VADの誤認識のうち51%を弾けるとされる。 [^]
  - Footnote: 「VAD が『割り込みだ』と誤認識しちゃうケースのうち、51% を弾いてくれる」
- 推論時間は30ms以下、判定までの音声中央値216msと説明。 [^]
  - Footnote: 「推論時間は 30ms 以下、割り込みとして判定するまでの音声は中央値 216ms」
- LiveKit Agentsの特定バージョン以降でデフォルト有効と明記。 [^]
  - Footnote: 「Python Agents v1.5.0+」「TypeScript Agents v1.2.0+」「Adaptive Interruption Handling は デフォルトで有効」

### References
- https://zenn.dev/kun432/scraps/4272213e191766
- https://livekit.com/blog/adaptive-interruption-handling

## 「Mengram」を試す
- Date: 2026-03-19T21:07:00+09:00

### Executive Summary
- MengramはAI向けの人間の脳型メモリAPIとして紹介されている。
- 意味記憶・エピソード記憶・手続き記憶の3種類を扱う点を強調。
- add()で会話を投入すると自動分類・抽出する仕組み。
- search_allで3種の記憶を一括検索し、get_profileでシステムプロンプト生成。
- RAGの配線をAPIで置き換える位置づけとして説明。
- 各種エージェント/フレームワーク連携やCLIインポートも言及。
- 料金プランやセルフホスト、ライセンスへの言及と所感がある。

### Key Findings
- 意味・エピソード・手続きの3種類の記憶をサポートすると記載。 [^]
  - Footnote: 「意味記憶、エピソード記憶、手続き記憶の3種類の記憶形式をサポート。」
- RAGパイプラインを1回のAPIコールで置き換え可能と述べている。 [^]
  - Footnote: 「RAGパイプラインを1回のAPIコールで置き換えることが可能」
- add()で会話やテキストを投入し、事実/出来事/手順を自動抽出する。 [^]
  - Footnote: 「add() で会話やテキストを突っ込むと…『事実』『出来事』『手順』って分類してくれる。」
- search_allで3種メモリをまとめて検索できると説明。 [^]
  - Footnote: 「search_all() で『Semantic / Episodic / Procedural をまとめて検索』できる。」
- get_profileでシステムプロンプトとして使えるプロフィールを生成。 [^]
  - Footnote: 「get_profile() でユーザーのプロフィール的なシステムプロンプトを作ったりできる」
- CrewAI/LangChain/n8n/OpenClawなど連携ツールが用意されている。 [^]
  - Footnote: 「CrewAI 用のツールセット…LangChain 用…n8n 用…OpenClaw プラグイン」
- 料金プランとしてFree/Starter/Pro/Business/Enterpriseが提示されている。 [^]
  - Footnote: 「Free…Starter ($5)…Pro ($19)…Business ($99)…Enterprise」
- ライセンスはApache-2.0と明記されている。 [^]
  - Footnote: 「ライセンスは Apache-2.0」

### References
- https://zenn.dev/kun432/scraps/0185eb735c3eca
- https://mengram.io/
- https://docs.mengram.io/claude-code
