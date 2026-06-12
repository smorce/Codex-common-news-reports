# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-06-12T09:04:51+09:00
- Articles: 3

## Discover — FablePool

### Executive Summary
- FablePoolは、大きなプロンプトに複数人が資金を出し合い、AIエージェントが公開で実行する仕組みを提示している。
- 支援者は少額から参加でき、プロジェクトの資金と進捗は公開台帳で見える形にされる。
- 資金目標はAIプランナーが設定し、合計100ドル以上のプロジェクトを前提にしている。
- 実行はマイルストーン単位で進み、AIが段階的に成果物を作る設計になっている。
- 掲載中のプロジェクトにはC#のHFT向けGC、PID調整ライブラリ、AWS互換のオープンソース実装などがある。
- 各案件には調達額、推定目標額、賛成票、ステータスが表示され、参加判断に必要な情報が整理されている。
- 一部案件はACTIVE、一部はAWAITING FUNDINGで、資金到達前のアイデアも一覧化されている。

### Key Findings
- FablePoolはクラウドファンディングとAI実行を組み合わせた公開型プロジェクト基盤である。 [^]
  - Footnote: 本文に「Pool money behind a big prompt. An AI attempts the build, in public.」とある。
- 支援者は0.25ドルから参加でき、出資のハードルを低くしている。 [^]
  - Footnote: 本文に「backers chip in any amount from $0.25」とある。
- プロジェクトの資金目標はAIプランナーが設定する。 [^]
  - Footnote: 本文に「Funding targets are set by the AI planner」とある。
- 実行は一括ではなく、マイルストーンごとに進む。 [^]
  - Footnote: 本文に「carries it out milestone by milestone」とある。
- 出資や進捗は公開台帳で透明化される。 [^]
  - Footnote: 本文に「with every credit on a public ledger」とある。
- 実際の掲載案件には技術系のオープンソース開発や研究寄りのテーマが多い。 [^]
  - Footnote: 一覧に「Solve Garbage Collection in C# for HFT」「Open-source PID tuning python library」「Build a completely greenroom, open source AWS」が表示されている。

### References
- https://fablepool.com/

## If You are Asking for Human Attention, Demonstrate Human Effort | Tom Bedor's Blog
- Date: 2026-06-11T00:00:00+00:00

### Executive Summary
- この記事は、AI生成物を他人に読ませるときのチーム内エチケットを扱っている。
- デバッグ調査、文書作成、コード作成でAI出力が増え、人間の読む負担が問題になっている。
- 著者は、未消化のAI出力を自分の文章のように共有することは配慮に欠けると述べる。
- きっかけとして、同僚が読んでいないAI批評文を送り、著者が違和感を覚えた経験が示されている。
- 中心原則は「人間の注意を求めるなら、人間の努力を示すべき」というものだ。
- AI生成コンテンツを共有する場合は、AI生成であることを明示し、自分のコメントを添えるべきだとしている。
- コードレビューでは、AIが生成したコードを人に依頼する前に自分で確認することが必要だと結論づけている。

### Key Findings
- AI生成物の増加により、ソフトウェア開発者の読む負担が増している。 [^]
  - Footnote: 本文に「debug investigations, document writing, and code is written by robots」とある。
- AI出力は有用な場合もあるが、そのまま人に渡すと疲労や不快感を生む。 [^]
  - Footnote: 本文に「often produces genuinely useful output」と「a fatigue sets in」が並んでいる。
- 読んでいないAI文書を他人に読むよう求める行為は、注意資源への配慮を欠く。 [^]
  - Footnote: 著者は「I didn't read this」と添えられたAI文書を受け取り、「why is it worth mine?」と感じたと述べている。
- 著者の原則は、人間の注意を求めるなら人間の努力を示すことだ。 [^]
  - Footnote: 本文に「If you are requesting human attention, demonstrate human effort.」と明記されている。
- AI生成コンテンツを共有する際は、ラベル付けと自分のコメントが必要だ。 [^]
  - Footnote: 本文に「clearly label what is AI generated, and I add my own commentary」とある。
- AI生成コードのレビュー依頼前には、依頼者自身の事前レビューが必要である。 [^]
  - Footnote: 本文に「I always review my AI-generated code first」とある。

### References
- https://tombedor.dev/human-attention-and-human-effort/

## 使える図解がコピペで揃う！ 『ブログ図解ジェネレーター』のログイン配布します！｜ひつじ
- Date: 2026-06-02T19:23:00+09:00

### Executive Summary
- この記事は、ブログ本文から図解作成用プロンプトを生成する「ブログ図解ジェネレーター」の公開案内である。
- 著者は過去に画像用プロンプトジェネレーターとスライドジェネレーターを公開しており、その延長として図解ツールを作った。
- 課題意識は、ブログ記事には図解が欲しいが、作成に時間がかかるという点にある。
- 使い方は、原稿内の図解を入れたい位置に[図解]タグを置き、全文をツールに貼り付ける流れだ。
- ツールはタグ位置や見出しをもとに図解候補を作り、選択したデザインに合わせたプロンプトを出力する。
- 対応スタイルにはフラット、アイソメトリック、3D、キャラクター解説などが含まれる。
- ツールはnoteメンバー向けに公開され、記事後半の具体的なログイン・操作解説はメンバーシップ領域に置かれている。

### Key Findings
- ツールの目的は、記事本文を貼るだけで世界観のそろった図解をまとめて作ることだ。 [^]
  - Footnote: 本文に「記事の本文を貼るだけで、世界観のそろった図解を一気に組み立てられるツール」とある。
- 図解の挿入位置は、原稿中の[図解]タグで指定できる。 [^]
  - Footnote: 本文に「図解が欲しい場所に[図解]のマークを入れておく」とある。
- 原稿全文をコピペすると、図解候補が自動登録される。 [^]
  - Footnote: 本文に「その原稿をツールに貼り付けると、[図解] を打った場所が『図解の差し込み位置』として自動で登録」とある。
- [図解]タグがなくても、H2やH3の見出しから生成対象を検出できる。 [^]
  - Footnote: 本文に「もし[図解]タグがなくてもH2タグ（##）やH3タグ（###）があれば自動検出」とある。
- デザインタイプは複数あり、用途や好みに応じて選べる。 [^]
  - Footnote: 本文に「フラットイラスト」「アイソメトリックイラスト」「3Dイラスト」「キャラクター解説」が列挙されている。
- 貼り付けたブログ内容は保存や学習に使わないと説明されている。 [^]
  - Footnote: 本文に「貼り付けたブログ内容は、保存も学習もされません」とある。
- 公開範囲はnoteメンバー向けで、記事後半は有料メンバーシップに含まれる。 [^]
  - Footnote: 本文に「noteメンバー向けに公開」とあり、後半に「メンバーシップ ¥780/月」と表示されている。

### References
- https://note.com/hituji1234/n/n5e436a50d138
