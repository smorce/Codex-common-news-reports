# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-08-28T09:01:47.9507746+09:00
- Articles: 3

## 「Cloudflare Containers」を試す

### Executive Summary
- Zenn のスクラップ一覧で最新上位に表示されていた Cloudflare Containers 関連のスクラップである。
- 状態は Open と表示され、作成時刻は相対表記で「10時間前に作成」と確認できた。
- 本文コメントはまだ投稿されておらず、ページ上には「最初のコメントを追加しましょう」と表示されていた。
- トピックは Cloudflare、Cloudflare Workers、containers に分類されている。
- スクラップ本文から具体的な検証手順や結果は取得できなかった。
- 現時点では、今後 Cloudflare Containers を試すための作業場所として作成されたものと解釈できる。
- 記事日付は ISO-8601 の絶対時刻として取得できなかったため null とした。

### Key Findings
- Cloudflare Containers を主題にしたスクラップである。 [^]
  - Footnote: ページタイトルに「「Cloudflare Containers」を試す」と表示されていた。
- スクラップは未完了状態である。 [^]
  - Footnote: 一覧およびページ上で状態が「Open」と表示されていた。
- 作成から間もないスクラップである。 [^]
  - Footnote: ページ上に「10時間前に作成」と表示されていた。
- 本文コメントはまだ存在しない。 [^]
  - Footnote: 本文領域に「最初のコメントを追加しましょう」と表示されていた。
- 関連トピックは Cloudflare とコンテナ技術である。 [^]
  - Footnote: タグとして「Cloudflare」「Cloudflare Workers」「containers」が表示されていた。

### References
- https://zenn.dev/kun432/scraps/3f3f211c8ad485

## Cloudflare WorkersでPython Workerを試す、再び
- Date: 2026-08-27T14:25:24+00:00

### Executive Summary
- Cloudflare Workers の Python Worker を改めて試す目的のスクラップである。
- 筆者は約 2 年前にも試しており、当時は Pyodide ベースで制約が強い印象だったと述べている。
- 現在も通常の Linux 上の Python と同じ感覚ではないが、以前より改善されたと受け止めている。
- Cloudflare Workers は Python を first-class に扱う体験を提供していると紹介している。
- FastAPI、Langchain、Pydantic などのパッケージを利用できる点が挙げられている。
- Python から JavaScript オブジェクトや Runtime API を使える FFI が重要な機能として整理されている。
- KV、D1、Durable Objects、Workers AI、Vectorize、R2 など Cloudflare サービス連携も確認対象になっている。

### Key Findings
- 過去の Python Worker 体験は Pyodide ベースで制約が強かった。 [^]
  - Footnote: 本文に「pyodideを使ったもので、パッケージの追加なども一切できず、かなりトリッキー」とある。
- 現在の Cloudflare Workers Python サポートは以前より改善されている。 [^]
  - Footnote: 本文に「以前よりは改善されたようで Cloudflare Workers provides a first-class Python experience らしい」とある。
- FastAPI、Langchain、Pydantic などの Python パッケージが利用候補として挙げられている。 [^]
  - Footnote: 本文に「FastAPI、Langchain、Pydantic など、簡単にインストール可能で高速起動するパッケージ群」とある。
- Python と JavaScript/Workers Runtime API の連携が重要な特徴である。 [^]
  - Footnote: 本文に「JavaScriptのオブジェクトや関数をPythonから直接利用できる堅牢な外部関数インターフェース」とある。
- Cloudflare の各種ストレージ、AI、キュー系サービスとの連携が可能と整理されている。 [^]
  - Footnote: 本文に「KV、D1、Durable Objects」「Workers AI や Vectorize」「R2」「Durable Workflows、キューシステム」とある。
- 筆者は今後 Cloudflare を活用する前提で再検証を始めている。 [^]
  - Footnote: 本文に「今後 Cloudflare を活用していきたいと思っているので、まずは Workers for Python を改めて試す」とある。

### References
- https://zenn.dev/kun432/scraps/2d874856edd409
- https://developers.cloudflare.com/workers/languages/python/

## Pyodide
- Date: 2026-08-27T15:36:56+00:00

### Executive Summary
- Cloudflare Workers for Python で使われている Pyodide を調べるスクラップである。
- 筆者は Cloudflare Workers の Python サポートが進んだ一方で、現在も Pyodide が使われているらしいと整理している。
- 今後 Cloudflare を活用するため、Workers for Python の基盤である Pyodide も一通り試す方針である。
- 公式ドキュメントのトップページを抜粋し、PLaMo 翻訳で日本語化した内容が掲載されている。
- Pyodide は WebAssembly を基盤とした、ブラウザおよび Node.js 向けの Python ディストリビューションとして説明されている。
- CPython を WebAssembly と Emscripten に移植した実装であることが中心的な技術要点である。
- micropip、Python パッケージ、JavaScript/Python 間 FFI、Web API 利用などが主要機能として整理されている。

### Key Findings
- Pyodide は Cloudflare Workers for Python の理解に関係する技術として扱われている。 [^]
  - Footnote: 本文に「Cloudflare Workers for Pythonで使用されているやつ」とある。
- Cloudflare Workers の Python サポートは進展しているが、基盤として Pyodide が使われていると見られている。 [^]
  - Footnote: 本文に「Pythonサポートは進んでいるみたいだが、どうやら今もPyodideが使用されているらしい」とある。
- Pyodide は WebAssembly ベースの Python ディストリビューションである。 [^]
  - Footnote: 本文に「WebAssembly を基盤としたブラウザおよび Node.js 向けの Python ディストリビューション」とある。
- Pyodide は CPython を WebAssembly と Emscripten に移植した実装である。 [^]
  - Footnote: 本文に「CPython を WebAssembly および Emscripten に移植した実装」とある。
- micropip によりブラウザ環境で Python パッケージをインストールして実行できる。 [^]
  - Footnote: 本文に「micropip を使ってブラウザ環境で Python パッケージをインストールして実行」とある。
- NumPy、pandas、SciPy、Matplotlib、scikit-learn など科学計算系パッケージも利用例として挙げられている。 [^]
  - Footnote: 本文に「NumPy」「pandas」「SciPy」「Matplotlib」「scikit-learn」とある。
- Python と JavaScript の相互運用性が Pyodide の重要な特徴である。 [^]
  - Footnote: 本文に「JavaScript と Python間の堅牢な外部関数インターフェースが標準で備わって」とある。

### References
- https://zenn.dev/kun432/scraps/e9054c2e0682a4
- https://pyodide.org/en/stable/
