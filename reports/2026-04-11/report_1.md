# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-04-11T23:21:16+09:00
- Articles: 3

## CodeDeploy で GitHubレポジトリのアプリをEC2にデプロイする
- Date: 2026-04-11T22:42:00+09:00

### Executive Summary
- AWS CodeDeployでGitHubリポジトリのアプリをEC2へデプロイする流れを一通り試している。
- Getting StartedはIAM準備中心で、実際のデプロイはチュートリアル参照と整理。
- 公式チュートリアルの中からGitHub→EC2の手順を選び、Terraformで環境を用意。
- CodeDeployのサービスロールと、EC2用インスタンスプロファイルの権限を作成。
- appspec.ymlとフックスクリプトで配置と起動停止を定義し、リポジトリへpush。
- コンソールでアプリケーション/デプロイグループを作成し、タグで対象EC2を指定。
- GitHub連携のトークン名やコミットID指定など、デプロイ作成時の注意点を記録。
- 削除時のGitHubトークン残存や自動化手段（CodePipeline等）にも触れている。

### Key Findings
- Getting StartedはIAM準備の説明が中心で、実デプロイはチュートリアルで確認する流れになっている。 [^]
  - Footnote: 「Getting Startedセクション、IAMユーザやIAMロールなどの設定の準備という側面が強くて、実際のデプロイについては以下のチュートリアル」
- チュートリアルには「EC2インスタンスにGitHubからアプリをデプロイ」など複数のテーマがある。 [^]
  - Footnote: 「EC2インスタンスにGitHubからアプリをデプロイ」
- CodeDeployのサービスロールはEC2の場合「AWSCodeDeployRole」を使用する前提で構成している。 [^]
  - Footnote: 「EC2の場合は "AWSCodeDeployRole" を使用する」
- EC2用インスタンスプロファイルにはS3/Systems Manager利用を想定した権限も付与している。 [^]
  - Footnote: 「EC2 用インスタンスプロファイルにはそれらに必要な権限も付けている」
- appspec.ymlに従ってファイル配置やイベントフックのスクリプト実行が可能と理解している。 [^]
  - Footnote: 「appspec.yml の内容に従って、ファイルを配置したり、イベントフックでスクリプトを実行したり」
- GitHubのコミットIDは先頭10文字で良いが、7文字の短縮IDは使えないと記載している。 [^]
  - Footnote: 「コミットIDはフルだと40文字になるが、その先頭10文字で良いみたい。ただし…7文字ぐらいの短いコミットIDは使用できない」
- CodeDeployアプリ削除ではGitHub連携トークンが残るため、AWS CLIで削除する必要がある。 [^]
  - Footnote: 「GitHub連携した際のトークンだけは残るようで…AWS CLIで消すことになりそう」
- CodeConnectionsはCodeDeployで使えないため、CodePipelineが必要になりそうと結論づけている。 [^]
  - Footnote: 「CodeConnections が使えるサービスに CodeDeploy が書いてない…この場合はCodePiplelineを使う必要がありそう」

### References
- https://zenn.dev/kun432/scraps/7df1c9aa2dd3ba

## git cherry-pick を試す
- Date: 2026-04-09T16:43:00+09:00

### Executive Summary
- git cherry-pick の公式リファレンスを翻訳しながら挙動を確認している。
- 既存コミットの変更を適用し、新しいコミットを作るという前提と制約を整理。
- 競合時のCHERRY_PICK_HEADや競合マーカーの扱いも言及。
- サンプルHTMLでfeatureブランチに3コミットを作成する手順を示す。
- mainに特定コミットだけを cherry-pick して新コミットが作られることを確認。
- 同内容でも元コミットとは別ハッシュになる点をログで示している。
- その後PRをマージした際の履歴がやや複雑になる例を提示。
- 結論として、細かいブランチと頻繁マージが基本で、cherry-pickは例外的に使うと整理。

### Key Findings
- cherry-pickは既存コミットの変更を適用して新しいコミットを作るが、作業ツリーはクリーンである必要がある。 [^]
  - Footnote: 「既存のコミットで導入された変更を適用し、新しいコミットとして記録します。ただし、作業ツリーはクリーンな状態」
