# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-21T09:01:41.8366558+09:00
- Articles: 3

## 「llama-benchy」を試す

### Executive Summary
- OpenAI互換LLMエンドポイント向けのベンチマークツール llama-benchy のREADME抜粋を紹介している。
- llama.cpp専用の llama-bench では測れない推論エンジンを対象にできる点が主眼である。
- 異なるコンテキスト深度でプロンプト処理速度とトークン生成速度を測れる。
- TTFR、推定プロンプト処理時間、エンドツーエンドTTFTなど複数の遅延指標を扱う。
- HuggingFaceトークナイザーやProject Gutenbergの書籍を使い、トークン数や入力文を制御できる。
- uvx、uv run、仮想環境、システムインストールなど複数の導入手順が示されている。
- 出力はMarkdown、JSON、CSVに対応し、時系列スループットも保存できる。
- 現在の制限として、評価対象は /v1/chat/completions のみとされている。

### Key Findings
- llama-benchy はOpenAI互換エンドポイントのベンチマークを llama-bench 風に出力するツールである。 [^]
  - Footnote: 本文に「OpenAI互換LLMエンドポイント向けのベンチマークツール（llama-bench形式）」とある。
- 背景には、llama-bench が llama.cpp 専用で他の推論エンジンに使えない課題がある。 [^]
  - Footnote: 本文に「llama.cpp専用に設計されており、vllmやSGLangといった他の推論エンジンでは使用できません」とある。
- 異なるコンテキスト深度でプロンプト処理速度と生成速度を測定できる。 [^]
  - Footnote: 主な機能に「異なるコンテキスト深度におけるプロンプト処理速度（pp）とトークン生成速度（tg）を測定可能」とある。
- 遅延指標としてTTFR、est_ppt、e2e_ttftを報告する。 [^]
  - Footnote: 主な機能に「初回応答までの時間（データチャンク）（TTFR）、推定プロンプト処理時間（est_ppt）、およびエンドツーエンドのTTFTを報告」とある。
- 複数回実行して平均値と標準偏差を出せるため、ばらつきを含む比較に使える。 [^]
  - Footnote: 主な機能に「複数の反復処理（--runs）を実行可能で、平均値±標準偏差を報告」とある。
- 結果保存はMarkdown、JSON、CSVに対応している。 [^]
  - Footnote: 主な機能に「結果をMarkdown、JSON、またはCSV形式でファイルに保存可能」とある。
- 評価対象エンドポイントには制限がある。 [^]
  - Footnote: 現在の制限事項に「評価対象は/v1/chat/completionsエンドポイントのみ」とある。

### References
- https://zenn.dev/kun432/scraps/91f1e0413c0a66

## 「aiperf」を試す

### Executive Summary
- AIPerf は生成AIモデルの性能測定を目的とする包括的なベンチマークツールとして紹介されている。
- ZMQ通信を使う10サービス構成のマルチプロセスアーキテクチャが特徴である。
- dashboard、simple、none の3種類のUIモードを持つ。
- 並行処理、リクエストレート、トレース再生など複数のベンチマークモードを備える。
- OpenAI系APIに加え、NIM embeddings や rankings などにも対応する。
- ShareGPT、AIMO、MMStar、ASRなど多様な公開データセットやカスタムデータセットを扱える。
- 負荷制御、到着パターン、ウォームアップ、キャンセル処理など実運用に近い条件設定が豊富である。
- 既知の問題として、高い同時接続数でのポート枯渇や無効設定時の停止などが挙げられている。

### Key Findings
- AIPerf は生成AIモデルの性能を測るベンチマークツールである。 [^]
  - Footnote: 本文に「生成AIモデルの性能を測定する包括的なベンチマークツール」とある。
- 詳細メトリクスとベンチマーク性能レポートの両方を提供する。 [^]
  - Footnote: 本文に「コマンドライン表示による詳細なメトリクスと、詳細なベンチマーク性能レポートの両方を提供」とある。
