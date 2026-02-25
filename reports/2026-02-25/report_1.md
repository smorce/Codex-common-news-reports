# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-02-25T09:02:21.9547643+09:00
- Articles: 3

## メモ: Dockerのネットワークについて（iptablesとか）
- Date: 2026-02-24T15:43:00+09:00

### Executive Summary
- OpenClaw的なものを安全に試すためにVMやDockerとネットワーク制御を検討している。
- Dockerネットワークやiptablesの理解不足を踏まえ、備忘メモとして整理する方針。
- ChatGPTと会話しながらまとめる前提で進めている。
- ホストOSはUbuntu-24.04を想定している。
- nftablesより情報量が多いとしてiptables中心で学ぶ方針を示した。
- Docker未導入の素のUbuntu-24.04状態で`ip a`の出力を確認している。
- filter/natテーブルの`iptables -L`出力を列挙し、ufwの存在にも言及した。

### Key Findings
- 安全に試すためVM/Dockerとネットワーク制御を検討している。 [^]
  - Footnote: OpenClaw的なものを安全に試したい、ということで、VMやDockerを駆使しつつ、かつネットワークも制御して
- Dockerネットワークやiptablesの理解不足を前提にメモ化している。 [^]
  - Footnote: Dockerのネットワークやiptablesなど、自分はちゃんと理解できていないと思うので、とりあえずメモ。
- まとめはChatGPTとの対話を前提にしている。 [^]
  - Footnote: ChatGPTと会話しながらまとめる。
- ホストOSはUbuntu-24.04を想定している。 [^]
  - Footnote: なお、ホストOSは Ubuntu-24.04 を想定。
- nftablesよりiptablesを優先して学ぶ意図を示した。 [^]
  - Footnote: 今なら nftables を学ぶほうがいい気もするが、Dockerのドキュメントなども含めて色々見る限り iptables のほうが情報量が多いので
- Docker未導入の素のUbuntu-24.04でネットワーク状態を確認している。 [^]
  - Footnote: Dockerを入れていない素のUbuntu-24.04の状態。
- iptablesのfilter/natテーブル出力を確認している。 [^]
  - Footnote: Chain INPUT (policy ACCEPT)
- Ubuntuではufwの存在に触れている。 [^]
  - Footnote: Ubuntuの場合はufwがいる。

### References
- https://zenn.dev/kun432/scraps/1551c3bd980c15
- https://qiita.com/bashaway/items/e405d59d92670fbc5341

## Agent Skills に対応したエージェントを実装してみる（Chat Completions API）
- Date: 2026-02-22T18:12:00+09:00

### Executive Summary
- Claude Codeでのスキル活用経験を踏まえ、他フレームワークへの組込みを考える導入がある。
- Agent Skillsのドキュメントをフラットに整理する意図が示されている。
- Agent Skillsはエージェントに機能と専門知識を付与するシンプルなオープンフォーマットと説明。
- スキルは指示書・スクリプト・リソースをフォルダにまとめる構成である。
- スキルは業務に必要なコンテキストを補い、必要時に参照できる点を強調。
- SKILL.mdやscripts/references/assetsを含む基本構造が提示されている。
- 段階的情報開示として発見→有効化→実行の流れが説明されている。
- スキル数は2〜3個が最適で、増えすぎると効果低下とされている。

### Key Findings
- 既存フレームワークのエージェントへスキル組込みを検討している。 [^]
  - Footnote: 例えば既存のフレームワークで作ったエージェントなんかに、どうやって組み込むのか？を考えたい。
- Agent Skillsは機能と専門知識を付与するオープンなフォーマットと説明されている。 [^]
  - Footnote: エージェントに「機能」と「専門知識」を付与するための、シンプル・オープンなフォーマット
- スキルは指示書・スクリプト・リソースをフォルダにまとめたものと定義される。 [^]
  - Footnote: 以下をファイルシステム上のフォルダにまとめたもの 指示書 スクリプト リソース
- スキルは業務遂行に必要なコンテキストを提供し、必要時に参照できる。 [^]
  - Footnote: スキルは、業務の遂行に必要なコンテキスト（手順やユーザー固有コンテキスト）を提供する
