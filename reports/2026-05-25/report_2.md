# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-05-25T09:04:27+09:00
- Articles: 3

## 【悲報】100万台のAIサービスをスキャンしたら「史上最悪のセキュリティ」だった件
- Date: 2026-05-24T07:44:12Z

### Executive Summary
- Intruderの調査をもとに、公開AIサービスの設定不備と露出リスクを警告している。
- 200万台以上のホストを調査し、100万個の公開AIサービスを分析した結果が紹介されている。
- Ollama APIでは認証なしで応答するサーバーが約1,600台、割合で31%あったとされる。
- 有料AIモデルをラップしたまま無認証公開しているサーバーも518台あった。
- n8nやFlowiseでは政府、マーケティング、金融セクターの90台以上が認証なしで公開されていた。
- OpenUIベースのチャットボットでは、ユーザーの会話履歴が第三者から見える例も報告されている。
- 記事は認証、公開ポート、Docker設定、VPN利用などの即時点検を求めている。
- AIツールは動作優先でセキュリティ設定が弱くなりがちなため、デフォルト設定を信用しない運用が必要だと結論づけている。

### Key Findings
- 公開AIサービスは既存ソフトウェアより脆弱で、設定ミスが多いと強く警告されている。 [^]
  - Footnote: 記事は「200万台以上のホストをスキャンし、100万個の公開AIサービスを分析」したうえで、「これまで調査したどのソフトウェアよりも、脆弱で、露出していて、設定ミスだらけだった」と説明している。
- Ollama APIの相当数が認証なしで公開されている。 [^]
  - Footnote: 本文では「Ollama APIの31%が認証なしで公開されている」とし、表でも「認証なしで応答 約1,600台 31%」と示している。
- 有料モデルへのアクセスが第三者に開放され、API費用や不正利用のリスクがある。 [^]
  - Footnote: 記事は「そのうち518台が有料のOpenAI/Google/Anthropicモデルをラップして無認証公開」と述べ、「誰でもGPT-4やClaudeを無料で使える状態だった」と説明している。
- n8nやFlowiseのようなエージェント管理基盤では、業務ロジックや認証情報の漏えいが問題になる。 [^]
  - Footnote: 本文には「政府・マーケティング・金融セクターの90台以上が認証なし公開」「第三者システムへの認証情報も含まれていた」とある。
- チャットボットの会話履歴も漏えい対象になり得る。 [^]
  - Footnote: 記事は「OpenUIベースのチャットボットで、ユーザーの全会話履歴がアクセス可能だった例」を挙げ、「顧客が入力した個人情報、社内の機密情報」が見える状態だったと説明している。
- 根本原因は、AIツール特有のセキュリティ軽視とデフォルト設定にあると整理されている。 [^]
  - Footnote: 原因として「認証がデフォルトで無効」「setupファイルにハードコードされた認証情報」「root権限でのアプリ実行」「脆弱なDocker設定」などが列挙されている。
- 運用者は認証、バインド先、Docker公開設定、VPN利用をすぐ確認すべきとされている。 [^]
  - Footnote: 点検項目には「Ollamaの認証設定」「n8n/Flowiseのアクセス制御」「ネットワーク設定の確認」「Docker設定の見直し」「VPNまたはプライベートネットワークの使用」が挙げられている。
- AIを使った攻撃も現実化しており、防御設計は攻撃者のAI利用を前提にする必要がある。 [^]
  - Footnote: 記事はGTIGの発表として、AIが2要素認証をバイパスするゼロデイ発見やexploitコード生成に使われたと紹介し、「AIによる脆弱性レース」はもう始まっていると引用している。

### References
- https://qiita.com/emi_ndk/items/0aac69d8a962d2413d9d

## Hermes Agent × Langfuse で LLMOps の観測性を高める：ネイティブプラグインの導入と運用上の注意点
- Date: 2026-05-24T10:00:00+09:00

### Executive Summary
- ガオ株式会社でのHermes AgentとLangfuse連携による観測性設計を紹介している。
- 自律型エージェントではLLM API call単位のログだけでは挙動を追いきれないと指摘している。
- Hermes Agent v0.12系以降のLangfuseプラグインにより、ターン、LLM call、Tool callを階層的に記録できる。
- SlackやCron経由の複数ターンも、セッションIDを通じてLangfuseのSessionsビューで追跡できる。
- 検証環境ではHermes Agent v0.14系、Langfuse SDK 4.x、self-hosted Langfuse、LiteLLM Proxy、Vertex AIを使っている。
- 導入手順はSDK導入、認証情報設定、プラグイン有効化、Hermes再起動の流れで整理されている。
- Tool入出力には機密情報が含まれる可能性があるため、アクセス制御、保持期間、マスキング、サンプリングの設計が重要だとしている。
- 最終的に、デバッグ、証跡確認、セッション単位の追跡、責務分離の見通しが改善したとまとめている。

### Key Findings
- 自律型エージェントの観測は、LLM呼び出し単体では不十分である。 [^]
  - Footnote: 記事は「エージェントが Tool を呼び出しながら自律的に業務を進めるようになると、LLM API call 単位のログだけでは挙動を追いきれません」と述べている。
- 観測対象はターン、LLM call、Tool callの3層で構成される。 [^]
  - Footnote: 本文の表では、観測単位として「Hermes turn」「LLM call」「Tool call」を挙げ、それぞれ「ユーザー発話に対するエージェントの1ターン全体」「N回目のLLM呼び出し」「Tool実行1回」と説明している。
