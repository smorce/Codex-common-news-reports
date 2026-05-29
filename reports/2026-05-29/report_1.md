# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-29T09:01:41.0870608+09:00
- Articles: 3

## 「LFM2.5-8B-A1B」を試す
- Date: 2026-05-28T17:11:35+00:00

### Executive Summary
- Liquid AI の LFM2.5-8B-A1B は、オンデバイス利用を強く意識した 8B MoE 系モデルとして紹介されている。
- 前世代から学習トークン数、コンテキスト長、指示追従、ツール呼び出し性能が大きく伸びた点が中心テーマである。
- 128K コンテキストとツールチェイン前提の調整により、ローカルエージェント用途への適性が強調されている。
- 幻覚対策や reasoning ループ対策にも触れられており、小型モデルでも信頼性を上げる設計が説明されている。
- LocalCowork のデモでは、クラウドや API キーなしに 13 MCP サーバーと 67 ツールを扱う構成が示されている。
- 実行形式は Transformers、vLLM、SGLang、ONNX、MLX、GGUF など幅広く、エッジから GPU サーバーまでを想定している。
- 筆者の試用では Colaboratory L4 上の Transformers 実行で VRAM 約 17.4GB を消費し、実用時は GGUF や MLX が候補と見ている。

### Key Findings
- LFM2.5-8B-A1B は 8B MoE、1.5B アクティブ、128K コンテキストのモデルとして提示されている。 [^]
  - Footnote: 本文に「8B MoE、1.5B アクティブ」「拡張された 128K コンテキスト」と記載されている。
- 前世代から学習量とコンテキスト長が大きく増えている。 [^]
  - Footnote: 本文の比較では「学習トークン数：12兆 → 38兆」「コンテキスト長：32,000トークン → 128,000トークン」とされている。
- 指示追従やツール関連ベンチマークで改善が報告されている。 [^]
  - Footnote: IFEval は 79.44 から 91.84、BFCLv3 は 45.07 から 64.36、BFCLv4 は 25.52 から 48.50 と記載されている。
- LocalCowork デモはオンデバイスのエージェント利用を示す代表例になっている。 [^]
  - Footnote: 本文では「シングルラップトップ」「13のMCPサーバー上で67のツール」「クラウドなし、APIキーなし」と説明されている。
- 多様な配布・実行形式があり、ローカル運用の選択肢が広い。 [^]
  - Footnote: モデルのバリエーションとして Transformers / vLLM / SGLang、ONNX、MLX、GGUF が列挙されている。
- 筆者の Transformers 試用では VRAM 消費が比較的大きい。 [^]
  - Footnote: Colaboratory L4 での実行結果として「VRAM消費は17.4GBぐらい」と書かれている。

### References
- https://zenn.dev/kun432/scraps/2dacfa5b91fcef
- http://liquid.ai/blog/lfm2-5-8b-a1b
- https://huggingface.co/LiquidAI/LFM2.5-8B-A1B

## 「FunASR」を試す
- Date: 2026-05-28T07:26:03+00:00

### Executive Summary
- FunASR は産業用音声認識ツールキットとして紹介され、Whisper より高速な処理や多機能統合が強調されている。
- 記事では英語版 README の内容を翻訳し、ASR、話者分離、感情検出、ストリーミング、API サーバー化などを整理している。
- FunASR は VAD、ASR、句読点、話者ダイアライゼーションなどを組み合わせて使える点が特徴として扱われている。
- ベンチマークでは SenseVoice-Small が GPU でリアルタイムの 170 倍、CPU でも 17 倍と説明されている。
- 筆者は Colaboratory L4 で中国語サンプルと日本語サンプルを試し、処理時間や出力構造を確認している。
- 日本語では SenseVoiceSmall を使い、感情タグや話者分離は確認できた一方、文字起こし品質には課題があると評価している。
- 最終的には、付加機能をまとめて扱える利点はあるが、モデルごとの対応範囲や英中中心の制約が残るとまとめている。

