# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-06-04T09:05:48+09:00
- Articles: 3

## マイクロソフト、翻訳“コストゼロ”も可能 EdgeのローカルAI強化 - Impress Watch
- Date: 2026-06-03T13:30:00+09:00

### Executive Summary
- Microsoft Edge向けオンデバイス生成AIに3つの更新が発表された。
- 既存のPrompt APIとWriting Assistance APIでは、より小さく効率的なAion-1.0-Instructが導入される。
- Aion-1.0-Instructにより、低性能GPUやGPU非搭載端末でも利用可能範囲が広がる。
- Edge 148にはLanguage Detector APIとTranslator APIが追加される。
- 翻訳は端末ローカルで実行され、クラウドを介さない設計になっている。
- ローカル処理により、プライバシー向上、ネットワーク非依存、翻訳コストゼロが利点として示された。
- Web Speech APIもオンデバイス対応し、低遅延と既存コードからの移行容易性が強調された。

### Key Findings
- Edgeのオンデバイス生成AI更新は3項目で構成される。 [^]
  - Footnote: 記事本文に「Microsoft Edgeに導入するオンデバイス動作の生成AIについて3つのアップデートを発表した」とある。
- Prompt APIとWriting Assistance APIのモデルはPhi-4-miniからAion-1.0-Instructへ置き換わる。 [^]
  - Footnote: 記事本文に「『Phi-4-mini』に代わり、より小さく効率的な小規模言語モデル『Aion-1.0-Instruct』が導入される」とある。
- 対応端末は低性能GPU搭載機やGPU非搭載機まで拡大する。 [^]
  - Footnote: 記事本文に「性能の低いGPUを搭載したデバイスや、CPU推論を介したGPU非搭載のデバイスなど、サポートできるデバイスが大幅に拡大する」とある。
- Edge 148には言語検出と翻訳のオンデバイスAPIが入る。 [^]
  - Footnote: 記事本文に「Microsoft Edge 148には…『Language Detector API』と『Translator API』が導入」とある。
- 翻訳APIは145以上の言語をサポートする。 [^]
  - Footnote: 記事本文に「高速で高品質な翻訳を提供、145以上の言語をサポートする」とある。
- クラウド不要のローカル翻訳により、費用と通信依存を抑えられる。 [^]
  - Footnote: 記事本文に「クラウドを介することなく端末ローカルで翻訳処理を行なえるため、プライバシー向上、ネットワーク非依存、翻訳コストゼロ」とある。
- Web Speech APIのオンデバイス対応は既存実装から移行しやすい。 [^]
  - Footnote: 記事本文に「既存の『Web Speech API』のコードのわずかな修正でオンデバイス対応にできる」とある。

### References
- https://www.watch.impress.co.jp/docs/news/2114069.html
- https://ai-news.dev/

## 使うほど賢くなる人気AIエージェントのアプリ版「Hermes Desktop」登場 - PC Watch
- Date: 2026-06-03T17:38:00+09:00

### Executive Summary
- Nous ResearchはHermes AgentのデスクトップアプリであるHermes Desktopを公開した。
- 公開形態はプレビューで、正式版前の利用開始として位置付けられる。
- Hermes Agentは自己改善型のAIエージェントとして紹介されている。
- 従来はCLI版として提供されていたが、デスクトップアプリにより操作性が変わる。
- チャット機能が1カ所にまとめられ、利用導線が整理された。
- スキル管理も容易になり、エージェント利用の管理負担を下げる狙いがある。
- 6種類のテーマを内蔵し、カスタマイズ性と利用者層の広がりが期待されている。

### Key Findings
- Hermes DesktopはHermes Agentのデスクトップアプリとして公開された。 [^]
  - Footnote: 記事本文に「自己改善型のAIエージェント『Hermes Agent』のデスクトップアプリ『Hermes Desktop』をプレビューとして公開」とある。
- 公開日は2026年6月3日である。 [^]
  - Footnote: 記事本文の日時欄に「2026年6月3日 17:38」とある。
- Hermes AgentはこれまでCLI版として展開されていた。 [^]
  - Footnote: 記事本文に「Hermes AgentはこれまでCLI版として展開してきた」とある。
- デスクトップ化により直感的な操作が可能になる。 [^]
  - Footnote: 記事本文に「デスクトップアプリの登場により、より直感的な操作が可能となった」とある。
- チャットは1カ所に集約される。 [^]
  - Footnote: 記事本文に「チャットが1カ所にまとめられ」とある。
- スキル管理も容易になる。 [^]
  - Footnote: 記事本文に「スキルなども容易に管理できる」とある。
- 6種類のテーマが内蔵され、見た目の調整が可能である。 [^]
  - Footnote: 記事本文に「6種類のテーマを内蔵し、カスタマイズ性が高い」とある。

### References
- https://pc.watch.impress.co.jp/docs/news/2114181.html
- https://ai-news.dev/

## マイクロソフト、AIエージェントにWindowsアプリ開発の知識を与える「Windows Development Skills」を一般提供開始 － Publickey
- Date: 2026-06-04T00:00:00+09:00

### Executive Summary
- MicrosoftはWindows Development Skillsの一般提供開始を発表した。
- 発表はMicrosoft Build 2026に合わせて行われた。
- この機能はAIエージェントへWindowsアプリ開発ライフサイクルの知識を与える。
- 提供形態はプラグインで、AIエージェントにインストールして使う。
- 対象にはGitHub Copilot、Claude Code、OpenAI Codexが含まれる。
- WinUI 3とWindows App SDKを用いたネイティブWindowsアプリ開発を支援する。
- ScaffoldからShipまでの開発サイクルを扱い、トークン効率の向上にも資するとされる。

### Key Findings
- Windows Development Skillsは一般提供が始まった。 [^]
  - Footnote: 記事本文に「『Windows Development Skills』の一般提供を開始したと発表しました」とある。
- 発表はMicrosoft Build 2026で行われた。 [^]
  - Footnote: 記事本文に「年次イベント『Microsoft Build 2026』で」とある。
- 目的はAIエージェントにWindowsアプリ開発ライフサイクルの知識を与えること。 [^]
  - Footnote: 記事本文に「AIエージェントにWindowsアプリ開発のライフサイクル全体に関する知識を与える」とある。
- 機能はプラグイン形式で提供される。 [^]
  - Footnote: 記事本文に「プラグインの形式になっており、AIエージェントにインストールをして利用を開始します」とある。
- GitHub Copilot、Claude Code、OpenAI Codexでの利用が想定される。 [^]
  - Footnote: 記事本文に「GitHub Copilot、Claude Clode、OpenAI Codexに対して」とある。
- WinUI 3とWindows App SDKによるネイティブ開発を支援する。 [^]
  - Footnote: 記事本文に「WindowsのUIフレームワーク『WinUI 3』と『Windows App SDK』を用いたネイティブなWindowsアプリケーション開発」とある。
- 開発工程はScaffoldからShipまでの一連の流れとして提示される。 [^]
  - Footnote: 記事本文に「『Scaffold → Design → Build → Run → Test → Package → Ship』のサイクル」とある。
- アプリ開発時のトークン効率にも効果があるとされる。 [^]
  - Footnote: 記事本文に「アプリケーション開発時のトークンの効率的な利用にも資するとしています」とある。

### References
- https://www.publickey1.jp/blog/26/aiwindowswindows_development_skills.html
- https://ai-news.dev/
