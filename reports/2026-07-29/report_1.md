# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-29T09:01:32+09:00
- Articles: 3

## メモ: 量子化時のキャリブレーションファイル
- Date: 2026-07-28T10:07:43+00:00

### Executive Summary
- APEX Quant が Wikipedia ではなく実用タスク寄りの独自キャリブレーションデータを使う点を起点に、量子化用データの作り方を整理している。
- GPTQ では C4 から抽出した 128 個の 2048 トークン区切りを使い、タスクに依存しない少量データでキャリブレーションする事例を確認している。
- AWQ では The Pile 由来の少量サンプルを用い、活性化値が大きい入力に対応する重みを重要とみなす考え方を説明している。
- GPTQ はキャリブレーションデータの分布に合わせ込みやすく、AWQ は相対的に分布差へ強いという違いを整理している。
- 一方で AWQ 実装でも、会話データを連結して固定長分割すると特殊トークンや会話境界が崩れ、結果に影響する可能性を指摘している。
- 圧縮技術全般の論文から、同じデータソース内のランダムサンプルでも性能差が出るため、単純なランダム選択では不十分な場合があるとまとめている。
- CoverCal は外れ値チャネルを広くカバーする文章を集合被覆で選ぶ新しい手法として紹介され、ランダム選択より少量データで改善できる可能性があるとされる。
- 最終的にはキャリブレーションデータを公開し、複数セットで評価し、異常値を手動で除くなど、実測を前提に判断する必要があるという結論になっている。

### Key Findings
- APEX Quant は Wikipedia ベースではなく、チャット、コード、reasoning、ツール呼び出しなど実用タスク寄りのデータでキャリブレーションしているとされる。 [^]
  - Footnote: 本文に「Wikipediaベースのものは使用せず、実用タスク寄り（チャット、コード、reasoning、ツール呼び出し等）のデータ」とある。
- GPTQ の代表例では C4 から 128 サンプル、各 2048 トークンを抽出する少量キャリブレーションが使われている。 [^]
  - Footnote: 本文に「C4...を使用」「128個のランダムな2048トークン区切り」とある。
- GPTQ のキャリブレーションは特定タスクに依存しない汎用ウェブテキストを使うことで、評価データとの重複を避ける意図がある。 [^]
  - Footnote: 本文に「特定のタスク固有のデータを一切含まない」「真のゼロショット評価が可能」とある。
- AWQ は重みの値そのものではなく、入力時の活性化値の大きさを見て重要な重みを判断する。 [^]
  - Footnote: 本文に「活性化値が大きい場合、その重みに生じた量子化誤差が出力へ大きく影響する」とある。
- AWQ は GPTQ よりキャリブレーションデータの内容への依存が弱く、少量データで済むと整理されている。 [^]
  - Footnote: 本文に「AWQでは16サンプルで十分」「GPTQほど...分布に敏感ではなく」とある。
- 実装によっては、複数サンプルの連結と固定長再分割で会話境界や特殊トークンが崩れ、AWQ の量子化結果にも影響しうる。 [^]
  - Footnote: 本文に「会話データの境界や特殊トークンの並びが崩れ...入力フォーマットから外れてしまった」とある。
- 圧縮手法の比較では、ランダムサンプリングやデータソースの違いが性能に影響し、プルーニングは量子化より感度が高い傾向がある。 [^]
  - Footnote: 本文に「ランダムサンプリングでは不十分」「プルーニングは...感度が高く」「量子化は比較的安定」とある。
- CoverCal は外れ値チャネルを発火させる入力を選び、同じ役割の文章を避けて重要チャネルを広くカバーする発想を取る。 [^]
  - Footnote: 本文に「どの外れ値チャネルを発火させるか調べ」「集合被覆」とある。

### References
- https://zenn.dev/kun432/scraps/3bbd34602b7866
- https://www.alphaxiv.org/abs/2210.17323
- https://www.alphaxiv.org/abs/2306.00978
- https://www.alphaxiv.org/abs/2604.24008

## 「Qwen-Audio-3.0-TTS」を試す
- Date: 2026-07-27T12:36:57+00:00