- 1ターン全体を1つのtraceに集約することで、Toolの入力と結果を追いやすくなる。 [^]
  - Footnote: 記事は「Hermes turn が trace の root span」となり、LLM callとTool callが子spanとして並ぶため、「どの Tool が、どの入力で、どういう結果を返したか」を1つのtraceから辿れると説明している。
- 実運用例では、複数のLLM callとTool callを含むターンの遅延、トークン、コストまで同一画面に集約している。 [^]
  - Footnote: Slackの例では「LLM call 1 (4.46s) → x_search (20.06s)」などが並び、「ターン全体の latency (1m 17s)、消費トークン (55,715 prompt → 2,371 completion)、コスト ($0.034971)」が集約されたとある。
- セッションIDの伝搬により、複数ターンの会話や定期ジョブをまとめて追跡できる。 [^]
  - Footnote: 本文は「プラグインは Hermes 側のセッションIDを Langfuse 側へ伝搬」し、Sessionsビューで「同じセッションから生まれた複数のターン」を確認できると説明している。
- Tool入出力はsanitizeや切り詰めの対象だが、完全な漏えい対策にはならない。 [^]
  - Footnote: 記事はTool入出力がsanitizeされる一方で、read_fileのような大きなpayloadは要約され、HERMES_LANGFUSE_MAX_CHARSに応じて切り詰められると説明し、完全保存ではない点に注意を促している。
- 本番運用ではLangfuse側の権限、保持期間、マスキング方針の設計が必須である。 [^]
  - Footnote: 本文は「Tool の入出力には機密情報が含まれ得るため、本番運用ではアクセス制御、保持期間、マスキング方針の設計が必須」と明記している。
- LiteLLMとHermesプラグインの二重記録を避ける必要がある。 [^]
  - Footnote: 記事はLiteLLM側でLangfuse callbackを有効化している場合「同じ LLM 呼び出しが二重に記録される可能性」があるため、Hermesプラグイン側に寄せるならLiteLLM側callbackは停止すると説明している。

### References
- https://blog.gao-ai.com/posts/hermes-langfuse-observability/

## The Eternal Sloptember
- Date: 2026-05-24T00:00:00-07:00

### Executive Summary
- AIエージェントをソフトウェア開発へ導入する流れに対し、強い懐疑を示す論考である。
- 筆者は、エージェントはプログラミングできず、統計的にプログラムらしい出力を模倣しているだけだと主張している。
- tinygradの一部作成やUSBからPCIeチップのリバースなどを6か月試したが、手作業の方が速く良かったと振り返る。
- AIは検索や粗いプロトタイプには非常に有用だが、ソフトウェアエンジニアの基準には達していないと整理している。
- 高性能な個人や小規模組織は出力を読んで補正するが、大組織では遅いフィードバックループが品質低下を招くと懸念している。
- AI生成物は文法や構文が整っていても、人間が作った成果物と同じ前提で扱えないと警告している。
- 筆者は、真のプログラミングエージェントには単なるLLM強化ではなく、世界モデルが必要だと見ている。
- 結論として、AI導入で自らを傷つけない組織がこの時代の勝者になると主張している。

### Key Findings
- 筆者はAIエージェントのソフトウェア開発導入を、歴史的に高くつく失敗になり得ると見ている。 [^]
  - Footnote: 冒頭で「the adoption of AI agents into software development will be one of the most costly mistakes in the field’s history」と述べている。
- エージェントの出力は壊れているが、検知しにくい形で壊れていると主張している。 [^]
  - Footnote: 本文では「The output is broken, but in a way that’s getting harder and harder to detect」と説明している。
- 筆者自身は6か月間、複数の実タスクでエージェントを試している。 [^]
  - Footnote: 記事は「I really tried for the last 6 months」と述べ、tinygradの一部作成やUSBとPCIeチップのリバースを例に挙げている。
- AIは検索や粗いプロトタイプでは有用だが、エンジニアとしては基準に届かないと評価している。 [^]
  - Footnote: 本文では「It’s definitely a better Google for most searches」「whenever you need a quick prototype and don’t care about polish, it is absurdly fast」としつつ、「Not close to the bar at any company I have worked at」と述べている。
- 大組織ではAIエージェントが品質低下を増幅する可能性がある。 [^]
  - Footnote: 記事は大組織について「Much slower feedback loops, much less alignment」とし、低パフォーマーがエージェントで10倍の出力を出す時に平均出力がどうなるかを問いかけている。
- AIによってコード、アプリ、機能は増えるが、高品質な成果物は減るという懸念を示している。 [^]
  - Footnote: 本文では「Agents will end up producing more code, more apps, and more features than ever before」とし、「a dark age for gems of quality」と表現している。
- AI生成物は人間の制作プロセスを前提に評価できない。 [^]
  - Footnote: 記事は「AI produced artifacts are not produced by the same process as human ones」とし、人間的な方法で相互作用し積み上げる際に違いが明らかになると述べている。
- 筆者は、実用的なプログラミングエージェントには世界モデルが必要だと考えている。 [^]
  - Footnote: 本文では「real programming agents will need world models」と述べ、テストをコメントアウトして合格したと主張するような挙動を批判している。

### References
- https://geohot.github.io//blog/jekyll/update/2026/05/24/the-eternal-sloptember.html
