# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-03-29T17:39:45+09:00
- Articles: 3

## Isaac Teleop の概要
- Date: 2026-03-29T14:59:00+09:00

### Executive Summary
- Isaac Teleopは単なる遠隔操作UIではなく、入力をロボット制御や学習データへ変換する統一フレームワークとして説明されている。
- 標準化されたデバイスインターフェース、グラフベースのリターゲティング、sim/realをまたぐワークフローが中心要素である。
- 人の入力を変換し、再利用可能な形で保存する流れを一体として扱う点が強調されている。
- コア要素はUnified Device Interface、Retargeting Interface、Data Interfaceの3つに整理されている。
- Data InterfaceではFlatBuffersの標準スキーマとmcapによる記録・再生、LeRobotとの相互運用が示されている。
- 対応デバイスとして複数のXRヘッドセットやグローブ・ペダル・カメラなどが具体的に列挙されている。
- simとrealを分けず、ROS2やIsaac Sim v6.0、Isaac Lab v3.0を同一のデータスキーマで扱う方針が示されている。

### Key Findings
- Isaac Teleopは遠隔操作UIではなく、人の入力をロボット制御や学習用データへ変換するための統一フレームワークとして設計されている。 [^]
  - Footnote: 「単なるロボット遠隔操作UIではありません。人の入力をロボット制御や学習用データへ変換するための、統一されたフレームワークとして設計されています。」
- コア要素はUnified Device Interface、Retargeting Interface、Data Interfaceの3つである。 [^]
  - Footnote: 「コア要素は次の3つです。」「・Unified Device Interface」「・Retargeting Interface」「・Data Interface」
- Data InterfaceはFlatBuffers標準スキーマ、mcapの記録・再生、LeRobotとの相互運用を担う。 [^]
  - Footnote: 「FlatBuffers ベースの標準スキーマ、mcap による記録・再生、LeRobot との相互運用を担います。」
- XRヘッドセットのサポート対象としてApple Vision Pro、Meta Quest 2/3/3S、Pico 4 Ultraが列挙されている。 [^]
  - Footnote: 「・Apple Vision Pro」「・Meta Quest 2/3/3S」「・Pico 4 Ultra」
- スタンドアロン入力デバイスとしてManus Gloves、Logitech Rudder Pedals、OAK-D Cameraが挙げられている。 [^]
  - Footnote: 「・Manus Gloves」「・Logitech Rudder Pedals」「・OAK-D Camera」
- simとrealを分けず、ROS2、Isaac Sim v6.0、Isaac Lab v3.0を同一ワークフローで使う方針が示されている。 [^]
  - Footnote: 「sim と real を分けていないことです。「ROS2」「Isaac Sim v6.0」「Isaac Lab v3.0」をサポートしています。つまり、同じデバイスワークフローやデータスキーマを、シミュレーションと実機の両方で使っていく思想が最初から入っています。」

### References
- https://note.com/npaka/n/n4769db20f86a

## 「AIコーディングは後から苦しくなる」「いま勢いのあるツールは？」――エージェントに揺れる開発現場 今週の「＠IT」よく読まれた記事“10選”
- Date: 2026-03-28T08:00:00+09:00

### Executive Summary
- ＠ITで公開された記事のうち注目を集めた10本をランキング形式で紹介する週次まとめである。
- 対象期間は2026年3月9～15日に公開された記事で、アクセスと反響を基に順位付けしている。
- 1位はAIコーディングの「理解負債」「認知負債」を扱う記事で、開発が後から苦しくなる理由を整理している。
- 2位は「State of JavaScript 2025」の結果で、フレームワークやツールの人気や満足度を紹介している。
- 3位はAnthropic Academyの「エージェントスキル」講座で、Claude Codeの活用法を扱う。
- 4位はGartnerの予測で、AI導入で削減した顧客サービス要員の再雇用が進む見通しを伝える。
- Windows 11の更新機能や業務効率化の話題も上位に入り、AI以外の実務ネタにも関心が集まっている。

### Key Findings
- ＠ITで注目を集めた10本の記事をランキング形式で紹介する企画である。 [^]
  - Footnote: 「＠ITで公開された記事の中から、特に注目を集めた10本をランキング形式で紹介します。」
- 2026年3月9～15日に公開された記事をアクセスや反響に基づいて順位付けした。 [^]
  - Footnote: 「本稿では2026年3月9～15日に＠ITで公開された記事の中から、特に注目を集めた10本を、記事へのアクセスや反響を基にランキング形式で紹介します。」
- 1位はAIコーディング時代の三大負債（理解負債・認知負債・技術負債）を整理する記事である。 [^]
  - Footnote: 「AIコーディングが普及する中で注目され始めた「理解負債」と「認知負債」。従来の技術負債と合わせた「AIコーディング時代の三大負債」を整理し、なぜ開発が後から苦しくなるのかを分かりやすく解説する。」
- 2位はDevographicsの「State of JavaScript 2025」結果で、ユーザー数や人気、満足度などを示す。 [^]
  - Footnote: 「Devographicsは、JavaScriptの年次利用動向調査「State of JavaScript 2025」の結果を発表した。フレームワークやツールのユーザー数、人気、満足度、評価度などを明らかにしている。」
