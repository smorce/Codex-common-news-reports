# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-04-26T09:00:55+09:00
- Articles: 3

## メモ: Qwen-Image-2.0-pro
- Date: 2026-04-25T22:20:00+09:00

### Executive Summary
- Qwen-Image-2.0-Pro の公開を伝えるメモで、画像品質と多言語テキスト描画の改善を強調している。
- Text-to-Image Arena で世界9位を獲得したとして、モデルの立ち位置を示している。
- 利用先として ModelScope と Alibaba Cloud の API 参照先が案内されている。
- コメントでは、配布形態がオープンモデルではなく API 提供である点が確認されている。
- 著者は日本語化したデモプロンプトを試し、多言語テキスト表示の挙動を確認している。
- 生成結果は、中国語表記が混じるものの、かなりそれらしく出ていると評価している。
- 最後に、オープンモデルとしてのリリース予定があるのかを気にして締めている。

### Key Findings
- 画像品質、多言語テキストレンダリング、指示追従が強化されたと案内している。 [^]
  - Footnote: 本文と埋め込み投稿で、これらの改善点が公開メッセージとして示されている。
- Text-to-Image Arena で世界ランキング9位に入ったと紹介している。 [^]
  - Footnote: ページ内の埋め込み投稿に「#9 worldwide for Text-to-Image」とある。
- 試用先として ModelScope のスタジオURLが明示されている。 [^]
  - Footnote: リンク先として Qwen-Image-2.0-pro の ModelScope ページが掲載されている。
- API 参照先として Alibaba Cloud の ModelStudio ドキュメントが挙げられている。 [^]
  - Footnote: 本文に Alibaba Cloud の model studio console URL が記載されている。
- 著者は多言語テキスト表示に関心を持ち、日本語化したデモを試している。 [^]
  - Footnote: コメントで「多言語テキスト表示ってのが気になったので、デモを試してみた。」と書いている。
- 日本語化デモでは、Qwen-Image の開発経緯スライドを題材にしている。 [^]
  - Footnote: 本文に『Qwen-Image の開発経緯』を日本語化した説明がある。
- 生成結果は中国語の漢字が残るものの、かなり期待できる出来だと見ている。 [^]
  - Footnote: 「ところどころ中国語の漢字表記になっているが、だいぶそれっぽい」と述べている。

### References
- https://zenn.dev/kun432/scraps/b3dd8c9b3ea9c2
- https://modelscope.ai/studios/Qwen/Qwen-Image-2.0-pro
- https://modelstudio.console.alibabacloud.com/ap-southeast-1?tab=doc#/doc/?type=model&url=2840914_2&modelId=qwen-image-2.0-pro-2026-04-22&serviceSite=international
- https://twitter.com/Alibaba_Qwen/status/2048022731548229869
- https://twitter.com/Alibaba_Qwen/status/2048024933805244779

## Terraformのコードから最小のIAM権限をリストアップしてくれる「Pike」を試す
- Date: 2026-04-24T18:49:00+09:00

### Executive Summary
- Terraform の IAM ポリシーを最小化したいという問題意識から、Pike を試している。
- Pike は OpenTofu/Terraform のコードから必要な IAM 権限を判定する CLI ツールとして説明されている。
- JSON モジュール対応や GCP 比較、バックエンド検出などの新機能も紹介されている。
- インストール方法は macOS、Windows、ソースビルドの3通りが示されている。
- コマンド一覧には apply、compare、inspect、make、parse など多くの機能がある。
- 実際に make を試したところ、AWS の policyDocument の ASCII 制約でエラーになっている。
- 著者は、最小権限の一覧が出るだけでも実用的だとしつつ、機能の多さはやや過剰とも見ている。

### Key Findings
- Pike は IaC から必要な最小 IAM 権限を判定するツールとして紹介されている。 [^]
  - Footnote: README 要約で「OpenTofu/Terraform のコードを実行するために必要な最小限の IAM 権限」を判定すると説明している。
- サポート対象は OpenTofu/Terraform と複数クラウドに広がっている。 [^]
  - Footnote: 本文で AWS、GCP、AZURE に対応していると書かれている。
- 新機能として JSON モジュール対応、GCP 比較、バックエンド検出が追加されている。 [^]
  - Footnote: 『主な新機能』の箇所に3点が列挙されている。
