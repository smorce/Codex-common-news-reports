# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-19T09:01:48+09:00
- Articles: 3

## 「cognee」を試す
- Date: 2026-03-18T20:58:00

### Executive Summary
- エージェントのメモリ実装としてcogneeを初めて試すメモ。
- cogneeはオープンソースの知識エンジンで、AIエージェント向けに文脈情報を提供する。
- ベクトル検索・グラフDB・認知科学アプローチを統合し、文書の意味的検索と関係性の追跡を狙う。
- 統一されたデータ取り込みやマルチモーダル対応などのメリットが挙げられている。
- Python 3.10〜3.13が前提で、デフォルトのLLM/EmbeddingやDB構成が記載されている。
- v0.5.0以降はマルチユーザーアクセス制御がデフォルト有効で、環境変数で無効化できる。
- Quick Startのコードでは.add/.cognify/.searchなどの非同期APIを利用する。
- 著者はマルチユーザー関連の負荷感を懸念しつつ、単一ユーザー用途なら有望と評価。

### Key Findings
- cogneeはAIエージェント向けのオープンソース知識エンジンとして位置づけられている。 [^]
  - Footnote: 「cogneeはオープンソースの知識エンジンで、あらゆる形式・構造のデータを取り込み、継続的に学習することで、AIエージェントに最適な文脈情報を提供します。」
- ベクトル検索・グラフDB・認知科学アプローチを統合し、文書の関係性と進化を追跡する設計。 [^]
  - Footnote: 「ベクトル検索、グラフデータベース、認知科学のアプローチを統合することで、文書を意味的に検索可能にするとともに、関係性によって文書間を接続し、内容が変化・進化する過程も追跡できるようにします。」
- 前提のPythonバージョンは3.10〜3.13。 [^]
  - Footnote: 「Python 3.10～3.13」
- デフォルトのLLM/EmbeddingはOpenAI系で、gpt-4o-miniとtext-embedding-3-smallが使われる。 [^]
  - Footnote: 「OpenAIが標準。デフォルトだと、LLMは gpt-4o-mini、Embedding は text-embedding-3-small が使用される」
- 標準DB構成はSQLite・LanceDB・Kuzuの組み合わせ。 [^]
  - Footnote: 「標準では、リレーショナルDB: SQLite・ベクトルDB: LanceDB・グラフDB: Kuzu が使用される」
- v0.5.0以降はマルチユーザーアクセス制御が既定で有効。 [^]
  - Footnote: 「From version 0.5.0 onwards, Cognee will run with multi-user access control mode set to on by default.」
- 非同期APIが基本で、.add/.cognify/.searchの利用が示されている。 [^]
  - Footnote: 「Cogneeでは非同期処理を多用しています。」および「.add」「.cognify」「.search」
- 著者はマルチユーザー対応の学習コストやオーバーヘッドを懸念している。 [^]
  - Footnote: 「オーバーヘッドや学習コストが大きそうに感じてしまったので、ちょっとペンディング・・・」

### References
- https://zenn.dev/kun432/scraps/6ffeabaf8aa7c4
- https://github.com/topoteretes/cognee
- https://docs.cognee.ai/getting-started/installation#environment-configuration

## 「LLaDA2.1-mini」を試す
- Date: 2026-03-17T15:18:00

### Executive Summary
- ZenMuxでLLaDA2.1-flash(100B拡散LLM)が出たという情報から開始。
- 誤り訂正可能な編集や速度/品質モード、100B向け強化学習などが列挙されている。
- 著者は100Bを動かせず、ZenMuxは有償っぽいと判断している。
- 代替として16BのLLaDA2.1-miniがHugging Faceで公開されている点に注目。
- 日本語で試したところ、速度が伸びず出力が崩れる例が見られた。
- 品質優先の推奨パラメータに変えても不自然な日本語が残った。
- 開発者のX返信では日本語コーパス不足とEOS未出力が原因だと説明されている。
- それでも拡散言語モデルへの期待は継続という結論。

### Key Findings
- LLaDA2.1-flashは100B拡散LLMで、編集可能生成や速度/品質モードを掲げている。 [^]
  - Footnote: 「スケール100Bの拡散型LLMが @TheInclusionAI から登場」「誤り訂正可能な編集可能な生成」「スピードモード：超高速推論」「品質重視モード：競合製品に匹敵する性能」
- 892トークン/秒で利用可能とされ、API/チャットで試せる旨が記載されている。 [^]
  - Footnote: 「⚡️ 892 トークン/秒 — 私たちの 100B 拡散 LLM、LLaDA2.1-flash が @ZenMuxAI で今すぐ利用可能になりました！」
