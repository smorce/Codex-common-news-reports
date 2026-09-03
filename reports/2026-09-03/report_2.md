# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-09-03T09:04:29.7941217+09:00
- Articles: 3

## Claude Fable 5.1、API仕様変更で違法蒸留の対策を強化 - PC Watch
- Date: 2026-09-02T11:18:22+09:00

### Executive Summary
- Anthropic は Claude Fable 5.1 の提供とあわせて、メッセージ API の思考ブロック処理仕様を変更した。
- 背景には、高度な AI モデルの知識や推論能力を不正に抽出して別モデルの訓練に使う違法蒸留への対策がある。
- 新仕様では、過去の思考ブロック前のコンテキストが改変された場合、API がエラーを返す。
- 従来は複数ターン会話で思考ブロックを含む文脈全体を送信でき、改変により復号・出力を誘導できたとされる。
- 不正利用は数千の偽アカウントを使った産業規模の行為として説明されている。
- 正当なコンテキスト改変用途向けには、過去の思考ブロックを除外して継続する非厳格モードも用意される。
- 仕様変更は 2026年8月31日以降作成の新規 API アカウントから順次適用され、既存アカウントやエンドユーザー向けアプリには影響しない。

### Key Findings
- Fable 5.1 は科学研究スコアで従来モデルの2倍を記録したとされる。 [^]
  - Footnote: 記事本文に「科学研究スコアで従来の『Fable 5』の2倍を記録した新モデル『Fable 5.1』」と記載。
- API 仕様変更の目的は、蒸留攻撃による不正な学習の防止である。 [^]
  - Footnote: 記事本文に「蒸留攻撃によるモデルの不正な学習を防止するため、メッセージAPIにおける思考ブロックの処理仕様を変更」と記載。
- コンテキスト改変が検知されると API がエラーを返す仕組みに変わった。 [^]
  - Footnote: 記事本文に「コンテキストが改変された場合、APIがエラーを返す仕組み」と記載。
- 不正利用は偽アカウントを使って大規模に行われていたと説明されている。 [^]
  - Footnote: 記事本文に「数千もの偽アカウントを用いて産業規模で行なわれていた」と記載。
- 正当な用途への配慮として非厳格モードが提供される。 [^]
  - Footnote: 記事本文に「過去の思考ブロック自体をモデルから除外して会話を継続する『非厳格』モードも提供」と記載。
- 適用対象は新規 API アカウントからで、既存アカウントや Claude Code などには影響しない。 [^]
  - Footnote: 記事本文に「2026年8月31日以降に作成された新規のAPIアカウントから順次適用」「Claude Codeなど...影響はない」と記載。

### References
- https://pc.watch.impress.co.jp/docs/news/2137479.html

## AIにまじなスライド作らせる｜【公式】Jinba
- Date: 2026-09-02T22:08:00+09:00

### Executive Summary
- Jinba 公式記事は、AI に実務品質のスライドを作らせるための仕組み一式を公開している。
- 著者は、生成 AI の出力が見た目だけ整っても役員会議や顧客提案には不足しがちだと指摘する。
- 品質の核はテンプレートやパイプラインではなく、レビュー指摘を蓄積した slide-rules.md という約80項目の規約集だと位置づける。
- 仕組みは、規約、38型カタログと SlideSpec、生成パイプライン、最後の調整という構成で説明されている。
- SlideSpec はスライドを JSON として定義し、HTML プレビューと編集可能な PPTX を生成する。
- check_deck.py により、タイトル表現、角丸、表ヘッダー、罫線、表記ゆれなどを機械チェックする運用が示されている。
- 記事は Claude Code 向けスキルとしての利用に加え、非エンジニア向けに Jinba App Neo で同じ資産を使う方向も紹介している。

### Key Findings
- AI のスライド出力は、そのままでは実務資料として使いにくいという問題認識から始まっている。 [^]
  - Footnote: 記事冒頭に「役員会議や顧客提案に持っていけるかというと、ほとんどの場合そのままでは使えません」と記載。
- 公開物の中心は、実務レビューの指摘を蓄積した規約ファイルである。 [^]
  - Footnote: 記事本文に「本質はテンプレでもパイプラインでもなく、slide-rules.md」と記載。
- 38型カタログと SlideSpec によって、頻出スライドのたたき台をデータ定義として扱う。 [^]
  - Footnote: 記事本文に「スライド38型の型カタログ＋SlideSpec」「機械が読めるデータ定義（JSON）」と記載。