- SKILL.mdを含む基本構造が提示されている。 [^]
  - Footnote: ├── SKILL.md          # 必須: プロンプト指示＋メタデータ
- 段階的情報開示の流れは発見→有効化→実行と説明されている。 [^]
  - Footnote: 「段階的情報開示」 発見 有効化 実行
- SKILL.mdにはYAMLフロントマターのname/descriptionが必須とされる。 [^]
  - Footnote: SKILL.md YAML形式のフロントマターが必須 name : スキル名。 description : このスキルを使用する場面。
- 最適なスキル数は2〜3個で、4個以上は効果低下とされる。 [^]
  - Footnote: 最適なスキルの数は2〜3個。4個以上になると効果が急激に低下。
- スキル実行はハーネス実装にも依存し、フォーマット指示が重要とされる。 [^]
  - Footnote: スキルを実行するエージェントハーネスの実装にも効果は依存する。

### References
- https://zenn.dev/kun432/scraps/701d45936960c1
- https://agentskills.io/home
- https://github.com/agentskills/agentskills

## 「Qwen3-Swallow-v0.2」を試す
- Date: 2026-02-21T17:43:00+09:00

### Executive Summary
- Qwen3-Swallow-v0.2を試したスクラップで、関連情報の整理が中心。
- リリース告知では継続事前学習+SFT+強化学習の刷新と日本語性能・推論能力の両立が示される。
- Apache 2.0ライセンスで利用できる旨が告知されている。
- 開発テックブログと来月のTechnical Report予定が紹介されている。
- Hugging Faceのコレクションや関連リンクが提示されている。
- パラメータサイズ8B/30B-A3B/32B、学習フェーズCPT/SFT/RLの9モデルに量子化6を加え合計15モデルと説明。
- 追加学習予定がない場合はRLモデル、OOM時はAWQ/GPTQ量子化を推奨としている。
- Tool Callingは未検証との注意が付いている。

### Key Findings
- 継続事前学習+SFT+強化学習を刷新し、日本語性能と推論能力の両立を掲げる。 [^]
  - Footnote: 継続事前学習＋SFT＋強化学習を全面刷新し、日本語性能と推論能力を両立させたオープンなLLM
- Apache 2.0ライセンスで利用可能と告知されている。 [^]
  - Footnote: Apache 2.0ライセンスで利用できます。
- テックブログ執筆と来月のTechnical Report予定が述べられている。 [^]
  - Footnote: さらに詳細については来月発表予定のTechnical Reportをご覧ください！
- パラメータサイズは8B/30B-A3B/32Bで、CPT/SFT/RLの学習フェーズがある。 [^]
  - Footnote: パラメータサイズ: 8B / 30B-A3B / 32B 学習フェーズ: CPT / SFT / RL
- 9モデルに量子化6モデルを加え合計15モデルと説明されている。 [^]
  - Footnote: 合計15モデルとなっている。
- 追加学習なしならRLモデル、OOM時はAWQ/GPTQ量子化モデルを推奨。 [^]
  - Footnote: 追加的な学習を行う予定ではない方は、RLモデル(xx-RL-v0.2)を利用してください。GPUのメモリサイズ等でOut of Memory(OOM)が発生する場合は、量子化モデル(xx-AWQ-INT4またはxx-GPTQ-INT4)を利用してください。
- SFTモデルについてはGGUFがある旨が言及されている。 [^]
  - Footnote: 現時点ではSFTモデルについてはmmngaさんのGGUFがある。
- まとめとして8B〜120Bのバリエーション、日本語強化、オープンライセンスが利点と述べられる。 [^]
  - Footnote: 8B〜120Bと幅広いバリエーション 日本語対応が強化 オープンなライセンス
- Tool Callingは未検証との注意がある。 [^]
  - Footnote: ただどちらも Tool Calling は検証されていないようなので

### References
- https://zenn.dev/kun432/scraps/473767858dcfee
- https://swallow-llm.github.io/qwen3-swallow.
- https://huggingface.co/collections/tokyotech-llm/qwen3-swallow-v02
