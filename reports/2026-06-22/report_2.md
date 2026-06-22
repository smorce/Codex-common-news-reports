# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-06-22T09:04:13.9656079+09:00
- Articles: 3

## AIエージェント時代に問われるのは「プロンプト力」ではなく「コンテキスト設計力」である― プロンプトの時代から、コンテキスト設計の時代へ ―
- Date: 2026-06-19T00:00:00+09:00

### Executive Summary
- 生成AIは質問応答から、目的達成に向けて作業するAIエージェントへ移行している。
- 従来のチャット型AIはカーナビ、AIエージェントは自動運転ドライバーに例えられている。
- AIエージェントでは、短い指示よりも目的、制約、参照資料、評価基準などの文脈設計が重要になる。
- 各社のエージェントはチャット画面に閉じず、デスクトップ、ブラウザ、Office、開発環境、CLI、モバイルへ広がっている。
- マルチモーダル化により、AIへ与える文脈は文章だけでなくPDF、画像、音声、動画、スライドにも拡張している。
- Dify、OpenClaw、Hermes Agentなどは、AIを業務ワークフロー内で動かす方向性を示している。
- 今後価値が高まるのは、AIを現場の制約や業務プロセスに合わせて使える形へ翻訳できる人材だ。

### Key Findings
- AIエージェント時代の成果は、プロンプト単体ではなくコンテキスト設計に左右される。 [^]
  - Footnote: 本文は「AI活用の成否は、プロンプト単体ではなく、コンテキスト設計の優劣によって決まり始めている」と述べている。
- AIエージェントには目的だけでなく、制約、資料、業務ルール、評価基準などを渡す必要がある。 [^]
  - Footnote: 本文では「目的、制約条件、参照資料、業務ルール、顧客の状況、評価基準、既存システム、過去の経緯」と列挙している。
- AIエージェントの利用面は、チャット画面から日常の作業環境へ拡大している。 [^]
  - Footnote: 本文は「デスクトップアプリ、ブラウザ、Officeアプリ、開発環境、CLI、モバイルアプリへと広げている」と説明している。
- マルチモーダル化により、信頼できる資料群をあらかじめ整えることが実践上の鍵になる。 [^]
  - Footnote: 本文は「PDF、画像、音声、動画、スライド、Webページ」などを扱えるようになったとし、NotebookLMを例に資料整理の重要性を示している。
- 企業導入では、SSO、権限管理、監査ログ、承認フロー、セキュリティを含むガバナンス設計が必要になる。 [^]
  - Footnote: 本文に「SSO、権限管理、監査ログ、承認フロー、セキュリティまで含めたガバナンス設計が欠かせない」とある。
- FDE型人材は、AIやソフトウェアを現場の課題に合わせて実用化する役割として重視される。 [^]
  - Footnote: 本文はFDEを「顧客企業の現場に入り込み、業務課題を理解し、データ、AI、システムを組み合わせて、実際に使える形にする職種」と説明している。

### References
- https://www.nttpc.co.jp/gpu/article/technical30.html

## AWS、AIエージェントがリポジトリを自動スキャンして技術的負債を指摘してくれる「AWS Transform – continuous modernization」プレビュー公開
- Date: 2026-06-22T00:00:00+09:00

### Executive Summary
- AWSは「AWS Transform – continuous modernization」のプレビュー公開を発表した。
- この機能はAIエージェントがコードリポジトリを継続的にスキャンする。
- 検出対象は、サポート終了ライブラリ、フレームワーク、廃止API、ランタイムなどの技術的負債だ。
- 検出結果は優先順位付きで提示され、修復用のプルリクエスト作成も可能とされる。
- 組織固有の承認済みライブラリや内部標準に合わせたポリシー拡張にも対応する。
- AWS Security Agentとの統合により、ソースコードレベルの脆弱性検出と修正も扱える。
- 継続スキャンにより、後回しになりがちな技術的負債対応を計画的に進めやすくする狙いがある。

