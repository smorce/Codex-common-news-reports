# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-07-13T07:00:00+09:00
- Articles: 3

## Adaptive Recall - Adaptive Memory for AI Applications

### Executive Summary
- Adaptive Recall は、AI アプリケーション向けの適応型メモリシステムとして紹介されている。
- 単純なベクトル検索だけでなく、複数の検索戦略を並列に使う点を差別化している。
- 検索結果の順位付けには、ACT-R に基づく認知スコアリングを利用すると説明している。
- 保存された記憶からエンティティと関係を抽出し、知識グラフを自動構築する。
- 記憶は静的な行ではなく、信頼度の変化やアクセス低下による自然な減衰を持つ。
- 利用履歴に基づく ML パイプラインで、検索品質を自己改善する設計を掲げている。
- MCP と HTTP REST の両方で利用でき、無料枠は 500 memories とされている。

### Key Findings
- サービスは「対話ごとに学習する記憶」を中核価値としている。 [^]
  - Footnote: ページ冒頭に「Store, recall, and forget with a memory system that learns from every interaction」と記載。
- 通常のメモリ API との差分として、単一の検索戦略に依存しない点を強調している。 [^]
  - Footnote: 比較表で Standard Memory API は「Single retrieval strategy」、Adaptive Recall は「Four retrieval strategies running in parallel」と対比。
- 検索方式はベクトル類似度、時間的新しさ、全文キーワード、知識グラフ探索の 4 種を並列実行する。 [^]
  - Footnote: Adaptive Retrieval の説明に「vector similarity, temporal recency, full-text keyword, and knowledge graph traversal」とある。
- 認知科学由来の ACT-R モデルで検索結果のランキングを行う。 [^]
  - Footnote: Cognitive Scoring で「ACT-R activation modeling from cognitive science」と説明。
- 記憶は根拠によって信頼度が増減し、アクセスされなくなると薄れていく。 [^]
  - Footnote: Memory Lifecycle で「gain or lose confidence based on corroborating evidence, and fade naturally」と記載。
- 開発者向け API は MCP と REST の両対応で、8 つの操作を提供する。 [^]
  - Footnote: Simple API で「Eight tools: store, recall, update, forget, graph, status, snapshot, feedback」と列挙。

### References
- https://www.adaptiverecall.com/

## Fable gets another bump
- Date: 2026-07-12T21:20:00+00:00

### Executive Summary
- Simon Willison 氏は、Anthropic が Claude Fable 5 の提供期限を再び延長したことを取り上げている。
- 延長対象は有料プラン上の Claude Fable 5 アクセスと、Claude Code の週次レート制限増量である。
- 延長期限は 2026 年 7 月 19 日までとされている。
- Fable 5 は週次利用枠の半分まで利用でき、その後は利用クレジットまたは別モデルへの切替が必要になる。
- Anthropic の背景には、需要と計算資源の見通しを見極めたいという制約があると整理している。
- 一方で OpenAI は GPT-5.6 Sol の利用制限を緩め、効率化と利用リセットを進めていると紹介している。
- 筆者は、不確実なアクセス条件が Anthropic から OpenAI へユーザーを流す要因になっていると見ている。

### Key Findings
- Anthropic は Claude Fable 5 の有料プラン提供を 7 月 19 日まで延長した。 [^]
  - Footnote: 本文で「We're extending Claude Fable 5 access on all paid plans ... through July 19」と引用。
- Claude Code の週次レート制限 50% 増量も同じ期限まで維持される。 [^]
  - Footnote: 同じ引用に「keeping Claude Code’s weekly rate limits 50% higher」とある。
- Fable 5 は週次使用量上限の半分まで利用できる設計である。 [^]
  - Footnote: 本文に「you can use up to half of your weekly usage limit on Fable 5」と記載。
- Anthropic の制限判断は、需要と計算資源の可用性を確認するためと説明されている。 [^]
  - Footnote: 筆者は「compute constraints」とし、需要と compute availability を見たい意図と整理。
- OpenAI は Plus、Business、Pro 向けの 5 時間利用制限を一時的に外している。 [^]
  - Footnote: Tibo 氏の更新として「Temporarily removing the 5 hour usage limit restriction」と引用。
- OpenAI は 600 万アクティブユーザー到達と利用リセットを発表している。 [^]
  - Footnote: 引用内に「We hit 6M active users, and are landing a usage reset」とある。
- 筆者は Fable を恒久的に提供すべきだと主張している。 [^]
  - Footnote: 結論部で「Anthropic should change track and keep Fable permanently available」と述べている。

### References
- https://simonwillison.net/2026/Jul/12/bump/

## アップルがOpenAIを提訴、元従業員による機密情報窃取の疑い | テクノエッジ TechnoEdge
- Date: 2026-07-13T06:45:02+09:00

### Executive Summary
- 記事は、Apple が OpenAI、io Products、元 Apple 従業員 2 名を相手に訴訟を起こしたと報じている。
- 訴訟の争点は、未発表製品に関する営業秘密の不正持ち出し疑惑である。
- Apple は差し止め請求と損害賠償を求めている。
- OpenAI は Jonathan Ive 氏の io Products を約 65 億ドルで買収し、ハードウェア事業を進めている。
- 記事では、OpenAI に 400 人超の元 Apple 社員が在籍しているとも伝えている。
- 訴状では、1000 ページ超の機密情報ダウンロードや PC 未返却など具体的な疑惑が示されている。
- Apple は、Apple Intelligence と ChatGPT 統合のパートナー契約には影響しないと述べている。

### Key Findings
- Apple は OpenAI、io Products、チャン・リウ氏、タン・タン氏を被告として提訴した。 [^]
  - Footnote: 冒頭で「OpenAIおよびその関連会社io Products、元アップル従業員...を被告とする訴訟」と記載。
- 訴訟は米カリフォルニア北部地区連邦地方裁判所に起こされた。 [^]
  - Footnote: 記事冒頭に「米カリフォルニア北部地区連邦地方裁判所に起こしました」とある。
- Apple は未発表製品に関する営業秘密が持ち出されたと主張している。 [^]
  - Footnote: 訴状について「未発表製品に関する営業秘密を不正に持ち出した」と説明。
- OpenAI のハードウェア事業強化が背景として示されている。 [^]
  - Footnote: 記事は io Products の約65億ドル買収と独自ハードウェア事業本格化を説明。
- OpenAI には 400 人超の元 Apple 社員が在籍しているとされる。 [^]
  - Footnote: 本文に「OpenAIにはいまや400人を超える元アップル社員が在籍」と記載。
- チャン・リウ氏には 1000 ページ超の機密情報をダウンロードした疑いがある。 [^]
  - Footnote: 本文に「1000ページ超の機密情報をダウンロードした疑い」とある。
- Apple は取得資料の破棄や製品再設計も求めている。 [^]
  - Footnote: 訴訟では「取得した機密資料の破棄、アップルの技術を使用しない形への製品再設計」を求めると記載。
- OpenAI 側は他社の企業秘密への関心を否定している。 [^]
  - Footnote: ドリュー・プサテリ氏が「他社の企業秘密には一切関心がない」と X で主張したと記事が紹介。

### References
- https://www.techno-edge.net/article/2026/07/13/5284.html
