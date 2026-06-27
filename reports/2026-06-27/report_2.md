# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-06-27T09:03:48+09:00
- Articles: 3

## GitHub - neospe/autofit2: Automated end-to-end data preprocessing, model training, and evaluation pipeline

### Executive Summary
- autofit2 は少数ラベルでのテキスト分類を自動化する GitHub リポジトリである。
- SetFit と SBERT 埋め込みを基盤に、few-shot text classification を扱う。
- README では 50 以上の言語に対応する多言語性が主な特徴として示されている。
- 単一の JSON 設定から前処理、微調整、評価、デプロイまでを実行する設計である。
- 出力にはデプロイ可能なモデルアーカイブとモデルカードが含まれる。
- 設定ファイルは base、targets、loader などのブロックで構成される。
- 再現性、透明性、CO2 排出量追跡を含む点が実運用向けの特徴である。

### Key Findings
- 少数のラベル付き例から高精度な分類器を作ることを狙う。 [^]
  - Footnote: README に「Few-Shot Learning: High precision (95-99%) with a few dozen labeled examples」とある。
- 多言語対応が主要な訴求点である。 [^]
  - Footnote: README に「Multilingual Support: Pretrained models for 20 languages; evaluation corpora for 50+」と記載されている。
- 処理は JSON 設定を起点とした一括実行を前提にしている。 [^]
  - Footnote: README は「Automated Pipeline: End-to-end preprocessing, fine-tuning, evaluation, and deployment from a single JSON config」と説明している。
- モデルカード生成と CO2 排出量追跡により透明性を確保する。 [^]
  - Footnote: README の Key Features に「model card generation, and CO2-emission tracking」とある。
- 実行コマンドは設定ファイルを train.py に渡す単純な形である。 [^]
  - Footnote: Usage では「python train.py myproject.json」と示されている。

### References
- https://github.com/neospe/autofit2
- https://ai-news.dev/

## 「+65」から始まる番号から不審な電話がありAIに「調べて」とお願いしたら急に通話発信をしはじめて焦った話
- Date: 2026-06-27T03:00:00+09:00

### Executive Summary
- +65 から始まる不審な電話番号を AI に調べさせた体験談をまとめた Togetter 記事である。
- 投稿者は Gemini Pro に調査を頼んだところ、意図せず通話発信が始まったと述べている。
- AI がスマートフォンの通話機能に触れる場合、ユーザーの意図確認が重要になる。
- 記事内では電話権限やアプリ連携をオフにする対策が話題になっている。
- 同様の体験談として、AI への曖昧な指示が実操作に変換されるリスクも共有されている。
- AI の回答内容だけでなく、端末権限と実行可能操作の管理が安全性の焦点である。
- ユーザー側には AI アプリの権限設定を見直す必要がある。

### Key Findings
- 不審番号の調査依頼が通話発信に変わったことが中心的な問題である。 [^]
  - Footnote: 本文に「+65から始まる不審電話」「その電話番号に通話発信」といった投稿内容が掲載されている。
- 投稿者は AI の挙動を危険視し、他者にも注意を促している。 [^]
  - Footnote: 本文には「絶対に折り返し連絡は行わないようご注意ください」という趣旨の注意喚起がある。
- Gemini そのものへの評価ではなく、端末権限との組み合わせが論点になっている。 [^]
  - Footnote: 投稿者は「Gemini さんが大嫌い、二度と使わないというつもりは無い」と補足している。
- 電話権限の無効化が実務的な対策として示されている。 [^]
  - Footnote: ai-news.dev のカード要約に「対策として電話権限をオフにする設定が勧められる」とある。
- 類似事例として、AI への文章指示が実際の電話操作につながる例が共有されている。 [^]
  - Footnote: 本文には「警察に電話をかける」に反応し、受付の自動音声が流れたという体験談が含まれる。

### References
- https://togetter.com/li/2713993
- https://ai-news.dev/

## OpenAI、次世代AIモデル「GPT-5.6」発表、まず米国政府承認ユーザーに限定プレビュー開始
- Date: 2026-06-27T06:30:00+09:00

### Executive Summary
- TechnoEdge は OpenAI が GPT-5.6 シリーズを発表したと報じている。
- シリーズは Sol、Terra、Luna の 3 種類で構成される。
- 提供はまず米国政府承認ユーザーや信頼できるパートナー向けの限定プレビューから始まる。
- 一般公開は数週間以内を目指す段階的リリースとして説明されている。
- Sol は最高性能モデルとして推論、コーディング、科学、セキュリティ領域を重視する。
- Terra は性能と価格のバランス、Luna は低価格と高速性を担う位置づけである。
- API、Codex、ChatGPT での提供や Cerebras 上での高速提供計画にも触れている。

### Key Findings
- GPT-5.6 は Sol、Terra、Luna の 3 モデル構成で発表された。 [^]
  - Footnote: 本文に「Sol」「Terra」「Luna」の 3 種類を発表したと記載されている。
- 初期提供は限定プレビューであり、一般公開は段階的に行う計画である。 [^]
  - Footnote: 本文に「信頼できるパートナー企業・組織を対象」「数週間以内に一般公開を計画」とある。
- Sol は最高性能モデルとして位置づけられている。 [^]
  - Footnote: 本文は GPT-5.6 Sol を「OpenAI がこれまでで最も高性能なモデル」と説明している。
- 安全対策としてリアルタイム検出や監視・審査機構が説明されている。 [^]
  - Footnote: 本文には「リアルタイムで検出するクラシファイア」や「アカウントレベルでの横断的な監視・審査機構」とある。
- 価格は 100 万トークンあたりで、Sol、Terra、Luna に差が設けられている。 [^]
  - Footnote: 本文に「Sol: 入力 $15 / 出力 $30」「Terra: 入力 $2.50 / 出力 $15」「Luna: 入力 $1 / 出力 $6」とある。

### References
- https://www.techno-edge.net/article/2026/06/27/5229.html
- https://ai-news.dev/
