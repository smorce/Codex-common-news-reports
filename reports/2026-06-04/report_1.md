# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-06-04T09:01:59+09:00
- Articles: 3

## 「Gemma4」を試す（12B）

### Executive Summary
- GoogleのGemma 4 12Bを試したスクラップで、12B版の位置づけと実行感が整理されている。
- 記事では、Gemma 4 12Bをテキスト、画像、音声を扱うマルチモーダルモデルとして紹介している。
- 専用のビジョンや音声エンコーダーを別立てにしない統一的なアーキテクチャが特徴として扱われている。
- ローカル実行可能性について、16GB級のVRAMまたはユニファイドメモリを意識したモデルとして説明している。
- 利用先としてLM Studio、Ollama、Google AI Edge、LiteRT-LM CLIなどが挙げられている。
- 試行ではTransformersを使ったロード例と推論例が掲載され、VRAM消費は約23GBと記録されている。
- 出力品質については、以前のGemma系と比べて12Bの出力が自然に見えるという筆者の所感が示されている。
- まとめでは、26B級に近い推論能力、ローカル実行可能な軽さ、エージェント用途への意識が主な価値として整理されている。

### Key Findings
- Gemma 4 12Bはマルチモーダル入力を扱うモデルとして紹介されている。 [^]
  - Footnote: 記事本文に「Gemma 4 12B」「テキスト・画像・音声」「マルチモーダル」という説明がある。
- 専用エンコーダーを分けずに扱う統一アーキテクチャが重要な特徴とされている。 [^]
  - Footnote: 記事では「エンコーダーレス」「統一アーキテクチャ」として、画像や音声もLLM側で扱う構成が説明されている。
- ローカル実行の現実性が評価軸になっている。 [^]
  - Footnote: 本文に「16GB VRAM / unified memory」「ローカル実行」といった記述がある。
- 利用できる周辺エコシステムが広い。 [^]
  - Footnote: LM Studio、Ollama、Google AI Edge Gallery / Eloquent、LiteRT-LM CLI、Hugging Face、Kaggleなどが列挙されている。
- Transformersでの実行例が示されている。 [^]
  - Footnote: 本文にAutoProcessor、AutoModelForMultimodalLM、MODEL_ID="google/gemma-4-12B-it"を使うコードが掲載されている。
- 実測ではメモリ負荷が軽いだけではないことも示されている。 [^]
  - Footnote: NVIDIA-SMIの出力としてA100上で約23316MiBのVRAM使用が掲載されている。
- Apache 2.0ライセンスで提供される点が利点として扱われている。 [^]
  - Footnote: モデルカード由来の説明として「Apache 2.0」ライセンスへの言及がある。
- 筆者は12B版の出力を以前のモデルより自然と評価している。 [^]
  - Footnote: 記事後半で「14Bの出力のほうが全然マシにみえる」「流石に何かおかしい気がする」といった所感が示されている。

### References
- https://zenn.dev/kun432/scraps/2a8f17ca02e189
- https://huggingface.co/google/gemma-4-12B

## ローカルAWSエミュレータ向けGUI「StackPort」を試す

### Executive Summary
- StackPortをローカルAWSエミュレータ向けGUIとして試したスクラップである。
- StackPortはローカルエミュレータと本番AWSアカウントの両方に対応するAWSリソースブラウザとして紹介されている。
- S3、DynamoDB、Lambda、SQS、IAM、EC2、CloudWatch Logs、Secrets Managerなど幅広いサービスが対象になっている。
- リソース閲覧だけでなく、S3操作、DynamoDBクエリ、Lambda呼び出し、SQS送受信などの書き込み系操作も扱える。
- AWS_PROFILEやAWS_ENDPOINT_URLを使って、LocalStack、Moto、MinIOなど任意のエンドポイントに向けられる。
- CLIとしてstatus、list、describe、exportが用意され、JSONやCSVでの出力にも対応している。
- 筆者はFlociで作成したDynamoDBテーブルをStackPortの画面から確認できたと述べている。
- まとめでは、本格的な作成・変更よりも、ちょっとした確認用途に便利という評価が示されている。

### Key Findings
- StackPortはローカルエミュレータと実AWSの両方を対象にできる。 [^]
  - Footnote: README引用部に「ローカルエミュレーターと本番AWSアカウントに対応」とある。
- 対応サービス数は35種類と説明されている。 [^]
  - Footnote: 本文の主な機能に「35種類のAWSサービス」と記載されている。
