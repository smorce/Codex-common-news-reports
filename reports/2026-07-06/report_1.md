# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-06T09:03:14.5171500+09:00
- Articles: 3

## Google Maps Places API の「テキスト検索」 を試す
- Date: 2026-07-05T07:50:08+00:00

### Executive Summary
- Google Maps Places API の新版にあるテキスト検索を、Colaboratory と curl で試した記録である。
- Places API は施設、地理的位置、有名スポットなどの位置データや画像を返すサービスとして説明されている。
- 試行では Places API (New) を有効化し、API キーを取得して Colaboratory のシークレットに保存している。
- 基本リクエストでは places:searchText に POST し、textQuery と X-Goog-FieldMask を指定する形を確認している。
- FieldMask は必須で、返却フィールドの量がレイテンシーと課金に影響するため必要な項目だけ指定する方針が示されている。
- textQuery は曖昧な場所検索にも使えるが、地理空間に関係しない意図や複数解釈が強いクエリには限界がある。
- pageSize、languageCode、regionCode、rankPreference、includedType、locationBias などの主要オプションが整理されている。
- 日本語向けの例として、神戸のアジアン料理検索や追加フィールド指定を使った結果確認まで行っている。

### Key Findings
- Places API (New) のテキスト検索は、自然言語に近い場所検索から候補を返す用途に使える。 [^]
  - Footnote: 本文では「テキスト入力、付近の場所、曖昧なユーザー クエリやカテゴリ別のユーザー クエリなど」から検索結果を提供できると説明している。
- 利用前にはプロジェクトで Places API (New) を有効化し、API キーを用意する必要がある。 [^]
  - Footnote: 前提条件として「プロジェクトで『Places API (New)』を有効化」「APIキーを取得」と記載されている。
- API キー利用時は制限設定が必要で、この記事では利用可能 API の制限を選んでいる。 [^]
  - Footnote: 著者は「APIキーの場合は何かしらの制限が求められる」が、今回は「利用できるAPIを制限することにした」と述べている。
- リクエストには textQuery と FieldMask の指定が重要である。 [^]
  - Footnote: 必須パラメータとして「FieldMask」「textQuery」が挙げられ、textQuery はリクエストボディ JSON で指定すると説明されている。
- FieldMask は返却内容を絞るための指定で、課金とレイテンシーの両面に関係する。 [^]
  - Footnote: 本文では「全部取得するとレイテンシーと課金が増加するため、必要なフィールドを指定するのがFieldMask」と説明している。
- すべてのフィールドを取得するにはアスタリスク指定が可能だが、本番利用では推奨されない。 [^]
  - Footnote: FieldMask の説明で「全部取りたかったら * で指定する必要がある（ただし本番では非推奨）」と記載されている。
- textQuery は曖昧な場所検索をランキング形式で返せるが、対象外のクエリ類型がある。 [^]
  - Footnote: 「やや特定が曖昧な文字列でも一致する候補を、関連性のある候補をランキング形式で返してくれる」としつつ、非対象例の表が示されている。
- デフォルトでは検索結果が 20 件返るため、pageSize で件数を絞れる。 [^]
  - Footnote: 日本語向け例で「検索結果はデフォルトだと20件でてくるので、5件に絞っている」と説明している。

### References
- https://zenn.dev/kun432/scraps/4cc9f0958b7b07

## 「Tau」を試す ③ ガイド
- Date: 2026-07-04T16:11:19+00:00

### Executive Summary
- Tau の前回記事に続き、公式ドキュメントのガイド群を読むためのスクラップである。
- 記事本文は現時点では導入と読む予定のトピック列挙が中心で、詳細な検証ログはまだ少ない。
- 扱う予定の範囲には、対話セッションとセッション管理が含まれている。
- プロバイダーとモデルの扱いも確認対象として挙げられている。
- スキルとプロンプトテンプレートも、Tau を使う上で読むべきテーマとして整理されている。
- プロジェクト指示とコンテキスト管理は、エージェント運用上の重要項目として含まれている。
- Print mode とスクリプト利用も対象で、対話だけでなく自動化・非対話実行まで確認する意図が見える。

### Key Findings
- この記事は Tau の連載的な検証の第3回に位置づけられている。 [^]
  - Footnote: 本文冒頭に「前回の続き」とあり、タイトルも「『Tau』を試す ③ ガイド」となっている。
- 今回の焦点は公式ドキュメントのガイドを読み進めることである。 [^]
  - Footnote: 本文では「今回は公式ドキュメントにある『ガイド』の各ドキュメントを読んでいく」と説明している。
- 対話セッションは確認予定トピックの先頭に置かれている。 [^]
  - Footnote: トピック一覧の最初に「対話セッション」と記載されている。
- セッション管理は対話セッションとは別項目として扱われている。 [^]
  - Footnote: トピック一覧に「対話セッション」とは別に「セッション」が挙げられている。
