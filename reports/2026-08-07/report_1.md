# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-08-07T09:01:36+09:00
- Articles: 3

## メモ: ByteShape

### Executive Summary
- ByteShapeは、AIモデルを軽量化・高速化するためのデータ型最適化に特化した企業として紹介されている。
- 中核技術はShapeLearnとShapeSqueezeで、前者はテンソルやブロックごとの最適ビット長を学習する。
- ShapeLearnは単純な固定ビット量子化ではなく、ハードウェアやコンテキスト長を踏まえた速度と精度のバランスを重視する。
- ShapeSqueezeはShapeLearn後の値をさらにエントロピー符号化し、メモリ転送量削減を狙うロスレス圧縮技術として説明されている。
- Qwen、Llama、Devstral、Cohere、Qwen-Imageなど複数モデル向けにGGUFやHumming形式の量子化済みモデルを提供している。
- 記事では、KLDやBPWのような単一指標だけでモデルを選ぶ危険性が強調されている。
- 実運用では、対象デバイスに載るか、タスク品質が保てるか、実際の推論速度が出るかを段階的に見るべきだとまとめている。
- 筆者は、独自ラベルが増えると比較は面倒になるが、評価マトリクスがあれば精度・速度・サイズの判断がしやすいと見ている。

### Key Findings
- ByteShapeは量子化フォーマット単体ではなく、どのデータ型をどこに割り当てるかを学習する会社として位置付けられている。 [^]
  - Footnote: 記事は「どのフォーマットを、どのテンソルに、何ビットで割り振るか」を学習して決める会社だとまとめている。
- ShapeLearnはテンソル、チャネル、グループ、ブロック単位など複数粒度でビット長を調整できる。 [^]
  - Footnote: 本文には、ShapeLearnの粒度として「テンソル単位 / チャネル単位 / グループ単位 / ブロック単位まで対応」とある。
- 量子化の目標は単なる最小サイズ化ではなく、まずデバイスとコンテキスト長に収まることを満たし、その上で品質と速度を最適化することにある。 [^]
  - Footnote: 記事では「メモリは『削れるだけ削るターゲット』じゃなくて『まず満たすべき予算』」と説明されている。
- ハードウェアごとに最適な量子化形式は異なり、3bitが常に速いとは限らない。 [^]
  - Footnote: 本文ではRTX 5090では3bitより4bitカーネルのほうが速いケースや、Pi/CPUではKQ系がIQよりよい例が挙げられている。
- ShapeSqueezeはメモリ帯域ボトルネックを緩和するために、ShapeLearn後の値をさらに圧縮する。 [^]
  - Footnote: 記事はShapeSqueezeについて「per-value entropy codingで圧縮」し「最大で 追加 40% 圧縮」と説明している。
- ByteShapeはQwen系、Devstral、Cohere North Mini Code、Qwen-Imageなどの実モデルで評価結果を提示している。 [^]
  - Footnote: 本文にはQwen3 4B、Qwen3.6 35B、Qwen3-Coder、Devstral Small 2、Cohere North Mini Code、Qwen-Image-2512などが列挙されている。
- KLDやBPWは有用な補助指標だが、本番デプロイ時の品質や速度を直接保証しない。 [^]
  - Footnote: 記事は「KLD は displacement であって direction じゃない」「BPW は storage cost であって実スピードじゃない」とまとめている。
- Qwen3.6-35B-A3Bの例では、ByteShape製GPU-5が精度・速度のバランスで良い候補として扱われている。 [^]
  - Footnote: 筆者はRTX4090の比較で「GPU-5 が最も精度・速度のバランスが良い」と述べている。

### References
- https://zenn.dev/kun432/scraps/e7c2c495c5cf16
- https://byteshape.com/
- https://byteshape.com/blogs/
- https://huggingface.co/byteshape

## 「Maple-Preview」を試す

### Executive Summary
- Maple-PreviewはDeepGroveが公開した20B-A1Bの三値重み推論LLMとして紹介されている。
- 記事では、Mac mini M4で200トークン/秒超、iPhoneでも120トークン/秒超というオンデバイス性能が強調されている。
- 重みを-1、0、1の三値で扱うことで、掛け算中心ではなく足し算や符号反転に近い計算へ寄せる発想が説明されている。
- DeepGroveは、フル精度モデルを後から圧縮するのではなく、最初から低精度前提で設計・学習する考え方を採っている。
- オンデバイス学習のデモでは、ユーザーの好みを外部メモリではなくモデル重みに反映する“Dreaming”の構想が紹介されている。
- 筆者はMLX版とllama.cpp版の導入手順を確認し、UbuntuとRTX4090環境でGGUFモデルを試している。
- CPUビルドでも普通に速いと感じつつ、CUDA有効ビルドではGPUメモリ使用が確認できたとしている。
- 日本語応答は可能だが、実例では固有名詞の誤りが見られ、日本語知識は十分ではない可能性が示唆されている。

### Key Findings
- Maple-Previewは20B-A1Bの三値重みLLMで、同クラスで高い効率を狙うモデルとして紹介されている。 [^]
  - Footnote: 冒頭で「オープンソースの 20B-A1B 三値重み推論 LLM」と説明されている。
- オンデバイス性能が主な訴求点で、Mac mini M4やiPhoneで高速に動くとされている。 [^]
  - Footnote: 本文には「Mac Mini M4 で 200+ トークン/秒」「iPhone 上でローカルに実行した場合でも、120+ トークン/秒」とある。
