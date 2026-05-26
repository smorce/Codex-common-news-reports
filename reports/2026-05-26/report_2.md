# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-05-26T13:10:00+09:00
- Articles: 3

## Runwayが動画編集AI「Aleph 2.0」をリリース、動画の一部分を編集すると残りはAIが自動で編集してくれる
- Date: 2026-05-25T10:53:00+09:00

### Executive Summary
- Runwayは動画編集AI「Aleph 2.0」と編集ツール「Edit Studio」を公開した。
- Aleph 2.0は1080p、30秒の動画編集に対応する。
- 編集対象の一部分だけを変更し、動画全体の一貫性を保てる点が特徴である。
- 1フレームの編集済み画像を入力し、動画全体へ変更を適用できる。
- Edit Studioでは変更内容を画像でプレビューしながら編集できる。
- 編集済みフレームは画像編集AIやローカル画像アップロードで用意できる。
- Aleph 2.0とEdit StudioはいずれもRunwayの有料会員向けに提供される。

### Key Findings
- Runwayは動画編集AIと専用編集ツールを同時にリリースした。 [^]
  - Footnote: 記事本文に「Runwayが動画編集AI『Aleph 2.0』と動画編集ツール『Edit Studio』をリリースしました」とある。
- Aleph 2.0は短尺の高解像度動画編集を対象にしている。 [^]
  - Footnote: 記事本文に「Aleph 2.0では1080p・30秒の動画を編集可能」と記載されている。
- 部分編集を動画全体へ自然に波及させる機能が中心である。 [^]
  - Footnote: 記事本文は「編集したい部分だけを的確に変更」でき、「1フレームの編集済み画像を入力するだけで動画全体に編集を適用」と説明している。
- 服の色や手に持つ物、動画全体のスタイル変更などに対応する。 [^]
  - Footnote: 記事本文に「手に持っている物を変更」「服の色を変更」「動画全体をアニメ風に変更」といった例が挙げられている。
- Edit Studioはプレビューを見ながら作業できる編集環境である。 [^]
  - Footnote: 記事本文に「Edit Studioでは変更内容を画像でプレビューしながら編集作業を実行できます」とある。
- 編集済みフレームの作成には外部画像編集AIも使える。 [^]
  - Footnote: 記事本文に「GoogleのNano Banana ProやOpenAIのGPT Image 2を使用可能」と記載されている。
- 提供対象はRunwayの有料会員に限定される。 [^]
  - Footnote: 記事本文に「Aleph 2.0とEdit StudioはRunwayの有料会員向けに公開されています」とある。

### References
- https://gigazine.net/news/20260525-runway-aleph-video-edit-ai/
- https://runwayml.com/product/aleph-2

## Harness, Scaffold, and the AI Agent Terms Worth Getting Right
- Date: 2026-05-25T00:00:00Z

### Executive Summary
- Hugging Faceの記事は、AIエージェント分野で混同されやすい用語を整理している。
- 対象は包括的な辞書ではなく、実務で議論がずれやすい概念に絞られている。
- モデル、スキャフォールド、ハーネス、エージェントの関係を明確に分けて説明する。
- ハーネスは実行層、スキャフォールドはモデルの行動を形作る周辺設定として扱われる。
- エージェントはモデル単体ではなく、行動ループを持つシステム全体として説明される。
- コンテキスト設計、ツール利用、スキル、サブエージェントも実務上の重要語として扱われる。
- 後半ではRL環境、トレーナー、ロールアウト、報酬など学習側の語彙も整理している。

### Key Findings
- AIエージェント分野では語彙の変化が速く、共通理解が追いついていない。 [^]
  - Footnote: 記事冒頭で、分野の進化が速いと語彙が共有理解より速く変化し、用語が曖昧になると説明している。
- 記事の目的は、混同されやすい用語に実用的なメンタルモデルを与えることにある。 [^]
  - Footnote: 本文に「包括的な辞書ではなく、混同・再利用・自明視されがちな概念に焦点を当てる」とある。
- モデル単体には記憶もループもなく、ツール実行にはハーネスが必要である。 [^]
  - Footnote: Model節で、LLMは入力から出力を返すだけで、単体ではメモリやループを持たず、ツール実行にはハーネスが必要だと説明している。