- S3、DynamoDB、Lambda、SQSなどは専用UIや書き込み操作が用意されている。 [^]
  - Footnote: 記事にはS3ブラウザ、DynamoDBクエリ、Lambda呼び出し、SQSメッセージ送受信が列挙されている。
- 読み取り専用モードを設定できるため、本番AWS接続時の安全策がある。 [^]
  - Footnote: 起動例にSTACKPORT_ALLOW_WRITES=false AWS_PROFILE=my-profile stackportが掲載されている。
- インストールはPyPI経由が推奨として示されている。 [^]
  - Footnote: クイックスタートにpip install stackportとあり、筆者もuv add stackportで0.3.4を導入している。
- ローカルAWSエミュレータへの接続はAWS_ENDPOINT_URLで指定する。 [^]
  - Footnote: LocalStack、Moto、MinIO向けにAWS_ENDPOINT_URL=http://localhost:4566などの例が掲載されている。
- CLIでもリソース状態の確認やエクスポートができる。 [^]
  - Footnote: stackport status、list、describe、exportのコマンド例が記載されている。
- 筆者の評価は確認用途に寄っている。 [^]
  - Footnote: まとめで「リソースの作成とか変更とかはGUIからはそんなにしない」「ちょっとした確認には便利」と述べている。

### References
- https://zenn.dev/kun432/scraps/93e99f30bb5225
- https://github.com/DaviReisVieira/stackport

## 「CAT-Thinking-8B」を試す

### Executive Summary
- CyberAgentのCAT-Thinking-8Bを試したスクラップで、日本語推論に焦点を当てている。
- モデルカードの説明として、CAT-Thinkingは日本語で推論過程を生成するよう訓練された小規模言語モデルと紹介されている。
- ベースモデルはQwen3-Swallow-v0.2で、日本語の読み書きに向いた継続事前学習モデルとされている。
- 評価対象にはmbpp、HumanEval、JHumanEval、LiveCodeBenchv6、GPQA、PolyMath、AIME 26などが挙げられている。
- 学習ではgpt-oss-120b由来の教師データ、CAT-Translate-7bによる日本語翻訳、SFT、GRPOが説明されている。
- Colaboratory L4でTransformersのtext-generation pipelineを使い、VRAM消費は約16GBと記録されている。
- 実行例では日本語の思考過程が出る一方、回答が長くなりがちで不自然な表現もあると観察されている。
- 筆者のまとめでは、日本語Reasoning自体は興味深いが、現時点ではQwen3-Swallowの方が好みに合う可能性も示されている。

### Key Findings
- CAT-Thinking-8Bは日本語で推論過程を生成することを狙ったモデルである。 [^]
  - Footnote: モデルカード引用部に「日本語で考える小規模言語モデル」「日本語の推論過程を生成」とある。
- ベースはQwen3-Swallow-v0.2である。 [^]
  - Footnote: 記事に「このモデルはQwen3-Swallow-v0.2を基盤」と記載されている。
- 評価はコーディング、数学、日本語・英語の複数ベンチマークで行われている。 [^]
  - Footnote: mbpp、HumanEval、JHumanEval、LiveCodeBenchv6、GPQA Main、PolyMath、AIME 26が列挙されている。
- 学習データ生成にはgpt-oss-120bとCAT-Translate-7bが使われている。 [^]
  - Footnote: 学習手順に、gpt-oss-120bを参照データにし、CAT-Translate-7bで日本語へ翻訳する説明がある。
- GRPOでは形式、言語、回答形式などを満たす場合に報酬を与える設計が説明されている。 [^]
  - Footnote: 記事に、推論形式に従うこと、日本語で推論過程と本文を生成すること、指定形式で答えることが条件として挙げられている。
- Colaboratory L4での実行では約16GBのVRAMを使っている。 [^]
  - Footnote: NVIDIA-SMI出力でL4のMemory-Usageが15964MiBと記録されている。
- Transformersのpipelineで比較的簡単に試せる。 [^]
  - Footnote: from transformers import pipeline、model="CyberAgent/CAT-Thinking-8B"のコードが掲載されている。
- 筆者は日本語推論の流暢さには課題を感じている。 [^]
  - Footnote: まとめで「日本語が流暢に越したことはない」「個人的にはQwen3-Swallowのほうが良い回答」と述べている。

### References
- https://zenn.dev/kun432/scraps/055ae79201d0ef
- https://huggingface.co/cyberagent/CAT-Thinking-8B