- モデル選択やプロバイダー設定も Tau 利用の確認対象である。 [^]
  - Footnote: トピック一覧には「プロバイダー・モデル」が含まれている。
- スキルとプロンプトテンプレートは Tau の拡張・指示設計に関わるテーマとして扱われる。 [^]
  - Footnote: トピック一覧に「スキル・プロンプトテンプレート」と記載されている。
- プロジェクト指示とコンテキスト管理も、エージェント運用の前提として確認される予定である。 [^]
  - Footnote: トピック一覧には「プロジェクト指示」「コンテキストの管理」が並んでいる。
- Tau は対話利用だけでなく、Print mode やスクリプト利用も想定して確認される。 [^]
  - Footnote: 最後のトピックとして「Print modeとスクリプトでの利用」が挙げられている。

### References
- https://zenn.dev/kun432/scraps/d750e143a0f676

## 「OpenWiki」を試す
- Date: 2026-07-04T16:29:59+00:00

### Executive Summary
- OpenWiki を、コードベース向けに wiki 形式のドキュメントを自動生成・自動更新するツールとして試した記録である。
- 大きなリポジトリを読む際に、README や AGENTS.md だけでは情報が肥大化しやすい問題意識が示されている。
- OpenWiki はリポジトリを解析して openwiki ディレクトリ配下に複数の Markdown ドキュメントを生成する。
- AGENTS.md や CLAUDE.md には wiki 本体を直書きせず、参照先を追記してエージェントに読ませる設計が説明されている。
- インストールは npm install -g openwiki で行い、openwiki --init でモデルプロバイダーや API キーを設定する。
- 試行では OpenRouter と GLM 5.2 を選び、LangSmith のトレーシング設定も任意項目として確認している。
- サンプルの Python ToDo CLI では quickstart、architecture、workflows、testing などの文書が生成された。
- 変更後は openwiki --update で差分更新でき、.last-update.json に更新日時、コマンド、gitHead、モデルが記録される。
- まとめでは、既存プロジェクトにも組み込みやすい一方、人間向けドキュメントとしての読みやすさは別問題だと評価している。

### Key Findings
- OpenWiki はコードベース用の wiki を AI が自動生成し、最新化するツールとして紹介されている。 [^]
  - Footnote: 本文のまとめでは「コードベースのための、自動生成＆自動更新されるエージェント向け wiki ツール」と表現している。
- 大規模コードベースでは、単一ファイルの説明書に情報を詰め込む運用に限界がある。 [^]
  - Footnote: 本文では README や AGENTS.md / CLAUDE.md に全部入れると「1ファイルがデカすぎ」「トークンの無駄」「メンテするのダルすぎ」と整理している。
- wiki 形式にする利点は、小さいページ群に分けて必要箇所だけ参照できることである。 [^]
  - Footnote: 本文では「リンクされた小さいページの集合」として整理し、エージェントが「必要なところだけ」取りに行けると説明している。
- OpenWiki は CLI 実行、GitHub Action 更新、AGENTS.md / CLAUDE.md 連携まで含む実用ツールとして位置づけられている。 [^]
  - Footnote: 本文では「CLI でサクッと回せて」「GitHub Action で自動更新できて」「AGENTS.md / CLAUDE.md ともちゃんとつながる」と説明している。
- 初期化ではモデルプロバイダー、API キー、モデル、任意の LangSmith キーを設定する。 [^]
  - Footnote: openwiki --init の出力として Provider、Provider key、Model、LangSmith が表示されている。
- 初期化時は対象プロジェクト内で実行する必要があるという注意点がある。 [^]
  - Footnote: 著者はホームディレクトリ直下で --init するとホームディレクトリを解析しようとしているように見えたため「これはアカン」と述べている。
- 生成物には openwiki/quickstart.md、architecture.md、workflows.md、testing.md などが含まれる。 [^]
  - Footnote: 実行完了ログに「Initialized OpenWiki documentation under openwiki/」として quickstart、architecture、workflows、testing が列挙されている。
- AGENTS.md には openwiki ディレクトリへの参照と quickstart の読み始め指示が追加される。 [^]
  - Footnote: 抜粋された AGENTS.md には「This repository has documentation located in the /openwiki directory」「Start here」として quickstart へのリンクがある。
- 更新管理には openwiki --update と .last-update.json が使われる。 [^]
  - Footnote: 本文では「何かしら変更後にドキュメントを更新する場合は --update」とし、.last-update.json の updatedAt、command、gitHead、model を示している。
- 著者は OpenWiki 生成ドキュメントをコーディングエージェントが直接編集しないよう指示する必要性も示唆している。 [^]
  - Footnote: 余談として「OpenWikiが生成したドキュメントを更新しないように AGENTS.md あたりに書いておいたほうがいいかも」と述べている。

### References
- https://zenn.dev/kun432/scraps/c4d2f75eb7e493
