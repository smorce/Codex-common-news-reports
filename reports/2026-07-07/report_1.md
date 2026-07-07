# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-07T09:01:36.6526256+09:00
- Articles: 3

## 日本語形態素解析ライブラリ「Vibrato」を試す
- Date: 2026-07-06T01:49:38+00:00

### Executive Summary
- Vibrato は Viterbi アルゴリズムを基盤にした高速な日本語トークン化・形態素解析ツールとして紹介されている。
- 筆者は既存の Sudachi、MeCab、Janome、Lindera、Kuromoji などと比較しつつ、未経験の Vibrato を試している。
- Python ラッパーを Colaboratory でインストールし、vibrato パッケージと本体バージョンを確認している。
- 辞書は GitHub Releases から取得し、今回は Vibrato v0.5.0 向けの mecab-ipadic v2.7.0 を利用している。
- zstd 圧縮された辞書を Python 側で展開し、Vibrato オブジェクトに読み込ませる必要がある。
- 短文の解析例では「社長は火星猫だ」を 5 トークンに分割し、表層形・素性・開始位置・終了位置を出力している。
- 複数辞書の違いも確認しており、ipadic と BCCWJ + UniDic 系では同じ文でも分割結果が変わることを示している。

### Key Findings
- Vibrato は MeCab の Rust 再実装として、高速化を重視した形態素解析ツールである。 [^]
  - Footnote: 記事中に「Vibratoは高速トークン化ツールMeCabをRustで再実装したもの」と説明がある。
- Python から利用できるラッパーモジュールが提供されている。 [^]
  - Footnote: 本文に「Pythonラッパーが用意されている」「!pip install vibrato」とある。
- Colaboratory での確認では vibrato パッケージ 0.2.3 と Vibrato 本体 0.5.2 が使われている。 [^]
  - Footnote: インストール出力に「Successfully installed vibrato-0.2.3」、バージョン確認出力に「0.5.2」とある。
- 辞書ファイルが zstd 圧縮されている場合、Vibrato に渡す前に展開処理が必要になる。 [^]
  - Footnote: 本文に「辞書がzstdで圧縮されている場合はVibratoの外で展開する必要がある」とある。
- ipadic の例では「社長は火星猫だ」が 5 トークンに分割された。 [^]
  - Footnote: 出力に「トークン数: 5」とあり、社長・は・火星・猫・だが列挙されている。
- Vibrato は複数の公開辞書・モデルを利用でき、BCCWJ + UniDic や IPADIC などが挙げられている。 [^]
  - Footnote: 本文の辞書一覧に「bccwj-suw+unidic-cwj-3_1_1」「ipadic-mecab-2.7.0」などがある。

### References
- https://zenn.dev/kun432/scraps/e6833d0bb59161

## Google Maps Places API の「テキスト検索」 を試す
- Date: 2026-07-05T07:50:08+00:00

### Executive Summary
- この記事は Google Maps Platform の Places API、特に Places API (New) のテキスト検索を試す内容である。
- Places API は施設、地理的位置、スポットなどの整形済み位置データや画像を返すサービスとして説明されている。
- 筆者は Google Maps 関連の知識や経験がない前提で、プロジェクト作成、API 有効化、API キー取得から始めている。
- テキスト検索では places:searchText エンドポイントに POST し、textQuery と FieldMask を指定している。
- FieldMask は返却フィールドを絞る必須要素として扱われ、レイテンシーや課金にも関係すると説明されている。
- 神戸のベジタリアン料理やアジアン料理を例に、表示名、住所、価格帯、Web サイト、タイプなどを取得している。
- オプションパラメータとして言語、地域、ランキング、タイプ、営業中、評価、価格帯、ページング、位置バイアスなどを整理している。

### Key Findings
- Places API (New) は場所検索、予測入力、詳細情報、写真取得などをアプリに追加できる。 [^]
  - Footnote: 本文に「場所の検索結果」「予測入力機能」「返される詳細情報」「高画質の写真」を追加できるとある。