### Key Findings
- FunASR は ASR 周辺機能を一度に扱える構成を売りにしている。 [^]
  - Footnote: 本文に「1つのモデル、1回の呼び出しで、VADによる分割処理、音声認識、句読点の付与、話者ダイアライゼーションがすべて自動的に行われます」とある。
- 速度面では Whisper に対する優位性が強調されている。 [^]
  - Footnote: 比較表で FunASR は「リアルタイムの170倍」、Whisper は「13倍のリアルタイム処理」とされている。
- SenseVoice-Small は GPU と CPU の両方で高速なモデルとして示されている。 [^]
  - Footnote: ベンチマーク表では SenseVoice-Small が GPU で「リアルタイムの170倍」、CPU で「リアルタイムの17倍」と記載されている。
- FunASR は複数モデルを役割別に組み合わせる設計になっている。 [^]
  - Footnote: 筆者は AutoModel で ASR、VAD、句読点、話者分離モデルを指定し、「役割ごとにモデルを組み合わせて定義する様子」と述べている。
- 日本語サンプルでは感情抽出や話者分離は確認できたが、品質には不満が残る。 [^]
  - Footnote: 本文に「ちょっと文字起こしの品質がイマイチな感はあるが、感情抽出や話者分離などができている」とある。
- 日本語対応や機能の完全なコンポーネント化には制約がある。 [^]
  - Footnote: まとめで「サポートしているモデルがまだ少ない・英中中心になっている、というところが残念」と書かれている。

### References
- https://zenn.dev/kun432/scraps/4a76e6a0e5c984

## Codex を試す、再び ④ インテグレーション（試していない）
- Date: 2026-05-28T03:25:31+00:00

### Executive Summary
- この記事は Codex の公式ドキュメントを読み直すシリーズの一部で、今回はインテグレーションを扱っている。
- 対象として GitHub、Slack、Linear の 3 種類が挙げられているが、筆者は Linear 未経験のため GitHub と Slack を確認している。
- GitHub 連携では PR に対するコードレビュー、@codex review による依頼、自動レビュー、ガイドラインのカスタマイズが取り上げられている。
- Slack 連携ではチャンネルやスレッドから直接コーディングタスクを開始できる点が整理されている。
- 筆者はこれらの連携が Codex Web 前提になると理解し、リモート完結の利点は認めつつも利用感には慎重である。
- GitHub については GitHub Actions のほうがよいかもしれないという所感も残している。
- 次回以降は GitHub Actions など、まだ使いこなせていない機能を試す方針で締めている。

### Key Findings
- Codex インテグレーションの公式ドキュメントは GitHub、Slack、Linear を対象にしている。 [^]
  - Footnote: 本文に「インテグレーションは3つほどドキュメントがある。GitHub Slack Linear」と記載されている。
- 筆者は Linear を除き、GitHub と Slack を確認対象にしている。 [^]
  - Footnote: 本文で「自分はLinearを使ったことがないので、GitHubとSlackについて見ていく」と述べている。
- GitHub 連携では PR レビューの起動方法とレビュー設定が主な機能として整理されている。 [^]
  - Footnote: GitHub の項目に「プルリクエストに対して、コードレビューが可能」「@codex review」「PRをトリガー」「レビューのガイドラインをカスタマイズ」とある。
- Slack 連携では会話上からクラウドタスクを作成できる点が要点である。 [^]
  - Footnote: Slack の項目に「チャンネルやスレッドから直接コーディングタスクを開始」「@Codex メンションで...クラウドタスクが生成」と書かれている。
- 筆者は Codex Web 前提である点を確認しつつ、現時点では導入に慎重な姿勢を示している。 [^]
  - Footnote: 本文に「これはCodex Webが前提になる」「個人的には微妙な印象」「一旦ペンディング」とある。
- 次の検証対象として GitHub Actions などの未習熟機能が挙げられている。 [^]
  - Footnote: 最後に「次は、上のGitHub Actionsもそうだけど、まだ使いこなせてない機能を色々試す」と記載されている。

### References
- https://zenn.dev/kun432/scraps/27431a3cb4b8a4
