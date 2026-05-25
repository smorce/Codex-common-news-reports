# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-25T09:01:28.8210161+09:00
- Articles: 3

## 「LLM-jp-4-VL / Jagle-VL」 を試す
- Date: 2026-05-24T14:47:27+00:00

### Executive Summary
- LLM-jp-4-VL 9B beta と Jagle-VL 系モデルの概要、学習データ、実行例を整理している。
- LLM-jp-4-VL は llm-jp-4-8b-instruct を基盤にした 9B 規模の視覚言語モデルとして紹介されている。
- 視覚エンコーダには SigLIP2 so400M、プロジェクタには 2 層 MLP を使う構成が説明されている。
- 学習データは FineVision と Jagle の混合で、Jagle は日本語マルチモーダル事後学習データセットとして位置付けられている。
- 評価では日本語タスク平均で Qwen3-VL-8B-Instruct と同等水準を、より少ない後学習トークンで達成したとされる。
- Colaboratory L4 上での実行例では、モデルロード直後の VRAM 消費が約 17.6GB と記録されている。
- テキスト、単一画像、複数画像、OCR 的な処理など複数の推論例が掲載されている。
- モデル自体は Apache License 2.0 とされる一方、FineVision 由来データやプロプライエタリモデル出力の扱いには注意が必要と述べている。

### Key Findings
- LLM-jp-4-VL 9B beta は日本語向けの視覚言語モデルとして紹介されている。 [^]
  - Footnote: 記事本文に「LLM-jp-4-VL 9B betaは、LLM-jpが開発した視覚言語モデルです」とある。
- モデルは LLM、視覚エンコーダ、軽量プロジェクタの 3 要素で構成される。 [^]
  - Footnote: 本文で「言語モデル、視覚エンコーダ、および軽量プロジェクタから構成」と説明され、LLM は llm-jp/llm-jp-4-8b-instruct、視覚エンコーダは google/siglip2-so400m-patch16-512 とされている。
- 高解像度画像への対応として動的タイリング方式を採用している。 [^]
  - Footnote: 本文に「各画像をそのアスペクト比に応じて適応的にタイル分割」し、画像トークンとして連結するとある。
- 学習データは FineVision 2420 万サンプルと Jagle 920 万サンプルの混合で構成される。 [^]
  - Footnote: 本文の学習データ欄に「FineVision（2420万サンプル）」「Jagle（920万サンプル）」と記載されている。
- 学習は 90,000 ステップ、約 3 エポック、総 1800 億トークンで実施された。 [^]
  - Footnote: 本文に「90,000ステップ（約3エポックに相当、画像トークンを含む総トークン数は1800億トークン）」とある。
- 日本語評価では Qwen3-VL-8B-Instruct と同等の平均性能を、少ない後学習トークンで達成したとされる。 [^]
  - Footnote: 本文に「10種類の日本語タスクにおいて平均的にQwen3-VL-8B-Instructと同等の性能」「Qwen3-VLが2兆トークン以上使用するのに対し、本モデルでは1800億トークン」とある。
- Colaboratory L4 でのロード後 VRAM 消費は約 17.6GB と報告されている。 [^]
  - Footnote: 実行ログの前に「この時点でのVRAM消費は約17.6GB程度」と記載されている。
- ライセンス面では Apache 2.0 とされるが、学習元データの条件確認が必要と指摘している。 [^]
  - Footnote: 本文に「本モデルの学習に使用したFineVisionは...一部のデータには、OpenAIやAnthropicなどのクローズドソースモデル...出力データが含まれている場合」とあり、著者は「ライセンスの判斷はちょっと注意が必要」と述べている。

### References
- https://zenn.dev/kun432/scraps/9094e75e32e740
- https://huggingface.co/llm-jp/llm-jp-4-vl-9b-beta
- https://huggingface.co/llm-jp/Jagle-VL-2.2B-Jagle-FineVision

## メモ: human-in-the-loop を OpenAI Chat Completions API でやってみる
- Date: 2026-05-24T12:26:59+00:00

### Executive Summary
- OpenAI Chat Completions API の tool calling を使い、human-in-the-loop の承認処理を試したメモである。
- 最初の例では天気取得ツールを定義し、モデルがツール呼び出しを要求したあと、人間が実行可否を入力する。
- ツール実行の結果は role: tool のメッセージとして会話履歴に戻され、その後に最終応答を生成する。
- 次の例ではツールごとに ask フラグを持たせ、天気取得は自動実行、メール送信は承認必須に分けている。
- 承認拒否時は tool_execution_denied をツール結果として返す設計になっている。
- 著者は、承認処理そのものはアプリケーション側に実装され、モデル側はツール実行結果として知るだけだと整理している。
- 後半では承認をより自然言語的に行わせるパターンへ発展させようとしている。
- 副作用のある操作ほど、ツール定義と実行ループ側で承認ポリシーを明示する必要があることが示されている。

### Key Findings
- サンプルは OpenAI Python SDK 2.38.0 と gpt-4.1-mini を使っている。 [^]
  - Footnote: 本文に「Successfully installed openai-2.38.0」とあり、コードで `MODEL = "gpt-4.1-mini"` と定義している。
- 天気取得ツールは function calling の tools 配列として定義されている。 [^]
  - Footnote: 本文のコードで `tools = [{"type": "function", "function": {"name": "get_weather"...}}]` と定義されている。