- スキャフォールドはシステムプロンプト、ツール説明、応答解析、文脈管理などの行動定義層である。 [^]
  - Footnote: Scaffolding節に「system prompt, tool descriptions, how the model's responses get parsed, what it remembers across steps」とある。
- ハーネスはモデル呼び出し、ツール呼び出し処理、停止判断を担う実行層である。 [^]
  - Footnote: Harness節で「it calls the model, handles its tool calls, decides when to stop」と定義している。
- LLMエージェントは、応答するだけのモデルを行動するループへ変える全体システムである。 [^]
  - Footnote: Agent節で、エージェントは情報を取り込み、次の行動を決め、結果に基づいて動くループへ変換すると説明している。
- ツール、スキル、サブエージェントは似ているが抽象度が異なる。 [^]
  - Footnote: Tool Use、Skills、Sub-agents節で、ツールは外部操作、スキルは複数ステップの知識パッケージ、サブエージェントは独立して推論する別エージェントと整理している。
- 学習側ではロールアウトと報酬が、エージェント改善の基礎データになる。 [^]
  - Footnote: Training節とRollout、Reward節で、実行結果を記録し、報酬を使ってモデル重みを更新すると説明している。

### References
- https://huggingface.co/blog/agent-glossary

## What ClickUp's mass layoff tells us about the future of work | TechCrunch
- Date: 2026-05-25T09:00:00-07:00

### Executive Summary
- TechCrunchはClickUpの大規模レイオフを、AI導入と将来の働き方の事例として報じた。
- ClickUpのCEO Zeb Evansは、22%の人員削減をコスト削減ではなくAI活用への転換と位置づけた。
- 同社はAIで大きな成果を出す従業員に高い報酬を与える方針を示している。
- ClickUpは約3,000体の社内AIエージェントを導入し、従業員は出力の指示と確認を担う。
- EvansはAIによってClickUpを「100x org」にする構想を掲げている。
- 一方でGartner調査は、自律技術を使う企業の多くが人員削減しても財務成果に直結していないと示す。
- 記事は、AIで仕事を自動化できる人が残る一方、組織に必要な人数が減る可能性を示している。

### Key Findings
- ClickUpはAI推進を理由に大規模な人員削減を実施した。 [^]
  - Footnote: 記事本文に、ClickUpが従業員の22%をレイオフし、CEOがそれをコスト削減ではなくAIへの急進的な適応と位置づけたとある。
- CEOはAI活用者への報酬を従来の給与帯外へ広げる考えを示した。 [^]
  - Footnote: Evansの投稿として「million-dollar salary bands」や、AIで大きなインパクトを出す人を従来のバンド外で支払う趣旨が引用されている。
- ClickUpは社内業務向けに約3,000体のAIエージェントを導入している。 [^]
  - Footnote: 記事本文に、Fortuneの記事によればClickUpが従業員のために幅広い複雑なタスクを処理する約3,000体の内部AIエージェントを導入したとある。
- 従業員の役割は、AIエージェントを指示し出力品質を確認する方向へ変わっている。 [^]
  - Footnote: 記事本文に、スタッフは自分で作業する代わりにエージェントを指示し、会社基準に合うか出力を確認することが期待されているとある。
- ClickUpはAIで組織生産性を大幅に引き上げる構想を掲げている。 [^]
  - Footnote: 記事本文は、Evansの目標がAIでClickUpを「100x org」にすることだと説明している。
- AI導入に伴う人員削減はClickUpだけの現象ではない。 [^]
  - Footnote: 記事本文は、Gartner調査で自律技術を使う企業の約80%が雇用を削減したと紹介している。
- ただし人員削減が必ず財務成果に結びつくとは限らない。 [^]
  - Footnote: 記事本文は、Gartnerの調査結果として人員削減が意味のある財務リターンに必ずしも変換されていないと述べている。
- AI活用の評価指標としてトークン消費量を見る動きには批判がある。 [^]
  - Footnote: 記事本文は、従業員のトークン消費をAI採用の指標にする企業が増える一方、単にAI費用を積み上げるだけだという批判を紹介している。

### References
- https://techcrunch.com/2026/05/25/what-clickups-mass-layoff-tells-us-about-the-future-of-work/