- インストール方法は Homebrew、Scoop、Go からのソースインストールの3系統。 [^]
  - Footnote: 『インストール方法は以下の3つ』と明記されている。
- pike の CLI には make, parse, compare, inspect など多数のサブコマンドがある。 [^]
  - Footnote: pike --help の出力でコマンド一覧が列挙されている。
- make 実行では policyDocument が printable ASCII のみ許可という AWS 側の制約で失敗した。 [^]
  - Footnote: エラー出力に『It must contain only printable ASCII characters.』が出ている。
- エラー回避のため、.pike 配下を個別に init / plan / apply する手順が示されている。 [^]
  - Footnote: 本文で『cd .pike』『terraform init』『terraform plan』『terraform apply』と案内している。
- 著者は最終的に、権限一覧が出れば十分で、使い切らない機能は多そうだと感じている。 [^]
  - Footnote: まとめで『権限一覧が出力できればそれで十分』と述べている。

### References
- https://zenn.dev/kun432/scraps/36b36da97dd228
- https://github.com/JamesWoolfenden/pike
- https://dev.classmethod.jp/articles/pike-terraform-generate-iam-policy/
- https://developer.hashicorp.com/terraform/install

## 「LiteParse」を試す
- Date: 2026-04-24T12:56:00+09:00

### Executive Summary
- LiteParse は、複雑な PDF レイアウトを空間グリッドに落とし込む OSS のドキュメントパーサーとして紹介されている。
- VLM や ML モデルを使わず、ヒューリスティクスで高速に動く点が強みとされている。
- 中核は grid projection algorithm で、表や複数カラムの崩れを抑えて構造を保つ。
- 既定の OCR は Tesseract.js で、言語データは初回に自動取得される。
- 日本語 OCR も使え、TESSDATA_PREFIX を指定してオフライン利用できる。
- HTTP OCR サーバーを差し替えることで、精度や性能をさらに上げる選択肢もある。
- PDF だけでなく、Office 文書や画像などを自動変換して扱える対応範囲の広さも確認している。

### Key Findings
- LiteParse は PDF の複雑なレイアウトをクリーンな空間グリッドに解析する。 [^]
  - Footnote: 本文と埋め込み投稿で、複数カラムや表を扱える点が説明されている。
- VLM や ML を使わず、ヒューリスティクスベースで高速に動く。 [^]
  - Footnote: 投稿に『doesn't use VLMs or any ML models at all』とある。
- grid projection algorithm がレイアウト保持の鍵として説明されている。 [^]
  - Footnote: 本文に『グリッド投影アルゴリズム』の詳細な手順が並んでいる。
- 既定 OCR は Tesseract.js で、初回実行時に言語データを取得する。 [^]
  - Footnote: 『デフォルトは Tesseract.js』と『言語データがダウンロードされる』と記載されている。
- 日本語 OCR は jpn.traineddata を使って有効化できる。 [^]
  - Footnote: 本文に `lit parse ... --ocr-language jpn` の例がある。
- オフライン利用では TESSDATA_PREFIX を設定してローカル辞書を参照できる。 [^]
  - Footnote: 本文に `/usr/share/tesseract-ocr/5/tessdata` を指定する手順が書かれている。
- HTTP OCR サーバーを使う拡張手段があり、API スペックも公開されている。 [^]
  - Footnote: 『オプション: HTTP OCR サーバー』と API スペックへのリンクがある。
- 対応フォーマットは Word、PowerPoint、Excel、CSV、TSV、画像まで広い。 [^]
  - Footnote: 『対応フォーマット』の節で各拡張子が列挙されている。
- JSON 設定ファイルや Node.js 依存ライブラリとしても利用できる。 [^]
  - Footnote: 『その他』の節に『JSONで設定ファイルを作成して使用可能』『依存ライブラリとして利用可能』とある。

### References
- https://zenn.dev/kun432/scraps/7a6de84125d54c
- https://www.llamaindex.ai/blog/how-liteparse-turns-pdfs-into-text-a-deep-dive-into-the-grid-projection-algorithm
- https://github.com/run-llama/liteparse
- https://twitter.com/jerryjliu0/status/2047041129326194882
- https://twitter.com/simonw/status/2047434783962354130