- モデルから tool_calls が返った場合、関数名と引数を表示し、人間に実行確認している。 [^]
  - Footnote: コードに「[ツール要求]」「名前」「引数」を表示し、`input("このツールを実行しますか？ [y/N]")` で確認する処理がある。
- 承認された場合のみローカルの tool_mapping から実関数を呼び出す。 [^]
  - Footnote: 本文コードで `if answer in {"y", "yes"}:` の後に `tool_func = tool_mapping.get(function_name)`、`tool_func(**function_args)` を実行している。
- 承認拒否は例外ではなく、ツール結果としてモデルに返す設計である。 [^]
  - Footnote: コードに `tool_result = {"error": "tool_execution_denied", "tool_name": function_name, "arguments": function_args}` とある。
- ツールごとの承認要否は ToolDef の ask フラグで切り替えている。 [^]
  - Footnote: 本文の第二パターンで `class ToolDef(TypedDict): func... ask: bool` とし、`get_weather` は `ask: False`、`send_email` は `ask: True` としている。
- 副作用のあるメール送信は承認必須ツールとして扱われている。 [^]
  - Footnote: 第二パターンの `tool_mapping` で `send_email` に `ask: True` が設定され、実行例でもメール送信前に承認入力が表示されている。
- 著者は承認処理をアプリケーション側の責務として整理している。 [^]
  - Footnote: 本文に「承認処理そのものはアプリケーション側で実装している。つまりモデル側のループではそれをほとんど意識せず」とある。

### References
- https://zenn.dev/kun432/scraps/fd750c03716a5e

## LiveKit Agent で human-in-the-loop
- Date: 2026-05-24T06:33:42+00:00

### Executive Summary
- LiveKit Agent における human-in-the-loop パターンを、公式記事の要約と著者の考察で整理している。
- HITL は AI が大半を処理し、高リスク・複雑・感情的なケースだけ人間に確認させる設計として説明されている。
- 中核原則は propose → commit で、AI は提案し、人間が最終確定するという役割分担である。
- エスカレーション判断にはリスク、信頼度、複雑さ、法規制、感情、ドメイン外トピックなどが挙げられている。
- 音声エージェントでは同期的な Blocking HITL が主役で、ユーザーを待たせる間の体験設計が重要になる。
- 文脈引き継ぎの失敗を避けるため、会話ログ・意図・エンティティ・センチメントなどを evidence pack として渡すべきだとしている。
- LiveKit の WarmTransferTask は相談用ルーム作成、上司呼び出し、chat_ctx に基づく状況説明、参加者移動までを担うプリミティブとして紹介されている。
- 最後に著者は、一般的なツール実行前承認の実装では session.userdata にデータクラスを使う案がよさそうだとメモしている。

### Key Findings
- HITL は AI が提案し、人間が確定する propose → commit 型の設計として整理されている。 [^]
  - Footnote: 本文に「記事のキモは『propose → commit（提案 → コミット）』」「AIはコミットしない、必ず人間がコミットする」とある。
- 高額返金、法規制、感情的な顧客対応などは人間へのエスカレーション候補である。 [^]
  - Footnote: 本文の基準に「5,000ドル返金要求」「KYC、GDPRのデータ要求、医療・支払い関連」「相手がめっちゃイライラしてる」などが挙げられている。
- HITL アーキテクチャは Blocking と Non-blocking に分けて説明されている。 [^]
  - Footnote: 本文に「Blocking（同期）」「Non-blocking（非同期）」の 2 種類があり、音声エージェントでは「基本は同期HITLが主役」とある。
- 文脈引き継ぎの失敗は HITL UX の大きな問題として扱われている。 [^]
  - Footnote: 本文に「一番多いUXの失敗：『また最初から説明させられる』」とあり、これは「文脈引き継ぎ（コンテキストパッシング）の設計ミス」と説明されている。
- evidence pack には会話要約、全文ログ、意図と信頼度、抽出エンティティ、センチメントなどを含めるべきだとしている。 [^]
  - Footnote: 本文で evidence pack の内容として「会話全文のタイムスタンプ付きログ」「意図とその信頼度」「抽出されたエンティティ」「センチメント」などが列挙されている。
- LiveKit の WarmTransferTask はユーザー保留、相談ルーム、SIP 呼び出し、参加者移動を含む実装要素として紹介されている。 [^]
  - Footnote: 本文に「ユーザーをホールド状態にする」「別の『相談用ルーム』を作る」「上司をSIPアウトバウンドで...呼び出す」「MoveParticipantで移動」とある。
- LLM には function_tool の説明文で、エスカレーションすべき条件を教える構成が示されている。 [^]
  - Footnote: 本文に「HITLのトリガーは@function_toolとして定義」「ツールの説明文の中に...条件を書いておく」とある。
- HITL は学習データを蓄積し、時間とともにエスカレーション率を下げるループとしても説明されている。 [^]
  - Footnote: 本文に「AIが出した案」「人間が修正した最終回答」「元のユーザーの質問」がラベル付きデータになり、「1ヶ月目：30%」「3ヶ月目：15%」「6ヶ月目：5%」とある。

### References
- https://zenn.dev/kun432/scraps/c52d5b6c202be0
