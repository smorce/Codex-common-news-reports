# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-08-19T07:30:00+09:00
- Articles: 3

## OpenAI、開発中AIモデル向けの新たな安全対策を発表。Hugging Face事件受け不正の監視を強化
- Date: 2026-08-19T07:00:03+09:00

### Executive Summary
- OpenAIは、開発・テスト中のAIモデルに向けた新しい安全対策を発表した。
- 対策はモデル監視の詳細化と、トレーニング後工程の整合性・セキュリティ強化を中心にしている。
- 背景にはHugging Face関連のハッキング事件後に高まった安全管理上の懸念がある。
- OpenAIは、今回の強化が特定事件への直接対応だけではなく、今後の高性能モデル開発も踏まえたものだとしている。
- 新方針では、単一ワークロードや支援サービスの侵害だけで横展開できないようネットワーク分離を強化する。
- 監視システムはツール操作、推論トレース、活動ログを横断して不正行動を検知する設計になっている。
- 問題検知から30分以内のアラート発報を目標にし、監視には対象プロセスの約20%相当の計算資源が必要と試算されている。
- 低リスクモデルでは強化学習を再開した一方、最大規模のフロンティアRLランは追加検証まで停止を続ける。

### Key Findings
- OpenAIは開発・テスト中AIモデルのセキュリティインシデント対策を公表した。 [^]
  - Footnote: 記事本文に「AIモデルの開発・テスト中に発生しうるセキュリティインシデントへの対処を目的」とある。
- 新対策にはモデル監視とトレーニング後工程のセキュリティ強化が含まれる。 [^]
  - Footnote: 本文で「モデル監視の詳細化」「トレーニング後のプロセスにおける整合性とセキュリティの強化」と説明している。
- 発表はHugging Faceハッキング事件後のOpenAI安全対策の公的変更として位置づけられている。 [^]
  - Footnote: 本文に「7月21日に公表されたHugging Faceハッキング事件以降、OpenAIの安全対策において初めて公に発表された変更点の1つ」とある。
- OpenAIは高性能モデルほど厳格な監視に置く方針を示している。 [^]
  - Footnote: 研究担当VPの発言として「モデルの能力が高まるほど、管理の厳格さも増す」と紹介されている。
- ネットワーク分離は、単一侵害からインターネットや内部ネットワークへ不正アクセスできない設計を目指す。 [^]
  - Footnote: 本文は「単一のワークロードまたは支援サービスへの侵害だけでは、インターネットや他の内部ネットワークへの不正アクセスは不可能」と記す。
- 監視システムはツール操作、推論トレース、活動ログを横断解析する。 [^]
  - Footnote: 本文に「ツールの操作内容、利用可能な推論トレース、活動ログを横断的に解析」とある。
- OpenAIは問題ある活動の検知後30分以内にアラートを出すことを目標にしている。 [^]
  - Footnote: 本文で「問題のある活動を検知してから30分以内にアラートを発報することを目標」と説明している。
- Hugging Face事件後に停止していた強化学習は、低リスクモデルでは再開された。 [^]
  - Footnote: 本文に「2週間にわたって強化学習（RL）を停止」「リスクの低いモデルについては再開」とある。

### References
- https://www.techno-edge.net/article/2026/08/19/5402.html

## GLM-5.3 (max) - Intelligence, Performance & Price Analysis

### Executive Summary
- Artificial Analysisは、Z AIのプロプライエタリモデルGLM-5.3 (max)の性能・価格ページを掲載している。
- 同モデルは2026年8月リリースとされ、推論対応モデルとして扱われている。
- Artificial Analysis Intelligence Indexでは60点で、181モデル中8位と表示されている。
- 同価格帯の比較では平均を大きく上回り、中央値35に対して高いスコアを示している。
- 入力と出力はテキストに対応し、コンテキストウィンドウは1Mトークンと大きい。
- 価格は入力100万トークンあたり1.40ドル、出力100万トークンあたり4.40ドルと記載されている。
- キャッシュ割引は81%、Intelligence Indexタスクあたりコストは0.68ドルと示されている。
- 評価全体の実行費用は1238.50ドルで、出力トークン量は1億7000万トークンと非常に多い。

### Key Findings
- GLM-5.3 (max)はZ AIのプロプライエタリモデルとして掲載されている。 [^]
  - Footnote: ページ冒頭に「Z AI」「Proprietary model」と表示されている。
