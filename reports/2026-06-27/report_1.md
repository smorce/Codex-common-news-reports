# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-06-27T09:00:42+09:00
- Articles: 3

## 「DiffusionGemma」を試す
- Date: 2026-06-26T10:01:27+00:00

### Executive Summary
- Google の DiffusionGemma を試すスクラップで、拡散型テキスト生成モデルの概要と特徴を整理している。
- DiffusionGemma は 1 トークンずつ生成する従来方式ではなく、256 トークン単位のブロックを反復的に整える方式を採る。
- 高速生成を重視した実験的モデルで、H100 や RTX 5090 で高い tokens/sec が示されている。
- 26B MoE モデルだが推論時に有効化されるパラメータは 3.8B とされ、量子化によりローカル GPU での利用も視野に入る。
- 双方向アテンションにより、コード補完、インライン編集、構造整合性が重要なタスクに強みがあると説明されている。
- 一方で生成品質は通常の Gemma 4 より劣るため、高品質な本番用途では従来の自己回帰モデルが推奨される。
- モデルカードの抜粋では、マルチモーダル入力、256K コンテキスト、関数呼び出し、多言語対応など幅広い機能も紹介されている。

### Key Findings
- DiffusionGemma は高速生成を目的とした実験的なオープンソースモデルとして紹介されている。 [^]
  - Footnote: 記事では「Apache 2.0ライセンスの下でリリースされた、テキスト生成の高速アプローチを探求する実験的なオープンソースモデル」と説明している。
- 生成方式は 256 トークンを並列に扱い、拡散モデルのように反復的に洗練する設計である。 [^]
  - Footnote: 記事本文に「1トークンずつじゃなくて 256トークンまとめて同時生成」「何ステップかかけてだんだん綺麗にする」とある。
- 速度面では標準アクセラレータ上で最大 4 倍、H100 で 1000 tokens/sec 超、RTX 5090 で 700 tokens/sec 超が示されている。 [^]
  - Footnote: 記事は「最大4倍の速度向上」「単一のNVIDIA H100で1秒あたり1000トークン以上、NVIDIA GeForce RTX 5090で1秒あたり700トークン以上」と引用している。
- モデルは 26B MoE だが、推論時に実際に動くのは 3.8B パラメータのみとされる。 [^]
  - Footnote: 記事に「26BのMixture of Experts (MoE)モデル」「推論時に3.8Bパラメータのみを活性化」と記載がある。
- 双方向アテンションにより、前後関係を同時に参照する編集・補完・構造的タスクとの相性が強調されている。 [^]
  - Footnote: 記事では「各トークンが『前後全部のトークン』を見ながら更新できる」と説明し、コードのインフィルや Markdown の整合性を例示している。
- 品質面では通常の Gemma 4 に及ばないため、最高品質が必要な本番用途には注意が必要である。 [^]
  - Footnote: 記事末尾に「生成品質は通常のGemma 4に及ばない」とあり、「プロダクションで最高品質が絶対条件なら、ふつうのオートレグレッシブ Gemma 4 推奨」と整理されている。
- モデルカード抜粋では最大 256,000 トークンの文脈長、キャンバス長 256、総 128 エキスパート中 8 個有効などの仕様が示されている。 [^]
  - Footnote: 記事の表に「文脈長 最大256,000トークン」「キャンバス長 256」「エキスパート数 有効8個 / 総128個」とある。

### References
- https://zenn.dev/kun432/scraps/7a93b4c3c076bf
- https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/
- https://huggingface.co/google/diffusiongemma-26B-A4B-it

## Herdr
- Date: 2026-06-26T09:13:24+00:00

### Executive Summary
- Herdr というコーディングエージェント向けターミナルツールを紹介するスクラップである。
- 筆者は Zed のエージェント評判を調べている過程で Herdr を見つけたとしている。
- 引用された X の投稿では、Zed のエージェント体験に不満があり、Herdr は実用的に動くという評価が示されている。
- Herdr は tmux のように複数セッションを保持し、コーディングエージェントを 1 つのターミナルで管理する発想のツールである。
- 公式説明では、エージェント多重化とターミナル内動作が中核機能として掲げられている。
- ブロック中、作業中、完了といった状態を一目で確認でき、SSH 接続可能な環境で動作する点が強調されている。
- cmux との比較では、GUI 以外の面で Herdr のほうがエージェント対応、SSH、速度、バグの少なさで優位とする感想が紹介されている。

### Key Findings
- Herdr はコーディングエージェントを 1 つのターミナルで管理するツールとして説明されている。 [^]
  - Footnote: 記事内の公式サイト抜粋に「1つのターミナルで全エージェントを管理」とある。
- ツールの位置づけは、エージェント向けの tmux 的マルチプレクサである。 [^]
  - Footnote: 公式説明として「Herdr はコーディングエージェントにとって tmux がターミナルにもたらすものと同様の機能を提供します」と記載されている。
