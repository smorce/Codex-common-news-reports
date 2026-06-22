# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-06-22T09:01:22+09:00
- Articles: 3

## 「UpSkill」を試す
- Date: 2026-06-21T17:40:15+00:00

### Executive Summary
- UpSkillは、軽量モデルを継続的なスキル改善で高性能化するフレームワークとして紹介されている。
- 背景には、Proモデルの高コストとFlashモデルの信頼性不足という実運用上の課題がある。
- Claude Code向けには単一コマンドで利用できる形が示されている。
- Terminal-Bench 2.0の未学習テストでは、Flashモデル+UpSkillがProモデルを上回ったとされる。
- コスト面では、タスクあたりProモデルより低い費用で性能改善を狙う設計になっている。
- 仕組みはセッションフック、失敗記録、Proモデルによる分析、Flashモデルでの検証を組み合わせる。
- Ralphループにより、弱いモデルが実際に従えるスキルだけを残す点が強調されている。
- 保存されたスキルはCLAUDE.mdの索引やSKILL.mdのオンデマンド読込で将来セッションへ配信される。

### Key Findings
- UpSkillはFlashモデルをProモデル級に近づける軽量フレームワークとして位置づけられている。 [^]
  - Footnote: 記事では「スキルを継続的に進化させ続ける軽量フレームワーク」「FlashモデルをProモデル並みの性能に引き上げる」と説明している。
- Proモデルの高コストが導入背景の主要課題になっている。 [^]
  - Footnote: Claude Opus、GPT-5.5、Gemini Proなどは「1タスクあたりのコストが3～5倍」とされ、大規模運用では持続困難と説明されている。
- Flashモデルは安価だが、修正工数により節約効果が失われる可能性がある。 [^]
  - Footnote: Claude Haiku、GPT-5.5 mini、Gemini Flashなどについて「エラー修正に費やす時間がコスト削減効果を上回ることが多い」と記載されている。
- Terminal-Bench 2.0で、Flash+UpSkillは未学習テストの合格率51.6%を示した。 [^]
  - Footnote: 表ではFlashモデル45.3%、Proモデル50.0%、Flashモデル+Upskill51.6%のテスト合格率が示されている。
- コスト面ではFlash+UpSkillがProモデルより安いとされる。 [^]
  - Footnote: タスクあたりコストはFlash+Upskillが$0.04、Proモデルが$0.06で、「41%低いコストで上回る性能」と説明されている。
- 改善効果が大きかった領域としてモデルトレーニング、データサイエンス、システム管理、ソフトウェアエンジニアリングが挙げられている。 [^]
  - Footnote: 記事では「モデルトレーニング（+33%）、データサイエンス（+17%）、システム管理（+17%）、ソフトウェアエンジニアリング（+11%）」と列挙している。
- UpSkillは既存インフラ変更なしにセッションフックとして統合される。 [^]
  - Footnote: 「エージェントのハーネスに軽量なセッションフックとして統合」「インフラストラクチャの変更は不要」と説明されている。
- Ralphループは、Proモデルの助言をFlashモデルで検証し、失敗時に改善を繰り返す。 [^]
  - Footnote: 第1ラウンドでFlashモデルが失敗し、Proモデルがスキルを生成、第2ラウンドでFlashモデルが再試行し、失敗が続く場合は改良すると説明されている。

### References
- https://zenn.dev/kun432/scraps/4217f31bcb231c
- https://github.com/HKUDS/Upskill

## 「LFM2.5-Embedding-350M / LFM2.5-ColBERT-350M」を試す
- Date: 2026-06-20T05:50:07+00:00

### Executive Summary
- Liquid AIのLFM2.5系検索モデル2種を紹介し、用途と性能を整理している。
- Embeddingモデルは文書ごとに1ベクトルを作る高速・軽量な検索向けモデルとして説明されている。
- ColBERTモデルはトークンごとのベクトルとMaxSimにより、精度重視の検索に向くとされる。
- どちらも350M規模で、LFMファミリー初の双方向エンコーダを備える点が特徴になっている。
- 対応言語は日本語を含む11言語で、多言語・クロスリンガル検索を狙っている。
- NanoBEIRやMKQA-11の表では、LFM2.5-ColBERTとEmbeddingが上位の性能として示されている。
- llama.cpp/GGUFやGPU内部スタックで低レイテンシを実現する点も強調されている。
- 筆者は旧LFM2ベースのColBERTからの性能向上とDense Embedding追加に期待しつつ、独自ライセンスに注意している。

### Key Findings
- LFM2.5の2モデルは11言語対応の多言語検索モデルとして紹介されている。 [^]
  - Footnote: 記事では「11言語にわたる超高速かつ高精度な検索」「多言語・クロスリンガル検索特化モデル」と説明している。
- Embeddingモデルはインデックスサイズと速度を重視する設計である。 [^]
  - Footnote: 「文書1件につき1つのベクトルを生成」「最も高速な検索が可能で、インデックスサイズも最小」と記載されている。
- ColBERTモデルは精度を重視し、トークン単位のベクトルを使う。 [^]
  - Footnote: 「トークン1つにつき1つのベクトルを生成」「単語レベルでのクエリマッチングが可能」と説明されている。
