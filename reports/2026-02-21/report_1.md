# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-02-21T09:01:53+09:00
- Articles: 3

## GPT-OSS-Swallow-v0.1
- Date: 2026-02-21T02:17:00+09:00

### Executive Summary
- GPT-OSS Swallow と Qwen3 Swallow のリリース告知が中心。
- 継続事前学習＋SFT＋強化学習のパイプラインを全面刷新。
- 日本語性能と推論能力の両立を狙ったオープンLLMと説明。
- Apache 2.0 ライセンスで利用可能と明記。
- GPT-OSS Swallow は 20B/120B のモデル規模が示されている。
- 量子化モデルは今後リリース予定という補足がある。
- 20B の GGUF 版が既に作成済みというコメントもある。

### Key Findings
- GPT-OSS Swallow と Qwen3 Swallow のリリースが告知された。 [^]
  - Footnote: GPT-OSS Swallow と Qwen3 Swallow をリリースしました。
- 継続事前学習・SFT・強化学習の刷新が明記されている。 [^]
  - Footnote: 継続事前学習＋SFT＋強化学習を全面刷新し、
- 日本語性能と推論能力の両立を狙うオープンLLMとして説明されている。 [^]
  - Footnote: 日本語性能と推論能力を両立させたオープンなLLMを、
- Apache 2.0 ライセンスでの利用が示されている。 [^]
  - Footnote: Apache 2.0ライセンスで利用できます。
- GPT-OSS Swallow は 20B/120B 規模のモデルとして記載されている。 [^]
  - Footnote: 大規模言語モデル (20B, 120B)
- 量子化モデルは今後リリース予定と補足されている。 [^]
  - Footnote: 量子化モデルは今後リリース予定とのこと。
- 20B の GGUF 版が既に作成済みであると記されている。 [^]
  - Footnote: 20Bは、GGUFがすでに作成されている。

### References
- https://zenn.dev/kun432/scraps/4f89cf406ae102
- https://twitter.com/chokkanorg/status/2024697240233922641
- https://huggingface.co/collections/tokyotech-llm/gpt-oss-swallow-v01

## AIエージェントビジネスシミュレーションベンチマーク「FoodTruck Bench」
- Date: 2026-02-20T20:31:00+09:00

### Executive Summary
- FoodTruck Bench はAIのビジネス運営能力を測るベンチマーク。
- 30日間のフードトラック運営をシミュレーションする。
- 出店場所・メニュー・価格・在庫・スタッフなどの判断が必要。
- 従来の知識テストとは異なる能力を測ると説明。
- 不確実性の中で一貫した意思決定を求める点が強調される。
- リーダーボードの数値だけでなく、体験でプロセス理解を促す。
- 作者は作り込みの良さに驚いたとまとめている。

### Key Findings
- FoodTruck Bench は AI ビジネスシミュレーションのベンチマークとして紹介されている。 [^]
  - Footnote: FoodTruck Bench — AI Business Simulation Benchmark
- 複数の最先端モデルで 30 日間のフードトラック運営シミュレーションを行う。 [^]
  - Footnote: Claude Opus 4.6, GPT-5.2, Gemini 3 Pro, DeepSeek V3.2, Grok 4.1 Fast — 30-day food truck simulation.
- AIエージェントがテキサス州オースティンでフードトラックを運営する設定。 [^]
  - Footnote: AIエージェントがテキサス州オースティンでフードトラックを運営します — 30日間のシミュレーション期間中、
- 出店場所やメニュー、価格、在庫、スタッフ配置などの意思決定が必要。 [^]
  - Footnote: 出店場所の選定、メニュー構成、価格設定、在庫管理、スタッフ配置などを決定します。
- 従来ベンチマークは知識能力を測るが、知識と実行は異なると説明。 [^]
  - Footnote: しかし、「知っている」ことと「実行できる」ことは根本的に異なるスキルなのです。
- 不確実性下で一貫したビジネス判断を下せるかを評価すると明示。 [^]
  - Footnote: 不確実性の中でAIが一貫したビジネス判断を下せるかどうか
- 立地・メニュー・価格・在庫・人員・融資など複数要素の同時管理を再現。 [^]
  - Footnote: 立地条件、メニュー構成、価格設定、在庫管理、人員配置、融資――これらすべてを同時に管理し、
- 誤った発注や価格設定、採用は即座に結果へ反映されると記述。 [^]
  - Footnote: 発注を1日怠れば食材が不足します。価格設定を誤れば顧客は離れていきます。不適切なスタッフを雇えば稼働率が低下します。
- リーダーボードの数値より体験による理解が重要だと説明。 [^]
  - Footnote: リーダーボード上の「GPT-5.2が19,000ドルを稼いだ」という数字よりも、実際に同じシミュレーションをご自身で体験することで、
- これはゲームではなくAI性能比較のベンチマークだと強調されている。 [^]
  - Footnote: 「これはフードトラック経営シミュレーションゲームではありません。これはAIの性能比較ベンチマークであり、あなた自身がそのベンチマークとなるのです」

### References
- https://zenn.dev/kun432/scraps/0253144c1789b0
- https://foodtruckbench.com/
- https://www.reddit.com/r/LocalLLaMA/comments/1r99wrj/can_glm5_survive_30_days_on_foodtruck_bench_full/

## 「GEPA」を試す
- Date: 2026-02-21T00:09:00+09:00

### Executive Summary
- GEPA を試すという短いメモ。
- DSPy を含めて腰を据えて取り組みたい意向。
- これまで手を付けられていなかったと述べる。
- まずは着手するという意思表明で締めている。
- 関連リンクとして GEPA 論文のスクラップが添付。
- そのリンクはリフレクティブ・プロンプト進化の性能主張を示す。
- 記事自体は着手宣言と参照提示が中心。

### Key Findings
- DSPy を含めて腰を据えて取り組みたいという意向が示されている。 [^]
  - Footnote: DSPy含めて腰据えてやりたいとずっと思っているのだが、
- これまで着手できていなかったと記述している。 [^]
  - Footnote: なかなか手がつけれていなかった。
- とりあえず着手する意思が明確に書かれている。 [^]
  - Footnote: とりあえずやる。
- 関連リンクとして GEPA 論文を扱うスクラップが挙げられている。 [^]
  - Footnote: [論文] GEPA: リフレクティブ・プロンプト進化は強化学習を凌駕する性能を発揮
- リンク先は同一作者のスクラップであることが示されている。 [^]
  - Footnote: kun432さんのスクラップ

### References
- https://zenn.dev/kun432/scraps/6b3df382816bdd
- https://zenn.dev/kun432/scraps/31b6e74cff8138
