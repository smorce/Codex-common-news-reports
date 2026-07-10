# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-07-10T09:04:27.9929382+09:00
- Articles: 3

## Zuck saves Meta bucks by reusing memory from old servers with a custom CXL ASIC
- Date: 2026-06-29T10:43:00Z

### Executive Summary
- Metaは古いサーバーからDDR4メモリを回収し、新しいサーバーで再利用する仕組みを本番投入している。
- 独自CXL ASIC「Vistara」により、DDR4をホストプロセッサへ接続し、異なる世代のメモリを組み合わせる。
- 記事は、同技術が一部の推論ワークロードで必要サーバー数を最大25%削減したと伝えている。
- Metaの課題は、巨大なサーバー群の約40%でメモリ増設が難しいことにある。
- VistaraはCXL 2.0/1.1準拠のPCIe Gen5 x16インターフェースを使い、DDR4をブリッジする。
- Linux CXLドライバのカスタム調整により、DDR4をCPUなしのNUMAノードとしてOSに見せている。
- 対象ワークロードはML推論、ビッグデータ処理、データベース、分散キャッシュ、CI/CDなど広い。
- CXLの追加メモリによりOOM起因の失敗や再実行負荷を減らす狙いも示されている。

### Key Findings
- Metaは古いDDR4 DIMMを新しいDDR5世代の機械に組み込み、容量プールとして活用している。 [^]
  - Footnote: 記事本文に「DDR4 DIMMs from old servers」を新しい機械に入れ、容量プールにする説明がある。
- Metaの大規模サーバー群では、約40%がメモリ増設できないという制約を抱えている。 [^]
  - Footnote: 記事は「around 40 percent of its vast server fleet」でメモリ量を増やせないと説明している。
- Vistara ASICはDDR4をCXL経由でホストへ接続するための独自チップとして設計された。 [^]
  - Footnote: 記事はVistaraが「DDR4 memory to host processors via a CXL 2.0/1.1-compliant PCIe Gen5 x16 interface」を橋渡しすると記す。
- 1つのVistara ASICは2つの72ビットDDR4チャネルを統合し、最大3,200 MT/sと最大256GBを扱う。 [^]
  - Footnote: 記事中に「two independent 72-bit DDR4 memory channels」「up to 3,200 MT/s」「up to 256 GB per chip」とある。
- MemServerはAMD Turinプロセッサ、768GBのDDR5、256GBのDDR4を組み合わせる構成で説明されている。 [^]
  - Footnote: 記事はMemServerが「AMD Turin processor」「768 GB of DDR5」「256 GB of DDR4 connected through Vistara ASICs」を備えると述べる。
- 追加メモリはOS上でCPUなしNUMAノードとして扱われ、必要時にCXLメモリを利用する。 [^]
  - Footnote: 記事はDDR4が「CPU-less NUMA node」として提示され、まずローカルDDR4、次にCXLメモリを使うと説明している。
- CXLのメモリ余力はOOM関連のジョブ失敗・再起動・リソース断片化を33%減らすとされる。 [^]
  - Footnote: 記事はOOMイベント緩和により「job failures and ... restarts and resource fragmentation by 33 percent」を減らすと引用している。
- 一部の分散推論では、サーバー台数を最大25%削減したと報告されている。 [^]
  - Footnote: 記事は導入効果として「reducing the server count by up to 25 percent for disaggregated inference」と述べる。

### References
- https://www.theregister.com/systems/2026/06/29/zuck-saves-meta-bucks-by-reusing-memory-from-old-servers-with-a-custom-cxl-asic/5263483

## SpaceXAI、新AIモデル「Grok 4.5」を正式公開　Cursorと共同トレーニング
- Date: 2026-07-10T06:30:00+09:00

### Executive Summary
- SpaceXAIは新AIモデル「Grok 4.5」を一般公開した。
- 同モデルはCursorと共同トレーニングした初のGrokモデルとされる。
- 主な対象はコーディング、エージェント型タスク、ナレッジワークである。
- 学習には数万基のNVIDIA GB300 GPUと、コーディング・科学・工学・数学データセットが使われたと記事は伝える。
- マスク氏はGrok 4.5をAnthropicのOpusクラスと位置づけ、高速・高効率・低コストを主張している。
- 価格は入力100万トークン2ドル、出力100万トークン6ドルで、上位競合より低めに設定されている。
- 用途にはアプリ開発、Office業務、リサーチ、ライティング、エージェント自動化が含まれる。
- Grok Buildのデフォルトモデルとして採用され、SpaceXAIコンソールとCursor全プランで利用可能とされる。

### Key Findings
- Grok 4.5はSpaceXAIから正式に一般公開された。 [^]
  - Footnote: 記事冒頭に「最新AIモデル『Grok 4.5』を正式に一般公開しました」とある。
