# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-02-16T09:07:48.5229538+09:00
- Articles: 3

## Arming the rebels with GPUs: Gradium, Kyutai, and Audio AI
- Date: 2026-02-12

### Executive Summary
- オーディオAIは大手よりも小規模チームが牽引しているという視点を提示している。
- KyutaiのMoshiはリアルタイムのフルデュプレックス対話を実現したと述べる。
- 少人数・限られた資金でもオープンソースで高性能な音声モデルを作れると示す。
- 音声分野はデータ不足と難易度の高さで長らく軽視されてきたと整理する。
- Moshiは7Bパラメータと2.1Tトークンで学習したと記載する。
- フルデュプレックスやMimiコーデックなど音声特有の工夫が重要だと強調する。
- Kyutai研究からGradiumが製品化へ橋渡しし資金調達で拡大中だと説明する。

### Key Findings
- Moshiは人間の会話より速い約160msで応答するリアルタイム音声対話モデルと説明されている。 [^]
  - Footnote: 本文に「around 160ms」とあり、リアルタイム応答の速さを強調している。
- 4人の研究者が6か月で基盤モデルをゼロから構築し、オープンソース化したという主張がある。 [^]
  - Footnote: 「team of 4 ... built it completely from scratch ... in 6 months」と記載。
- Moshiは7Bパラメータ・2.1Tトークンで学習した小型音声モデルである。 [^]
  - Footnote: 「Moshi has 7B parameters and was trained on only 2.1T tokens」と明記。
- 学習データは7M時間の音声、Fisher 2000時間、合成対話20k時間超という構成で示されている。 [^]
  - Footnote: 「Pretrained on 7M hours」「Fisher dataset (2000 hours)」「20k+ hours of synthetic dialogue」と列挙。
- フルデュプレックスは相互割り込みやバックチャンネルを可能にし、ターンベースより自然だと述べる。 [^]
  - Footnote: 「Full duplex ... can both interrupt each other」「backchanneling」などの説明がある。
- Gradiumは研究の製品化を担い、70Mドルを調達したと説明されている。 [^]
  - Footnote: 本文に「raised $70M to do it」とある。

### References
- https://www.amplifypartners.com/blog-posts/arming-the-rebels-with-gpus-gradium-kyutai-and-audio-ai

## AIコーディングが隆盛する一方でマネジメントが辛い件
- Date: 2026-02-14

### Executive Summary
- AIコード生成の品質向上で導入が進む一方、機密情報の外部提供リスクを指摘する。
- 組織ルールの整備が前提で、承認プロセスを文化化したいと述べる。
- MCPサーバは効率向上に寄与するが、自由導入はサプライチェーン攻撃の懸念がある。
- IDEをVSCodeに限定し設定や拡張の標準化から始める案を示す。
- AI生成コードは理解不足のセキュリティ欠陥を生む可能性があるとする。
- AI生成PRを明示する運用をまず導入し、徐々に緩める方針を提案する。
- 推進派との意見対立がマネジメントの辛さや評価の不安につながると述べる。

### Key Findings
- AIコーディングはリリース短縮や工数削減に寄与する一方、ソースコード提供による漏えいリスクがある。 [^]
  - Footnote: 「リリースサイクルの短縮化や工数削減」および「機密情報漏えいのリスク」を併記。
- ルール整備なしの導入は不可で、承認プロセスを通す文化が必要だと主張する。 [^]
  - Footnote: 「ルール無しに、ツールの導入があってはならない」「承認プロセスを通す文化をつくりたい」と記載。
- MCPサーバを各人が自由に導入すると悪意あるパッケージによるサプライチェーン攻撃の恐れがある。 [^]
  - Footnote: 「任意のMCPサーバを自由にインストール」「サプライチェーン攻撃」「情報漏洩」への言及。
- 利用IDEをVSCodeに限定し、設定ファイルや拡張機能のホワイトリストを統一配布する方針を提示している。 [^]
  - Footnote: 「利用対象IDEをVSCodeに限定」「.vscode/settings.json」「ホワイトリストを組織で統一配布」とある。
- AI生成コードは人間が理解していないセキュリティ欠陥を混入させる可能性があるとする。 [^]
  - Footnote: 「人間が理解していないコードが混じるリスク」「セキュリティ欠陥を生み出す恐れ」と明記。
- 例としてパスワードをURLクエリに載せるコードを挙げ、AIはリスクを考慮しないと指摘する。 [^]
  - Footnote: 「emailとpasswordをURLのクエリパラメータに直接載せている部分は…リスクを考慮していない」と説明。

### References
- https://zenn.dev/hiroharu8864/articles/782ed847d52aae

## 【draw.io MCP】AIで ER 図が一瞬で生成できるようになった話 — 実際に使って検証してみた
- Date: 2026-02-14

### Executive Summary
- draw.io開発元のJGraphが公式MCPサーバを公開したことを紹介している。
- MCPは外部ツールやデータベースと安全・効率的に連携する共通プロトコルと説明する。
- draw.io MCPでER図やアーキテクチャ図などをプロンプトから自動生成できる。
- 生成後にdraw.io上で手動編集でき、軽微な修正も簡単だと述べる。
- Claude DesktopとCursorへの導入手順を具体的に示している。
- ER図やAWS構成図、シーケンス図などのプロンプト例を提示している。
- 設計レビュー前のたたき台作成などが高速化するとまとめている。

### Key Findings
- JGraphがdraw.ioの公式MCPサーバをリリースしたと明記されている。 [^]
  - Footnote: 冒頭で「公式MCPサーバーがリリース」と説明。
- MCPは外部ツールやDBと安全かつ効率的に連携する共通規格と定義されている。 [^]
  - Footnote: 「外部のツールやデータベースと安全かつ効率的に連携する共通の通信規格」とある。
- draw.io MCPはAIがdraw.ioを直接操作して図を自動生成できる。 [^]
  - Footnote: 「AIが draw.io を直接操作し、図を自動生成できる」と箇条書きにある。
- 文章やスキーマからER図を瞬時に作成し、既存ER図の更新もプロンプトで可能とされる。 [^]
  - Footnote: 「文章やスキーマからER図を瞬時に作成」「既存ER図のカラム追加・削除・リレーション変更もプロンプトで更新」と記載。
- Claude Desktopでは設定ファイルにmcpServersとしてdrawioを追加し、npxと@drawio/mcp@latestを指定する手順が示される。 [^]
  - Footnote: 設定例に「command: npx」「args: @drawio/mcp@latest」とある。
- CursorではAdd Custom MCPからmcp.jsonに同様の設定を入れ、左側のドットが緑なら成功と説明される。 [^]
  - Footnote: 「Add Custom MCP」「mcp.json」「左側のドットが緑色になれば成功」とある。

### References
- https://zenn.dev/aya1357/articles/12f4ede03bc32c