- 競合時はCHERRY_PICK_HEADが設定され、競合マーカーで内容が示される。 [^]
  - Footnote: 「CHERRY_PICK_HEAD 参照は…競合マーカー <<<<<<< と >>>>>>> で囲まれた形」
- -xオプションは元コミット由来をメッセージ末尾に追記し、公開ブランチ間で有用とされる。 [^]
  - Footnote: 「末尾に『…からチェリーピックされました』という行を追加…公開ブランチ間で…有用」
- featureのコミット「85f048e」をmainへ cherry-pick すると、main側では別コミット「256103b」になる。 [^]
  - Footnote: 「git cherry-pick 85f048e」「[main 256103b] Fix button color」
- 同内容でも別コミットになる点に注意が必要と明記している。 [^]
  - Footnote: 「コミットログを見るとmainブランチでコミットされているのがわかる。ただし別のコミットになる点に注意」
- PRをマージすると履歴が複雑になり、後から見ると分かりにくい可能性がある。 [^]
  - Footnote: 「あとから見たときになんだろう？にはなりそう。」
- 基本は小さなブランチを頻繁にマージし、cherry-pickは必要な場合に使う方針だとまとめている。 [^]
  - Footnote: 「ブランチを『細かく』作って『頻繁』にマージ…そのためにチェリーピックは存在」

### References
- https://zenn.dev/kun432/scraps/58b40bf359e4bb

## VoxCPMを高速化する「Nano-vLLM-VoxCPM」を試す
- Date: 2026-04-08T19:10:00+09:00

### Executive Summary
- VoxCPM2は音声品質は良いがリアルタイム用途には生成が遅めという前提から開始。
- 高速推論向けとして公式リポジトリで紹介されていたNano-vLLM-VoxCPMを試す。
- Nano-vLLMベースでPyTorch実装より高速、同時リクエスト対応、非同期APIを特徴とする。
- Pythonパッケージに加え、FastAPIデモが用意されている点を確認。
- インストールはpip/uvで可能だが、FastAPIデモはPyPI未公開。
- Linux+NVIDIA GPU、Python 3.10+、flash-attn必須でCPUのみは非対応。
- example.pyでの起動やfrom_pretrainedでのモデル読み込み手順を示す。
- APIパラメータやベンチマーク指標・実行例も整理されている。

### Key Findings
- VoxCPM2は遅めなので、より高速な推論エンジンとしてNano-vLLM-VoxCPMが推奨されている。 [^]
  - Footnote: 「リアルタイム用途で使うにはちょっと生成は遅め…より高速に推論できるのでオススメ、と紹介されていたのが、Nano-vLLM-VoxCPM」
- Nano-vLLM-VoxCPMはPyTorch実装より高速で、同時リクエスト対応・非同期APIを備える。 [^]
  - Footnote: 「PyTorch実装版よりも高速」「同時リクエスト処理に対応」「使いやすい非同期APIインターフェース」
- リポジトリにはPythonパッケージと、オプションのFastAPIデモアプリが含まれる。 [^]
  - Footnote: 「Pythonパッケージ…と、オプションとしてFastAPIデモアプリケーションが含まれています」
- FastAPIデモはPyPIに公開されておらず、別途取得が必要とされる。 [^]
  - Footnote: 「FastAPIデモサービス…はPyPIには公開されていません」
- 実行要件はLinux+NVIDIA GPU、Python 3.10以上、flash-attn必須でCPUのみは非対応。 [^]
  - Footnote: 「Linux環境 + NVIDIA GPU（CUDA対応）」「Python 3.10以上」「flash-attn パッケージが必須」「CPUのみの環境での実行はサポートしていません」
- from_pretrainedはローカル/Hubのモデル指定に対応し、config.json・*.safetensors・audiovae.pthが必要。 [^]
  - Footnote: 「ローカルのモデルディレクトリパス」「HuggingFaceリポジトリID」「config.json」「*.safetensors」「audiovae.pth」
- APIの主要パラメータとしてmax_generate_length=2000、temperature=1.0、cfg_value=1.5が示されている。 [^]
  - Footnote: 「max_generate_length…既定値は 2000」「temperature…既定値は 1.0」「cfg_value…既定値は 1.5」

### References
- https://zenn.dev/kun432/scraps/0ebb3793132bdb