### Executive Summary
- Alibaba の Qwen-Audio-3.0-TTS を、外部評価、公式情報、API 利用、ローカルからの実行例まで幅広く検証している。
- モデルは Flash と Plus の 2 系統で、Flash は低遅延、Plus は高品質という位置づけとして整理されている。
- Artificial Analysis の Speech Arena では Plus が Elo 1,236 で上位に入り、品質面の注目度が高い一方、生成速度は競合より遅めとされる。
- 公式ページの要約では、12.5 Hz の低フレームレート音声トークナイザー、5 段階学習、多言語、方言、感情、長文、ロバスト性が主要特徴として挙げられている。
- 利用経路は Alibaba Cloud Model Studio と OpenRouter が候補だが、フル機能を使うなら本家 Alibaba Cloud がよいという判断になっている。
- リアルタイム音声合成は DashScope SDK と WebSocket エンドポイントを使い、Flash と Plus の両方で日本語文の音声生成を試している。
- 自然言語の instruction やインラインタグにより、速度、声色、感情、笑い、ため息などの制御が可能で、実際に変化を確認している。
- 音声クローンは公開 URL の参照音声を API に渡して voice_id を作成し、その ID を使って合成する流れで、クローン時は生成がやや長めになると報告している。

### Key Findings
- Qwen-Audio-3.0-TTS は Flash と Plus の 2 バリエーションで提供され、低遅延と高品質の使い分けが想定される。 [^]
  - Footnote: 本文に「Flash: リアルタイム対話」「Plus: 高品質生成」とある。
- Plus は Speech Arena の Provider Voices で Elo 1,236 を記録し、Simba 3.2 を僅差で上回ったと紹介されている。 [^]
  - Footnote: 本文に「Eloスコアは1,236」「Simba 3.2の1,234を僅差で上回っています」とある。
- 品質評価は高いが、スループットは秒間 16 文字で、Simba 3.2、Gemini 3.1 Flash TTS、Sonic 3.5 より低いとされる。 [^]
  - Footnote: 本文に「秒間16文字を生成し...Simba 3.2（30.2）...Sonic 3.5（120）よりも低い」とある。
- 12.5 Hz の低フレームレート音声トークナイザーにより、音声生成時の処理ステップを減らしつつ内容と話者特徴を保持する設計が説明されている。 [^]
  - Footnote: 本文に「12.5 Hz の低フレームレートの音声トークナイザー」「処理ステップをかなり減らしてる」とある。
- 自然言語指示と 86 種類のインラインタグで、感情、間、笑い、咳払い、呼吸音などの細かい演出が可能とされる。 [^]
  - Footnote: 本文に「自然言語の指示」「インラインの細かいタグ（86種類追加）」とある。
- 公式ドキュメント上、Qwen-Audio-3.0-TTS が利用できる音声合成機能はリアルタイム音声合成と音声クローンに限られると整理されている。 [^]
  - Footnote: 本文に「リアルタイム音声合成」「音声クローン」「のみとなる」とある。
- DashScope SDK のサンプルでは Flash の初回パケット遅延が約 824 ms、Plus が約 950 ms と記録されている。 [^]
  - Footnote: 本文の出力例に「初回パケット遅延: 823.805908203125 ms」「949.994140625 ms」とある。
- 音声クローンでは 10〜20 秒推奨、最大 60 秒、10MB 以下、16kHz 以上などの参照音声条件が示されている。 [^]
  - Footnote: 本文の音声ファイル要件に「推奨10～20秒、最大60秒」「10MB以下」「16kHz以上」とある。
- クローン音声の生成では voice_id を使い、実測では初回パケット遅延が約 1126 ms と通常合成よりやや長めだった。 [^]
  - Footnote: 本文に「クローンの場合は生成時間がちょっとだけ長め」「初回パケット遅延: 1126.4912109375 ms」とある。

### References
- https://zenn.dev/kun432/scraps/04ff5d177b1cc4
- https://funaudiollm.github.io/qwen-audio-3.0-tts/
- https://www.alibabacloud.com/help/en/model-studio/tts-model/
- https://www.alibabacloud.com/help/en/model-studio/realtime-tts-user-guide
- https://www.alibabacloud.com/help/en/model-studio/voice-cloning-user-guide

## 「Inflect-Micro-v2 / Inflect-Nano-v2」を試す
- Date: 2026-07-28T02:52:52+00:00