- 著者は100Bを動かせず、ZenMuxは有償利用が前提と推測している。 [^]
  - Footnote: 「流石にこのサイズは動かせないのと、ZenMuxのプラットフォームでもどうやら有償でないと使えない様子。」
- 16Bの小型モデルLLaDA2.1-miniの公開が示されている。 [^]
  - Footnote: 「が、16Bの小型モデルもリリースされているみたい。」
- 日本語だと英語より遅く、出力が崩れる傾向があると述べている。 [^]
  - Footnote: 「英語に比べるとあまり速くない」「出力が少しおかしくなる」
- 品質優先パラメータで改善を試みたが、日本語の崩れが残った。 [^]
  - Footnote: 「threshold 0.7」「editing_threshold 0.5」および「今度は別の箇所『算算の順序（（優））』がおかしくなっている。」
- 開発者は日本語コーパス不足とEOS未出力が原因と説明している。 [^]
  - Footnote: 「we sincerely lack the japanese training corpora in training, and that maybe the cause.」「the model failed to output the proper <eos> token during decoding.」
- それでも拡散言語モデルへの期待は継続と締めている。 [^]
  - Footnote: 「それでも拡散言語モデルには引き続き期待したいところ。」

### References
- https://zenn.dev/kun432/scraps/94f7ed181d6683
- https://zenmux.ai/inclusionai/llada2.1-flash
- https://huggingface.co/inclusionAI/LLaDA2.1-mini

## 「InternVL-U」を試す
- Date: 2026-03-14T00:55:00

### Executive Summary
- InternVL-Uは4Bの統一マルチモーダルモデルとして紹介される。
- 推論・生成・編集を単一フレームワークに統合する点が強調されている。
- 統一コンテキスト、モダリティ別モジュール、デカップル視覚表現で性能効率を狙う。
- GitHub/Hugging Face/技術レポートなどの主要リソースが列挙されている。
- Diaによる要約では「見る・考える・描く・直す」を一体化した設計と説明。
- InternVLUPipelineでgeneration_modeを切り替えて理解・生成・編集を実行できる。
- Reasoning付き生成は時間が伸び、出力がループする例もある。
- VRAM消費や4Bサイズの限界、日本語用途の懸念が述べられている。

### Key Findings
- InternVL-Uは軽量な4B統一マルチモーダルモデルとして提示されている。 [^]
  - Footnote: 「軽量な4B統一マルチモーダルモデル」
- 推論・生成・編集を統一フレームワークに統合することが明示されている。 [^]
  - Footnote: 「推論、生成、編集を統一フレームワークに統合します。」
- 統一コンテキストやモダリティ別設計、デカップル視覚表現に基づくと説明。 [^]
  - Footnote: 「統一コンテキストモデリング、モダリティ固有のモジュール設計、デカップルされた視覚表現」
- GitHubの説明では4Bパラメータの統一マルチモーダルモデルとされる。 [^]
  - Footnote: 「InternVL-U is a 4B-parameter unified multimodal model (UMM) that brings multimodal understanding, reasoning, image generation, image editing into a single framework.」
- Dia要約で「見る・考える・描く・直す」を一体化したオールインワン設計と説明されている。 [^]
  - Footnote: 「4Bパラメータなのに『見る・考える・描く・直す』を全部まとめてできる統一マルチモーダルモデル（UMM）」
- InternVLUPipelineでgeneration_modeを切り替えて各種タスクを実行する設計。 [^]
  - Footnote: 「generation_mode="text"」「generation_mode="image"」「generation_mode="text_image"」
- Reasoning付き生成は時間が長くなると述べられている。 [^]
  - Footnote: 「Reasoningが行われる分、ちょっと生成時間は長くなるみたい。」
- Reasoningの出力がループした例が示されている。 [^]
  - Footnote: 「ただ途中で出力がループしちゃったみたい。」
- 実験中にVRAM消費が増大したという指摘がある。 [^]
  - Footnote: 「ちなみに一通り試してたらVRAM消費がだいぶ膨れてた。」
- 4Bサイズで日本語用途に十分か懸念がある。 [^]
  - Footnote: 「日本語で普通に使いたいと思うと、4Bでも足りない気がする」

### References
- https://zenn.dev/kun432/scraps/89e873b7670fb2
- https://github.com/OpenGVLab/InternVL-U
- https://huggingface.co/InternVL-U/InternVL-U
- https://arxiv.org/pdf/2603.09877