- SSH 接続可能なマシンやサーバー上で動作することが特徴として挙げられている。 [^]
  - Footnote: 記事では「お使いのマシンやサーバーなど、SSH接続可能なあらゆる場所――で動作するマルチプレクサ」と説明している。
- 作業状態を可視化し、ノートパソコンを閉じても状態を失わないことが訴求されている。 [^]
  - Footnote: 公式説明に「ブロック中、作業中、および完了状況を一目で確認可能」「ノートパソコンを閉じたりしても、何も失われることはありません」とある。
- cmux から Herdr に切り替えたユーザー評価では、GUI 以外の利点が Herdr 側にあるとされている。 [^]
  - Footnote: 引用投稿は「cmuxの唯一の利点はGUIがあることだった」としたうえで、Herdr の利点を列挙している。
- Herdr の利点として、より完全なエージェントサポート、セッション保持、SSH、少ないバグ、高速性、フォークしやすさが挙げられている。 [^]
  - Footnote: 記事本文には「より完全なエージェントサポート」「tmuxみたいにすべてのセッションを保持」「ssh経由でめっちゃうまく動く」「バグが少ない」「cmuxよりずっと速い」「ビルドが1分未満」とある。

### References
- https://zenn.dev/kun432/scraps/d35cb38f16de12

## 「Unlimited-OCR」を試す
- Date: 2026-06-26T06:18:49+00:00

### Executive Summary
- Baidu の Unlimited-OCR を Colaboratory L4 で試すスクラップである。
- Unlimited-OCR は長文書を一度に読むことを目的にした OCR モデルとして紹介されている。
- 総 3B パラメータ、アクティブ 500M の構成で、OmniDocBench v1.5 と v1.6 の SOTA 結果が示されている。
- 中核技術として Reference Sliding Window Attention が挙げられ、長文書でも一定の KV Cache サイズと低いアテンションコストを保つと説明されている。
- 筆者は Colaboratory の既定 transformers 5.0.0 では動かないため、4 系へのダウングレードと addict、pymupdf の追加が必要と記録している。
- モデルロード時点で VRAM 消費は約 6.7GB とされ、単一画像、複数画像、PDF から画像化した複数ページ OCR の試行が行われている。
- 神戸市の観光動向調査 PDF を例に、単一ページ OCR と複数ページ OCR、さらに 21 ページ相当の PDF OCR 実行結果が確認されている。

### Key Findings
- Unlimited-OCR は長文書を一度に読むために構築されたオープンソース OCR モデルとして紹介されている。 [^]
  - Footnote: 記事冒頭に「Unlimited OCRをオープンソース化します — 長文書を一度に読むために構築されたもの」とある。
- モデル規模は総 3B、アクティブ 500M とされ、OmniDocBench v1.5/v1.6 で SOTA を達成したとされる。 [^]
  - Footnote: 記事では「総パラメータ3B、アクティブ化されたものはわずか500M」「OmniDocBench v1.5およびv1.6で新たなエンドツーエンドのSOTA結果」と記載している。
- Reference Sliding Window Attention により、40 ページ以上の書き写しを単一フォワードパスで扱えることが主張されている。 [^]
  - Footnote: 記事に「Reference Sliding Window Attention (R-SWA)」と「単一のフォワードパスで40ページ以上の書き写しが可能」とある。
- Colaboratory では transformers 5 系が不適合で、4 系への調整が必要だった。 [^]
  - Footnote: 筆者は「transformers は5系だと動かない。Colaboratoryデフォルトは 5.0.0 なのでダウングレードが必要」と記録している。
- 追加依存として addict と pymupdf が必要で、筆者は pip で追加している。 [^]
  - Footnote: 記事では「addict と pymupdf はインストールされていないので追加が必要」とし、`pip install addict pymupdf` を実行している。
- Colab L4 でモデルとトークナイザーをロードした時点の VRAM 消費は約 6.7GB と報告されている。 [^]
  - Footnote: 記事本文に「この時点でのVRAM消費は6.7GB程度」とあり、NVIDIA-SMI の 6684MiB 表示が掲載されている。
- PDF は PyMuPDF でページ画像に変換し、`infer_multi` に画像パス配列を渡すことで複数ページ OCR として扱っている。 [^]
  - Footnote: 記事では「PDFなどは、PyMuPDFで複数画像に変換すればよい」「複数画像の場合はパスの配列で渡す」と説明している。
- 21 ページの PDF 全体 OCR は約 17 分かかり、画像切り出しを含む出力が生成された。 [^]
  - Footnote: 記事に「延々とOCRし続けて、17分程かかって完了」「画像が含まれているページの画像も切り出されている」とある。

### References
- https://zenn.dev/kun432/scraps/433dbcc79fad36
- https://github.com/baidu/Unlimited-OCR
- https://huggingface.co/baidu/Unlimited-OCR
