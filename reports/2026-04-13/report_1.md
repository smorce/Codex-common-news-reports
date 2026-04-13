# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-04-13T09:09:22+09:00
- Articles: 3

## CodeDeploy で GitHubレポジトリのアプリをAutoScalingのEC2にデプロイする

### Executive Summary
- EC2単体ではなくALB＋AutoScaling構成でCodeDeployを試す位置づけ。
- 前回のEC2単体デプロイを踏まえ、AutoScalingでも同様に検証する流れ。
- 公式チュートリアルを参照しながら手順を進めている。
- AutoScalingでは起動テンプレートから新規インスタンスが起動される前提を指摘。
- CodeDeployは稼働中と今後起動するインスタンスの両方にデプロイ可能である必要がある。
- 追加のIAM権限として`ec2:RunInstances`等が必要と整理。
- デプロイは約6分で完了し、ALBのトラフィック制御が動作したと推測。

### Key Findings
- AutoScaling構成で試すのは、実運用ではALB＋AutoScalingが一般的という判断から。 [^]
  - Footnote: 「上記は単体のEC2だが実際にやる場合はALB＋AutoScalingにするほうが一般的だろう、ということで、AutoScalingでも試してみる。」
- AutoScalingでは起動テンプレートから新しいEC2インスタンスが起動する前提になる。 [^]
  - Footnote: 「Auto Scaling の場合は、起動テンプレートから新しい EC2インスタンスが起動することを前提になる。」
- CodeDeployは稼働中だけでなく今後起動するインスタンスにもデプロイできる必要がある。 [^]
  - Footnote: 「現在稼働しているインスタンスだけでなく、今後起動するインスタンスの両方に対して、デプロイできる必要がある。」
- CodeDeployのサービスロールには`ec2:RunInstances`/`ec2:CreateTags`/`iam:PassRole`の追加権限が必要。 [^]
  - Footnote: 「CodeDeployのサービスロールには、以下の権限が追加で必要になる。 ec2:RunInstances / ec2:CreateTags / iam:PassRole」
- ALBのロードバランシングを有効化してターゲットグループを選ぶと、デプロイ中のトラフィック遮断が行われる。 [^]
  - Footnote: 「Load balancerで『ロードバランシングを有効にする』、ロードバランサータイプで『ALB』にチェックを入れて、該当のターゲットグループを選択。これでデプロイ中にインスタンスとのトラフィックを止めてくれる。」
- デプロイは約6分で完了し、BlockTraffic/AllowTrafficがロードバランシング有効化時の動きと推測している。 [^]
  - Footnote: 「6分ほどかかったが、デプロイできた。BlockTraffic / AllowTraffic ってのが上のロードバランシングを有効にした場合の動きなのだと思う。」

### References
- https://zenn.dev/kun432/scraps/76cd9b1cceaa97
- https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-auto-scaling-group.html
- https://github.com/kun432/terraform-codedeploy-sample/tree/autoscaling

## 「Nix」を試す ② Zero to Nix（挫折した）

### Executive Summary
- 前回の公式チュートリアルの触りを試した続編。
- Nix言語や内部構造より、まず使い方に慣れたいという意向。
- 英語のチュートリアルが目的に合いそうと判断。
- Zero to Nixのチュートリアルを進めてみる方針。
- チュートリアルは公式ではなくDeterminate Nixインストーラを前提にしている。
- 用語説明が少なく理解が追いつかないと感じている。
- 結果としてこのチュートリアルは中断し、他の資料を読む予定。

### Key Findings
- 前回は公式ドキュメントのチュートリアルの触りを試した。 [^]
  - Footnote: 「前回とりあえず公式ドキュメントのチュートリアルの触りを試した。」
- 次のステップはNix言語や内部構造ではなく、まず使い方に慣れることを重視している。 [^]
  - Footnote: 「Nix言語とか内部構造とかに進んでもいいのだけど、もうしばらく使い方に慣れたい。」
- 目的に合いそうな英語チュートリアルとしてZero to Nixを選定した。 [^]
  - Footnote: 「英語のチュートリアル記事が良さそうな事が書いてあった。」「とりあえずこれを進めてみようかと思う。」
