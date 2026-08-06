# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-08-06T09:03:01.0304125+09:00
- Articles: 3

## Maple-Preview

### Executive Summary
- Maple-Preview は、20B-A1B の三値重み推論 LLM として紹介されている。
- Mac Mini M4 で 200 トークン/秒以上、iPhone 上でも 120 トークン/秒以上というオンデバイス性能が強調されている。
- Gemma 4、Qwen3.5、gpt-oss などの効率モデルより 5-16 倍高速とされる。
- 低精度化を後処理ではなく学習設計の前提に置く思想が中心にある。
- オンデバイス適応では、ユーザーの好みを外部メモリではなく重みに埋め込む構想が示されている。
- ヴィーガン嗜好を反映したバッグ推薦の例で、テキストメモリ方式との差を説明している。
- 現時点の実行環境は MLX 向けが中心で、Mac Apple Silicon での試用が現実的と見られている。
- 筆者は日本語対応は明記されていないが、一応使えたものの日本語知識は強くなさそうと評価している。

### Key Findings
- Maple-Preview はオープンソースの 20B-A1B 三値重み推論 LLM と位置付けられている。 [^]
  - Footnote: 記事本文に「オープンソースの 20B-A1B 三値重み推論 LLM」「その重みクラスで SOTA」とある。
- オンデバイス推論速度が主要な訴求点である。 [^]
  - Footnote: Mac Mini M4 で 200+ トークン/秒、iPhone 上で 120+ トークン/秒と記載されている。
- 既存の効率モデルに対する速度優位が主張されている。 [^]
  - Footnote: Gemma 4、Qwen3.5、gpt-oss などより 5-16 倍高速と説明されている。
- モデルの軽量性はオンデバイス適応の前提として扱われている。 [^]
  - Footnote: 「軽量なフットプリントにより、オンデバイス適応が可能」と説明されている。
- ユーザー固有の記憶を重みに反映する Dreaming 的な仕組みが示されている。 [^]
  - Footnote: MacBook Pro 上で食事の好みを記憶し、その後「夢を見る」ことで重みに埋め込む例が挙げられている。
- 外部メモリ方式より細かなユーザー嗜好を保持できる可能性が示唆されている。 [^]
  - Footnote: テキストベースの記憶では見逃されがちな微妙なユーザー固有の詳細を保持すると説明されている。
- 提供物にはチャット、Hugging Face 重み、MLX 形式、mlx-lm 手順が含まれる。 [^]
  - Footnote: chat.deepgrove.ai、huggingface.co/deepgrove/maple-preview、maple-preview-2bit-mlx、mlx-lm-deepgrove が参照されている。

### References
- https://zenn.dev/kun432/scraps/6da529da4a42b0
- http://deepgrove.ai/maple-preview
- http://huggingface.co/deepgrove/maple-preview
- http://github.com/deepgrove-ai/mlx-lm-deepgrove

## 「anydoc」を試す

### Executive Summary
- anydoc は Firecrawl が開発する Rust ベースの高速ドキュメント変換ライブラリとして紹介されている。
- Word、PowerPoint、Excel、OpenDocument、RTF、EPUB、CSV、PDF などを GitHub Flavored Markdown に変換する。
- Node.js、Python、ブラウザ WebAssembly 向けのバインディングが用意されている。
- ベンチマークでは 14/14 フォーマット対応、中央値 4.4ms、スコア 81 とされている。
- 筆者の PDF 試行では変換速度は非常に速かったが、表や見出し抽出の品質には課題が見られた。
- 元文書の見た目ではなく文書構造に依存するため、構造が崩れている PDF では精度が落ちる可能性がある。
- 高精度が必要な用途では OCR モデルや VLM、Firecrawl API の併用が望ましいと考察している。
- 大量文書を短時間で粗く抽出し、後段を LLM に任せる用途に向く可能性がある。

### Key Findings
- anydoc は複数ドキュメント形式を Markdown に統一変換するライブラリである。 [^]
  - Footnote: README 抜粋として Word、PowerPoint、Excel、OpenDocument、RTF、EPUB、CSV、PDF をクリーンな GFM に変換すると記載されている。
- 処理系は Rust 実装で、複数ランタイム向けバインディングを持つ。 [^]
  - Footnote: Node.js、Python、ブラウザ環境 WebAssembly 向けのバインディングを提供すると説明されている。
