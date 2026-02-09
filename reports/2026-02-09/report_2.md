# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-02-09T10:36:46.5909859+09:00
- Articles: 3

## From Svedka to Anthropic, brands make bold plays with AI in Super Bowl ads | TechCrunch
- Date: 2026-02-08T08:18:00-08:00

### Executive Summary
- 2026年のスーパーボウル広告はAIの活用自体が主役になった。
- Svedkaは「主にAI生成」の30秒CMでロボキャラを踊らせた。
- Anthropicは「Claudeは広告なし」を掲げ、OpenAIの広告計画を揶揄した。
- Metaはスポーツ向けのOakleyブランドAIグラスを実演した。
- AmazonはAlexa+の強化機能をブラックコメディで紹介した。
- RingはAIとコミュニティで迷子犬を探すSearch Partyを訴求した。
- GoogleやWix、RampなどもAI製品の利用シーンを前面に出した。

### Key Findings
- Svedkaは「primarily AI-generated」な全国向け30秒CM「Shake Your Bots Off」を投入し、FembotとBrobotが登場する。 [^]
  - Footnote: 本文で「first “primarily” AI-generated national Super Bowl spot」「Shake Your Bots Off」「Fembot」「Brobot」と説明。
- SvedkaはFembotの再構築と表情・動作模倣のAI学習に約4カ月を要し、ストーリー作りは人間が担った。 [^]
  - Footnote: 「took roughly four months to reconstruct the Fembot and train the AI」「storyline」部分は人間が担当と記載。
- AnthropicのCMは「Ads are coming to AI. But not to Claude.」を掲げ、OpenAIの広告計画を皮肉った。 [^]
  - Footnote: 本文でタグラインと「OpenAI’s plan to introduce ads to ChatGPT」への言及がある。
- MetaはOakleyブランドのAIグラスをスポーツ・冒険用途として訴求し、IShowSpeedやSpike Leeが出演した。 [^]
  - Footnote: 「Oakley-branded AI glasses」「IShowSpeed」「Spike Lee」「hands-free to Instagram」などの記述。
- AmazonはChris Hemsworth出演の風刺CMでAlexa+を紹介し、Alexa+が全米向けに正式提供されたと記載された。 [^]
  - Footnote: 「Chris Hemsworth」「Alexa+」「officially launched to all U.S. users on Wednesday」とある。
- RingのSearch Party機能は非Ringカメラ利用者にも開放され、1日1件超の迷子犬再会実績が示された。 [^]
  - Footnote: 「anyone can now use Search Party」「more than one lost dog with its owner every day」と記載。

### References
- https://techcrunch.com/2026/02/08/super-bowl-60-ai-ads-svedka-anthropic-brands-commercials/

## Billing can be bypassed using a combination of subagents with an agent definition, resulting in unlimited free premium requests. · Issue #292452 · microsoft/vscode

### Executive Summary
- VS Code Copilotの課金回避を主張するGitHub Issueが公開された。
- 投稿者はサブエージェントとモデル指定の組み合わせで無料枠から高額モデルを使えると述べる。
- Issueには具体的な手順やサンプルのプロンプト/エージェント定義が載っている。
- 別経路として、リクエスト上限やツール呼び出しのループ悪用が示された。
- 投稿者はMSRCに報告したが、公開Issueとして出すよう求められたと書いた。
- ボットがメタIssueへの誘導を行い、一度はnot plannedでクローズされた。
- その後、担当者が再オープンしてラベル付けが更新された。

### Key Findings
- Summaryでは、サブエージェントと無料モデルの組み合わせで「premium request」を回避できると主張している。 [^]
  - Footnote: 「bypass any billing / 'premium request' usage」「free models」「unlimited, usage of expensive premium models」と記載。
- 手順欄では、無料モデルで開始し、プレミアムモデルを指定したエージェントをサブエージェントとして呼ぶ流れを示す。 [^]
  - Footnote: 「Set the model to a "free" model」「Create an agent... premium model」「launch an agent ... runSubagent」とある。
- 例として、プロンプトファイルとエージェント定義ファイルが提示され、無料モデルとプレミアムモデルの組み合わせが示されている。 [^]
  - Footnote: 「.github/prompts/ask-opus.prompt.md」「.github/agents/opus.agent.md」「GPT-5 mini」「Claude Opus 4.5」と記載。
- 別ベクトルとして、リクエスト上限の設定やツール呼び出しループで長時間・大量のサブエージェント実行が可能だと述べる。 [^]
  - Footnote: 「chat.agent.maxRequests」「loop」「3hr+ process」「hundreds of Opus 4.5 subagents」と記載。
- 投稿者はMSRCが課金回避は対象外として、公開バグ報告を求めたと説明している。 [^]
  - Footnote: 「MSRC insisted bypassing billing is outside of MSRC scope... file as a public bug report」とある。
- botがメタIssueへの参照を促し、いったんnot plannedでクローズされた後に再オープンされた履歴がある。 [^]
  - Footnote: イベント欄に「closed this as not planned」「reopened this」が並ぶ。

### References
- https://github.com/microsoft/vscode/issues/292452

## (AI) Slop Terrifies Me – ezhik.jp
- Date: 2026-02-08

### Executive Summary
- 筆者はAIの出力が「90%の十分さ」で止まる未来を恐れる。
- 「good enough to ship」が常態化すると残り10%が見捨てられると懸念する。
- AIはソフト開発を助けるが、学ばずに出荷する人が増えることを怖がる。
- AIは平均的なNext/React/Tailwind的解に寄せ、独自性に弱いと指摘する。
- 低品質ソフトはAI以前からあったが、エージェントでさらに加速すると述べる。
- 多くのユーザーがプライバシーや不具合を気にしない可能性を憂う。
- 結果として職人技的なソフトウェアの文化が消えると悲観する。

### Key Findings
- AIが「90%の完成度」で止まった場合、残り10%を気にしなくなる社会を恐れている。 [^]
  - Footnote: 「You get AI that can make you like 90% of a thing!」「Will you care about the last 10%?」とある。
- 「good enough to ship」が支配し、誰も気にしなくなる状況を強い恐怖として表明する。 [^]
  - Footnote: 「I'm terrified of the "good enough to ship"—and I'm terrified of nobody else caring.」と明記。
- AIは平均的な技術スタックに寄せがちで、独自性のある制作に弱いと述べる。 [^]
  - Footnote: 「median Next-React-Tailwind, good enough app」「off the beaten path」への言及。
- ソフトの「temufication」は単なるコモディティ化より痛いとし、IKEA比喩で語る。 [^]
  - Footnote: 「software temufication stings much more than software commoditization」「standing in the middle of an IKEA」とある。
- インセンティブの結果として低品質が生まれ、AIエージェントでその速度が上がると指摘する。 [^]
  - Footnote: 「Move fast and break things」「agent herders can do the same thing much faster」と記載。
- 多くの人がプライバシーや不具合を気にせず、職人技が消える未来を危惧している。 [^]
  - Footnote: 「people truly just don't care about tech problems, about privacy...」「our craft will die」とある。

### References
- https://ezhik.jp/ai-slop-terrifies-me/