- 生成パイプラインは HTML プレビューと編集可能 PPTX の自動生成を担う。 [^]
  - Footnote: 記事本文に「SlideSpecからHTMLプレビューと編集可能なPPTXを自動で組み立てるスクリプト群」と記載。
- 最新の運用では自由記述テンプレートを使う本線と、たたき台生成用パイプラインの2レーン構成にしている。 [^]
  - Footnote: 記事本文に「現在のスキルは2レーン構成」とあり、本線とパイプラインの位置づけを説明。
- 機械チェックは FAIL が1つでもあれば納品しない運用として紹介されている。 [^]
  - Footnote: 記事本文に「FAILが1つでもあれば納品しない運用」と記載。
- 同じスキル資産を Claude Code とブラウザ型チャットエージェントの両方で使う構想が示されている。 [^]
  - Footnote: 記事本文に「エンジニアはClaude Codeで、現場はチャットで — 同じスキル資産を両方から使い回せます」と記載。

### References
- https://note.com/jinbaflow/n/nc8372b84e572
- https://github.com/gozen3ji/consulting-pptx-skill

## Accessing OpenAI models on Amazon Bedrock from Australia with global cross-Region inference | Artificial Intelligence
- Date: 2026-09-02T13:22:05-08:00

### Executive Summary
- AWS ブログは、オーストラリアのチームが Amazon Bedrock 経由で OpenAI GPT-5.6 系モデルを利用できるようになったと説明している。
- 対象モデルは GPT-5.6 Sol、Terra、Luna で、Sydney と Melbourne の AWS リージョンから利用できる。
- アプリケーションは現地リージョンの Bedrock Runtime エンドポイントを呼び出し、Bedrock が対応商用リージョンへ処理をルーティングする。
- Sol は高負荷な推論、コーディング、エージェント用途、Terra は性能とコストのバランス、Luna は高速・低コスト用途向けとされる。
- 3モデルはいずれもテキストと画像入力、テキスト出力、最大100万トークンのコンテキストをサポートする。
- 利用経路として Responses API、Chat Completions API、Amazon Bedrock Converse API の3種類が紹介されている。
- 記事はプロンプトキャッシュ、OIDC ベースの Codex 設定、CloudWatch と Coding Agent Insights による監視まで運用面も扱っている。

### Key Findings
- OpenAI GPT-5.6 Sol、Terra、Luna が Bedrock でオーストラリアの2リージョンから利用可能になった。 [^]
  - Footnote: 本文に「Amazon Bedrock offers OpenAI GPT-5.6 Sol, Terra, and Luna... from both Asia Pacific (Sydney) and Asia Pacific (Melbourne)」と記載。
- グローバルクロスリージョン推論により、アプリ側で処理先リージョンを管理しなくてよい。 [^]
  - Footnote: 本文に「without requiring applications to manage destination Region routing」と記載。
- 3モデルは用途別に、重い推論、汎用本番利用、高頻度・低遅延用途へ整理されている。 [^]
  - Footnote: 本文で Sol は「demanding reasoning, coding, and agentic workloads」、Terra は「balances performance and cost」、Luna は「fast, affordable inference」と説明。
- テキスト・画像入力、テキスト出力、最大100万トークンのコンテキストを共通サポートする。 [^]
  - Footnote: 本文に「All three models accept text and image inputs, generate text, and support context windows of up to 1 million tokens」と記載。
- OpenAI 互換 API と Bedrock Converse API の両方が利用経路として示されている。 [^]
  - Footnote: 本文に「Responses API, Chat Completions API, and the Converse API」と記載。
- 認証は SigV4 または Bedrock model inference API key に対応し、短期キー生成例も提示されている。 [^]
  - Footnote: 本文に「The endpoint accepts either AWS Signature Version 4 (SigV4) or an Amazon Bedrock model inference API key」と記載。
- 本番導入前にはクォータ、代表プロンプト、出力長、ストリーミング、並行数、ピークトラフィックの検証が推奨されている。 [^]
  - Footnote: 本文に「Before production rollout, request increases early, monitor quota utilization, and test representative prompts...」と記載。

### References
- https://aws.amazon.com/jp/blogs/machine-learning/accessing-openai-gpt-5-6-models-on-amazon-bedrock-from-australia-with-global-cross-region-inference/
