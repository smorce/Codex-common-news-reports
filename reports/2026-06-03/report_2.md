# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-06-03T09:05:39.1745458+09:00
- Articles: 3

## GitHub Copilotの従量課金がついに開始、「AIクレジット」を使い切ると追加利用には別料金が必要に
- Date: 2026-06-02T11:48:00+09:00

### Executive Summary
- GitHub Copilotは2026年6月1日から全プランでGitHub AIクレジットを使う従量課金制に移行した。
- 従来の月額プラン内利用から、AI処理の重さに応じて共通単位のクレジットを消費する形へ変わった。
- 各プランには毎月の標準利用分が含まれ、超過後も使うには追加支出上限の設定が必要になる。
- コードレビューではGitHub AIクレジットに加え、標準のGitHubホストランナー利用時にGitHub Actions実行時間も消費する。
- セルフホストランナーを使う場合はGitHub Actionsの実行時間消費を避けられる。
- 組織やEnterprise向けにはユーザー単位の予算設定が一般提供され、利用量全体を統制できる。
- ヘビーユーザー向けのCopilot Maxも有効化されたが、一部個人向け新規登録は記事時点で一時停止中である。

### Key Findings
- GitHub Copilotの課金単位はGitHub AIクレジットへ移行した。 [^]
  - Footnote: 記事は、GitHubが2026年6月1日からすべてのGitHub CopilotプランでGitHub AIクレジットを利用量の単位とする従量課金制を有効化したと説明している。
- 処理の複雑さに応じて消費クレジットが変動する。 [^]
  - Footnote: 軽い処理では少ないクレジット、複雑な処理や大きな作業では多くのクレジットを消費する仕組みと記載されている。
- 標準利用分を超えた継続利用には追加支出上限の設定が必要になる。 [^]
  - Footnote: 記事は、標準利用分を使い切った後も使い続ける場合、追加の支出上限を設定して月末に利用量に応じた料金を支払うと説明している。
- コードレビューはAIクレジットだけでなくGitHub Actions実行時間も消費し得る。 [^]
  - Footnote: GitHub Copilotによるコードレビューは標準でGitHubホストランナーを使用するため、2026年6月1日からGitHub AIクレジットに加えてGitHub Actionsの実行時間も消費するとある。
- セルフホストランナー利用時はActions実行時間の消費を回避できる。 [^]
  - Footnote: 記事は、セルフホストランナーを利用する場合はGitHub Actionsの実行時間は消費しないと説明している。
- 管理者はユーザー単位の予算で組織内利用を制御できる。 [^]
  - Footnote: 組織やEnterprise向けには、全ユーザー共通予算や特定ユーザー群への上書き予算を設定できる機能が一般提供されたと記載されている。
- Copilot Maxは集中的なCopilot利用を想定した上位プランとして有効化された。 [^]
  - Footnote: 記事は、Copilot Maxが既存のStudent、Pro、Pro+加入者向け上位プランで、より多い標準利用分と高い支出上限を備えると述べている。

### References
- https://gigazine.net/news/20260602-github-copilot-update-plan/
- https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/

## 「AIを使え」から「あまり使うな」へ、米企業が半年で生成AIの利用制限に動き始めた理由
- Date: 2026-06-02T00:00:00+09:00

### Executive Summary
- 記事は、米国企業が生成AI利用を無制限に推奨する段階から、利用量やツールを絞る段階へ移り始めたと論じている。
- 背景にはトークン消費の増加と、AI投資のROIを経営層が問い直し始めたことがある。
- WSJの記事を起点に、Microsoft、Meta、Uber、Salesforce、DoorDashなどの動きが紹介されている。
- MicrosoftではClaude Codeの社内利用停止通知が取り上げられ、標準化や統制の文脈で説明されている。
- 記事は、単純な禁止ではなく「考えて使え」への転換としてこの潮流を位置づけている。
- 日本企業にも同様の利用制限やROI確認が波及する可能性が示唆されている。
- 現場社員には、制限が来る前にAI利用の成果、コスト、代替手段を説明できる準備が求められる。

### Key Findings
- 米国企業ではAI利用を配給制にする動きが出ている。 [^]
  - Footnote: 記事はWSJの見出しとして「米国企業はAIを配給制にし始めた」という表現を紹介している。
- 主要企業の経営層は、AI利用拡大から利用抑制とROI再評価へ姿勢を変えつつある。 [^]
  - Footnote: Microsoft、Meta、Uber、Salesforce、DoorDashのCTOやCOOが、利用を抑え、ツールを絞り、ROIを問い直す側に回り始めたと説明されている。
