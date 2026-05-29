# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-05-29T09:04:35+09:00
- Articles: 3

## OpenAI、プライベートMCPサーバをChatGPTやCodexに安全に接続できるSecure MCP Tunnelを提供開始
- Date: 2026-05-28T11:45:00+09:00

### Executive Summary
- OpenAIはプライベートネットワーク内のMCPサーバをOpenAI製品から利用できる仕組みを公開した。
- Secure MCP TunnelはChatGPT、Codex、Responses APIなどから使える。
- MCPサーバを公開インターネットへ直接出さずに接続できる点が特徴である。
- ファイアウォールの受信用ポートを開放しない構成を取れる。
- 内部ネットワークではtunnel-clientを実行しOpenAI側へ外向きHTTPS通信を行う。
- OpenAI側のトンネルサービスとロングポーリングでMCP応答を中継する。
- ChatGPTのカスタムコネクタ設定から利用するトンネルを選択できる。

### Key Findings
- Secure MCP Tunnelは社内などのプライベートMCPサーバをOpenAI製品へ接続する機能である。 [^]
  - Footnote: 記事はOpenAIが2026年5月28日にSecure MCP Tunnelの提供を開始したと説明している。
- サーバ公開や受信用ポート開放を避けられる。 [^]
  - Footnote: 本文ではパブリックインターネットへの公開やファイアウォールの受信用ポート開放なしに接続できるとされている。
- 通信は内部側からOpenAI側への外向きHTTPSとして開始される。 [^]
  - Footnote: tunnel-clientはapi.openai.com:443またはmtls.api.openai.com:443へ外向きHTTPSリクエストを送ると説明されている。
- ロングポーリングでタスクを取得しMCP応答を返す。 [^]
  - Footnote: OpenAI製品の要求はトンネルサービスに入り、tunnel-clientがキューからタスクを取得して応答を返すとある。
- 導入にはtunnel_idとAPIキーが必要である。 [^]
  - Footnote: 記事はTunnel設定からtunnel_idとtunnel-clientのAPIキーを入手し設定できると述べている。

### References
- https://gihyo.jp/article/2026/05/openai-secure-mcp-tunnel
- https://ai-news.dev/

## AIでタンパク質を予測・設計・発見するモデルをBiohubが無料公開
- Date: 2026-05-28T12:07:00+09:00

### Executive Summary
- Biohubはタンパク質の予測、設計、発見を支援するAIシステムを公開した。
- システムはESMC、ESMFold2、ESM Atlasの3要素を中心に構成される。
- ESMCは大規模なタンパク質配列で学習した表現言語モデルである。
- ESMFold2は配列表現を3次元構造へ変換する設計エンジンである。
- ESM Atlasは配列と予測構造を探索可能にするデータベースである。
- Biohub Platform上で科学コミュニティに無料公開される。
- 計算による初期探索で治療候補の設計期間を短縮できる可能性が示されている。

### Key Findings
- Biohubのシステムは構造予測だけでなく設計と発見も対象にしている。 [^]
  - Footnote: 記事はタンパク質構造予測・設計・発見のためのシステムを開発したと説明している。
- 中核要素はESMC、ESMFold2、ESM Atlasの3つである。 [^]
  - Footnote: 本文では3つの要素を中心に構築されたシステムとして紹介されている。
- ESMCは約28億件の配列で学習したモデルである。 [^]
  - Footnote: 記事には生命全体から収集された約28億件の配列で学習したタンパク質表現言語モデルとある。
- ESMFold2は標的に高い親和性を持つ構造の予測に使われる。 [^]
  - Footnote: 本文は受容体など特定標的に対して高い親和性を発揮する可能性が高い構造を予測できると説明している。
- ESM Atlasは既存データベースでは見えない関連性の探索を助ける。 [^]
  - Footnote: 記事は28億件の配列と11億件の予測構造を探索可能にし、既存データベースで捉えられなかった関連性を明らかにすると述べている。

### References
- https://gigazine.net/news/20260528-biohub-protein-ai-model/
- https://biohub.org/news/world-model-of-protein-biology/
- https://ai-news.dev/

## 生成AIが本当に変えるのは検索ではなく設計知だ
- Date: 2026-05-28T00:00:00+09:00

### Executive Summary
- 記事は生成AIの価値を検索やチャットではなく設計知の構造化に置いている。
- 製造業ではCAD、CAE、試験結果、設計変更履歴、レビュー議論などに知識が分散している。
- RAGや文書検索だけではナレッジの形が扱いにくい場合に限界が出る。
- GHELIA AutoDeckはLLMを答えるAIではなく知識を作るAIとして使う例である。
- CAD/CAEデータ、画像、解析条件、環境条件、ログなどを構造化ナレッジへ変換する。
- 3D形状をベクトル化して保存し形状類似性に基づく検索を可能にする。
- モデル選定以上に自社の知識資本をAIが使える形に整えることが重要だと結論づける。

### Key Findings
- 生成AIの価値は検索精度より設計知を再利用可能な資産に変える点にある。 [^]
  - Footnote: 記事は生成AIが本当に変えるのは検索ではなく設計知だと述べている。
- 製造業の知識は文書だけでなく多様な成果物に分散している。 [^]
  - Footnote: 本文はCADデータ、CAE解析結果、試験結果、設計変更履歴、レビュー議論などを例示している。
- RAGの失敗は対象ナレッジの構造にも起因する。 [^]
  - Footnote: 記事は検索対象のナレッジがAIにも人間にも扱いにくい形で散らばっていることを問題視している。
- GHELIA AutoDeckはLLMを知識生成と構造化の前段に置く。 [^]
  - Footnote: 本文ではGADがLLMを答えるAIではなく知識を作るAIとして使うと説明している。
- 3D形状検索は文章だけでは扱えない製造業の知識を補完する。 [^]
  - Footnote: 記事は3D形状をベクトル化して保存し、形状の類似性に基づいた検索を可能にすると述べている。

### References
- https://wirelesswire.jp/2026/05/93805/
- https://ai-news.dev/
