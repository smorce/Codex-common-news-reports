# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-03-09T09:08:50+09:00
- Articles: 3

## AIエージェント7体でパープルチーム演習を回してみた
- Date: 2026-03-07

### Executive Summary
- AIエージェント7体でパープルチーム演習を実施し、設計・実行・評価・執筆までAIが担当した。
- 演習は閉じたラボ環境で行われ、無許可攻撃の禁止が明記されている。
- Round 1はDomain Admin前提でDCSync等を実施し、攻撃のリアリティが低いと評価された。
- CrowのダミーアラートはalertsCount=0などの特徴で即座に見破られ、訓練にならない課題が露呈。
- Round 2は低権限からKerberoasting→オフラインクラック→横展開→RCEの現実的チェーンを完走。
- hashcatで11秒でパスワードをクラックし、SMBはWindows Firewallに阻まれた後に再挑戦した。
- Defender XDRが自動検知・封じ込めを実行し、Blue Teamの人手対応はほぼ出番がなかった。
- AIは数字だけで勝敗判断しがちで、人間レビューが文脈評価に不可欠と結論づけた。

### Key Findings
- 演習の設計・実行・評価・記事執筆までAIエージェントが担当し、人間はレビューのみ。 [^]
  - Footnote: 「この記事は AI（Eagle: 演習統制官エージェント）が執筆し、人間がレビューしたものです。」
- Round 1はDomain Adminの認証情報を最初から持つ前提で攻撃計画が組まれ、リアリティが低い。 [^]
  - Footnote: 「Round 1 はお試しということで、Fox は Domain Admin の認証情報を最初から持っている前提で攻撃を組み立てた。」
- Kerberoastingで取得したハッシュをhashcatで11秒でクラックし、弱いSPNパスワードのリスクを実証。 [^]
  - Footnote: 「11 秒。labuser0037:Welcome1」
- 横展開はWindows FirewallのSMB(445)ブロックで一度失敗し、基本的な防御層の有効性が示された。 [^]
  - Footnote: 「JP-02 の Windows Firewall が SMB (445) をブロックしていた。」
- XDRが検知と相関分析の後にアカウント自動無効化を行い、人的対応なしで封じ込めが完了。 [^]
  - Footnote: 「約 9 分後——XDR Attack Disruption が labuser0037 を自動無効化した。」
- Owlのトリアージ精度は100%だが、alertsCount=0のダミー判定が容易で訓練効果が低い。 [^]
  - Footnote: 「Owl のトリアージ精度：100%。」／「alertsCount = 0 です。全部ゼロでした。」

### References
- https://zenn.dev/microsoft/articles/ai-purple-team-exercise

## 現代人、深刻な「AI疲労」を発症していることが判明
- Date: 2026-03-08

### Executive Summary
- BCG・カリフォルニア大学リバーサイド校・ハーバードの共同研究が「AI疲労」を定義した。
- AIエージェント監視やマルチタスクが強い精神的疲労を生み、監督作業が増えると指摘。
- 米国の大企業勤務者の14%がAI疲労を経験し、優秀な人材ほど影響が大きい。
- 症状はメンタルフォグ、集中力低下、意思決定の鈍化に加え身体的疲労も含む。
- AIツールは3つ同時利用で生産性がピークに達し、4つ以上で切替負荷が増大する。
- AI疲労は軽微なミスを11%、重大ミスを39%増加させると報告された。
- 検証を諦め誤りを受容する「デス・クーリング」や離職意向34%の増加が示された。
- 対策としてAIツール同時使用数の制限と、思考の余白を確保するワークフロー再設計が急務。

### Key Findings
- AIエージェント監視やマルチタスクによる精神的疲労を「AI疲労」と定義した。 [^]
  - Footnote: 「AIエージェントの監視やAIのマルチタスクによって引き起こされる極度の精神的疲労を『AI疲労』と定義」
- 米国大企業勤務者の14%がAI疲労を経験し、優秀な人材ほど影響が大きい。 [^]
  - Footnote: 「米国のビジネスパーソンの14%がこの『AI疲労』を経験」
- 監督作業への移行が記憶力や注意力を著しく消耗させる。 [^]
  - Footnote: 「この絶え間ない監督作業は人間の記憶力と注意力を著しく消耗させ」
- 症状はメンタルフォグ、集中力低下、意思決定の鈍化に加え身体的疲労も含む。 [^]
  - Footnote: 「メンタルフォグ」「集中力の著しい低下、意思決定の鈍化」「眼精疲労や頭痛、首の痛み、睡眠障害」
- AIツールは3つ同時利用で生産性ピーク、4つ以上でパフォーマンスが低下する。 [^]
  - Footnote: 「3つのAIツールを並行して使用する段階で生産性はピーク」「4つ以上のAIツールを同時に稼働させると…パフォーマンスが低下」
- AI疲労は軽微ミス11%・重大ミス39%増加、離職意向34%に達する。 [^]
  - Footnote: 「軽微なミスを11%、安全性や成果に関わる重大なミスを39%増加」「離職意向は34%に達しており」

### References
- https://www.sbbit.jp/article/cont1/182151

## システムのメモリ・CPU・GPUに合わせて適切なAIモデルを教えてくれるターミナルツール「llmfit」 - GIGAZINE
- Date: 2026-03-08T19:00:00+09:00

### Executive Summary
- llmfitはPCのスペックに合わせて動作可能なAIモデルを提示するターミナルツールとして紹介された。
- 公式GitHubが案内するScoop経由でWindows 11へインストールする手順が示されている。
- 「llmfit」実行でTUIモードが起動し、モデル一覧を見やすく操作できる。
- FitフィルタでRunnable/Perfect/Good/Marginal/Too Tightなど動作適合度を切替できる。
- SortやUse Caseフィルタでスコア・tok/s・Params・Mem%・用途などで並べ替え可能。
- プランモードでは最小/推奨ハードウェアや実行パスを提示し、入力値の調整もできる。
- CLIモードでは一覧出力や検索、JSON形式の推薦などがコマンドで実行可能。
- テーマ切り替えにより配色を変更でき、複数のテーマが用意されている。

### Key Findings
- llmfitは実行PCの環境に合わせて最適なAIモデルを教えるツールとして紹介された。 [^]
  - Footnote: 「実行PCの環境に合わせてどのAIモデルなら快適に動作するのかを教えてくれる夢のようなツール」
- Windows 11ではScoopを導入し、scoop install llmfitでインストールできる。 [^]
  - Footnote: 「Scoopを利用する方法が紹介」「scoop install llmfit」
- TUIモードは「llmfit」実行で起動し、ターミナル上で操作できる。 [^]
  - Footnote: 「PowerShellで『llmfit』と入力しエンターキーを押すとTUIモードでllmfitが起動」
- FitのフィルタでRunnable/Perfect/Good/Marginal/Too Tightなど動作適合度を切替可能。 [^]
  - Footnote: 「Runnable」「Perfect」「Good」「Marginal」「Too Tight」
- プランモードは対象モデルの最小/推奨ハードウェアと実行パスを提示する。 [^]
  - Footnote: 「Minimum Hardware」「Recommended Hardware」「Run Paths」
- CLIモードは一覧出力や検索、JSON推薦などをコマンドで実行できる。 [^]
  - Footnote: 「llmfit --cli」「recommend --json --limit 5」

### References
- https://gigazine.net/news/20260308-llmfit/
- https://github.com/AlexsJones/llmfit
