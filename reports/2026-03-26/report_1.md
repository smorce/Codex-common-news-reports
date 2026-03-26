# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-26T09:23:45.9587380+09:00
- Articles: 3

## 「Takumi Guard」を試す
- Date: 2026-03-26T01:38:00+09:00

### Executive Summary
- LiteLLMのサプライチェーン攻撃を契機に、依存パッケージ対策の必要性を再確認した。
- Takumi GuardはPyPIとクライアントの間に入るセキュリティプロキシとして紹介されている。
- 悪意あるパッケージのブロックに加え、後日判定時の通知機能もある点が強調されている。
- 新規公開パッケージに検疫期間を設け、即時インストールを避ける運用が有効とされる。
- pip/uvでの利用は環境変数の設定で容易に切り替え可能と説明されている。
- 検証ではTakumi Guard有効時に古いバージョンが選ばれ、検疫が機能している様子が示された。
- 完全解決は難しいが、無料で使える自衛策として採用価値があるという結論。
- 依存の安全確認は個別に行いにくく、ツール活用が現実的という問題意識が示されている。

### Key Findings
- Takumi GuardはPyPIとクライアントの間に置くセキュリティプロキシとして説明されている。 [^]
  - Footnote: 「Takumi Guard は pip/uv/poetry と PyPI（レジストリ）の間に位置するセキュリティプロキシで、悪意あるパッケージがブロックされます。」
- 検疫期間の導入により、新規公開パッケージが一定期間インストールできない。 [^]
  - Footnote: 「新規公開バージョンが 72 時間はインストールできない仕組み」
- 悪意パッケージのブロックだけでなく、後日判明時の通知も用意されている。 [^]
  - Footnote: 「後日の通知を行う仕組みもあります。なお通知を受けるためには、メールアドレスの登録が必要」
- 機能概要としてブロック・ダウンロード追跡・感染可能性通知が挙げられている。 [^]
  - Footnote: 「悪意のあるパッケージのブロック」「ダウンロード追跡」「感染可能性の通知」
- pip/uvで利用する場合はインデックスURLを環境変数に設定する手順が示されている。 [^]
  - Footnote: 「export PIP_INDEX_URL=https://pypi.flatt.tech/simple/」「export UV_INDEX_URL=https://pypi.flatt.tech/simple/」
- uv addでインデックスURLを永続化するには`--default-index`か`pyproject.toml`指定が必要とされる。 [^]
  - Footnote: 「--default-index オプションを追加するか、pyproject.toml にインデックスURLを設定するのが良さそう。」

### References
- https://zenn.dev/kun432/scraps/b52d4907bf3195
- https://shisho.dev/docs/ja/t/guard/

## 「hf-mount」を試す
- Date: 2026-03-25T14:24:00+09:00

### Executive Summary
- hf-mountはHugging FaceのバケットやリポジトリをローカルFSとしてマウントできる。
- リモートストレージをローカルより大きく扱える点が利点として紹介されている。
- 5TBデータセットをマウントしてDuckDBで必要部分だけクエリできる例が挙げられている。
- モデルリポジトリをls/catで閲覧するなど、ファイルシステム操作で扱えると述べられる。
- バックエンドはNFS推奨で、FUSEはmacOSではmacFUSEが必要とされる。
- LinuxでNFSマウントする場合はsudoが必要という実運用上の注意が書かれている。
- 大きなモデルはダウンロードした方が使いやすい場合もあるという所感が示された。

### Key Findings
- hf-mountはHugging Faceのバケット/リポジトリをローカルファイルシステムとして扱える。 [^]
  - Footnote: 「Hugging Face のストレージバケットとリポジトリをローカルファイルシステムとしてマウントします。ダウンロードやコピーは不要」
- 大容量データセットをマウントし、DuckDBで必要部分だけをクエリ可能とされる。 [^]
  - Footnote: 「5TBのデータセットをローカルフォルダとしてマウントし、DuckDBで必要な部分だけをクエリ」
- モデルリポジトリをUSBドライブのようにls/catで閲覧できると説明されている。 [^]
  - Footnote: 「任意のモデルリポジトリをUSBドライブのようにls/catで閲覧」
- バックエンドはNFS推奨で、FUSEはmacOSでmacFUSEが必要とされる。 [^]
  - Footnote: 「NFS（推奨）」「FUSE -- カーネルとの統合がより緊密で、macOS ではルート権限または macFUSE が必要」
- LinuxではNFSマウントはrootのみで、sudoが必要という運用面の注意がある。 [^]
  - Footnote: 「Linuxの場合は一般的にNFSのマウントは root しかできないと思うので、sudo が必要になる。」
- 大きなモデルはダウンロードした方が使いやすい場合もあるという所感が示された。 [^]
  - Footnote: 「大きなモデルだと、ダウンロードしてしまったほうが使いやすいかなという気もした。」

### References
- https://zenn.dev/kun432/scraps/5299232ff623dc
- https://github.com/huggingface/hf-mount

## OpenClawクローン「nanobot」を試す
- Date: 2026-03-25T00:26:00+09:00

### Executive Summary
- OpenClawの重さやメンテ負荷を踏まえ、軽量なPython実装のnanobotを試す流れ。
- nanobotはOpenClawにインスパイアされた超軽量パーソナルAIアシスタントと説明される。
- OpenClaw比でコード行数を99%削減しつつ中核機能を実現するとされている。
- 研究向けの可読性や高速動作を特徴として挙げ、ワンクリックデプロイも示される。
- HKUDSはLightRAGなど他プロジェクトも手掛けており発展性に期待を示している。
- LiteLLMのサプライチェーン攻撃に関する注意喚起と依存削除の記述がある。
- インストール方法はソース/uv tool/PyPI/Dockerなど複数提示される。

### Key Findings
- nanobotはOpenClawにインスパイアされた超軽量パーソナルAIアシスタントと位置付けられている。 [^]
  - Footnote: 「nanobot は、OpenClawにインスパイアされた超軽量なパーソナルAIアシスタントです。」
- OpenClaw比でコード行数を99%削減したと明記されている。 [^]
  - Footnote: 「OpenClawと比べてコード行数を99%削減」
- 特徴として超軽量設計・研究向け仕様・超高速動作・使いやすさが列挙されている。 [^]
  - Footnote: 「超軽量設計」「研究向け仕様」「超高速動作」「使いやすさ」
- LiteLLMの影響に関する注意喚起と、依存関係の削除が示されている。 [^]
  - Footnote: 「litellm のサプライチェーン攻撃の影響」「このコミットで litellm 依存関係を完全に削除済み」
- 作者環境ではインストール時のLiteLLMバージョンが1.82.6だったと記載されている。 [^]
  - Footnote: 「インストールされていたバージョンは 脆弱性が注入される前の 1.82.6 だった。」
- インストール方法としてソース/uv tool/PyPIに加えDockerも案内されている。 [^]
  - Footnote: 「ソースからインストール」「uv toolとしてインストール」「PyPIからパッケージ」「Docker / Docker Compose でのインストール」

### References
- https://zenn.dev/kun432/scraps/1209c2ad491647
- https://github.com/HKUDS/nanobot