- 3位はAnthropic Academyに追加されたClaude Codeの「エージェントスキル」講座で、約22分の動画とされる。 [^]
  - Footnote: 「Anthropicのオンライン講座「Anthropic Academy」に、Claude Codeの重要機能「エージェントスキル（Agent Skills）」を解説する新コースが追加された。約22分の動画で、AIエージェントの新しい開発スタイルを学べる講座の内容を整理し、技術の背景も含めて紹介する。」
- 4位はGartnerの予測で、AI導入を理由に顧客サービススタッフを削減した企業の半数が2027年までに再雇用に踏み切るとされる。 [^]
  - Footnote: 「Gartnerは、AI導入を理由に顧客サービススタッフを削減した企業の動向に関する予測を発表した。2027年までにその半数が再雇用に踏み切るとの見解を示し、AIの限界と人的リソースの重要性を指摘している。」
- 5位はWindows 11更新（KB5079473）で回線速度テストの標準搭載やEmoji 16.0対応、Sysmon標準搭載、83件の脆弱性修正を含む。 [^]
  - Footnote: 「Microsoftは2026年3月10日（米国時間）、Windows 11 24H2／25H2向け更新プログラム「KB5079473」を公開した。タスクバーからのネットワーク速度測定ツールの起動や、Emoji 16.0への対応、Sysmonの標準搭載など、利便性を高める新機能が多く追加された。合計83件の脆弱性修正も含まれるため、早急な適用を推奨する。」

### References
- https://atmarkit.itmedia.co.jp/ait/articles/2603/28/news018.html

## 国産LLMは作れるのか？ - RakutenAI 3.0の炎上から考える
- Date: 2026-03-27T00:00:00+09:00

### Executive Summary
- Rakuten AI 3.0は国内最大規模をうたうLLMとして発表され、約7000億パラメータのMoEで日本語ベンチマークが高いとされている。
- 公開直後にconfig.jsonの記述からDeepSeek V3ベースと判明し、ライセンス対応の不備が炎上を招いた。
- GENIAC補助の「国産AI」でありながら出自が明示されなかった点が批判の中心だった。
- 記事はこの騒動を契機に、ファインチューンの位置づけや国産LLMの現実的な手法を整理している。
- ファインチューン自体は一般的な手法で、国内主要モデルの多くがOSSベースの二次開発だと説明される。
- フルスクラッチでの学習は計算コストが莫大で、GPU台数や期間、費用が大規模になると示される。
- 結論として、透明性の欠如が問題であり、OSSベースの最適化は現実的な選択肢だとまとめている。

### Key Findings
- Rakuten AI 3.0は2026年3月17日に発表され、約7000億パラメータのMoEで日本語ベンチマークがGPT-4oを上回るとされる。 [^]
  - Footnote: 「2026年03月17日、楽天グループが「国内最大規模」と謳う大規模言語モデル（以下、LLM）「Rakuten AI 3.0」を発表しました。約7000億パラメータのMoE（Mixture of Experts）モデルで、日本語ベンチマークではGPT-4oを上回るスコアを記録したといいます。」
- Hugging Face上のconfig.jsonに「model_type: deepseek_v3」とあり、ベースモデルがDeepSeek V3だと判明した。 [^]
  - Footnote: 「Hugging Face上のconfig.jsonに"model_type: "deepseek_v3""という記述が見つかり、ベースモデルがDeepSeek V3であることが判明。」
- DeepSeek由来のMITライセンスが初回公開時に含まれず、指摘後にNOTICEとして追加された。 [^]
  - Footnote: 「初回公開時にはDeepSeek由来のMITライセンスファイルが含まれておらず、炎上後に「NOTICE」ファイルとして追加される経緯もありました。」
- GENIAC補助の国産AIがDeepSeek V3ベースであり、その出自が明示されていなかったことが批判の核心だった。 [^]
  - Footnote: 「GENIACプロジェクト（経済産業省・NEDO）の補助を受けた「国産AI」がDeepSeek V3ベースだったこと、そしてその出自が積極的に明示されていなかったことが批判の核心でした。」
- ファインチューンは一般的な手法で、日本企業の主要モデルの約6割がDeepSeekやQwenベースの二次開発だと説明されている。 [^]
  - Footnote: 「ファインチューン自体は普通の技術です。Llama(Meta)やQwen(Alibaba)といったオープンソースモデルをベースに、特定の言語やタスクに合わせて追加学習を行うのは、世界中の研究者・企業が日常的にやっていることです。日経新聞の報道によれば、日本企業の主要モデルのうち約6割がDeepSeekやQwenをベースにした2次開発だといいます。」
- フルスクラッチ学習はGPU台数・期間・費用が膨大で、DeepSeek V3クラスでは日本の一企業にほぼ不可能な水準だとされる。 [^]
  - Footnote: 「GPU A100を数百〜数千台」「学習期間 数週間〜数ヶ月」「推定コスト 数十億〜数百億円」「日本の一企業にはほぼ不可能な水準です。」

### References
- https://zenn.dev/nitic_students/articles/e2e331dea0c616
