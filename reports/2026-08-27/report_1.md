# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-08-27T09:00:00+09:00
- Articles: 3

## llama.cppの「inception」パターン
- Date: 2026-08-27T02:58:00+09:00

### Executive Summary
- llama.cpp の reasoning 関連オプションと「inception」パターンを扱うスクラップ。
- 発端は llama.cpp 作者 Georgi Gerganov 氏の Qwen3.8-27B リリース時の投稿。
- inception パターンは、推論が長く続く場合に追加メッセージを注入して行動を促す方法として紹介されている。
- 具体的には --reasoning-budget と --reasoning-budget-message の組み合わせが示されている。
- Qwen3.8-27B-GGUF を llama serve で動かす simple/advanced/DGX Spark 向け例も参照されている。
- 著者は --reasoning on/off と同時期に追加された PR を確認している。
- 従来の --chat-template-kwargs による thinking 制御は deprecated 扱いの可能性があると整理している。

### Key Findings
- inception パターンはエージェント用途で、推論しすぎるモデルに行動を促すための手法として位置づけられている。 [^]
  - Footnote: 記事本文に「指定した推論予算の後に思考を注入することで、モデルが長く考えすぎたときにアクションを取るよう強制できます」とある。
- 仕様が曖昧なタスクでモデルが過度に推論する問題への対処が主眼になっている。 [^]
  - Footnote: 記事本文に「モデルが過度に長く推論してしまう、仕様不足のタスクに対処するのに役立ちます」とある。
- 推論長の制限には --reasoning-budget 4096 と --reasoning-budget-message の利用例が示されている。 [^]
  - Footnote: 記事中の引用に「--reasoning-budget 4096」「--reasoning-budget-message」が掲載されている。
- Qwen3.8-27B-GGUF では draft-mtp 指定で llama serve を起動する例が複数示されている。 [^]
  - Footnote: 埋め込み投稿に「llama serve -hf ggml-org/Qwen3.8-27B-GGUF --spec-type draft-mtp」とある。
- advanced 例では --spec-default、--reasoning-preserve、--agent も併用されている。 [^]
  - Footnote: 埋め込み投稿に「--spec-default」「--spec-type draft-mtp」「--reasoning-preserve --agent」とある。
- reasoning 関連の新オプションは llama.cpp の PR #20297 で追加されたものとして参照されている。 [^]
  - Footnote: 記事本文に「以下のPRで --reasoning on/off といっしょに追加されてたみたい」とあり、GitHub PR 20297 がリンクされている。
- thinking の有効無効を --chat-template-kwargs で行う使い方は、少なくとも reasoning 制御用途では deprecated と見られている。 [^]
  - Footnote: 記事本文に「--chat-template-kwargs '{"enable_thinking":false}' は、一応 deprecated になってるし」とある。

### References
- https://zenn.dev/kun432/scraps/b2089a4ea8ec4e
- https://github.com/ggml-org/llama.cpp/pull/20297
- https://twitter.com/ggerganov/status/2089214161884414147

## メモ: Breeze TTS 2
- Date: 2026-08-26T21:33:00+09:00

### Executive Summary
- Breeze TTS 2 の公式情報、モデルカード、ランキング、ライセンスを確認したスクラップ。
- Artificial Analysis の Provider Voices Speech Arena では Open Weights TTS モデル中1位と紹介されている。
- Fish Audio S2 Pro に対して Provider Voices で 90 Elo ポイントのリードがある。
- 公式ブログでは Voice Design、Voice Direction、Low Latency、Multilingual Speech が主要価値として整理されている。
- モデル重みと PyTorch 推論コードは 2026年8月25日に公開されたとされる。
- モデルカードでは 40ms 未満の初回音声出力や 0.32 RTF など低遅延性が強調されている。
- 一方で、モデル重みは研究・非商用ライセンスで、商用利用には別途許可が必要な点を著者は懸念している。

### Key Findings
- Breeze TTS 2 は Provider Voices で Open Weights TTS モデル中1位、全体6位と紹介されている。 [^]
  - Footnote: 記事本文に「Open Weights TTS モデルの中で #1」「全体で 100 以上のモデル中 #6」「Elo スコアは 1,215」とある。
- Provider Voices では Fish Audio S2 Pro を 90 Elo ポイント上回るとされる。 [^]
  - Footnote: 記事本文に「Fish Audio S2 Pro を 90 Elo ポイント上回り」とある。
- Controlled Voices では Open Weights TTS モデル中3位で、Voxtral TTS や Fish Audio S2 Pro が上位にある。 [^]
  - Footnote: 記事本文に「Controlled Voices: Breeze TTS 2 は Open Weights TTS モデルの中で #3」とあり、上位モデルとして Voxtral TTS と Fish Audio S2 Pro が挙げられている。
