# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-06-21T09:01:28.5406243+09:00
- Articles: 3

## UpSkill
- Date: 2026-06-20T17:20:38+00:00

### Executive Summary
- UpSkillは、スキルを継続的に進化させる軽量フレームワークとして紹介されている。
- 主眼は、Flash系の安価なモデルをプロ級の性能に近づけることにある。
- 記事は、Claude Code、Codex、CursorなどのAIエージェント利用が広がる一方で、基盤モデル性能が実務品質を制限すると説明している。
- Proモデルは高品質だが、1タスクあたりのコストが3から5倍になるため大規模運用に向きにくいとされる。
- Flashモデルは低コストだが、エラー修正にかかる時間で節約分が相殺されることがあると指摘されている。
- UpSkillは、このコストと信頼性のトレードオフを解消する試みとして位置づけられている。
- 著者は開発元HKUDSについて、過去にも興味深い小規模プロジェクトを出しており注目していると補足している。

### Key Findings
- UpSkillはスキルを継続的に改善する軽量フレームワークとして説明されている。 [^]
  - Footnote: 記事中に「スキルを継続的に進化させ続ける軽量フレームワーク」とある。
- 対象はFlashモデルの性能向上であり、安価なモデルを実用水準へ引き上げる狙いがある。 [^]
  - Footnote: 本文では「あなたのFlashモデルをプロレベルのパフォーマンスに引き上げます」と紹介されている。
- AIエージェントの性能は、支払っている基盤モデルの性能に制限されるという問題意識が示されている。 [^]
  - Footnote: Claude Code、Codex、Cursorなどを挙げたうえで「性能は、結局のところあなたが支払っているモデルの性能に限界づけられている」と述べている。
- Proモデルは高性能だが、大規模運用ではコストが課題になる。 [^]
  - Footnote: Claude Opus、GPT-5.5、Gemini Proについて「1タスクあたりのコストが3～5倍」と記載されている。
- Flashモデルは安価でも、修正工数が増えると総コストが悪化する可能性がある。 [^]
  - Footnote: Claude Haiku、GPT-5.5 mini、Gemini Flashについて「エラー修正に費やす時間がコスト削減効果を上回ることが多い」とある。

### References
- https://zenn.dev/kun432/scraps/4217f31bcb231c
- https://github.com/HKUDS/Upskill

## 「LFM2.5-Embedding-350M / LFM2.5-ColBERT-350M」を試す
- Date: 2026-06-19T14:11:39+00:00

### Executive Summary
- Liquid AIのLFM2.5-Embedding-350MとLFM2.5-ColBERT-350Mを試したスクラップである。
- 両モデルは11言語対応の多言語・クロスリンガル検索モデルとして紹介されている。
- Embeddingモデルは文書ごとに1つのベクトルを作るため、高速でインデックスが小さい。
- ColBERTモデルはトークンごとにベクトルを持ち、MaxSimによる単語レベルの照合で精度を重視する。
- どちらもLFM2.5-350M-Baseを基盤にした双方向エンコーダで、RAGパイプラインの代替候補として扱われている。
- 記事ではNanoBEIRやMKQAのスコア、llama.cppやGPUでの推論速度など、性能面の根拠が多く引用されている。
- 著者の実験では多言語・クロスリンガル検索は概ね良好だが、日本語の曖昧な飲食検索例では期待通りでない結果も見られた。

### Key Findings
- 2つのモデルは11言語の高速・高精度検索を目的に設計されている。 [^]
  - Footnote: 本文に「11言語にわたる超高速かつ高精度な検索を実現するために設計された多言語検索モデル」とある。
- Embeddingモデルは軽量・高速、ColBERTモデルは高精度という役割分担がある。 [^]
  - Footnote: 記事ではEmbeddingを「文書1件につき1つのベクトル」、ColBERTを「トークン1つにつき1つのベクトル」と説明している。
- 両モデルはLFMファミリー初の双方向モデルとして説明されている。 [^]
  - Footnote: モデルカード抜粋に「両モデルともパラメータ数は350Mで、LFMファミリー初の双方向モデル」と記載されている。
- NanoBEIR多言語拡張版ではColBERTが平均0.605、Embeddingが平均0.577を記録している。 [^]
  - Footnote: NanoBEIR Multilingual Extendedの表で、LiquidAI/LFM2.5-ColBERT-350M AVG 0.605、LFM2.5-Embedding-350M AVG 0.577と示されている。
- llama.cpp環境でも低レイテンシで動作する実測値が示されている。 [^]
  - Footnote: MacBook Pro M4 Maxの表で、Embeddingのクエリ埋め込みp50が7.3ms、ColBERTのクエリ埋め込み+MaxSim p50が8.2msとされている。

### References
- https://zenn.dev/kun432/scraps/66e1bf19755d3c
- https://liquid.ai/blog/lfm2-5-retrievers
- https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M
- https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M

## 「worktrunk」を試す
- Date: 2026-06-18T15:11:54+00:00

### Executive Summary
- Worktrunkはgitワークツリー管理のためのCLIツールとして紹介されている。
- AIエージェントを並列実行する開発スタイルを支援することが主な目的である。
- ワークツリーの作成、切り替え、削除、一覧表示をブランチ操作のように簡単にする点が強調されている。
- 通常のgit worktree操作ではブランチ名やパス指定が煩雑になりやすいが、Worktrunkはテンプレートからパスを自動計算する。
- フック、LLMによるコミットメッセージ生成、マージワークフロー、インタラクティブピッカーなど周辺機能も多い。
- PRチェックアウトやワークツリーごとの開発サーバーポート割り当てなど、並列開発向けの実務機能が含まれている。
- 著者は現在ghqとgwqに不満はないが、別の選択肢としてWorktrunkを試したいという動機を述べている。

### Key Findings
- WorktrunkはAIエージェントの並列実行を前提にしたgitワークツリー管理CLIである。 [^]
  - Footnote: 本文に「gitワークツリー管理のためのCLIツールで、AIエージェントを並列実行するように設計」とある。
- 3つの基本コマンドでワークツリー操作を簡略化できると説明されている。 [^]
  - Footnote: 記事では「Worktrunkの3つの基本コマンドを使えば、ワークツリーの操作がブランチの操作と同じくらい簡単」と述べている。
- Git標準のworktree操作は、作成時の入力が煩雑だという課題が示されている。 [^]
  - Footnote: 本文では「新しいワークツリーを作成するといった単純な作業でも、ブランチ名を3回も入力する必要」と説明している。
- Worktrunkはブランチ名からワークツリーパスを自動計算する。 [^]
  - Footnote: 記事に「ワークツリーをブランチ名で指定でき、パスは設定可能なテンプレートから自動的に計算」とある。
- 並列開発を支える機能として、フック、LLMコミットメッセージ、PRチェックアウト、固有ポート割り当てなどが挙げられている。 [^]
  - Footnote: ワークフロー自動化機能の一覧に「フック機能」「LLMによるコミットメッセージ生成」「PRチェックアウト」「hash_portテンプレートフィルター」が記載されている。

### References
- https://zenn.dev/kun432/scraps/9cc5951727014e
- https://github.com/max-sixty/worktrunk
- https://worktrunk.dev