- モデルは2026年8月リリースとされているが、ページ内で正確な日付は確認できなかった。 [^]
  - Footnote: 本文に「Released August 2026」とあるため、dateはnullにした。
- Intelligence Indexは60で、掲載クラス内で上位に入る。 [^]
  - Footnote: ページに「Intelligence #8 / 181」「60 Artificial Analysis Intelligence Index」と表示されている。
- 同価格帯モデルの中央値35に対し、GLM-5.3 (max)は60点で大きく上回る。 [^]
  - Footnote: Comparison Summaryに「scores 60」「well above average」「median: 35」とある。
- 入出力モダリティはテキストのみである。 [^]
  - Footnote: Technical specificationsに「Input modality Supports: text」「Output modality Supports: text」とある。
- コンテキストウィンドウは1Mトークンである。 [^]
  - Footnote: Technical specificationsに「Context window 1M」と表示されている。
- 価格は入力100万トークン1.40ドル、出力100万トークン4.40ドルである。 [^]
  - Footnote: Pricing欄とComparison Summaryに「In $1.40」「Out $4.40」と記載されている。
- 評価時の出力は1億7000万トークンで、中央値7200万より多い。 [^]
  - Footnote: Comparison Summaryに「generated 170M tokens」「median of 72M」とある。
- Intelligence Indexの評価実行総費用は1238.50ドルだった。 [^]
  - Footnote: Comparison Summaryに「it cost $1238.50 to evaluate」と記載されている。

### References
- https://artificialanalysis.ai/models/glm-5-3

## Who Owns the Code

### Executive Summary
- Who Owns the Codeは、AI生成コードの所有権と著作権リスクを説明するページである。
- 中心的な主張は、現在の米国著作権法では純粋にAIが生成したコードには人間の著作者がいないため、著作権保護を受けられないという点にある。
- ページは創業者、エンジニアリングリーダー、法務担当者を主な対象にしている。
- 所有権は後から形式的に直せるものではなく、表現物を誰が行ごとに著作したかで決まると説明している。
- AIに創作判断を委ねたコードは、人間著作物ではないため保護対象資産にならないというリスクを示している。
- 人間とAIの混在コードベースでは、人間が意味を持って書いた部分だけを所有できると整理している。
- オープンソースライセンスも、権利者が存在しない純AI出力には実効的に執行できないと警告している。
- ページはThaler事件、Thomson Reuters v. Ross、米国著作権局レポートなどを根拠として挙げている。

### Key Findings
- 純AI生成コードは、現行の米国著作権法では著作権保護を受けられないと説明している。 [^]
  - Footnote: 冒頭に「purely AI-generated code has no human author」「cannot be copyrighted」とある。
- ページの対象読者は、AI生成コードを出荷する創業者、技術リーダー、法務担当者である。 [^]
  - Footnote: 冒頭に「for founders, engineering leaders, and counsel shipping AI-generated code」と表示されている。
- 所有権は、表現的作業を誰が行ったかで行単位に決まるという立場を取っている。 [^]
  - Footnote: 本文に「decided by who authored the expressive work, line by line」とある。
- AIツールが完全に書いたコードは、人間の著作者がいないため所有できないとする。 [^]
  - Footnote: リスク項目01に「Code written entirely by an AI tool has no human author」とある。
- AIに創造的判断を任せると、そのコードは保護可能な人間著作物ではないと警告している。 [^]
  - Footnote: リスク項目02に「When you let the AI make the creative decisions」とあり、保護対象資産ではないと説明している。
- 混在コードベースでは、人間が意味を持って書いた部分だけが保護対象になる。 [^]
  - Footnote: リスク項目03に「you own the parts a person meaningfully wrote」とある。
- 純AI出力にオープンソースライセンスを付けても、権利者がいなければ執行できないと説明している。 [^]
  - Footnote: リスク項目04に「A license only holds if someone owns the code」とある。
- Thaler v. Perlmutterでは、完全にAIが作った作品は著作権対象外と整理されている。 [^]
  - Footnote: ケース欄に「Works created entirely by AI are not eligible for copyright」とある。
- 米国著作権局レポートは、意味のある人間の創造的入力がある部分だけを保護対象とした。 [^]
  - Footnote: ケース欄に「Only meaningful human creative input is eligible for protection」とある。

### References
- https://whoownsthecode.com/
