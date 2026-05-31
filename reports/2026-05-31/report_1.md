# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-31T09:01:47.5016654+09:00
- Articles: 3

## Stable Diffusion WebUI Forge - Neo
- Date: 2026-05-30T18:34:16+00:00

### Executive Summary
- Stable Diffusion WebUI Forge - Neo を試すための短い調査メモである。
- きっかけは、従来の Forge に近い操作感で AI イラスト制作ができるという紹介記事だった。
- 筆者は以前 Stable Diffusion Web UI を利用していたが、最近は ComfyUI をよく見かけると述べている。
- Stable Diffusion Web UI 系列では、複数のフォークを経て Neo が現在の移行先として位置付けられている。
- AUTOMATIC1111 版と lllyasviel 版 Forge は更新停止と整理されている。
- Forge - Classic はバグ修正のみとなり、Neo への移行が示されている。
- 画像生成の利用頻度が高くない場合、Gradio ベースのシンプルな UI が適する可能性がある。

### Key Findings
- 筆者は ComfyUI ではなく Stable Diffusion WebUI Forge - Neo を試す方針を示した。 [^]
  - Footnote: 本文に「ComfyUIはちょっと過剰な感もあって、Gradio ベースのシンプルな UI で十分かも」とある。
- Stable Diffusion Web UI の元祖 AUTOMATIC1111 版は更新停止と整理されている。 [^]
  - Footnote: 本文の系譜に「Stable Diffusion Web UI（AUTOMATIC1111） ※更新が止まっている」とある。
- lllyasviel の Stable Diffusion Web UI Forge も更新停止と記載されている。 [^]
  - Footnote: 本文の系譜に「Stable Diffusion Web UI Forge（lllyasviel） ※更新が止まっている」とある。
- Forge - Classic はバグ修正のみで、Neo への移行段階にある。 [^]
  - Footnote: 本文に「Stable Diffusion Web UI Forge - Classic（Haoming02） ※バグフィックスのみ。Neoに移行。」とある。
- 現在試す対象として Forge - Neo が示されている。 [^]
  - Footnote: 本文の系譜末尾に「Stable Diffusion Web UI Forge - Neo（Haoming02） ←イマココ」とある。

### References
- https://zenn.dev/kun432/scraps/0f551d4a90c946

## エージェント向けサンドボックス環境「NVIDIA OpenShell」を試す
- Date: 2026-05-30T09:36:57+00:00

### Executive Summary
- NVIDIA OpenShell の概念、構成、インストール、Quickstart を確認した検証メモである。
- OpenShell は自律型 AI エージェントをカーネルレベルで分離して実行するオープンソースのランタイム環境と説明されている。
- 宣言型 YAML ポリシーにより、ファイル、認証情報、外部ネットワークへのアクセスを制御する。
- 主要コンポーネントは CLI、Gateway、Supervisor で、管理と実行時制約を分離する。
- ローカルマシンと Kubernetes クラスターの双方で同じ基本モデルを利用できる。
- Ubuntu VM 上の Quickstart では OpenShell 0.0.52 を導入し、Claude Code 用サンドボックスを作成した。
- 外側からエージェントを統一制御できる点が利点だが、構成の複雑さとエージェント別対応状況がトレードオフとして挙げられている。

### Key Findings
- OpenShell はエージェントのアクセス権限を外側から明示的に制御するためのランタイムである。 [^]
  - Footnote: 本文に「サンドボックス型の実行環境制御と宣言型YAMLポリシーを組み合わせる」とある。
- Gateway は制御プレーン、Supervisor はサンドボックス内のローカルセキュリティ境界として機能する。 [^]
  - Footnote: 本文に「ゲートウェイは制御プレーンとして機能」「スーパーバイザーはすべてのサンドボックスワークロード内で動作し、ローカルセキュリティ境界として機能」とある。