- 両モデルはLFM2.5-350M-Baseを基盤にした双方向モデルである。 [^]
  - Footnote: 記事では「LFM2.5-350M-Baseアーキテクチャを基盤」「LFMファミリーで初めて双方向処理に対応したエンコーダ」と述べている。
- 短文脈の製品カタログ、FAQ、ナレッジベース、サポート文書に適している。 [^]
  - Footnote: 「製品カタログ、FAQ、ナレッジベース、サポートドキュメント、および多言語検索用途」に適すると書かれている。
- NanoBEIR多言語拡張版ではLFM2.5-ColBERTが平均0.605、Embeddingが平均0.577を示した。 [^]
  - Footnote: 性能表のNanoBEIR Multilingual Extended NDCG@10で、LFM2.5-ColBERT-350M AVG 0.605、LFM2.5-Embedding-350M AVG 0.577と記載されている。
- MKQA-11では両モデルが平均Recall@20で0.69前後を示している。 [^]
  - Footnote: MKQA-11 Recall@20の表では、ColBERTがAVG 0.694、EmbeddingがAVG 0.691と示されている。
- MacBook M4 Maxのllama.cppでは、クエリ埋め込みが一桁ミリ秒台で測定されている。 [^]
  - Footnote: 推論速度表ではEmbeddingのp50が7.3ms、ColBERTのクエリ埋め込みp50が8.1msと記載されている。
- 筆者はLiquid AIモデルの独自ライセンスに注意を促している。 [^]
  - Footnote: 記事中で「Liquid AIのモデルは全て独自ライセンスなので、その点だけ注意」と述べている。

### References
- https://zenn.dev/kun432/scraps/66e1bf19755d3c
- https://liquid.ai/blog/lfm2-5-retrievers
- https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M
- https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M

## 「worktrunk」を試す
- Date: 2026-06-18T15:16:25+00:00

### Executive Summary
- Worktrunkはgit worktreeを扱いやすくするCLIツールとして紹介されている。
- AIエージェントを複数並列で走らせる開発ワークフローを主な想定としている。
- 基本コマンドにより、作成、切替、削除、一覧表示をブランチ操作に近い感覚で扱える。
- 通常のgit worktreeではパスやブランチ名入力が煩雑で、その課題をテンプレートで緩和する。
- フック、マージ、LLMコミットメッセージ生成、インタラクティブピッカーなどの機能が挙げられている。
- ビルドキャッシュ共有やワークツリーごとのポート割当など、複数作業環境の運用支援も含まれる。
- 筆者は既存のghq+gwqに不満はないが、代替選択肢として試したいという動機を述べている。
- ライセンスはMITとして紹介されている。

### Key Findings
- Worktrunkはgitワークツリー管理用CLIであり、AIエージェントの並列実行を意識している。 [^]
  - Footnote: 記事では「gitワークツリー管理のためのCLIツール」「AIエージェントを並列実行するように設計」と説明されている。
- 3つの基本コマンドでワークツリー操作を簡単にすることを狙っている。 [^]
  - Footnote: 「Worktrunkの3つの基本コマンドを使えば、ワークツリーの操作がブランチの操作と同じくらい簡単」と記載されている。
- git worktreeの素のUIは、作成や移動で入力が多いことが課題として挙げられている。 [^]
  - Footnote: 新しいワークツリー作成では「ブランチ名を3回も入力する必要」があり、`git worktree add -b feat ../repo.feat`後に移動も必要と説明されている。
- Worktrunkはブランチ名からワークツリーパスを自動計算する。 [^]
  - Footnote: 「ワークツリーをブランチ名で指定でき、パスは設定可能なテンプレートから自動的に計算」と書かれている。
- CLI例では、`wt switch -c -x claude feat`で作成とClaude起動をまとめて実行できる。 [^]
  - Footnote: 比較表で、Worktrunkの作成・Claude起動コマンドとして`wt switch -c -x claude feat`が示されている。
- フックで作成時、マージ前、マージ後などに任意コマンドを実行できる。 [^]
  - Footnote: ワークフロー自動化機能として「フック機能 — ワークツリー作成時、マージ前、マージ後などに任意のコマンドを実行可能」とある。
- 複数並行変更を扱うため、LLMコミットメッセージ生成やマージワークフローも提供される。 [^]
  - Footnote: 機能一覧に「LLMによるコミットメッセージ生成」「スクワッシュマージ、リベース、通常マージ、クリーンアップ作業を1つのコマンドで実行可能」とある。
- ワークツリーごとの開発サーバーポート割当にも対応する。 [^]
  - Footnote: 「hash_portテンプレートフィルターにより、各ワークツリーに固有のポート番号を割り当て可能」と説明されている。
- 筆者は既存環境に不満はないが、別選択肢としてWorktrunkを試す意図を述べている。 [^]
  - Footnote: 筆者は「現在 ghq + gwq を使っていて」「特に不満があるわけではない」「他のチョイスも試してみたい」と記載している。

### References
- https://zenn.dev/kun432/scraps/9cc5951727014e
- https://github.com/max-sixty/worktrunk
