# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-06-03T09:01:29.9751828+09:00
- Articles: 3

## 「CAT-Thinking-8B」を試す
- Date: 2026-06-02T03:48:40+00:00

### Executive Summary
- CyberAgent の CAT-Thinking-8B を試したスクラップである。
- モデルは Qwen3-Swallow-v0.2 を基盤に、日本語で推論過程を生成するよう強化学習されている。
- 評価では日本語と英語のコーディング、数学タスクが対象になっている。
- 学習は gpt-oss-120b の合成データ、CAT-Translate-7b による翻訳、SFT、GRPO を組み合わせている。
- Colaboratory L4 で transformers の text-generation パイプラインから実行している。
- 実行時の VRAM 消費はおよそ 16GB と記録されている。
- 曖昧な指示では長大な推論や繰り返しが出やすく、repetition_penalty の利用が推奨されている。
- 日本語推論は自然さに課題があるが、日本語ネイティブでの利用には意義があると評価している。

### Key Findings
- CAT-Thinking-8B は日本語で推論過程を生成する小型言語モデルとして紹介されている。 [^]
  - Footnote: 記事本文に「日本語で考える小型言語モデル」「強化学習によって日本語の推論過程を生成するように訓練されたモデル」とある。
- 基盤モデルは Qwen3-Swallow-v0.2 で、日本語の読み書き能力を前提にしている。 [^]
  - Footnote: 本文に「Qwen3-Swallow-v0.2を基盤」「流暢な日本語の読み書きが可能」と記載されている。
- 評価はコーディングと数学タスクで行われ、比較対象は Qwen-3-8B と Qwen3-Swallow-8B-RL-v0.2 である。 [^]
  - Footnote: 評価節に「日本語と英語によるコーディングタスクおよび数学タスク」「Qwen-3-8B」「Qwen3-Swallow-8B-RL-v0.2」とある。
- 学習は合成データ作成、翻訳、SFT、形式重視の GRPO、厳格報酬の GRPO という段階を踏む。 [^]
  - Footnote: 学習手順として「gpt-oss-120bを参照データ」「CAT-Translate-7b」「SFT」「寛容な報酬モデル」「厳格な報酬モデル」と説明されている。
- Colaboratory L4 では transformers の pipeline で実行できる。 [^]
  - Footnote: 記事に「Colaboratory L4で」「from transformers import pipeline」「model="CyberAgent/CAT-Thinking-8B"」のコードがある。
- 実行時の GPU メモリ使用量は約 16GB だった。 [^]
  - Footnote: 本文に「VRAM消費は16GB程度」とあり、NVIDIA-SMI の Memory-Usage は「15964MiB / 23034MiB」と示されている。
- 長い出力や繰り返しを抑えるには repetition_penalty が有効とされている。 [^]
  - Footnote: モデルカード引用部に「繰り返し発生の確率を低減するためには、repetition_penalty=1.05 以上の設定が有効」とある。

### References
- https://zenn.dev/kun432/scraps/055ae79201d0ef
- https://huggingface.co/cyberagent/CAT-Thinking-8B

## ローカルでAWSをエミュレートする「Floci」を試す
- Date: 2026-06-01T17:20:43+00:00

### Executive Summary
- Floci をローカル AWS エミュレーターとして試すためのスクラップである。
- 背景として、ユーザー数が多そうで最近見かけることが増えたため Floci を選んでいる。
- Floci は開発、テスト、CI/CD 向けの無料オープンソース AWS エミュレーターと説明されている。
- アカウント登録、認証トークン、機能制限なしで利用できる点が強調されている。
- AWS SDK、CLI、Terraform、CDK、OpenTofu、テストスイートを localhost:4566 に向けるだけで使える。
- LocalStack Community のサポート終了予定を踏まえた代替として位置づけられている。
- 52 種類の AWS サービスに対応し、Docker ベースの実サービス統合も備える。
- LocalStack からの移行ではイメージ差し替えや環境変数の自動変換が説明されている。

### Key Findings
- Floci は無料かつ認証不要の AWS エミュレーターとして設計されている。 [^]
  - Footnote: README 抜粋に「アカウント登録不要。認証トークンも不要。機能制限もありません」とある。
- 既存の AWS ツールを localhost:4566 に向けるだけで利用できる。 [^]
  - Footnote: 本文に「AWS SDKやCLI、Terraform、CDK、OpenTofu、あるいはテストスイートを http://localhost:4566 に向けるだけ」とある。
- LocalStack Community の制約を意識した代替として説明されている。 [^]
  - Footnote: 記事に「LocalStackのコミュニティエディションは2026年3月にサポート終了予定」「Flociはこうした制約のない代替」とある。
