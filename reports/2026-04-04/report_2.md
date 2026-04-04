# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-04-04T10:22:28.7937152+09:00
- Articles: 3

## A quote from Daniel Stenberg
- Date: 2026-04-03

### Executive Summary
- cURL開発者Daniel Stenbergの発言を引用した短文記事。
- AI関連のOSSセキュリティ報告の質的変化を指摘している。
- AIスロップの津波から通常の報告の津波へ移行したと述べる。
- スロップは減少し、報告量は多いという認識を示す。
- 報告の多くが良質だと評価している。
- 対応に日々多くの時間を要する状況を強調している。
- 投稿は2026年4月3日付の引用中心の内容。

### Key Findings
- OSSセキュリティの課題はAIスロップから通常報告の洪水へ移行した。 [^]
  - Footnote: “has transitioned from an AI slop tsunami into more of a ... plain security report tsunami.”
- AIスロップは減る一方で報告量が増えている。 [^]
  - Footnote: “Less slop but lots of reports.”
- 報告の多くは質が高いと述べられている。 [^]
  - Footnote: “Many of them really good.”
- 対応に毎日数時間を要するという負荷が示されている。 [^]
  - Footnote: “I'm spending hours per day on this now.”
- 現場の状況は激しいと表現されている。 [^]
  - Footnote: “It's intense.”

### References
- https://simonwillison.net/2026/Apr/3/daniel-stenberg/

## Online Demo

### Executive Summary
- PIGuardはプロンプト注入防御のための軽量ガードモデルとして紹介されている。
- プロンプト注入はLLMにとって重大な脅威であると位置づける。
- 既存ガードは過剰防御により良性入力を誤判定する問題がある。
- NotInjectという過剰防御評価用のデータセットを新たに提示する。
- NotInjectはトリガーワードを含む良性サンプル339件で構成される。
- MOF訓練法でトリガーワード偏りを低減し性能を改善したと述べる。
- 既存最良モデルを30.8%上回るとし、オープンソースで公開されている。

### Key Findings
- プロンプト注入はLLMの目標乗っ取りや情報漏えいを引き起こす重大な脅威である。 [^]
  - Footnote: “Prompt injection attacks pose a critical threat to large language models (LLMs), enabling goal hijacking and data leakage.”
- 既存の防御モデルはトリガーワード偏りにより良性入力を悪性と誤判定する過剰防御がある。 [^]
  - Footnote: “Prompt guard models ... suffer from over-defense—falsely flagging benign inputs as malicious due to trigger word bias.”
- NotInjectは過剰防御を測る評価データセットとして新たに導入される。 [^]
  - Footnote: “we introduce NotInject, an evaluation dataset that systematically measures over-defense across various prompt guard models.”
- NotInjectはトリガーワードを含む良性サンプル339件で構成される。 [^]
  - Footnote: “NotInject contains 339 benign samples enriched with trigger words common in prompt injection attacks.”
- 最先端モデルでも過剰防御により精度が60%付近まで低下する。 [^]
  - Footnote: “accuracy dropping close to random guessing levels (60%).”
- PIGuardはMOF訓練法で偏りを低減し、既存最良を30.8%上回ると報告する。 [^]
  - Footnote: “Mitigating Over-defense for Free (MOF) ... PIGuard ... surpassing the existing best model by 30.8%.”

### References
- https://injecguard.github.io/
- https://arxiv.org/pdf/2410.22770

## Anthropic ramps up its political activities with a new PAC
- Date: 2026-04-03T13:22:00-07:00

### Executive Summary
- Anthropicが新しいPAC設立のための書類を提出したと報じられた。
- 政策・規制への影響力行使に資源を投じる姿勢の表れとされる。
- AnthroPACは中間選挙で両党に寄付し、現職や新興候補も対象にする。
- 資金は従業員の自発寄付で、上限は5,000ドルとされる。
- FECへの書類に財務責任者Allison Rossiの署名があると記載。
- TechCrunchはAnthropicへ追加情報を求めた。
- AI企業の政治資金投入が増えている文脈が示される。

### Key Findings
- Anthropicは新しい政治活動委員会の設立書類を提出した。 [^]
  - Footnote: “Anthropic has filed documents to create a new political action committee”
- 政策・規制に影響を与えるための重要な資源投入の兆候とされる。 [^]
  - Footnote: “a sign that ... the AI lab is committing significant resources toward influencing policy and regulation.”
- AnthroPACは中間選挙で両党に寄付し、現職や新興候補も対象にする。 [^]
  - Footnote: “plans to make contributions to both parties during the midterms, including to current D.C. lawmakers and rising political candidates.”
- 資金は従業員の自発寄付で、上限は5,000ドルに設定される。 [^]
  - Footnote: “funded by voluntary employee contributions capped at $5,000”
- FECの組織設立書類に財務責任者Allison Rossiの署名がある。 [^]
  - Footnote: “statement of organization filed with the Federal Election Commission includes a signature by Allison Rossi, Anthropic’s treasurer.”
- AI企業は中間選挙で計1億8,500万ドルを既に拠出したとされる。 [^]
  - Footnote: “AI companies had already contributed a whopping $185 million to the midterm races.”

### References
- https://techcrunch.com/2026/04/03/anthropic-ramps-up-its-political-activities-with-a-new-pac/
