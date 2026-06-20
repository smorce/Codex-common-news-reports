# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-06-20T09:01:35.1135894+09:00
- Articles: 3

## 「LFM2.5-Embedding-350M / LFM2.5-ColBERT-350M」を試す
- Date: 2026-06-19T14:11:39+00:00

### Executive Summary
- Liquid AI の LFM2.5-Embedding-350M と LFM2.5-ColBERT-350M を調査したスクラップ。
- 両モデルは 11 言語対応の多言語・クロスリンガル検索モデルとして紹介されている。
- Embedding は文書単位で 1 ベクトルを作るため、軽量で高速な検索に向く。
- ColBERT はトークン単位のベクトルと MaxSim により、精度重視の検索に向く。
- モデルカードや公式ブログの内容を整理し、性能評価と推論速度を確認している。
- Colaboratory L4 上で sentence-transformers から Embedding モデルをロードして試している。
- 日本語・多言語の検索例では、期待する文書が上位に来る結果が示されている。

### Key Findings
- 2つのモデルはいずれも 350M 級で、多言語検索とクロスリンガル検索を主目的にしている。 [^]
  - Footnote: 記事本文に「どっちも 350M パラメータで、11言語対応の多言語＆クロスリンガル検索特化モデル」とある。
- Embedding モデルはインデックスサイズと速度を重視する用途に適している。 [^]
  - Footnote: 記事本文に「文書1件につき1つのベクトルを生成します。最も高速な検索が可能で、インデックスサイズも最小」とある。
- ColBERT モデルは単語レベルの照合により検索精度を高める設計である。 [^]
  - Footnote: 記事本文に「トークン1つにつき1つのベクトルを生成します。単語レベルでのクエリマッチングが可能」とある。
- llama.cpp / GGUF 版が用意され、CPU やエッジ環境でも利用可能とされている。 [^]
  - Footnote: 記事本文に「どちらのモデルもllama.cpp GGUF形式を採用しており（CPU、ノートPC、エッジデバイスで動作可能）」とある。
- MacBook M4 Max でのクエリ埋め込みは 10ms 未満の例が示されている。 [^]
  - Footnote: 記事本文に「Embedding: クエリ埋め込み p50 7.3ms」「ColBERT: クエリ埋め込み + MaxSim でも p50 8.2ms」とある。
- H100 上の内部スタックではさらに低レイテンシの結果が示されている。 [^]
  - Footnote: 記事本文に「Embedding：クエリ埋め込み p50 1.5ms」「ColBERT：クエリ + Doc + MaxSim でも p50 22.8ms」とある。
- 利用時は Liquid AI 独自ライセンスへの注意が必要と筆者は述べている。 [^]
  - Footnote: 記事本文に「Liquid AIのモデルは全て独自ライセンスなので、その点だけ注意」とある。

### References
- https://zenn.dev/kun432/scraps/66e1bf19755d3c
- https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M
- https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M

## 「worktrunk」を試す
- Date: 2026-06-18T15:11:54+00:00

### Executive Summary
- Git ワークツリー管理ツール Worktrunk を調べたスクラップ。
- Worktrunk は AI エージェントの並列実行を意識した CLI ツールとして紹介されている。
- ワークツリーの作成、切り替え、削除、一覧表示をブランチ操作に近い形で扱える。
- フック、LLM によるコミットメッセージ生成、マージ支援などの自動化機能が整理されている。
- PR チェックアウトやワークツリーごとの開発サーバーポート割り当ても特徴として挙げられている。
- 筆者は現在 ghq + gwq を使っているが、別の選択肢として Worktrunk を試している。
- ライセンスは MIT と記載されており、導入しやすいツールとして扱われている。

### Key Findings
- Worktrunk は git worktree の操作を簡略化する CLI ツールである。 [^]
  - Footnote: 記事本文に「Worktrunkはgitワークツリー管理のためのCLIツール」とある。
- AI エージェントを複数並列で動かす用途が明確に想定されている。 [^]
  - Footnote: 記事本文に「AIエージェントを並列実行するように設計されています」とある。