- 性能面では起動時間、メモリ、イメージサイズで LocalStack Community より軽量とされている。 [^]
  - Footnote: 比較表に「起動時間 約24ms」「アイドル時のメモリ使用量 約13MB」「Dockerイメージサイズ 約90MB」とある。
- 対応サービスは 52 種類で、S3、SQS、DynamoDB、Lambda、API Gateway、Cognito など幅広い。 [^]
  - Footnote: 本文に「52種類のAWSサービスに対応」とあり、カテゴリ別のサポート対象サービス表が掲載されている。
- RDS、ElastiCache、MSK、EKS などは実際の Docker コンテナを使う構成が説明されている。 [^]
  - Footnote: サービス詳細メモに「実際のDockerコンテナを使用」とあり、PostgreSQL、MySQL、Redpanda、k3s などが列挙されている。
- 永続化は memory、persistent、hybrid、wal の 4 モードを選べる。 [^]
  - Footnote: 永続化とストレージモード節に「memory」「persistent」「hybrid」「wal」の表がある。
- LocalStack からの移行を意識し、環境変数や初期化スクリプトの互換性が用意されている。 [^]
  - Footnote: 移行節に「LocalStackの環境変数は自動的に変換」「/etc/localstack/init/ディレクトリにマウントされた初期化スクリプトは、そのまま変更なしで動作」とある。

### References
- https://zenn.dev/kun432/scraps/9d5473bd03acb5
- https://github.com/floci-io/floci

## LocalStackの代替比較
- Date: 2026-06-01T16:50:35+00:00

### Executive Summary
- LocalStack のライセンス体系変更を受けて代替候補を比較したスクラップである。
- 無料利用を続ける場合、OSS 性、テレメトリ、アカウント登録、CI 利用に影響があると見ている。
- 比較対象は LocalStack 新モデル、kumo、Floci、MiniStack を中心に整理されている。
- Floci は LocalStack Community の置き換えを強く意識した高機能、無料、軽量な選択肢として評価されている。
- MiniStack は Terraform や本番寄りインフラ再現を重視する用途に向くとされている。
- kumo は Go 製の軽量なテスト向けエミュレーターとして位置づけられている。
- 既存の LocalStack 構成を痛み少なく移行するなら Floci から試すのがよいという結論に近い。
- Moto も候補として触れられているが、用途はよりテスト寄りと見ている。

### Key Findings
- LocalStack の変更により、無料利用でもアカウントや auth token が必要になる点が問題視されている。 [^]
  - Footnote: 本文に「latest など最新を使うには アカウント作成 + auth token 必須」とある。
- LocalStack Community の OSS リポジトリは非アクティブ化し、更新やセキュリティパッチ停止が懸念されている。 [^]
  - Footnote: 比較節に「OSS リポジトリは残るけど『非アクティブ』扱い」「更新もセキュリティパッチも基本止まる」とある。
- kumo は MIT ライセンス、認証不要、単一バイナリの軽量用途として整理されている。 [^]
  - Footnote: 本文に「kumo MIT ライセンス」「Docker イメージ / 単一バイナリで、認証不要」とある。
- Floci は LocalStack Community の完全代替と改良を狙う選択肢とされている。 [^]
  - Footnote: Floci 節に「フォーカスは『LocalStack Community の完全代替 + 改良版』」とある。
- Floci は 52 サービス対応に加え、Docker バックエンドで実装するサービスがある点が強みとされる。 [^]
  - Footnote: 記事に「52サービス」「Lambda / RDS / ElastiCache / MSK / ECS / EC2 / EKS / CodeBuild / OpenSearch などは Docker バックエンド」とある。
- MiniStack は RDS、ElastiCache、ECS、Athena、Glue、EKS、OpenSearch など本番寄りの再現度が高いと評価されている。 [^]
  - Footnote: MiniStack 節に「RDS が 本物の Postgres/MySQL/MariaDB コンテナ」「Athena が DuckDB」「EKS(k3s) / OpenSearch(real engine)」とある。
- 性能面では Floci がミリ秒起動と低メモリを明確に打ち出している。 [^]
  - Footnote: パフォーマンス節に「起動時間: Floci 約24ms」「アイドルメモリ: Floci 約13MiB」とある。
- LocalStack からの乗り換えやすさでは Floci が最も移行コストが低いと判断されている。 [^]
  - Footnote: DX 節に「既に LocalStack 前提の Compose / CI / IaC があるが、コードを書き換えたくないなら Floci が一番」とある。
- 最初に試す候補として Floci が選ばれている。 [^]
  - Footnote: 末尾に「ユーザー数ベースで見るならば、とりあえず Floci から試すのがいいかな」とある。

### References
- https://zenn.dev/kun432/scraps/e92d3f9c92ed68