- 今回の検証対象は Places API の中の「テキスト検索」である。 [^]
  - Footnote: 本文に「今回はこの中の『テキスト検索』を試す」とある。
- 利用前提として Places API (New) の有効化と API キー取得が必要である。 [^]
  - Footnote: 前提条件に「プロジェクトで『Places API (New)』を有効化」「APIキーを取得」とある。
- テキスト検索の最小構成では FieldMask と textQuery が重要な必須パラメータになる。 [^]
  - Footnote: 本文の必須パラメータ欄に「FieldMask」「textQuery」が列挙されている。
- FieldMask を広げすぎるとレイテンシーと課金が増えるため、必要フィールドの指定が重要である。 [^]
  - Footnote: 本文に「全部取得するとレイテンシーと課金が増加するため、必要なフィールドを指定する」とある。
- pageSize を指定すると検索結果数を制御でき、例では 5 件に絞っている。 [^]
  - Footnote: 本文に「検索結果はデフォルトだと20件でてくるので、5件に絞っている」とある。

### References
- https://zenn.dev/kun432/scraps/4cc9f0958b7b07

## 「Tau」を試す ③ ガイド
- Date: 2026-07-06T13:35:51+00:00

### Executive Summary
- この記事は Tau の公式ドキュメントにあるガイドを読み、コーディングエージェントとしての使い方を整理している。
- 対象トピックは対話セッション、セッション、プロバイダー・モデル、スキル、プロンプトテンプレート、プロジェクト指示などである。
- Tau は引数なしで起動すると対話型 TUI が立ち上がり、下部の入力欄からプロンプトを送信する。
- 実行中は Esc でキャンセルでき、Enter や Alt+Enter によりステアリングやフォローアップ指示をキューに追加できる。
- スラッシュコマンドでセッション情報、モデル変更、コンテキスト圧縮、再開、履歴分岐、ホットキー表示などを操作できる。
- セッションは追記専用 JSONL として保存され、再開、分岐、エクスポート、名前変更が可能である。
- プロバイダーは OpenAI、Anthropic、OpenRouter、HuggingFace、OpenAI Codex などに対応し、認証やモデル選択の手順も整理されている。

### Key Findings
- Tau の通常利用は対話型 TUI で、引数なしの tau 実行から始まる。 [^]
  - Footnote: 本文に「引数なしで tau を実行すると、対話型のターミナルユーザーインターフェース（TUI）が起動」とある。
- 実行中のキャンセルと追加指示は明確に区別されている。 [^]
  - Footnote: 本文に「Esc 実行中処理がキャンセル」「Enter ステアリング」「Alt+Enter フォローアップ」とある。
- コマンドパレットやスラッシュコマンドで主要操作を呼び出せる。 [^]
  - Footnote: 本文に「Ctrl+k もしくは / で、コマンドの検索や補完入力が可能」とある。
- セッションは作業ディレクトリごとに保存され、後から再開できる。 [^]
  - Footnote: 本文に「すべての会話はセッションとして保存され、後から再開が可能」「~/.tau/sessions/」とある。
- 履歴分岐は会話には効くが、既存の作業ファイル変更までは自動で巻き戻さないと筆者は観察している。 [^]
  - Footnote: 本文に「会話だけに思える」「プロジェクトに対する変更は一度変更したら変更したままになる」とある。
- プロバイダー設定は API キー方式とサブスクリプション認証の両方を扱える。 [^]
  - Footnote: 本文に「APIキー OpenAI Anthropic OpenRouter HuggingFace」「サブスク OpenAI ChatGPTサブスクリプション」とある。
- スキルとプロンプトテンプレートは、ユーザーレベルとプロジェクトレベルの両方で定義できる。 [^]
  - Footnote: 本文に「どちらも2つのレベルがある」「ユーザレベル」「プロジェクトレベル」とある。

### References
- https://zenn.dev/kun432/scraps/d750e143a0f676