- 基本コマンドで切り替え、作成、削除、一覧表示を扱える。 [^]
  - Footnote: 記事本文の表に「wt switch feat」「wt switch -c -x claude feat」「wt remove」「wt list」が示されている。
- ワークフロー自動化として、作成時やマージ前後のフックを実行できる。 [^]
  - Footnote: 記事本文に「フック機能 — ワークツリー作成時、マージ前、マージ後などに任意のコマンドを実行可能」とある。
- 差分から LLM がコミットメッセージを生成する機能がある。 [^]
  - Footnote: 記事本文に「LLMによるコミットメッセージ生成 — 差分情報から適切なコミットメッセージを生成」とある。
- 複数ワークツリーでの開発サーバー衝突を避ける仕組みがある。 [^]
  - Footnote: 記事本文に「hash_portテンプレートフィルターにより、各ワークツリーに固有のポート番号を割り当て可能」とある。
- 筆者は既存の ghq + gwq 環境に不満はないが、代替候補として試している。 [^]
  - Footnote: 記事本文に「現在 ghq + gwq を使っていて、すぐに手に馴染んだし、特に不満があるわけではない」とある。

### References
- https://zenn.dev/kun432/scraps/9cc5951727014e
- https://github.com/max-sixty/worktrunk

## 今更「tmux」を試す ②
- Date: 2026-06-18T07:20:52+00:00

### Executive Summary
- tmux の設定、キーバインド、プラグイン、自動化、ネットワーク利用を整理した続編スクラップ。
- 設定ファイルの場所と優先順位、初期設定例、設定反映方法がまとめられている。
- キーバインドでは設定再読込、prefix 変更、Alt キーでのペイン移動などが紹介されている。
- TPM を使った tmux プラグイン管理と tmux-sensible の導入例が説明されている。
- tmux コマンドを外部スクリプトから実行し、開発環境を再現する自動化例が示されている。
- SSH 越しの長時間作業や、共有ソケットを使ったリモートペアプログラミングも扱っている。
- 筆者は Codex と gRPC サーバ・クライアントの複数ペーン運用を試し、エージェント用の道具として有用性を見ている。

### Key Findings
- tmux の設定は複数の設定ファイル候補があり、ユーザレベルの設定が優先される。 [^]
  - Footnote: 記事本文に「設定は以下で行う。優先度も以下の順になる」「ユーザレベル ~/.tmuf.conf」とある。
- マウス操作、履歴行数、ウィンドウ番号、true color などの基本設定例が紹介されている。 [^]
  - Footnote: 記事本文に「set -g mouse on」「set -g history-limit 50000」「set -g base-index 1」「terminal-overrides」が示されている。
- 既存セッションに設定を反映するには source-file を使う方法がある。 [^]
  - Footnote: 記事本文に「tmux source-file ~/.tmux.conf」「source-file ~/.tmux.conf」とある。
- キーバインドは bind / unbind で追加・削除でき、prefix キー変更も設定可能である。 [^]
  - Footnote: 記事本文に「bind r source-file ~/.tmux.conf」「unbind C-b」「set -g prefix C-a」とある。
- TPM によりプラグイン管理を行い、tmux-sensible などを有効化できる。 [^]
  - Footnote: 記事本文に「git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm」「set -g @plugin 'tmux-plugins/tmux-sensible'」とある。
- tmux は外部スクリプトからセッション・ウィンドウ・ペーンを操作できる。 [^]
  - Footnote: 記事本文に「tmux の外部から tmux コマンドを直接実行できる」「tmux send-keys」「tmux split-window」などの例がある。
- SSH 切断後もセッションを維持できる点がリモート作業に向く。 [^]
  - Footnote: 記事本文に「SSHが切断されても、セッションは維持され、再接続できる」とある。
- 筆者は Codex、gRPC サーバ、gRPC クライアントを3ペーンで動かす利用例を試している。 [^]
  - Footnote: 記事本文に「3つのペーンを用意」「Codex用」「gRPCサーバ用」「gRPCクライアント用」とある。

### References
- https://zenn.dev/kun432/scraps/27b1c1a4c8501a
