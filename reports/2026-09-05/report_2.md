# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-09-05T09:06:11.7253978+09:00
- Articles: 3

## 「GPT-6 Astra」登場、PC操作が非常に上手で「Blenderで3Dモデルを作ってUE5で歩ける空間にする」なども可能＆ARC-AGI-3で99.9％を達成
- Date: 2026-09-04T12:35:00+09:00

### Executive Summary
- OpenAIが2026年9月3日に新AIモデル「GPT-6 Astra」を発表した。
- PC操作、ブラウジング、プログラミング、科学、サイバーセキュリティで従来モデルを上回る性能をうたう。
- フォーム入力、カレンダー整理、ウェブ調査、サイト制作、ソフトウェアのインストールやテストなどを実行できる。
- Blenderで3Dモデルを作り、Unreal Engine 5へ持ち込む制作デモが紹介された。
- Agents' Last Examでは59.3％を記録し、GPT-5.6 Solの53.6％を上回った。
- ARC-AGI-3ではProvider Adapter harnessで最大99.9％、Standard harnessで62.7％を記録した。
- サイバー分野ではExploitBenchで100％を記録し、安全対策強化も説明されている。
- 記事作成時点では一部組織向けに提供が始まり、今後ChatGPTやAPI、Amazon Bedrockへ展開予定とされる。

### Key Findings
- GPT-6 AstraはPC操作を含む長時間の実作業を重視したモデルとして位置付けられている。 [^]
  - Footnote: 記事は「PC操作やブラウジング、プログラミング、科学、サイバーセキュリティなどで従来のGPT-5.6 Solを上回る性能」と説明している。
- 日常的なPC作業やウェブ作業をエージェントとして実行できる能力が強化された。 [^]
  - Footnote: 本文には「フォームへの入力やカレンダー整理、ウェブ調査、ウェブサイト制作、ソフトウェアのインストールやテストなどを実行できる」とある。
- 業務に近いPC作業ベンチマークでは前世代を上回った。 [^]
  - Footnote: Agents' Last ExamでGPT-6 Astraは59.3％、GPT-5.6 Solは53.6％と記載されている。
- クリエイティブ制作ではBlenderとUnreal Engine 5をまたぐ作業例が示された。 [^]
  - Footnote: 本文は「Blenderでモデル化した家をUnreal Engine 5に持ち込み、歩き回れる状態にしたデモ」と説明している。
- ゲーム制作では手作業の修正削減という実務効果も報告された。 [^]
  - Footnote: PlaycoがGPT-6 Astraを使ったゲーム制作で「従来モデルと比べて手作業による修正が50％減少した」と報告している。
- ARC-AGI-3では条件により非常に高い成績を示した。 [^]
  - Footnote: Provider Adapter harnessでは最高99.9％、Standard harnessでは最高62.7％と記載されている。
- サイバーセキュリティ能力の伸長は安全上の制御強化とセットで扱われている。 [^]
  - Footnote: ExploitBenchで100％を記録し、OpenAIはCritical水準に達した初のモデルとして高度な攻撃につながる要求を制限する対策を強化したとある。
- 提供は段階的で、ChatGPT、API、Amazon Bedrockへの展開が予定されている。 [^]
  - Footnote: 記事は「一部の組織向けに提供が始まっており、今後数日かけてChatGPT Plus、Pro、Business、EnterpriseやOpenAI API、Amazon Bedrockにも展開」と述べている。

### References
- https://gigazine.net/news/20260904-openai-gpt-6-astra/
- https://openai.com/index/gpt-6-astra/

## AI監視カメラを欺け！派手な柄のデジタル迷彩シャツで検出を回避
- Date: 2026-09-04T09:00:00+00:00

### Executive Summary
- AIカメラから人間として認識されにくくする「デジタル・カモフラージュ」シャツが紹介された。
- ドイツ・ベルリンのAI監視カメラ計画を背景に作られた。
- 開発者はベルリン拠点のアーティスト、サイモン・ヴェッカート氏である。
- 模様はAI検知システムに候補を繰り返し見せて調整する敵対的ループで作られた。
- 高彩度の色の切り替わりと重なり合う形で、AIが人物像として結び付ける処理を崩す。
- 検証にはオープンソースのリアルタイム物体検出AI YOLO が使われた。
- ただしベルリン警察が実際に使うシステムで回避できるかは不明と記事は断っている。
- 価格は日本円換算で11,897円からとされ、今後は検知側との改良競争が想定される。

### Key Findings
- シャツはAI監視カメラに人間として認識されることを避ける狙いで設計された。 [^]
  - Footnote: 冒頭で「着るだけでAIカメラから『人間』と認識されなくなるシャツ」と説明されている。
