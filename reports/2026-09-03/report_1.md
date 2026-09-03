# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-09-03T09:01:30+09:00
- Articles: 3

## MiaAI-Lab Qwen3.8-27B EXL3量子化版を試す
- Date: 2026-09-01T16:11:00+09:00

### Executive Summary
- MiaAI-Lab が公開した Qwen3.8-27B の EXL3 量子化版を、ローカル推論の観点で試している。
- 対象モデルは 24GB VRAM 環境で 200k 超のコンテキストを扱える点が大きな特徴として紹介されている。
- 筆者は EXL3 や dflash2、MiaAI-Lab の既存レシピとの関係を踏まえて検証している。
- Pi のモデル設定例を追加し、OpenAI 互換の completions API としてローカルサーバーを登録している。
- reasoning_effort や thinkingFormat など、推論系パラメータの扱いも確認対象になっている。
- 過去に試した Qwen3.8-27B 量子化モデルと比較し、今回の構成は最も高速だったと評価している。
- 一方で API はまだシンプルで、reasoning budget や Inception パターン対応など追加改善が必要としている。

### Key Findings
- 記事は Qwen3.8-27B の EXL3 量子化版を主題にしている。 [^]
  - Footnote: 本文に「Qwen3.8-27BのEXL3版を出された方がいる」とある。
- 公開元の説明では 24GB VRAM で 200k 超コンテキストを扱えることが訴求されている。 [^]
  - Footnote: 引用された投稿に「24GB VRAMでdflash2を使用しながら200k+のコンテキストでQwen3.8-27Bを提供」とある。
- 筆者はローカル推論ツール Pi の設定に Qwen3.8 EXL3 ローカルプロバイダを追加している。 [^]
  - Footnote: 本文に「Piの設定を変更」とあり、models.json に baseUrl、api、model id などを設定している。
- reasoning_effort は low でも実行時間が長く、truncated 発生後に compaction で完走した。 [^]
  - Footnote: 本文に「low で Pagoda Garden を試してみたら、一回 "truncated" が発生したけど、compactionして何とか完走」とある。
- 過去の量子化モデル比較では今回の構成が最速とされている。 [^]
  - Footnote: まとめに「条件が違う...それでも今までで最も高速に動作するものだった」とある。

### References
- https://zenn.dev/kun432/scraps/d1ddb8405e0b13

## OpenAI CLI
- Date: 2026-08-29T20:01:00+09:00

### Executive Summary
- OpenAI CLI の存在に気づいた筆者が、インストールから主要 API 操作までを試している。
- CLI は Go 製で、GitHub に openai/openai-cli として公開されていると紹介している。
- Homebrew でインストールし、手元環境では openai version 1.9.0 を確認している。
- Responses API へのリクエストでは gpt-5.6 を指定し、日本語が JSON 内で Unicode エスケープされる挙動を確認している。
- --format には auto、explore、json、jsonl、pretty、raw、yaml があり、pretty や yaml では日本語表示が読みやすいとしている。
- Files API では PDF をアップロードし、取得した file_id を input_file として Responses API に渡す流れを示している。
- 画像生成・編集や音声合成も CLI から扱えるが、TTS の instructions は新しいモデル別名では効きにくい可能性を観察している。

### Key Findings
- OpenAI CLI は公式ドキュメントと GitHub リポジトリが確認されている。 [^]
  - Footnote: 本文に OpenAI CLI ドキュメントへの埋め込みと「openai/openai-cli Official CLI for the OpenAI API」が表示されている。
- CLI は比較的新しいものとして認識され、v1.0.0 は 2026年5月のリリースとされている。 [^]
  - Footnote: 本文に「Releasesを遡るとv1.0.0は2026年5月なので、4ヶ月ほど前」とある。
- Homebrew から `brew install openai/tools/openai` で導入できる。 [^]
  - Footnote: 本文のインストール例に「brew install openai/tools/openai」とある。
- Responses API の標準 JSON 出力では日本語が Unicode エンコードされたまま表示される場合がある。 [^]
  - Footnote: 本文に「日本語はUnicodeエンコードされたままになる」とあり、出力例にもエスケープ文字列が示されている。
- CLI の `--format` 指定で yaml や pretty を使うと日本語を読みやすく出力できる。 [^]
  - Footnote: 本文に「explore / pretty / yaml では日本語で出力された」とある。
- Files API 連携では `files create` で file_id を取得し、Responses API の input_file に渡す手順が示されている。 [^]
  - Footnote: 本文に「ファイルをアップロード。これでファイルのIDを取得する」「file_id: ${FILE_ID}」とある。

### References
- https://zenn.dev/kun432/scraps/6070a2fd5dca29

## 「Pyodide」 を試す ③ Python compatibility
- Date: 2026-08-29T01:46:00+09:00

### Executive Summary
- Pyodide の Python 互換性と制約を、通常の CPython と比較する目的で整理している。
- Pyodide は WebAssembly VM 上で動くため、Python 自体の多くの機能は動くが OS 依存機能には制約がある。
- 標準ライブラリの大部分は利用できる一方、一部は機能制限、削除、またはインポートできても動作しない。
- decimal、pydoc、webbrowser、zoneinfo、hashlib、ssl などは制限や追加ロードの必要がある。
- HTTP 通信はブラウザのネットワーク API を経由するため、証明書、タイムアウト、プロキシ、CORS などを自由に制御できない。
- threading、multiprocessing、socket は WebAssembly VM の制約で実用上動かないと整理されている。
- 筆者は Cloudflare Workers for Python の理解に向けた下調べとして確認し、次は Workers 側を見る予定としている。

### Key Findings
- Pyodide は Python 機能の多くを動かせるが、OS・ネットワーク・スレッド依存機能に制約がある。 [^]
  - Footnote: 本文に「Python そのものの機能は結構動く」「OS・ネットワーク・スレッドなどに依存する機能には制約がある」とある。
- 標準ライブラリは大部分が動作するものの、例外として制限・削除・非動作のカテゴリがある。 [^]
  - Footnote: 本文に「Python標準ライブラリの大部分は動作する。ただし...例外がある」とある。
- pydoc は初期状態では含まれず、pydoc_data を明示的にロードまたはインストールする必要がある。 [^]
  - Footnote: 本文に「pydoc...デフォルトでは組み込まれていない」「pyodide.loadPackage('pydoc_data')」「micropip.install('pydoc_data')」とある。
- HTTP 通信はブラウザ経由であり、サーバー上の Python と同じ自由度はない。 [^]
  - Footnote: 本文に「HTTP通信はブラウザ経由」「ブラウザの制約を受ける」「サーバー上のPythonのような自由な通信はできない」とある。
- ストリーミングダウンロードには Web Worker と cross-origin isolated が必要で、条件外では非ストリーミングになる。 [^]
  - Footnote: 本文に「Pyodideが Web Worker 内で動いている」「Webサイトが cross-origin isolated」「条件を満たさない場合は非ストリーミング」とある。
- threading、multiprocessing、socket はインポートできても WebAssembly VM の制約で機能しないとされている。 [^]
  - Footnote: 本文に「WebAssembly VMの制約からインポートはできても機能しないもの」として multiprocessing、threading、socket が挙げられている。

### References
- https://zenn.dev/kun432/scraps/77b53e782bdeef