### Executive Summary
- ローカル TTS ベンチマーク tts-bench を起点に、軽量モデル Inflect-Micro-v2 と Inflect-Nano-v2 を試している。
- tts-bench は TTFA、RTFx、メモリ使用量、音声試聴、UTMOS、WER、SIM などを通じてローカル TTS モデルを比較する仕組みとして紹介されている。
- Inflect 系は 2026 年 7 月リリースの英語向けプリセット音声モデルで、Nano は 396 万、Micro は 936 万パラメータ、Apache 2.0 ライセンスと整理されている。
- もともとの Inflect-Nano v1 は、4.63M パラメータで人間の声として成立する限界を探る実験的モデルとして説明されている。
- v2 では英語のみ、男性音声 1 種類のみという制限が残るが、将来的な言語追加、音声バリエーション、安定性向上への期待が述べられている。
- Colaboratory T4 で Hugging Face からモデルをダウンロードし、同梱の requirements と inference.py を使って Nano と Micro を実行している。
- Nano-v2 は CPU で約 607 ms、GPU で約 61 ms、Micro-v2 は CPU で約 1.32 秒、GPU で約 82 ms という実測が示されている。
- 著者は v1 と間違えて試した際の印象から、Nano-v2 ではロボット感が減り、CPU でも速そうだと評価している一方、日本語対応には追加作業が必要と見ている。

### Key Findings
- tts-bench は処理速度、音声確認、評価スコアの 3 観点でローカル TTS モデルを比較するベンチマークとして紹介されている。 [^]
  - Footnote: 本文に「3つの主要な評価指標」「処理速度」「音声確認」「評価スコア」とある。
- ベンチマークは TTFA、RTFx、メモリ使用量、CPU/CUDA/Apple Silicon の各環境での性能を測る。 [^]
  - Footnote: 本文に「TTFA」「RTFx」「メモリ使用量」「CPU/CUDA/Apple Silicon環境でのパフォーマンス」とある。
- 品質評価では UTMOS、WER、SIM が補助指標になり、主観的な聴取比較も重視されている。 [^]
  - Footnote: 本文に「UTMOS（自然さ）、WER（理解可能性）、SIM（クローン精度）」と「最終的な判断基準となるのはあなたの耳」とある。
- Inflect-Micro v2 は 936 万パラメータ、Inflect-Nano v2 は 396 万パラメータで、いずれも 2026 年 7 月リリース、Apache 2.0 とされる。 [^]
  - Footnote: 本文の追跡対象モデル表に「Inflect-Micro v2 936万 2026年7月 Apache 2.0」「Inflect-Nano v2 396万 2026年7月 Apache 2.0」とある。
- 現時点の Inflect v2 は英語のみ、男性音声 1 種類のみという制約がある。 [^]
  - Footnote: 本文に「英語のみ」「男性音声1種類のみ」とある。
- Inflect-Nano v1 は音響モデル約 3.46M とボコーダ約 1.17M の 2 段構成で、合計 5M 未満を守る設計思想だった。 [^]
  - Footnote: 本文に「音響モデル（約 3.46M パラメータ）」「ボコーダ（約 1.17M パラメータ）」「合計5Mパラメータ以下」とある。
- Nano-v2 の推論時間は Colab T4 で CPU 約 607 ms、GPU 約 61.2 ms と計測されている。 [^]
  - Footnote: 本文の timeit 出力に「607 ms ± 24.5 ms」「61.2 ms ± 16.6 ms」とある。
- Micro-v2 の推論時間は CPU 約 1.32 秒、GPU 約 82.3 ms と計測されている。 [^]
  - Footnote: 本文の timeit 出力に「1.32 s ± 282 ms」「82.3 ms ± 19 ms」とある。
- 著者は Nano-v2 について、v1 よりロボット的な印象が減り、CPU でも速そうだと評価している。 [^]
  - Footnote: 本文に「nano-v2に変えたら、v1のようなロボットっぽさはそんなに感じないし、CPUでも速そう」とある。

### References
- https://zenn.dev/kun432/scraps/688cef5359c0f8
- https://github.com/5uck1ess/tts-bench
- https://huggingface.co/owensong/Inflect-Nano-v2
- https://huggingface.co/owensong/Inflect-Micro-v2