- アーキテクチャはZMQ通信を採用した10サービス構成である。 [^]
  - Footnote: 主な機能に「ZMQ通信を採用した10個のサービスで構成されるスケーラブルなマルチプロセスアーキテクチャ」とある。
- UIはリアルタイムTUI、進捗バー、ヘッドレスの3モードを選べる。 [^]
  - Footnote: 主な機能に「3種類のUIモード：dashboard（リアルタイム操作可能なTUI）、simple（進捗バー表示）、none（ヘッドレスモード）」とある。
- OpenAI chat completions だけでなく、embeddings、audio、images など複数APIに対応する。 [^]
  - Footnote: 対応APIに「OpenAI chat completions, completions, embeddings, audio, images」とある。
- 公開データセットとカスタム形式データセットをサポートする。 [^]
  - Footnote: 主な機能に「公開データセットのサポート：ShareGPTやカスタム形式データセットを含む」とある。
- 負荷制御ではリクエストレートや最大同時リクエスト数を組み合わせられる。 [^]
  - Footnote: 負荷制御に「最大同時リクエスト数を考慮したリクエストレート制御」とある。
- 非常に高い同時接続数では環境側のポート枯渇に注意が必要である。 [^]
  - Footnote: 既知の問題点に「非常に高い同時接続数設定（通常15,000件以上）では、一部のシステムでポート枯渇が発生」とある。

### References
- https://zenn.dev/kun432/scraps/32e432d4803d32
- https://github.com/ai-dynamo/aiperf

## 「Colima」を試す

### Executive Summary
- Colima はmacOSおよびLinux向けのコンテナランタイムとして紹介されている。
- 最小限の設定でコンテナ実行環境を利用できることが目的とされている。
- Intel Mac、Apple Silicon、Linux に対応する。
- 直感的なCLI、自動ポートフォワード、ボリュームマウントなど基本機能を備える。
- Docker、containerd、Incus など複数のランタイムに対応する。
- DockerおよびcontainerdではオプションでKubernetesも利用可能とされている。
- AIワークロード向けのGPUアクセラレーション対応コンテナも機能に含まれる。
- 裏側ではLimaでVMを立ち上げ、その中でコンテナを動かす構成だと筆者が補足している。

### Key Findings
- Colima はmacOSとLinuxで使えるコンテナランタイムである。 [^]
  - Footnote: 本文に「macOS（およびLinux）向けの最小限の設定で動作するコンテナランタイム」とある。
- プロジェクトの目的はmacOSで最小限の設定によりコンテナランタイムを使えるようにすることにある。 [^]
  - Footnote: プロジェクトの目的に「macOS環境において、最小限の設定でコンテナランタイムを利用できるようにすること」とある。
- 対応環境はIntel Mac、Apple Silicon、Linuxである。 [^]
  - Footnote: 主な機能に「IntelプロセッサおよびApple Silicon搭載のmacOS、およびLinux環境に対応」とある。
- ポートフォワードとボリュームマウントを標準的な利便機能として備える。 [^]
  - Footnote: 主な機能に「自動ポートフォワード機能」「ボリュームマウント機能」とある。
- 複数インスタンスを同時に実行できる。 [^]
  - Footnote: 主な機能に「複数インスタンスの同時実行」とある。
- Docker、Containerd、Incus の複数ランタイムをサポートする。 [^]
  - Footnote: 主な機能に「Docker」「Containerd」「Incus」が列挙されている。
- Colima はLima上でコンテナを動かすという設計に由来する。 [^]
  - Footnote: 名前の由来に「Colima」とは「Lima上でのコンテナ」を意味します」とある。
- 筆者はREADME補足として、裏側でLimaを使いVM内でコンテナを動かす構成だと理解している。 [^]
  - Footnote: 本文末に「裏ではLimaを使ってVMを立ち上げてそこでコンテナを動かすという感じみたい」とある。

### References
- https://zenn.dev/kun432/scraps/7e0becc836485f
- https://github.com/abiosoft/colima