- 合言葉は「AIを使え」から「考えて使え」へ変化した。 [^]
  - Footnote: 記事本文は、この数カ月で経営の合言葉が「AIを使え」から「考えて使え」へ変化したと述べている。
- MicrosoftはClaude Codeの社内利用を停止する通知を出したとされる。 [^]
  - Footnote: 記事は、MicrosoftがExperiences and Devices部門の社員に対し、Claude Codeの社内利用を6月30日付で停止すると通知したと整理している。
- Microsoftの動機は外部からはコストかガバナンスか判然としないが、実質的には利用量を絞る指示と捉えられている。 [^]
  - Footnote: 広報担当は標準化が動機と説明する一方、記事は「使う量を絞れ」という事実上の指示であることは間違いないと述べている。
- 社内利用を絞りつつ、対外顧客向けにはAnthropicモデルを提供する二段構えも示されている。 [^]
  - Footnote: Microsoft Foundryでは2026年に最新のClaude Opus 4.6を含むAnthropicモデルの提供を開始しており、関係そのものを断ったわけではないと説明されている。
- 日本企業の現場にも、AI利用制限に備えた説明責任が必要になる可能性がある。 [^]
  - Footnote: 記事は、このトレンドが日本企業の経営層にも届くのか、現場で働く社員は何を準備すべきかを問題提起している。

### References
- https://jbpress.ismedia.jp/articles/-/95142

## AlibabaがClaude Opus 4.6に匹敵するAIモデル「Qwen3.7-Plus」を発表
- Date: 2026-06-02T14:19:00+09:00

### Executive Summary
- AlibabaのAI研究チームQwenは、新モデルQwen3.7-Plusを発表した。
- Qwen3.7-Plusはテキスト、画像、動画入力に対応するマルチモーダルモデルである。
- 記事では、一部ベンチマークでClaude Opus 4.6を上回ったと紹介されている。
- Terminal-Bench 2.0では、Qwen3.7-PlusがClaude Opus 4.6を超えるスコアを記録したとされる。
- モデルは対話型ハイブリッドエージェントとして、UI認識、自動操作、画像に基づくコード生成などを想定している。
- デモとして、画像差分をPythonで取得して間違い探しを解く操作や、既存アプリのクローンコード生成が紹介されている。
- Qwen StudioやAlibabaのAI経由で利用でき、100万トークン当たり入力0.4ドル、出力1.6ドルの価格が示されている。

### Key Findings
- Qwen3.7-PlusはAlibabaのQwen(Tongyi Lab)が発表した新AIモデルである。 [^]
  - Footnote: 記事冒頭は、AlibabaのAI研究チームであるQwen(Tongyi Lab)がAIモデル「Qwen3.7-Plus」を発表したと述べている。
- 一部ベンチマークではClaude Opus 4.6を上回る性能が示された。 [^]
  - Footnote: 記事は、Qwen3.7-Plusが一部のベンチマークテストでClaude Opus 4.6のスコアを上回っていると説明している。
- Qwen3.7-Plusはテキスト、画像、動画を入力できるマルチモーダルモデルである。 [^]
  - Footnote: 本文に、Qwen3.7-Plusはテキスト・画像・動画の入力に対応したマルチモーダルモデルと記載されている。
- Terminal-Bench 2.0では複数モデルとの比較が行われた。 [^]
  - Footnote: 記事は、Qwen3.7-Plus、Qwen3.6-Plus、DeepSeek-V4-Pro、GLM-5.1、Kimi K2.6、Claude Opus 4.6、GPT-5.4でTerminal-Bench 2.0を実行した結果を紹介している。
- モデルはUI認識や自動操作を含むエージェント用途を想定している。 [^]
  - Footnote: Qwen3.7-Plusは、アプリのUIを認識して自動操作、画像入力に基づくコード記述、インターネット上の知識を活用した視覚質問回答が可能と説明されている。
- 価格は100万トークン当たり入力0.4ドル、キャッシュ入力0.08ドル、出力1.6ドルと示された。 [^]
  - Footnote: 記事は、100万トークン当たりの価格として入力0.4ドル、キャッシュあり入力0.08ドル、出力1.6ドルを挙げている。
- 利用経路はQwen StudioとAlibabaのAI経由とされる。 [^]
  - Footnote: 本文は、Qwen3.7-PlusがチャットAIサービスのQwen Studioで利用可能なほか、AlibabaのAI経由でも使用できると記載している。

### References
- https://gigazine.net/news/20260602-qwen3-7-plus/
- https://qwen.ai/blog?id=qwen3.7-plus