- Zero to Nixは公式インストーラではなくDeterminate Nixインストーラを使う前提。 [^]
  - Footnote: 「このチュートリアルは、Nix公式のインストーラではなく、Determinate Systemsというところが作成した Determinate Nixインストーラを使うことになっている。」
- Determinate NixはNixプロジェクトのダウンストリームで、遅延ツリーや並列評価など追加機能があると説明されている。 [^]
  - Footnote: 「Nix プロジェクトのダウンストリームディストリビューションです。このディストリビューションでは、遅延ツリー、並列評価、ネイティブLinuxビルダー など、アップストリーム版にはない多彩な機能を利用できます。」
- 用語説明が不足して理解が追いつかず、チュートリアル継続に迷いが生じている。 [^]
  - Footnote: 「いろいろな用語が出てくるが、説明なく進むので、正直理解が追いつかない。」
- 最終的に今回のチュートリアルはやめて、他の日本語/公式資料を読む方針に切り替えた。 [^]
  - Footnote: 「とりあえず今回のチュートリアルはやめた。上の記事や日本語のチュートリアル、あとは公式の記事をもう少し読んでみるつもり。」

### References
- https://zenn.dev/kun432/scraps/90e870e03d4643
- https://zero-to-nix.com/
- https://docs.determinate.systems/determinate-nix

## CodeDeploy で GitHubレポジトリのアプリをEC2にデプロイする

### Executive Summary
- CodeDeploy未経験のため、流れ把握を目的に実施した記録。
- 公式のGetting Startedを確認するところから始めている。
- Getting StartedはIAM準備が中心で、実デプロイはチュートリアル側にあると判断。
- チュートリアルのテーマ一覧を整理し、GitHubデプロイの題材に注目。
- GitHub連携はGUI前提に見え、Terraform対応に課題があると感じている。
- CodeConnectionsを調べるがCodeDeploy対応が見当たらず戸惑い。
- 結論としてCodePipelineの利用が必要になりそうと推測している。

### Key Findings
- 未経験のため、手順の流れを押さえる目的で実施している。 [^]
  - Footnote: 「やったことないので、流れを押さえるためにやる。」
- Getting StartedはIAM準備色が強く、実デプロイはチュートリアルに位置付けられていると見ている。 [^]
  - Footnote: 「Getting Startedセクション、IAMユーザやIAMロールなどの設定の準備という側面が強くて、実際のデプロイについては以下のチュートリアルのほうになってるように思える。」
- チュートリアルのテーマとしてWordPress/Hello World/オンプレ/Auto Scaling/GitHub/ECS/SAMなどが列挙されている。 [^]
  - Footnote: 「EC2インスタンス（Linux）に WordPress をデプロイ」「EC2インスタンス（Windows Server）に "Hello, World!" アプリをデプロイ」「オンプレミスのサーバにアプリをデプロイ」「オートスケーリンググループにアプリをデプロイ」「EC2インスタンスにGitHubからアプリをデプロイ」「Amazon ECSにアプリをデプロイ」「AWS SAMと組み合わせて、Lambda関数をデプロイ」
- GitHub連携はGUI前提に見え、AWS CLIにも作成系コマンドがなくTerraformからの作成は難しそうと判断。 [^]
  - Footnote: 「GitHubとの連携を設定するところはGUI前提っぽくなっている」「create-* みたいなのはないので、あらかじめ作っといて、Terraformからは参照だけさせるみたいなのはできなさそう。」
- 代替案としてCodePipelineやGitHub Actions+OIDCを挙げ、CodeConnectionsも検討している。 [^]
  - Footnote: 「となると、やっぱり CodePipeline / GitHub Actions + OIDC になるのかなー？と思って調べてみると、CodeConnections ってのがあるらしい。」
- CodeConnectionsはCodeDeploy対応が見当たらず、CodePipelineが必要になりそうと結論づけている。 [^]
  - Footnote: 「CodeConnections が使えるサービスに CodeDeploy が書いてない。」「この場合はCodePiplelineを使う必要がありそう。」

### References
- https://zenn.dev/kun432/scraps/7df1c9aa2dd3ba
- https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-codedeploy.html
- https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials.html
- https://aws.amazon.com/jp/training/digital/
