# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-03-23T00:02:54Z
- Articles: 3

## Transformers are Bayesian Networks
- Date: 2026-03-17

### Executive Summary
- トランスフォーマーをベイジアンネットとして厳密に定式化する論文。
- シグモイド型トランスは因子グラフ上の重み付きルーピーBPを実装すると証明。
- 任意の知識ベース上で厳密なBPを構成できると主張。
- 正確な事後確率にはBP重みが必須という一意性を示す。
- アテンション=AND、FFN=ORでPearlのGather/Updateに対応づける。
- 形式的結果を実験で検証し、ルーピーBPの実用性も示唆。
- 概念空間の有限性が検証可能推論に必須で、幻覚は構造的帰結と論じる。

### Key Findings
- トランスフォーマーはベイジアンネットであるという中心主張を提示。 [^]
  - Footnote: 概要で「a transformer is a Bayesian network」と明記している。
- シグモイド型トランスは任意の重みで重み付きルーピーBPを実装する。 [^]
  - Footnote: 概要で「every sigmoid transformer ... implements weighted loopy belief propagation」と説明。
- 宣言された知識ベース上で厳密BPを実装でき、循環がなければ正しい確率推定が可能。 [^]
  - Footnote: 「exact belief propagation on any declared knowledge base」「without circular dependencies...provably correct」などの記述。
- 正確な事後確率を出すにはBP重みが必要で、他経路はないと主張。 [^]
  - Footnote: 「uniqueness」「no other path ... to exact posteriors」とある。
- アテンション=AND、FFN=OR、層の交互はPearlのGather/Updateに対応。 [^]
  - Footnote: 「attention is AND, the FFN is OR...Pearl's gather/update algorithm」と記載。
- 検証可能推論には有限の概念空間が必要で、幻覚は構造的に避けられないと論じる。 [^]
  - Footnote: 「verifiable inference requires a finite concept space」「Hallucination is...structural consequence」と記載。

### References
- https://arxiv.org/abs/2603.17063

## Summary - Rust Project Perspectives on AI

### Executive Summary
- RustコミュニティのAIに関する多様な意見をまとめた要約文書。
- 2月6日から意見収集を開始し、2月27日ごろに要約が作成された。
- これは公式見解ではなく、個々の参加者の見解に限定されると明記。
- AIは適切な設計と環境整備が必要な道具だという見方が示される。
- 非コーディング作業や探索・調査で価値があるという声が複数ある。
- AI生成の低品質貢献がレビュー負荷を高める懸念が共通認識。
- 支持と拒否、個人の選択とプロジェクト姿勢の間に緊張があると整理。

### Key Findings
- 2月6日開始の意見収集を2月27日ごろに要約したと記されている。 [^]
  - Footnote: 冒頭で「Starting on Feb 6... authored ... on Feb 27 or so」と説明。
- 文書はRustプロジェクトの公式見解ではないと明確に注意喚起している。 [^]
  - Footnote: 「do not represent 'the Rust project's view'」などの注意書きがある。
- AIをうまく使うには問題構造化や文脈設計などの工学的配慮が必要とする。 [^]
  - Footnote: 「careful engineering」「structure the problem...context and guidance」と記述。
- 調査・探索やドキュメント検索のような非コーディング用途で有用とされる。 [^]
  - Footnote: 「research-y things」「searching our 10,000+ page architecture documentation」などの引用がある。
- AI生成の低品質PRがレビュー負荷を増やす点は賛否両派で共通認識。 [^]
  - Footnote: 「Maintainers are overburdened」「low-quality, AI-generated contributions」などの箇所。
- AIの支持と拒否の間に妥協が難しい倫理的緊張があると整理している。 [^]
  - Footnote: 「deep integration vs rejection on moral grounds」「no room for compromise」等の記述。

### References
- https://nikomatsakis.github.io/rust-project-perspectives-on-ai/feb27-summary.html

## Learnings from training a font recognition model from scratch
- Date: 2026-03-16

### Executive Summary
- フォント認識モデルをゼロから構築した技術的学びを共有する記事。
- 既存ツールは商用フォント依存と手動選択が課題と指摘。
- 入力画像から最も近いGoogle Fontを返すモデル「Lens」を構築。
- 推論は2-3秒で、太さやスタイル、画質差にも対応する。
- モデルは単一.ptではなく前処理や後処理を含むパイプラインだと強調。
- 学習データ作成や入力設計が最大の難所だったと述べる。
- CPU/GPU分離や小規模からの反復で効率化した経験を共有。

### Key Findings
- 既存のフォント認識は商用フォント依存で高価、手動の文字選択が必要という課題を挙げる。 [^]
  - Footnote: 「proprietary fonts」「letterform selection step...manual input」などの説明。
- 入力画像から最も近いGoogle Fontを返すモデル「Lens」を構築した。 [^]
  - Footnote: 「map any input image to the closest-looking Google Font...I called this model Lens」と記載。
- 推論は2-3秒で、太さ・スタイル・画質差に対応すると述べる。 [^]
  - Footnote: 「returns in 2-3 seconds」「handles a variety of font weights, styles, and image qualities」。
- モデルは前処理・OCR・切り出し・後処理を含むパイプラインであると学んだ。 [^]
  - Footnote: 「model is more than just the trained PyTorch model...downloads...OCR...mapping outputs」と説明。
- CPU処理がGPU利用率を阻害し、前処理を先に終える設計に変更した。 [^]
  - Footnote: 「GPU utilization was only around 10%...offload all the CPU work up front」と記載。
- 最初は5フォント×10画像で小さく始め、反復改善に役立ったとする。 [^]
  - Footnote: 「classify only 5 fonts...only 10 images...start small」と記述。

### References
- https://www.mixfont.com/blog/learnings-from-training-a-font-recognition-model-from-scratch
