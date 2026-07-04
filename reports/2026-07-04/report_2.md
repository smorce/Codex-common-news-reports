# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-07-04T09:03:59.9071214+09:00
- Articles: 3

## Open Source AI Gap Map
- Date: 2026-07-03T22:04:00+00:00

### Executive Summary
- Current AI がオープンソース AI の現状を整理する Gap Map v0.1 を公開した。
- 同団体は AI の公共オプションを目指す非営利として、2025年2月のパリ AI Action Summit で設立された。
- すでに 4 億ドルの資金コミットメントを得ている点が、取り組みの規模を示している。
- Gap Map v0.1 は 421 製品を詳細化し、未分類の長い裾野として 24,400 件の成果物も扱う。
- 対象はソフトウェア、モデル、データセット、ハードウェアにまたがり、14 カテゴリと 3 層のスタックに整理される。
- Simon Willison は地図そのものより、MIT ライセンスで公開された基盤データに注目している。
- GitHub 上の YAML、ノートブック、スキーマ、スクリプトにより、第三者がデータを再利用・分析できる。

### Key Findings
- Gap Map はオープンソース AI エコシステムの索引化を目的としている。 [^]
  - Footnote: 記事では Gap Map を「indexing the current state of open source AI」と説明している。
- Current AI は公共性を掲げた AI 基盤づくりを進めている。 [^]
  - Footnote: 本文に「a global partnership building a public option for AI」とある。
- v0.1 では 421 製品が詳細化されている。 [^]
  - Footnote: 記事は「The Gap Map v0.1 details 421 products in depth」と記載している。
- 内訳は 266 のツール・ライブラリ、85 モデル、50 データセット、20 ハードウェアである。 [^]
  - Footnote: 本文に「266 software tools and libraries, 85 models, 50 datasets, and 20 hardware projects」とある。
- 未分類の成果物も 24,400 件あり、今後の調査対象として残されている。 [^]
  - Footnote: 記事は「The remaining 24,400 artifacts constitute the uncategorized long tail」と述べている。
- 基盤データは MIT ライセンスで公開され、再利用しやすい。 [^]
  - Footnote: 本文では「released under an MIT license」とし、GitHub アカウント currentai-org/os-ai-map に言及している。

### References
- https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/

## Leanstral 1.5: Proof Abundance for All
- Date: 2026-07-02T00:00:00+00:00

### Executive Summary
- Mistral AI は Lean 4 向けの形式検証モデル Leanstral 1.5 を公開した。
- モデルは Apache-2.0 ライセンスで無償提供され、総パラメータ 119B、アクティブ 6B と説明されている。
- miniF2F を完全に飽和し、PutnamBench では 672 問中 587 問を解いた。
- FATE-H で 87%、FATE-X で 34% の state-of-the-art 結果を主張している。
- 訓練は中間学習、教師あり微調整、CISPO による強化学習の 3 段階で構成される。
- コード検証では 57 リポジトリを対象に、未知のバグ 5 件を含む実バグを発見した。
- Hugging Face と無料 API エンドポイントで利用でき、Mistral Vibe での利用が推奨されている。

### Key Findings
- Leanstral 1.5 は形式検証と Lean 4 の実用的な証明工学を主対象にしている。 [^]
  - Footnote: 本文は「practical proof engineering in Lean 4」として利用目的を説明している。
- モデルは 119B 総パラメータ、6B アクティブパラメータという構成である。 [^]
  - Footnote: 記事に「119B total and only 6B active parameters」と記載されている。
- miniF2F では検証セットとテストセットの双方で 100% に到達した。 [^]
  - Footnote: 本文は「reaching 100% on both the validation and test sets」と述べている。
- PutnamBench では最大 4M トークン予算で 587 問を解いた。 [^]
  - Footnote: 記事は「587 at 4M」と、トークン予算拡大に伴う解答数を示している。
- FLTEval では pass@1 と pass@8 を改善し、コスト面でも優位性を示した。 [^]
  - Footnote: 本文に「pass@1 ... from 21.9 to 28.9 and pass@8 from 31.9 to 43.2」とある。
- 実コード検証では violated properties を 47 件検出し、11 件が真正のバグにつながった。 [^]
  - Footnote: 記事は「flagged 47 violated properties, with 11 pointing to genuine bugs」と報告している。
- datrs/varinteger の zigzag decoding では U64.MAX 入力時のオーバーフロー問題を検出した。 [^]
  - Footnote: 本文は「On input Std.U64.MAX, the expression (value + 1) overflowed」と説明している。

### References
- https://mistral.ai/news/leanstral-1-5/

## Dispersion loss (LM-Dispersion)

### Executive Summary
- ICML 2026 採択の LM-Dispersion は、小型言語モデルの埋め込み凝縮に注目する研究である。
- 埋め込み凝縮とは、Transformer 層を進むにつれてトークンベクトルが狭い円錐状の方向へ寄る現象を指す。
- この現象は同一モデルファミリー内で小型モデルほど深刻で、大型モデルほど起きにくいと報告されている。
- 制御実験でも、MLP 次元だけを変えた GPT2 風モデルで同じ傾向が再現された。
- 凝縮は初期化直後から観測され、事前学習では悪化ではなく緩和されると説明されている。
- 著者らは dispersion loss を導入し、埋め込みを単位超球面上で分散させる正則化として使う。
- 効果は探索的で控えめとされ、大規模予算投入前に小規模な通常手順で検証することが推奨されている。

### Key Findings
- 埋め込み凝縮は、トークン埋め込みが高次元空間で互いに似た方向へ寄る幾何現象である。 [^]
  - Footnote: 本文は「confined to a narrow cone」とし、pairwise cosine similarity で測ると説明している。
- 小型モデルでは大型モデルより凝縮が強い。 [^]
  - Footnote: ページは特徴 1 として「More severe in smaller models than in larger counterparts」と記載している。
- データセットを変えても凝縮効果は一貫して観測された。 [^]
  - Footnote: 本文に「consistent regardless of the input text dataset」とあり、wikitext、pubmed_qa、imdb、squad が挙げられている。
- モデルサイズ以外の交絡を抑えた実験でも同じ傾向が再現された。 [^]
  - Footnote: 記事は MLP 次元のみを変え、層数、埋め込み次元、データセット、訓練設定を固定したと説明している。
- 知識蒸留は凝縮への抵抗性を移す解決策ではないとされる。 [^]
  - Footnote: ページは「Knowledge distillation from a larger model does not transfer the desired resistance」と述べている。
- dispersion loss は埋め込み空間の未活用を抑え、小型モデルの表現を大型モデルに近づける狙いがある。 [^]
  - Footnote: 本文は「under-utilizing the representation space」とし、dispersing embeddings で性能差を縮める仮説を示している。
- 著者は dispersion loss の改善幅を控えめで探索的と位置づけている。 [^]
  - Footnote: Disclaimers では「The gains are modest」および「Treat this part as more exploratory」と明記している。

### References
- https://chenliu-1996.github.io/projects/LM-Dispersion/