- 公式ベンチマークでは速度と対応形式数が強みとして示されている。 [^]
  - Footnote: 表では anydoc が対応フォーマット 14/14、中央値変換時間 4.4ms、スコア 81 とされている。
- 他ツールと比べても変換速度は大きく速い。 [^]
  - Footnote: libreoffice 1129.5ms、unstructured 572.9ms、markitdown 134.8ms に対し anydoc は 4.4ms と記載されている。
- PDF 変換では OCR サービスなしでローカル処理できる範囲がある。 [^]
  - Footnote: PDF サポートを内蔵し、テキストベース PDF は pdf-inspector を使用してローカルで変換可能とある。
- 筆者の実試行では速度は優秀だが、Markdown 構造の品質に難があった。 [^]
  - Footnote: 神戸市 PDF の変換結果について「表組がおかしく」「見出しとかがきちんとなってなくて読みにくい」と評価している。
- 利用判断には実ドキュメントでの検証が必要である。 [^]
  - Footnote: まとめで「実際に抽出したいドキュメントで色々試してから、判断したほうが良さそう」と述べている。

### References
- https://zenn.dev/kun432/scraps/6b1cfc49cbde39
- https://github.com/firecrawl/anydoc
- https://firecrawl.github.io/anydoc/
- https://www.city.kobe.lg.jp/documents/15123/r5_doukou.pdf

## 「Escha-W2 quantization」を試す

### Executive Summary
- Escha-W2 は Qwen3.6-35B-A3B を 2 ビット量子化した高速ローカル推論向けモデルとして紹介されている。
- モデルサイズはディスク上 12.3GB で、単一のコンシューマ GPU で動作可能とされる。
- 12 ベンチマーク平均で約 100% の FP8 性能を維持するという主張がある。
- MATH-500 や GPQA-Diamond では FP8 より高い数値も示される一方、LiveCodeBench は低下している。
- 専用ランタイムは SGLang と ZML をサポートし、vLLM と llama.cpp は今後対応予定とされている。
- 筆者は Ubuntu 24.04 と RTX 4090 で SGLang 側を試し、OpenAI 互換 API として起動している。
- 実測ログでは約 175 トークン/秒前後が確認され、動作自体は成立している。
- ただし日本語出力に英語トークンが混じる例があり、2 ビット量子化の影響かは未確定としている。

### Key Findings
- Escha-W2 は Qwen3.6-35B-A3B を 2 ビット級に圧縮したモデルである。 [^]
  - Footnote: 「2ビットQwen3.6-35B-A3Bモデル」「ディスク上で12.3GB」と説明されている。
- 単一の RTX 4090 で高速生成できることが訴求されている。 [^]
  - Footnote: 単一の RTX 4090 上で 225 tok/s シングルストリーム生成と記載されている。
- 公式主張では FP8 性能をほぼ維持している。 [^]
  - Footnote: 12 のベンチマークで平均約 100% の FP8 性能を発揮するとある。
- 代表ベンチマークには数学、科学、コード、ツール利用、長文文脈が含まれる。 [^]
  - Footnote: MMLU-Pro 80.9、MATH-500 93.8、GPQA-Diamond 77.8、LiveCodeBench v6 62.6、BFCL 88.9、RULER 89.9 が列挙されている。
- 圧縮には単純な量子化以上のモデル認識型手法が使われている。 [^]
  - Footnote: 低ビット量子化をモデル認識型ファインチューニングとリカバリと組み合わせたと説明されている。
- 専用ランタイムは現時点で SGLang と ZML を対象にしている。 [^]
  - Footnote: ランタイムは現在 SGLang および ZML デプロイをサポートし、vLLM と llama.cpp は次回リリース予定とされている。
- 筆者の SGLang 試行では OpenAI 互換 API として起動できている。 [^]
  - Footnote: curl /v1/models の出力に escha-qwen36-35b-a3b-w2 と max_model_len 32768 が表示されている。
- 筆者は出力品質について、日本語中に英語トークンが混じる場合がある点を懸念している。 [^]
  - Footnote: 出力例の deeper やログ後のコメントで「たまにトークンがおかしい」「英語トークンが紛れる」と述べている。

### References
- https://zenn.dev/kun432/scraps/d17891fd595a32
- https://huggingface.co/EschaLabs/Qwen3.6-35B-A3B-Escha-W2
- https://huggingface.co/EschaLabs/escha-runtime-qwen3moe
- https://www.eschalabs.com/