### Key Findings
- 新機能はAIエージェントによるリポジトリの継続的な自動スキャンを中核にしている。 [^]
  - Footnote: 記事は「AIエージェントがコードリポジトリを継続的に自動スキャン」と説明している。
- 技術的負債は優先順位付きで報告され、修復のためのプルリクエスト提案まで行える。 [^]
  - Footnote: 記事に「優先順位をつけて報告あるいは修正のためのプルリクエストの提案」とある。
- 検出対象には廃止API、サポート終了ランタイム、ライブラリ、フレームワークが含まれる。 [^]
  - Footnote: 記事は「廃止されるAPIやサポートが終了したランタイムやライブラリ、フレームワーク」を例示している。
- 組織固有のルールに合わせて、技術的負債検出ポリシーをカスタマイズできる。 [^]
  - Footnote: 記事は「承認済みのライブラリ、内部コーディング標準など技術的負債検出ポリシーのカスタマイズも可能」と述べている。
- AWS Security Agentとの統合により、脆弱性の検出と修正も対象になる。 [^]
  - Footnote: 記事に「AWS Security Agentと統合されているため、ソースコードレベルで脆弱性の検出、修正も行えます」とある。
- 数時間で結果が得られる継続スキャンにより、技術的負債の早期発見が期待されている。 [^]
  - Footnote: 記事は「継続的にコードをスキャンして数時間で結果が得られる」とし、早期発見と計画的対応への期待を述べている。

### References
- https://www.publickey1.jp/blog/26/awsaiaws_transform_continuous_modernization.html

## APERTVS.ai
- Date: 2026-06-15T00:00:00+09:00

### Executive Summary
- APERTVS.aiは、主権AI向けの完全オープンな基盤モデルを掲げるプロジェクトだ。
- Swiss AI Initiativeにより、EPFL、ETH Zurich、CSCSの協働で開発されている。
- サイトは、オープンウェイト、オープンデータ、オープンサイエンスを明示している。
- 訓練データ、コード、重み、手法、アラインメント原則を文書化し、再現可能にする方針を示している。
- EU AI Act要件への適合を意識し、オプトアウト尊重、PII除去、記憶化防止を特徴としている。
- 8Bおよび70B規模相当で、主要なオープンモデルと競合する性能を主張している。
- ニュース欄では、蒸留と量子化の実証を目的に16種の小型言語モデルを公開したと告知している。

### Key Findings
- APERTVS.aiは主権AI向けの完全オープンな基盤モデルとして位置付けられている。 [^]
  - Footnote: ページ冒頭に「Fully Open Foundation Model for Sovereign AI」と記載されている。
- 開発主体はSwiss AI Initiativeで、EPFL、ETH Zurich、CSCSの協働とされる。 [^]
  - Footnote: ページは「Developed by the Swiss AI Initiative as a collaborative effort between EPFL, ETH Zurich, and CSCS」と説明している。
- オープン性は重みだけでなく、データ、コード、手法、アラインメント原則まで含む。 [^]
  - Footnote: ページには「Training data, code, weights, methods, and alignment principles — all documented and reproducible」とある。
- EU AI Actへの適合を意識し、オプトアウト、PII除去、記憶化防止を掲げている。 [^]
  - Footnote: ページは「Built to meet EU AI Act requirements: the model respects opt-outs, removes PII, prevents memorization」と記載している。
- 性能面では8Bと70B相当規模でトップクラスのオープンモデルと競合すると主張している。 [^]
  - Footnote: ページは「Competitive with top open models at an equivalent scale of 8B and 70B parameters」と述べている。
- 多言語対応は初日から1000以上の言語で訓練された点を強調している。 [^]
  - Footnote: ページに「Multilingual from day one — trained on 1000+ languages」とある。
- 最新ニュースとして、Apertus Miniは蒸留と量子化技術の実証用に16種の小型言語モデルを公開した。 [^]
  - Footnote: ニュース欄に「Jun 15 Apertus Mini」と「A set of 16 small language models released to demonstrate distillation and quantization techniques」とある。

### References
- https://apertvs.ai/
