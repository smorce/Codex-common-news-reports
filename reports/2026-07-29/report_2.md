# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-07-29T09:06:10.7351965+09:00
- Articles: 3

## AI検索「Perplexity」もCLIに、コマンドラインツールやエージェントとの連携に - 窓の杜
- Date: 2026-07-28T18:13:00+09:00

### Executive Summary
- Perplexityが検索APIをターミナルから扱うCLIツール「pplx」を発表した。
- 検索結果やWebページ内容を整形済みJSONとして出力できる点が中心機能である。
- 他のCLIツールとの連携だけでなく、コーディングエージェントのツール呼び出しにも向く。
- 対応環境は現時点でmacOSのApple SiliconとLinuxのx86_64/arm64に限られる。
- 利用にはPerplexityのAPIキーが必要で、インストールはcurl経由で案内されている。
- 主なコマンドはWeb検索とページ内容取得の2系統に整理されている。
- ページ取得ではタイトル、説明、著者、公開日、ドメイン、ペイウォール情報なども得られる。

### Key Findings
- Perplexity CLIは同社の検索APIをターミナルから利用するためのツールである。 [^]
  - Footnote: 記事本文に「同社の検索APIをターミナルから利用できるコマンドラインツール」とある。
- 出力形式はJSONで、検索結果やページ内容を機械処理しやすい形にできる。 [^]
  - Footnote: 記事本文に「検索結果やWebページの内容を整形されたJSONとして出力」とある。
- コーディングエージェントとの連携が想定ユースケースに含まれている。 [^]
  - Footnote: 記事本文に「コーディングエージェントにとっても扱いやすい」とある。
- 対応OSはmacOS Apple SiliconとLinux x86_64/arm64である。 [^]
  - Footnote: 記事本文に「macOS（Apple Silicon）、Linux（x86_64/arm64）で利用可能」とある。
- 利用にはPerplexityのAPIキーが必要である。 [^]
  - Footnote: 記事本文に「利用の際は『Perplexity』のAPIキーが必要」とある。
- 主要コマンドはWeb検索とページ内容取得に分かれている。 [^]
  - Footnote: 記事本文に「pplx search web」と「pplx content fetch」の2種類が示されている。

### References
- https://forest.watch.impress.co.jp/docs/news/2128588.html

## Pacing the Frontier

### Executive Summary
- フロンティアAI企業の従業員1134人による声明として公開されている。
- AIは大きく良い未来を作り得るが、その結果は保証されないと警告している。
- 主要AI企業はAI研究の自動化に近づいている可能性があると述べている。
- 研究自動化が能力開発を急加速させ、理解や制御を超えるリスクがあるとする。
- 社会がリスク対応、安全対策、監督強化の時間を買う選択肢を持つ必要性を訴えている。
- 個社や各国には単独で減速しにくい競争圧力があると位置づけている。
- 米国政府に対し、国際的な技術・ガバナンス整備の支援を求めている。

### Key Findings
- 声明はフロンティアAI企業の従業員1134人によるものとされる。 [^]
  - Footnote: ページ冒頭に「A statement from 1,134 employees of frontier AI companies」とある。
- AIの便益は大きいが、望ましい未来が自動的に実現するとは見ていない。 [^]
  - Footnote: 本文に「AI could help create a dramatically better future, but that outcome is not guaranteed」とある。
- 主要企業がAI研究の自動化に近づいているという認識が示されている。 [^]
  - Footnote: 本文に「leading AI companies believe they could be close to automating AI research」とある。
- 能力開発が理解や制御を超えて加速するリスクを懸念している。 [^]
  - Footnote: 本文に「capability development rapidly accelerates beyond our ability to understand or control」とある。
- 安全対策や監督を強めるために時間を確保する必要があると主張している。 [^]
  - Footnote: 本文に「buy time to address emerging risks, develop security measures, and strengthen oversight」とある。
- 競争圧力により、企業や国が単独で減速することは難しいとする。 [^]
  - Footnote: 本文に「intense competitive pressure not to unilaterally slow that acceleration」とある。
- 米国政府に国際的なペース管理の取り組み支援を求めている。 [^]
  - Footnote: 本文に「U.S. government support an international effort」とある。

### References
- https://www.pacingthefrontier.com/

## ChatGPTが著名作家の正確な文体模倣を拒否へ。しかし特徴や雰囲気を捉えた文章なら出力可能 | テクノエッジ TechnoEdge
- Date: 2026-07-29T06:45:02+09:00

### Executive Summary
- ChatGPTが著名作家の文体を直接模倣する依頼を拒否するようになったと報じている。
- 以前は存命作家と故人で扱いに差があったが、最近の調査では故人も含めて拒否したという。
- 拒否対象は「スタイルを正確に」模倣する依頼である。
- 代替として、作品に見られる特徴や雰囲気を取り入れた文章を提案する挙動が紹介されている。
- 米国著作権法では抽象的な文体自体は一般に保護対象ではないと説明している。
- ただし生成物が原作と実質的に類似すれば著作権侵害になり得ると指摘している。
- OpenAIが複数の著作権訴訟に直面する中で、この運用変更の法的意味が注目される。

### Key Findings
- ChatGPTは著名作家の文体を直接模倣する依頼を拒否する方向に変わったとされる。 [^]
  - Footnote: 記事冒頭に「著名作家の文体を直接模倣するよう求めるリクエストを断るようになった模様」とある。
- 以前の調査では存命作家と故人で拒否挙動に差があった。 [^]
  - Footnote: 本文に「存命の作家の文体を模倣した文章の作成は拒否する一方で、すでに死去した作家であれば模倣の要求を拒むことはありませんでした」とある。
- Ars Technicaの最近の調査では存命か故人かに関わらず拒否したとされる。 [^]
  - Footnote: 本文に「存命か故人かに関わらず著名作家の模倣文章を出力することを拒否した」とある。
- ChatGPTは正確な模倣ではなく特徴や雰囲気を取り入れる代替案を示す。 [^]
  - Footnote: 本文に「特徴を取り入れ、雰囲気的に似た文章にすることを提案」とある。
- 米国著作権法では抽象的な文体までは一般に保護しないと説明されている。 [^]
  - Footnote: 本文に「著者のより抽象的な文体までは保護しません」とある。
- 生成物が原作者の作品と実質的に類似すると侵害リスクがある。 [^]
  - Footnote: 本文に「原作者の作品と『実質的に類似』していると判断される場合には、著作権侵害にあたる可能性」とある。
- OpenAIは作家団体やメディアなどから複数の著作権訴訟に直面している。 [^]
  - Footnote: 本文に「著名な作家たちの組合や、New York Times、ブリタニカ百科事典などから起こされた様々な著作権侵害訴訟」とある。

### References
- https://www.techno-edge.net/article/2026/07/29/5342.html
