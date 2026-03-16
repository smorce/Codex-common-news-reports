# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-03-16T09:09:19+09:00
- Articles: 3

## 無料でローカル動作するAI顧客管理ツール「DenchClaw」は自然言語でデータベースを扱えて見込み客への連絡も自動化可能
- Date: 2026-03-15T22:15:00+09:00

### Executive Summary
- ローカル環境で動くAI CRM「DenchClaw」を紹介する記事。
- クラウドに顧客データを置きたくない需要に応える設計が強調されている。
- OpenClawを基盤にした無料のAI CRMとして位置付けられる。
- 自然言語でCRMデータベースを操作し、SQLへ変換して問い合わせる仕組みがある。
- LinkedInやメールを使った見込み客探索・連絡の自動化を想定。
- 複数サービス連携で連絡先やドキュメントを一元化できる。
- 営業パイプラインの可視化やリード情報補完まで扱えると説明される。

### Key Findings
- クラウドに顧客データを預けたくない層向けに、ローカル動作型AI CRMとして設計されている。 [^]
  - Footnote: 「顧客データはクラウドに預けたくないが、AIで整理や営業作業は自動化したい」というニーズを狙ったローカル動作型のAI CRM
- OpenClawをベースにした無料のAI CRMとして提供されている。 [^]
  - Footnote: DenchClawはOpenClawをベースに作られた無料のAI CRM
- 自然言語でのDB操作と、LinkedIn・メールを使った連絡自動化に対応する。 [^]
  - Footnote: 自然言語によるデータベース操作やLinkedIn・メールを使った見込み客への連絡の自動化に対応
- Google DriveやNotion、Salesforceなど複数サービスと連携し、情報を統合できる。 [^]
  - Footnote: Google DriveやNotion、Salesforce、HubSpot、Gmail、Calendar、Slack、LinkedInなどのサービスと連携
- 英語で質問するとSQLに変換してDuckDBへ問い合わせる例が示されている。 [^]
  - Footnote: 簡単な英語で質問するとDenchClawがそれをSQLに変換してDuckDBへ問い合わせ
- LinkedInでの見込み客探索から連絡先補完、メッセージ作成・送信までを一括で処理できる。 [^]
  - Footnote: LinkedInを使った見込み客探しから連絡先情報の補完、メッセージの作成や送信までまとめて処理

### References
- https://gigazine.net/news/20260315-denchclaw-local-ai-crm/

## Stop Sloppypasta: Don't paste raw LLM output at people

### Executive Summary
- 未検証のLLM出力をそのまま貼り付ける行為を「sloppypasta」と定義して批判するエッセイ。
- 受け手に検証や要約の負担を押し付けるため失礼だと説明する。
- 具体例を挙げ、会話の流れを壊したり無関係な長文を投下する問題を示す。
- 送信者と受信者の労力が非対称になることが主要な害として描かれる。
- 「読む・検証する・要約する・開示する」などの簡潔なガイドラインを提示。
- AI出力が古い・誤りを含む可能性がある点を強調する。
- AIは生産性向上に使うべきだが、他者の負担にすべきではないと結ぶ。

### Key Findings
- sloppypastaは未読・未検証のLLM出力をそのまま貼り付ける行為として定義される。 [^]
  - Footnote: Verbatim LLM output copy-pasted at someone, unread, unrefined, and unrequested.
- 送信者が検討していないテキストを送ることは受信者に追加作業を要求し、失礼とされる。 [^]
  - Footnote: they are asking you to do work they chose not to do. The asymmetric effort makes it rude.
- チャットボットに聞いてそのまま転送する行為は検証や批判的レビューが欠けると指摘。 [^]
  - Footnote: They asked a chatbot and forwarded its response to you verbatim without validation or critical review.
- 「Read」「Verify」「Distill」「Disclose」「Share only when requested」「Share as a link」の簡易指針が示される。 [^]
  - Footnote: Read. / Verify. / Distill. / Disclose. / Share only when requested. / Share as a link.
- LLMは古い知識や誤情報を生成しうるため、事実確認が必要とされる。 [^]
  - Footnote: LLMs are trained to "be helpful", and will produce outdated facts, wrong figures, and plausible nonsense
- AI利用の開示は信頼を回復し、受信者が何を検証済みか判断できるようにする。 [^]
  - Footnote: Disclosure restores the trust signals that sloppypasta destroys

### References
- https://stopsloppypasta.ai/

## What is agentic engineering? - Agentic Engineering Patterns - Simon Willison's Weblog
- Date: 2026-03-15

### Executive Summary
- 「agentic engineering」をコーディングエージェント支援でのソフト開発と定義する。
- コーディングエージェントはコードを書くだけでなく実行できる点が重要とされる。
- エージェントはツールをループで回して目標達成を目指すという定義を示す。
- コード実行能力が、実用的な反復改善を可能にする中核だと述べる。
- 人間の役割は何を作るべきかの判断や、要件に合う選択肢の探索にある。
- 道具の提供、問題定義、検証と反復が成功の鍵と説明する。
- ガイドは進化中で、章の追加・更新を続けると明記する。

### Key Findings
- agentic engineeringはコーディングエージェント支援での開発実践を指す。 [^]
  - Footnote: the practice of developing software with the assistance of coding agents.
- コーディングエージェントはコードを書くだけでなく実行もできる。 [^]
  - Footnote: agents that can both write and execute code.
- エージェントはツールをループで回してゴールに到達するという定義を提示。 [^]
  - Footnote: Agents run tools in a loop to achieve a goal
- コード実行がagentic engineeringを成立させる決定的な能力だと強調する。 [^]
  - Footnote: Code execution is the defining capability that makes agentic engineering possible.
- 人間は何を書くべきかを判断し、トレードオフを見極める役割を担う。 [^]
  - Footnote: The craft has always been figuring out what code to write.
- ツール提供、適切な問題定義、検証と反復で信頼性を高める必要がある。 [^]
  - Footnote: provide our coding agents with the tools they need... specify those problems... verify and iterate
- 指示やツールを更新すれば、コーディングエージェントは学習を反映できる。 [^]
  - Footnote: coding agents can, provided we deliberately update our instructions and tool harnesses

### References
- https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/
