# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-08-07T09:05:19.2394633+09:00
- Articles: 3

## Inside vLLM: Anatomy of a High-Throughput LLM Inference System - Aleksa Gordić
- Date: 2025-08-29

### Executive Summary
- vLLM を題材に、高スループットな LLM 推論システムの構成要素を俯瞰する記事である。
- シリーズ第 1 回として、詳細に入る前に全体像を作る構成になっている。
- 対象は vLLM の V1 エンジンで、V0 は非推奨として扱われている。
- エンジン、スケジューラ、KV キャッシュ、連続バッチングが中心テーマである。
- 単一 GPU のオフライン同期実行から、オンライン・非同期・分散実行へ拡張する流れを説明している。
- KV キャッシュ管理と paged attention が推論性能の核として位置づけられている。
- 後続記事では高度機能、スケールアウト、サービング層、ベンチマークを詳述する予定である。

### Key Findings
- 記事は vLLM の高スループット推論システムを段階的に分解して説明する導入編である。 [^]
  - Footnote: 本文に「gradually introduce all of the core system components and advanced features」とあり、vLLM の仕組みを分解すると説明している。
- 扱う対象は V1 エンジンであり、V0 は理解には有用だが非推奨として位置づけられている。 [^]
  - Footnote: Notes に「I'll focus on the V1 engine」「V0 (now deprecated)」と記載されている。
- 推論エンジンは、設定、入力処理、エンジンコア、出力処理から構成される。 [^]
  - Footnote: 本文の LLM Engine constructor で「vLLM config」「processor」「engine core client」「output processor」を主要コンポーネントとして挙げている。
- エンジンコアにはモデル実行器、構造化出力管理、スケジューラが含まれる。 [^]
  - Footnote: 本文に「Engine core itself is made up of several sub components」として Model Executor、Structured Output Manager、Scheduler が列挙されている。
- KV キャッシュマネージャは paged attention の中心で、利用可能な KV ブロックのプールを管理する。 [^]
  - Footnote: 本文に「KV cache manager - the heart of paged attention」「maintains a free_block_queue」とある。
- 同期エンジンでも連続バッチングの基本は支えられるが、新規リクエスト注入は非同期エンジンで扱う。 [^]
  - Footnote: 本文に「asynchronous engine supports this (aka continuous batching)」および同期例では新規リクエストを途中投入しないと説明されている。

### References
- https://www.aleksagordic.com/blog/vllm
- https://ai-news.dev/

## AI使い自然界にないウイルスを作成　米スタンフォード大学が成果発表 - 日本経済新聞
- Date: 2026-08-06T21:24:36.000Z

### Executive Summary
- 米スタンフォード大学が AI を使い、自然界にない新たなウイルス作成に成功したと発表した。
- AI がゲノム配列全体を設計し、その機能を確認できた初の事例とされる。
- 研究対象は感染症の原因になる細菌を殺すファージに関するものとして説明されている。
- 成果は医療や創薬の進歩につながる可能性がある。
- 一方で、バイオ兵器などへの悪用懸念が明示されている。
- 専門家コメントでは、AI 設計と自動化ラボの組み合わせが研究サイクルを短縮し得ると指摘されている。
- Evo 2 はヒト感染ウイルスの DNA 配列を学習データから除外したが、オープンウェイトゆえの追加学習リスクが残るとされる。

### Key Findings
- スタンフォード大学は AI による新規ウイルス作成の成功を発表した。 [^]
  - Footnote: 公開本文に「米スタンフォード大は6日、人工知能（AI）を使って自然界にない新たなウイルスを作成することに成功したと発表」とある。
- 生成 AI がゲノム配列全体を設計し、機能確認まで行えた初の事例と説明されている。 [^]
  - Footnote: 公開本文に「ゲノム（全遺伝情報）の配列全体を設計し、機能を確認できた初の事例」と記載されている。
- 研究は細菌を殺すファージを対象にしている。 [^]
  - Footnote: 公開本文に「感染症の原因などになる細菌を殺す『ファージ...』」と表示されている。
- 医療応用の可能性とバイオ兵器化のリスクが同時に示されている。 [^]
  - Footnote: 公開本文に「医療の進歩につながる一方、バイオ兵器など悪用懸念もある」とある。
- 専門家は、AI 設計と自動化ラボの閉ループ化により創薬とバイオリスクが同時に加速すると見ている。 [^]
  - Footnote: 比屋根一雄氏の解説に「創薬とバイオリスクが同時に加速します」とある。
- Evo 2 は安全性のためヒト感染ウイルス DNA 配列を学習データから除外したが、追加学習リスクは残る。 [^]
  - Footnote: 解説に「ヒト感染ウイルスのDNA配列を学習データから除外」「オープンウェイトなので、追加学習のリスクは残ります」とある。

### References
- https://www.nikkei.com/article/DGXZQOGN070020X00C26A8000000/
- https://ai-news.dev/

## ChatGPT、FreeおよびGoプランのテキストチャット制限を撤廃。「GPT-5.6 Luna」を標準モデルに採用 | テクノエッジ TechnoEdge
- Date: 2026-08-07T07:00:03+09:00

### Executive Summary
- OpenAI が ChatGPT の Free および Go プランで、テキストチャットの利用制限を撤廃すると発表した。
- ファイル添付、画像添付、音声機能、画像生成には引き続き別の制限が残る。
- Free と Go では GPT-5.6 Luna がデフォルトモデルになり、従来の GPT-5.5 から置き換わる。
- 複雑な質問向けに、より熟考した回答を生成する Think ボタンが追加される。
- Plus と Pro には GPT-5.6 Sol のアップデート版が提供される。
- OpenAI の内部評価では、GPT-5.5-Instant 比で Luna は 62%、Sol は 68% 事実誤りを減らしたとされる。
- Sol は Plus・Pro 向けに提供開始済みで、Luna と Think は今週中、無制限化は来週予定とされる。

### Key Findings
- Free と Go のテキストベースチャット制限が撤廃される。 [^]
  - Footnote: 本文に「FreeプランおよびGoプランユーザーを対象に、テキストベースのチャットに設けていた利用制限を撤廃」とある。
- 制限撤廃の対象外として、ファイル、画像、音声、画像生成は別制限のまま残る。 [^]
  - Footnote: 本文に「ファイルや画像の添付、音声機能、画像生成については引き続き別途の利用制限」と記載されている。
- Free と Go の標準モデルは GPT-5.6 Luna に切り替わる。 [^]
  - Footnote: 本文に「新たに『GPT-5.6 Luna』がデフォルトモデルとして採用され、これまでのGPT-5.5から置き換え」とある。
- Think ボタンにより、複雑な質問で熟考型の回答生成を使えるようになる。 [^]
  - Footnote: 本文に「複雑な質問に対してモデルがより熟考して回答を生成する『Think』ボタン」と説明されている。
- Plus・Pro には GPT-5.6 Sol の更新版と、思考量を調整するスライダーが提供される。 [^]
  - Footnote: 本文に「Plus・Proユーザーに対しては...『GPT-5.6 Sol』のアップデート版」「思考量を...調整できるスライダー機能」とある。
- 内部評価では、事実誤りが Luna で 62%、Sol で 68% 減少したとされる。 [^]
  - Footnote: 本文に「GPT-5.6 Lunaでは事実誤りが62%、GPT-5.6 Solでは68%それぞれ減少」と記載されている。

### References
- https://www.techno-edge.net/article/2026/08/07/5370.html
- https://ai-news.dev/