- Cursorとの共同トレーニングによる初のGrokモデルとして位置づけられている。 [^]
  - Footnote: 記事は「AI企業Cursorと共同でトレーニングした初のGrokモデル」と説明している。
- コーディング、エージェント型タスク、ナレッジワークを主眼に設計されている。 [^]
  - Footnote: 記事は設計目的として「コーディング、エージェント型タスク、ナレッジワークへの対応」を挙げる。
- 学習基盤として数万基のNVIDIA GB300 GPUが使われたとされる。 [^]
  - Footnote: 本文に「数万基のNVIDIA GB300 GPUを用いて」と記載がある。
- マスク氏はOpusクラスの能力を持ち、より高速でトークン効率が高いと主張している。 [^]
  - Footnote: 記事はマスク氏の説明として「Opusクラス」「より高速でトークン効率が高く、低コスト」と引用している。
- 公開ベンチマークでは競合トップ級に近いが、最高クラスにはわずかに届かないと整理されている。 [^]
  - Footnote: 記事は「競合トップモデルに匹敵する水準」を示す一方「最高クラスにはわずかに届かない」と述べる。
- 価格は入力100万トークン2ドル、出力100万トークン6ドルである。 [^]
  - Footnote: 記事本文に「入力100万トークンあたり2ドル、出力100万トークンあたり6ドル」とある。
- EU圏では2026年7月中旬以降に提供開始予定とされる。 [^]
  - Footnote: 記事末尾に「EU圏のでは2026年7月中旬以降の提供開始になる見込み」と記載されている。

### References
- https://www.techno-edge.net/article/2026/07/10/5277.html

## Meta「Muse Spark 1.1」を一般公開。AIコーディング市場に算入
- Date: 2026-07-10T06:45:00+09:00

### Executive Summary
- Meta Superintelligence Labsはマルチモーダル推論AIモデル「Muse Spark 1.1」を発表した。
- 4月の初代モデルから、エージェントタスク、コーディング、マルチモーダル理解が改善された。
- Meta AIアプリとmeta.aiでは「Thinking」モードとして即時利用できる。
- 開発者向けにはMeta Model APIのパブリックプレビューが始まった。
- Metaは本リリースを「個人向け超知性」のビジョン実現に向けた取り組みと位置づける。
- 複数アプリやサービスをまたぐ計画・実行を行うエージェント型AIとしての実用性を強めた点が焦点である。
- コンテキストウィンドウは100万トークンに対応し、長期作業履歴や重要情報の保持を想定している。
- 安全性評価では化学・生物兵器、サイバー、制御喪失リスクで安全基準内とされ、耐ジェイルブレイク性も説明されている。

### Key Findings
- Muse Spark 1.1はマルチモーダル推論AIモデルとして発表された。 [^]
  - Footnote: 記事は「マルチモーダル推論AIモデル『Muse Spark 1.1』を発表」と書いている。
- 前モデルからエージェントタスク、コーディング、マルチモーダル理解が改善された。 [^]
  - Footnote: 本文に「エージェントタスク、コーディング、マルチモーダル理解の各分野での改善」とある。
- Meta AIアプリとmeta.aiのThinkingモードで即時利用可能である。 [^]
  - Footnote: 記事は「Meta AIアプリおよびmeta.aiにて『Thinking』モードとして即時利用可能」と説明する。
- Meta Model APIのパブリックプレビューが始まり、開発者がAPI経由でアクセスできる。 [^]
  - Footnote: 本文に「『Meta Model API』のパブリックプレビューも開始」とあり、APIアクセス可能と述べる。
- マルチエージェントシステムでは、メインエージェントとして計画や委任を行い、サブエージェントとしても動作する。 [^]
  - Footnote: 記事は「メインエージェントとして計画立案やサブエージェントへのタスク委任」「サブエージェントとしても機能」と記す。
- 100万トークンのコンテキストウィンドウにより、長期作業履歴の参照や重要情報の保持を想定している。 [^]
  - Footnote: 本文に「コンテキストウィンドウは100万トークンに対応」とある。
- コンピュータ操作では、スクリプト自動化と直接操作を状況に応じて使い分ける設計とされる。 [^]
  - Footnote: 記事は「スクリプトによる自動化と直接操作を使い分ける設計」と説明している。
- 安全性では化学・生物兵器、サイバー、制御喪失の各リスクカテゴリで基準内と評価されたとしている。 [^]
  - Footnote: 本文は「化学・生物兵器リスク、サイバーセキュリティ、制御喪失」の各カテゴリで安全基準内と述べる。

### References
- https://www.techno-edge.net/article/2026/07/10/5278.html
