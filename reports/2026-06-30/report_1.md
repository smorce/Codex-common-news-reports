# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-06-30T09:01:16.8904947+09:00
- Articles: 3

## ModernBERT-ja
- Date: 2026-06-29T19:03:00+09:00

### Executive Summary
- SB Intuitions の日本語対応 ModernBERT 関連資料と Hugging Face モデルを試したスクラップ。
- 主に modernbert-ja-130m のモデルカード内容を翻訳・抜粋し、学習条件やモデル構成を確認している。
- ModernBERT-Ja-130M は 4.39T トークン規模の日本語・英語コーパスで学習されたと説明されている。
- モデルシリーズは 30m、70m、130m、310m の 4 サイズが提示され、語彙サイズなどの共通仕様も整理されている。
- 用途はマスク言語モデルとしての下流タスク向けファインチューニングが中心で、テキスト生成向けではない点が強調されている。
- 実行例では fill-mask パイプラインを使い、天気や対話形式のマスク補完を試している。
- VRAM 消費は 470MB 程度と記録され、軽量に動くことが確認されている。

### Key Findings
- ModernBERT-Ja-130M は日本語対応 ModernBERT モデルとして提供されている。 [^]
  - Footnote: 記事本文に「本リポジトリでは、SB Intuitions によって学習された日本語対応のModernBERTモデルを提供しています」とある。
- 学習データは日本語・英語を含む大規模コーパスで、4.39T トークン規模とされる。 [^]
  - Footnote: 本文に「4.39Tトークン規模の高品質な日本語・英語テキストコーパスを用いて学習」とある。
- 入力長は 8,192 トークンで、語彙サイズは 102,400 とされる。 [^]
  - Footnote: 本文に「語彙サイズは102,400、シーケンス長は8,192トークン」とある。
- モデルは 30m、70m、130m、310m の複数サイズで公開されている。 [^]
  - Footnote: モデルシリーズ表に sbintuitions/modernbert-ja-30m、70m、130m、310m が並んでいる。
- 主用途は分類・検索・抽出などの下流タスクで、生成用途には向かない。 [^]
  - Footnote: 本文に「このモデルはテキスト生成を目的として設計されていない」「分類・検索・抽出等の下流タスク」とある。
- 試行では L4 GPU 上で約 466MiB のメモリ使用量が示されている。 [^]
  - Footnote: 記事中の nvidia-smi 出力に「466MiB / 23034MiB」とあり、筆者も「VRAM消費は470MB程度」と記している。

### References
- https://zenn.dev/kun432/scraps/0bc84713bb2991
- https://huggingface.co/sbintuitions/modernbert-ja-130m

## 「ERNIE-Image」を試す
- Date: 2026-06-29T10:40:00+09:00

### Executive Summary
- Baidu の画像生成モデル ERNIE-Image を試したスクラップ。
- 筆者は日本語文字に強いという紹介記事をきっかけに関心を持っている。
- 通常版 ERNIE-Image と蒸留版 ERNIE-Image-Turbo の 2 モデルを確認している。
- 通常版は 8B パラメータの DiT ベースのテキスト画像生成モデルとして説明されている。
- モデルカード抜粋では、複雑な指示理解、テキスト描画、構造化ビジュアル生成への強みが示されている。
- 筆者の試行では、日本語文字そのものは比較的よく生成できているという所感が記録されている。
- Prompt Enhancer は中国語出力を前提にしている可能性があり、自前プロンプトでは中国語または英語が良さそうだと考察している。

### Key Findings
- ERNIE-Image は Baidu が公開するオープンソースのテキスト画像生成モデルである。 [^]
  - Footnote: 本文に「ERNIE-Imageは、バイドゥのERNIE-Imageチームが開発したオープンソースのテキストから画像を生成するモデル」とある。
- 通常版は 80 億パラメータ規模の軽量設計と説明されている。 [^]
  - Footnote: 本文に「わずか80億パラメータという軽量設計」とある。
- テキスト描画やポスター、インフォグラフィック、UI 風画像などに適する特徴がある。 [^]
  - Footnote: 主な特徴に「密度が高く長文・レイアウト依存型のテキスト処理」「ポスターやインフォグラフィック、UI風画像」とある。
