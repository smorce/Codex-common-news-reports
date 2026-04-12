# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-04-12T09:01:50+09:00
- Articles: 3

## 「Nix」を試す ② Zero to Nix
- Date: 2026-04-12T01:58:00+09:00

### Executive Summary
- 前回の公式チュートリアルの続きとして学習を継続している。
- 次の教材として英語の「Zero to Nix」チュートリアルを選択した。
- チュートリアルはDeterminate Nixインストーラ前提で進める方針を確認。
- 公式インストーラとの違いやダウンストリーム関係を整理している。
- Ubuntu 24.04（Proxmox上）でインストール手順を実行。
- Determinate Nixインストール後にバージョン確認を実施。
- `nix run`で`ponysay`を実行し、Nix CLIの動きが解説されている。
- Nixの概念（flake参照やNixストア等）は今後掘り下げると述べている。

### Key Findings
- 次に進める教材として「Zero to Nix」を選んだ。 [^]
  - Footnote: とりあえずこれを進めてみようかと思う。
- このチュートリアルはDeterminate Nixインストーラを前提としている。 [^]
  - Footnote: このチュートリアルはDeterminate Nixインストーラーが前提のようなので、それに従うこととする。
- Determinate NixはNixプロジェクトのダウンストリームであると整理している。 [^]
  - Footnote: Nix プロジェクトのダウンストリームディストリビューション
- 公式インストーラは /nix 作成やユーザー作成など複数の変更が必要と記載されている。 [^]
  - Footnote: Nixを正しく動作させるためには、新しい "/nix" ディレクトリの作成、シェルプロファイルの設定、複数のシステムユーザーとグループの作成など
- Determinate Nixのインストーラをcurlで実行する手順を採用した。 [^]
  - Footnote: https://install.determinate.systems/nix
- インストール後のバージョンはDeterminate Nix 3.17.3である。 [^]
  - Footnote: nix (Determinate Nix 3.17.3) 2.33.3
- nix runでponysayを実行する例を試している。 [^]
  - Footnote: nix run "https://flakehub.com/f/NixOS/nixpkgs/*#ponysay"
- Nix CLIがflake参照でコード取得し、ビルドしてNixストアに保存する流れが説明されている。 [^]
  - Footnote: flake参照 を使用してNixコードを取得し、ponysay パッケージをビルドし、その結果を Nixストア に保存しました。

### References
- https://zenn.dev/kun432/scraps/90e870e03d4643

## CodeDeploy で GitHubレポジトリのアプリをEC2にデプロイする
- Date: 2026-04-11T22:42:00+09:00

### Executive Summary
- CodeDeployでGitHubレポジトリのアプリをEC2へデプロイする流れを学習。
- Getting StartedはIAM準備中心で、実デプロイはチュートリアルが本命と判断。
- GitHubデプロイのチュートリアルを選び、Terraformのサンプルで基盤を作成。
- CodeDeploy用サービスロールとEC2インスタンスプロファイルを準備。
- コンソールでアプリケーションとデプロイグループを作成し、タグで対象EC2を指定。
- GitHub連携を行い、コミットIDを指定してデプロイを実行。
- デプロイ完了後、イベント確認やWeb表示で成果を確認。
- 削除時のトークン扱いや自動デプロイ手段（CodePipeline等）を検討。

### Key Findings
- Getting StartedはIAM準備が中心で、実デプロイはチュートリアル側にあると判断している。 [^]
  - Footnote: Getting Startedセクション、IAMユーザやIAMロールなどの設定の準備という側面が強くて、実際のデプロイについては以下のチュートリアル
- チュートリアルのテーマにGitHubからEC2へデプロイが含まれている。 [^]
  - Footnote: EC2インスタンスにGitHubからアプリをデプロイ
- Terraformで事前に環境を構築する方針を取っている。 [^]
  - Footnote: terraform apply して環境を構築しておく。
- EC2向けのCodeDeployサービスロールとしてAWSCodeDeployRoleを利用するとしている。 [^]
  - Footnote: EC2の場合は "AWSCodeDeployRole" を使用する。
- EC2インスタンスプロファイルにはS3やSystems Manager向けの権限も付与している。 [^]
  - Footnote: EC2 用インスタンスプロファイルにはそれらに必要な権限も付けている。
- GitHubリビジョン指定は先頭10文字のコミットIDで、7文字は不可としている。 [^]
  - Footnote: コミットIDはフルだと40文字になるが、その先頭10文字で良いみたい。ただしGitHubで表示されるような7文字ぐらいの短いコミットIDは使用できない
- GitHub連携トークンは管理画面で削除できず、AWS CLIで削除する必要があると述べている。 [^]
  - Footnote: GitHub連携した際のトークンだけは残るようで、これは管理画面からは削除できない様子。AWS CLIで消すことになりそう。
- GitHub OAuthトークンの上限が10個である点に注意が必要としている。 [^]
  - Footnote: GitHub OAuthトークンの最大数は10個らしくて、11個目を足すと最初の1つが消えるらしい。

### References
- https://zenn.dev/kun432/scraps/7df1c9aa2dd3ba

## git cherry-pick を試す
- Date: 2026-04-09T16:43:00+09:00

### Executive Summary
- git cherry-pick の公式ドキュメントを翻訳しながら理解を整理。
- cherry-pickは既存コミットの変更を新規コミットとして適用する操作と説明。
- 実行にはクリーンな作業ツリーが必要で、競合時の挙動も記述。
- 主要オプション（-x, -m, --no-commit, --abort等）の意味を要約。
- 例としてHTMLを変更する複数コミットを作り、特定コミットだけをmainに適用。
- cherry-pick後のコミットは内容同一でも別コミットになる点を確認。
- PRでマージした場合の履歴の見え方も確認。
- 基本は小さなブランチを頻繁にマージするが、cherry-pickが必要な場面もあると結論。

### Key Findings
- cherry-pickは既存コミットの変更を新しいコミットとして記録する操作で、作業ツリーはクリーンである必要がある。 [^]
  - Footnote: 既存のコミットで導入された変更を適用し、新しいコミットとして記録します。ただし、作業ツリーはクリーンな状態
- 競合が発生した場合、CHERRY_PICK_HEADが設定される。 [^]
  - Footnote: CHERRY_PICK_HEAD 参照は、適用が困難な変更を導入したコミットを指すように設定されます。
- 競合時には通常の競合マーカーが作業ツリーに記録される。 [^]
  - Footnote: 作業ツリーのファイルには、通常の競合マーカー "<<<<<<<"
- -xオプションは元コミットからのチェリーピックであることを明示する行を追加する。 [^]
  - Footnote: 元のコミットメッセージの末尾に 「（コミット…​からチェリーピックされました）」という行を追加
- マージコミットのチェリーピックにはmainline指定が必要になる。 [^]
  - Footnote: マージコミットをチェリーピックすることはできません。
- 例として特定コミットをmainへ適用する操作が示されている。 [^]
  - Footnote: git cherry-pick 85f048e
- cherry-pick後のmainには別のコミットIDで反映される。 [^]
  - Footnote: 256103b (HEAD -> main) Fix button color
- cherry-pick元と先のコミットは内容同一でも別コミットになると述べている。 [^]
  - Footnote: cherry-pick 元 と cherry-pick 先のコミットは、内容は同じだが別のコミットとなっている。
- 運用としては小さなブランチを頻繁にマージするのが基本だと述べている。 [^]
  - Footnote: 基本はブランチを「細かく」作って「頻繁」にマージするのが正解だと思う。

### References
- https://zenn.dev/kun432/scraps/58b40bf359e4bb