- ファイルシステム制限には Landlock、権限昇格対策には非特権プロセスと seccomp が使われる。 [^]
  - Footnote: 脅威と対策の表に「ファイルシステム制限機能（Landlock）」および「非特権プロセスのアイデンティティとseccomp制限」とある。
- 推論トラフィックは inference.local を介してルーティングされ、認証情報をエージェントへ直接公開しない。 [^]
  - Footnote: 本文に「https://inference.local パスは、サンドボックス外にプロバイダーの認証情報を保持したまま」転送するとある。
- ローカル環境では Docker、Podman、MicroVM のコンピュートドライバーが説明されている。 [^]
  - Footnote: サポートするコンピュートドライバーの表に Podman、Docker、MicroVM が列挙されている。
- 検証環境では OpenShell 0.0.52 のインストールと Gateway 接続成功が確認された。 [^]
  - Footnote: インストール出力に「installed openshell package from v0.0.52」、status 出力に「Status: Connected」「Version: 0.0.52」とある。
- サンドボックスは作成、一覧表示、再接続、削除が可能で、削除時には対応する Docker コンテナも削除された。 [^]
  - Footnote: 本文に openshell sandbox create、list、connect、delete の実行例と「Dockerコンテナも削除されていた」とある。

### References
- https://zenn.dev/kun432/scraps/85a7f3640c0e57
- https://docs.nvidia.com/openshell/latest/about/how-it-works

## Codex を試す、再び ⑤ CLI
- Date: 2026-05-29T11:18:39+00:00

### Executive Summary
- Codex CLI の公式ドキュメントを読み直し、未使用の機能を試したメモである。
- 対話モード、セッション再開、画像入力、テーマ、レビュー、Web 検索、非対話実行など幅広い機能が整理されている。
- リモート TUI モードでは Codex App Server を別ホストで起動し、クライアントから接続できる。
- 非ループバック WebSocket リスナーでは認証が必須で、リモート認証トークン利用時は wss またはループバック ws が必要だった。
- 検証では SSH トンネル経由の localhost 接続によりリモート App Server へ接続できた。
- codex exec を使うと非対話モードで処理を実行し、スクリプトへ組み込める。
- 筆者はリモート接続、外部エディタ起動、会話履歴編集、追加ディレクトリ指定などを有用な機能として挙げている。

### Key Findings
- Codex CLI は対話型 TUI と非対話型 codex exec の両方を提供する。 [^]
  - Footnote: 本文に対話モードの説明と「codex execを使えば、スクリプトなどに組み込みが可能」「非対話モードで実行される」とある。
- 過去の会話は codex resume で再開でき、セッション ID 指定や --last が利用できる。 [^]
  - Footnote: 本文に codex resume、codex resume --last、codex resume <SESSION_ID> などの例が列挙されている。
- 非ループバックの App Server 起動では WebSocket 認証が必須である。 [^]
  - Footnote: 実行結果に「refusing to start non-loopback websocket listener 0.0.0.0:4500 without auth」とある。
- リモート認証トークンは wss またはループバック ws 経由でのみ利用できる。 [^]
  - Footnote: 実行結果に「--remote-auth-token-env requires a wss:// or loopback ws:// remote」とある。
- 検証では SSH ローカルフォワードを使い、localhost 経由でリモート App Server に接続できた。 [^]
  - Footnote: 本文に ssh -L 4500:127.0.0.1:4500 の例と「接続できた」とある。
- Codex CLI の機能フラグは codex features list、enable、disable で確認・変更できる。 [^]
  - Footnote: 本文に codex features list、codex features enable memories、codex features disable memories の実行例がある。
- 外部エディタは VISUAL または EDITOR を設定し、Ctrl+G で呼び出せる。 [^]
  - Footnote: 本文に「VISUAL または EDITOR で設定されたエディタを Ctrl+G で呼び出せる」とある。

### References
- https://zenn.dev/kun432/scraps/9c0c19b19abd76