- Turbo 版は DMD と RL による最適化で、8 回の推論ステップを特徴としている。 [^]
  - Footnote: リリース版モデル欄に「DMDとRLによる最適化」「わずか8回の推論ステップ」とある。
- 筆者の環境では Turbo 版の処理が 4 秒と速かったと記録されている。 [^]
  - Footnote: 実行コード後のコメントに「こちらは4秒と速い」とある。
- 日本語文字生成は完全ではないが、オープンモデルとしてはメリットがあると評価されている。 [^]
  - Footnote: まとめに「日本語文字がそこそこ安定して生成できるオープンモデルはほとんどないと思うので、それだけでもメリット」とある。
- Prompt Enhancer を使わない場合は中国語または英語プロンプトが良さそうだと推測している。 [^]
  - Footnote: 本文に「自前でプロンプト作る場合は中国語もしくは英語のほうが良さそう」とある。

### References
- https://zenn.dev/kun432/scraps/75ff2ddb507b12
- https://huggingface.co/baidu/ERNIE-Image
- https://huggingface.co/baidu/ERNIE-Image-Turbo

## 「whichllm」を試す
- Date: 2026-06-29T00:42:00+09:00

### Executive Summary
- ローカル LLM 選定 CLI whichllm を試したスクラップ。
- whichllm は手元の GPU、CPU、RAM、ディスクを検出し、Hugging Face 上のモデル候補をランキングする。
- 単に VRAM に入る最大モデルではなく、ベンチマーク、量子化、速度、実行形態、モデル世代をまとめて評価する点が説明されている。
- インストール方法として uvx、uv tool install、Homebrew、pip が示されている。
- GPU に完全に載る候補だけを見たい場合の `--gpu-only`、速度条件の `--speed usable`、VRAM 余白指定などが紹介されている。
- JSON や Markdown 表で出力でき、GitHub や Slack に貼りやすい形式も用意されている。
- 筆者は最新モデルを自分で即試す派だが、手早く最適なローカルモデルを見つけたい用途には良いと評価している。

### Key Findings
- whichllm はローカル環境で実行できる LLM 候補を探す CLI である。 [^]
  - Footnote: README 抜粋に「手元のハードウェアで実際に動くローカルLLMを探すCLI」とある。
- ハードウェア検出と Hugging Face モデル取得を組み合わせて候補をランキングする。 [^]
  - Footnote: 本文に「GPU / CPU / RAM / ディスクを検出し、HuggingFace 上のモデルを取得して、実行できる候補をランキング」とある。
- 評価軸は VRAM 容量だけではなく、ベンチマーク、量子化、速度、実行形態、モデル世代を含む。 [^]
  - Footnote: README 抜粋に「ベンチマーク、量子化、速度、実行形態、モデル世代をまとめて評価」とある。
- 余裕を持って動く候補を見るには GPU 限定、速度条件、VRAM 余白を指定する。 [^]
  - Footnote: 記事中に `uvx whichllm@latest --gpu-only --speed usable --vram-headroom 1GB` の例がある。
- JSON 出力には速度推定、Fit 種別、VRAM 必要量、利用可能量、ベンチマーク根拠などが含まれる。 [^]
  - Footnote: README 抜粋に `estimated_tok_per_sec`、`fit_type`、`vram_required_bytes`、`benchmark_source` などが入るとある。
- plan コマンドは特定モデルを動かすために必要な GPU や VRAM を確認できる。 [^]
  - Footnote: 記事中に `whichllm plan "deepseek v4 flash"` の例と、Q4_K_M で 151.4GB 必要という出力がある。
- 筆者は、自分で試さず手早く最適モデルを見つけたいニーズには有用と結論づけている。 [^]
  - Footnote: まとめに「手っ取り早く自分のマシンで最適なローカルモデルを見つけたい、っていうニーズなら良い」とある。

### References
- https://zenn.dev/kun432/scraps/b1ca9f8300ea3a
- https://github.com/Andyyyy64/whichllm