- 三値重みは低精度化を前提にしたアーキテクチャ設計の中核になっている。 [^]
  - Footnote: 記事は重みが「-1, 0, 1 の3パターンだけ」で、計算を軽くできると説明している。
- DeepGroveの設計思想は、後処理の圧縮ではなく、最初から低精度前提でモデルを育てることにある。 [^]
  - Footnote: 本文では「高性能モデルを後からダイエットさせる」ではなく「最初から低精度前提で学習」と対比している。
- モデルはMoE系の構成を採り、ハードウェア実測を踏まえて構成調整されている。 [^]
  - Footnote: まとめでは「256エキスパート・24層」や「Mac mini 実機で速度測りながら」調整したことが説明されている。
- Dreamingデモは、ユーザーの嗜好をコンテキスト外部メモリではなく重みに埋め込む方向性を示している。 [^]
  - Footnote: 本文には、ヴィーガン好みを学習し、翌日のバッグ推薦で合成素材を勧める例がある。
- llama.cppサポートは追加されたが、記事時点ではフォーク版を使って試す形になっている。 [^]
  - Footnote: 筆者は「llama.cpp版もどうやらフォークみたい」と述べ、deepgrove-ai/llama.cppのビルド手順を記録している。
- 日本語での簡単な会話はできる一方、作品名やキャラクター名の認識には問題がある例が出ている。 [^]
  - Footnote: 試行出力では『魔法少女まどか☆マギカ』への回答で実在しないような名前を挙げており、筆者も日本語知識は強くなさそうだとしている。

### References
- https://zenn.dev/kun432/scraps/6da529da4a42b0
- https://deepgrove.ai/maple-preview
- https://huggingface.co/deepgrove/maple-preview
- https://github.com/deepgrove-ai/mlx-lm-deepgrove

## 「anydoc」を試す

### Executive Summary
- anydocはFirecrawlが開発した、各種ドキュメントをMarkdownへ変換するRustベースの高速ライブラリとして紹介されている。
- 対応対象はWord、PowerPoint、Excel、OpenDocument、RTF、EPUB、CSV、PDFなど広範囲に及ぶ。
- README由来の説明では、Node.js、Python、ブラウザWebAssembly向けのバインディングが用意されている。
- ベンチマークでは14種類の形式すべてに対応し、中央値4.4ms、総合スコア81という結果が示されている。
- 筆者はPythonパッケージfirecrawl-anydocをUbuntu 24.04 VMに導入し、神戸市公開PDFをMarkdownへ変換して試している。
- 変換速度は非常に速い一方、PDFの表組みや見出し抽出には崩れが見られ、文書構造の品質には課題があると評価している。
- 元ファイルの見た目が整っていても、内部構造が正しくない場合は変換結果が不自然になる可能性があると推測している。
- 用途としては、大量の比較的単純な文書を高速にざっくり抽出し、その後をLLM処理に任せる場面が向いているとまとめている。

### Key Findings
- anydocは複数のオフィス文書やPDFをGitHub Flavored Markdownへ変換するライブラリである。 [^]
  - Footnote: README抜粋では「Word、PowerPoint、Excel、OpenDocument、RTF、EPUB、CSV、PDF」をMarkdownに変換すると説明されている。
- Rust実装で、機械学習モデルや外部サービスに依存しない高速処理が特徴とされる。 [^]
  - Footnote: 機能一覧には「純粋なRust実装で、機械学習モデルや外部サービスに依存しません」とある。
- コンテンツベースのフォーマット自動検出により、拡張子だけに依存しない判定を行う。 [^]
  - Footnote: 記事はPDFヘッダー、RTFのオープングループ、OLEストリーム名、ZIPパッケージのmimetypeなどで判定すると説明している。
- ベンチマーク上は、anydocが14/14形式に対応し、中央値4.4ms、総合スコア81を記録している。 [^]
  - Footnote: 比較表には「anydoc 14/14 4.4 94 81 87 79 78 81」と記載されている。
- PDFサポートは内蔵されているが、スキャン文書などではFirecrawl API側のOCR併用が必要になる場合がある。 [^]
  - Footnote: README抜粋には、FirecrawlのホスティングAPIではanydoc単独では読めないスキャン文書ページ向けOCRモデルも使えるとある。
- 筆者のPDF検証では、変換速度は高速だったが表や見出し構造の抽出に問題があった。 [^]
  - Footnote: 筆者は実行時間0.109秒の例を示した後、「表組がおかしくなっている」「見出し部分を見出しとして扱ってしまっている」と述べている。
- 文書構造が正しくない元ファイルでは、見た目が問題なくてもMarkdown化が崩れる可能性がある。 [^]
  - Footnote: まとめで、元ファイルが見た目的に問題なくても「文書構造的に正しくないとかだとうまくいかない可能性」があると推測している。
- 大量文書を短時間で処理し、粗い抽出後にLLMへ渡す用途に適している可能性がある。 [^]
  - Footnote: 記事は「文書ファイルが大量にあって高速に処理したい」「ある程度ざっくりでもいいから短時間に抽出」といったユースケースを挙げている。

### References
- https://zenn.dev/kun432/scraps/6b1cfc49cbde39
- https://github.com/firecrawl/anydoc
- https://firecrawl.dev/parse
- https://www.city.kobe.lg.jp/documents/15123/r5_doukou.pdf