- 価格は BreezeBlue ホストエンドポイントで 1M 文字あたり $34 とされ、Fish Audio S2 Pro より高い。 [^]
  - Footnote: 記事本文に「1M 文字あたり $34」「Fish Audio S2 Pro（1M 文字あたり $15）より高価」とある。
- 公式ブログは、声のデザイン、演技指示、低レイテンシ、多言語対応を中核機能としている。 [^]
  - Footnote: 記事本文に「Voice Design」「Voice Direction」「Low Latency」「Multilingual Speech」が必要な4つのポイントとして列挙されている。
- Hugging Face では 2026年8月25日にモデル重みと PyTorch 推論コードが公開されたと記載されている。 [^]
  - Footnote: 記事本文に「[2026年8月25日] Breeze TTS 2 モデルの重みデータと PyTorch推論コードをオープンソースとして公開しました」とある。
- 低遅延性能として、H100 上の高速パスで初回音声出力 40ms 未満、RTF 0.32 が示されている。 [^]
  - Footnote: 記事本文に「最初の音声出力まで40ミリ秒未満」「0.32のリアルタイム係数（RTF）」とある。
- 商用利用には注意が必要で、モデル材料は研究目的および非商用利用に限定される。 [^]
  - Footnote: 記事本文に「モデルの重みデータ、派生モデル、およびセルフホスト環境での出力は、研究目的および非商用利用に限定」とある。

### References
- https://zenn.dev/kun432/scraps/0babe532fe9a4a
- https://breezeblue.ai/breeze-tts-2
- https://huggingface.co/BreezeBlue/Breeze-TTS-2

## 「LLM-jp-4」 を試す（33B）
- Date: 2026-08-25T18:10:00+09:00

### Executive Summary
- LLM-jp-4 33B の公開情報とローカル試用結果をまとめたスクラップ。
- LLM-jp は約332億パラメータの Dense 型モデルとして 33B を公開した。
- 公開対象は base と thinking の2種類で、DPO 用データセットも案内されている。
- 著者は以前の 32B-A3B との違いとして、今回は Dense 型である点に注目している。
- 外部の推論性能比較では Qwen3.8-27B と明確な優劣を付けにくいとの評価が引用されている。
- 著者の試用では日本語品質に期待を示しつつ、エージェント用途では不安定さも見ている。
- temperature を低くすると日付回答などの誤りが減ると観察し、エージェント設定との相性に課題を感じている。

### Key Findings
- LLM-jp-4 33B は約332億パラメータの Dense 型 LLM として公開された。 [^]
  - Footnote: 埋め込み投稿と記事本文に「約332億パラメータのDense型LLM『LLM-jp-4 33B』」とある。
- 公開モデルはベースモデルと事後学習済み thinking モデルの2種類である。 [^]
  - Footnote: 記事本文に「llm-jp-4-33b-base」と「llm-jp-4-33b-thinking」が公開対象として記載されている。
- 事後学習済みモデルは SFT と DPO によるアライメントを行い、強化学習は行っていない。 [^]
  - Footnote: 記事本文に「教師ありファインチューニング（SFT）と直接的選好最適化（DPO）によるアライメント処理を実施しており、強化学習は行っていません」とある。
- 以前公開された LLM-jp-4 8B と 32B-A3B に続く新モデルとして位置づけられている。 [^]
  - Footnote: 記事本文に「2026年4月には、Dense型の『LLM-jp-4 8B』モデルと、Mixture of Experts（MoE）型の『LLM-jp-4 32B-A3B』モデルを公開」とある。
- 第三者比較では Qwen3.8-27B と一方を明確に優れるとは言いにくいとの評価が紹介されている。 [^]
  - Footnote: 埋め込み投稿に「少なくとも今回の問題群からは、どちらか一方を明確に優れたモデルと言うことは難しい」とある。
- 著者の試用では日付回答で誤答があり、temperature 0 では正答する例が示されている。 [^]
  - Footnote: 記事本文に、temperature デフォルト時は 2027年1月7日と誤答し、--temp 0 では「2026年8月26日（水曜日）」と回答したログがある。
- 著者は 0.05 程度まで temperature を下げると誤りが減ったと観察している。 [^]
  - Footnote: 記事本文に「0.05 ぐらいにしたら、間違えることがなくなったように思える」とある。
- 日本語性能には好印象がある一方、エージェント用途にはまだ課題があると結論づけている。 [^]
  - Footnote: 記事本文に「日本語はかなり安心して使える印象」「エージェントに適したフォーマットは使用されてるが、モデル自体はまだそこまでは届いてない」とある。

### References
- https://zenn.dev/kun432/scraps/22c57c093bd516
- https://llm-jp.nii.ac.jp/news/20260818/
- https://huggingface.co/llm-jp/llm-jp-4-33b-thinking