- 開発の直接的背景はベルリンで始まったAI監視カメラの試験運用である。 [^]
  - Footnote: 本文は「2026年8月、警察がベルリンの繁華街で始めたAI監視カメラの試験運用」がきっかけと述べている。
- 人間の目ではなく、機械が見落とす特徴を機械に探させる設計思想が中心にある。 [^]
  - Footnote: ヴェッカート氏は「機械が見落とすポイントを教えてくれるのは機械自身だけだ」と語っている。
- 模様生成には候補生成、検知、評価、再調整を繰り返す敵対的ループが使われた。 [^]
  - Footnote: 記事は「候補の模様を作っては、検知システムに見せ、'人'だと認識しているかを測定し、調整してまた見せる」と説明している。
- 技術的には色と形状の組み合わせで人物の輪郭統合を妨げる。 [^]
  - Footnote: 本文には「彩度の高い切り替わり」は浅い層に影響し、「重なり合う形」は輪郭のつながりを断つとある。
- 検証対象はYOLOであり、実運用中の警察システムそのものではない。 [^]
  - Footnote: 記事は「YOLOは、現地で使われているシステムそのものではない」と明記している。
- 類似のAI対AI型の衣服は以前から存在し、2023年のCap-ableの事例も紹介されている。 [^]
  - Footnote: Cap-ableのニットはYOLOテストで「着用者の6割以上が、シマウマやキリン、犬などと認識された」と書かれている。
- 記事はプライバシー保護ファッションとしての可能性と、検知精度改良との競争を示唆している。 [^]
  - Footnote: 末尾で「プライバシー保護ファッション」として浸透するかに触れつつ、「カメラの精度が改良される」といった競争を予感している。

### References
- https://karapaia.com/archives/626046.html
- https://simonweckert.com/digitalcamouflage.html

## GPT-6 Astra - API Pricing & Providers | OpenRouter
- Date: 2026-09-05T00:00:00Z

### Executive Summary
- OpenRouterのモデルページは、OpenAI: GPT-6 AstraのAPI価格、提供プロバイダー、性能指標を掲載している。
- GPT-6 Astraは高度な分析、ソフトウェアエンジニアリング、深い調査、科学作業、文書作成向けと説明されている。
- 特にコンピューターやブラウザ利用を含む長期的なエージェント作業に強みがあるとされる。
- 表示上の標準価格は入力100万トークンあたり10ドル、出力100万トークンあたり50ドルである。
- コンテキスト長はページ上で1M、メタ説明では1,050,000トークン、最大出力128,000トークンとされる。
- 提供プロバイダーにはOpenAI Flex、Azure、OpenAI、Azure (US)、OpenAI Fastが掲載されている。
- 最良P50のスループットは48 tok/s、最良P50レイテンシは2.77秒と表示されている。
- 過去3日間のOpenRouter側アップタイムは100.00％、可用性は99.35％と示されている。

### Key Findings
- OpenRouterはGPT-6 Astraを高負荷なエンドツーエンド作業向けのフラッグシップモデルとして説明している。 [^]
  - Footnote: ページ本文は「OpenAI's flagship model for demanding end-to-end work」と記載している。
- 主な用途は高度分析、ソフトウェアエンジニアリング、深い調査、科学作業、文書作成である。 [^]
  - Footnote: 説明文に「advanced analysis, software engineering, deep research, scientific work, and document creation」と列挙されている。
- 長期的なエージェント作業、とくにPCとブラウザを使うタスクが強みとされる。 [^]
  - Footnote: 本文には「particular strengths in long-horizon agentic tasks that involve computer and browser use」とある。
- 標準表示価格は入力10ドル、出力50ドルのトークン単価である。 [^]
  - Footnote: ページ上部のIN / OUT PRICEに「$10 / $50 per 1M」と表示されている。
- OpenAI Flexは標準より安い価格を提示している。 [^]
  - Footnote: プロバイダー表ではOpenAI FlexがInput /M $5.00、Output /M $25.00、Cache read /M $0.50と示されている。
- 複数プロバイダーにより価格、速度、稼働率を選べる設計になっている。 [^]
  - Footnote: OpenRouterは同一モデルを複数社がホストし、Balanced、Nitro、Exactoのルーティングモードを選べると説明している。
- OpenRouterの実効平均価格は表示価格より低くなる場合がある。 [^]
  - Footnote: Pricing欄はキャッシュや割引により実際の支払価格が表示価格を下回ることが多いと説明し、Weighted Avg Input Price $2.383、Output Price $49.89を示している。
- 可用性面では過去3日間でOpenRouter側のルーティング効果が示されている。 [^]
  - Footnote: Uptime欄にUptime (3d) 100.00％、Availability (3d) 99.35％、OpenRouter Availability 98.89％、Without Routing 94.63％と表示されている。

### References
- https://openrouter.ai/openai/gpt-6-astra
