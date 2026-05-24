# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-24T09:10:00+09:00
- Articles: 3

## 「CAM++」を試す
- Date: 2026-05-23T14:24:23+00:00

### Executive Summary
- CAM++ は話者認証向けの軽量かつ高速なネットワークとして紹介されている。
- 記事では論文要約、3D-Speaker の位置づけ、実環境での推論手順が整理されている。
- 構成は 2D 前段 CNN、狭く深い D-TDNN、各層のマルチ粒度 CAM が中心である。
- ベンチマークでは ECAPA-TDNN より少ないパラメータと FLOPs で高い性能を示す。
- 3D-Speaker では CAM++ が選択可能なモデルアーキテクチャの一つとして扱われる。
- Proxmox 上の Ubuntu 24.04、GPU なし環境で事前学習済みモデルを試している。
- 日本語と英語の TTS 音声を使った話者類似度では、モデルによってスコア傾向が異なった。
- 著者は単純なしきい値運用には追加データでの分布確認が必要だと見ている。

### Key Findings
- CAM++ は ECAPA-TDNN 相当の性能と TDNN 相当の計算効率を狙う設計である。 [^]
  - Footnote: 記事では論文要約として「ECAPA-TDNNと同等の性能を達成しつつ、vanilla TDNNと同等の計算効率」と説明している。
- 中核構成は FCM、D-TDNN、Context-Aware Masking の組み合わせである。 [^]
  - Footnote: 本文に「Front-End Convolution Module（FCM）」「D-TDNN Backbone」「CAM（Context-Aware Masking）」の2段構成と記載されている。
- VoxCeleb1-O では EER 0.73%、ECAPA-TDNN より相対 18% 良いと整理されている。 [^]
  - Footnote: 性能欄に「VoxCeleb1-O で EER 0.73%」「ECAPA-TDNN より EER が18%相対的に良い」とある。
- 計算面では CAM++ が 7.18M parameters、1.72G FLOPs、RTF 0.013 とされる。 [^]
  - Footnote: 表3の要約として「7.18M params」「1.72G FLOPs」「RTF 0.013（CPUシングルスレッド）」が列挙されている。
- 3D-Speaker では CAM++、ERes2Net、ECAPA-TDNN など複数の学習レシピが提供される。 [^]
  - Footnote: GitHub README 抜粋として「CAM++、ERes2Net、ERes2NetV2、ECAPA-TDNN、ResNet、およびRes2Netの学習レシピ」と記載されている。
- GPU なし環境でも CAM++ の埋め込み抽出と類似度算出は実行できている。 [^]
  - Footnote: 実行ログに「No cuda device is detected. Using cpu.」「The extracted embedding」「Computing the similarity score」とある。
- 中英混在モデルでは Alloy 同一音声の日本語・英語が 0.5358、Sage 同一音声の日本語・英語が 0.6805 だった。 [^]
  - Footnote: 比較表に「Alloy・日本語 / Alloy・英語 0.5358」「Sage・日本語 / Sage・英語 0.6805」と記載されている。
- 中国語汎用モデルでは 0.7 をしきい値にすれば一応可能という暫定評価になっている。 [^]
  - Footnote: モデル変更後の表に続けて「まあ 0.7 をしきい値にすれば一応できなくはないかな」と述べている。

### References
- https://zenn.dev/kun432/scraps/9ad61aa83b8405

## 高速なTTSサービス「Cartesia Sonic 3.5」を試す
- Date: 2026-05-23T06:09:25+00:00

### Executive Summary
- Cartesia Sonic 3.5 の品質、価格、速度、リアルタイム TTS 機能を試した記事である。
- Artificial Analysis の TTS Arena で高評価を得たことが導入の動機になっている。
- Sonic 3.5 は 42 言語、日本語、500 以上の音声、音声クローンなどに対応すると整理されている。
- 料金プランとクレジット消費の目安がまとめられ、商用利用は Pro 以上が必要そうだと示されている。
- Python SDK と WebSocket を使い、テキスト入力と音声出力をストリーミングするサンプルを実装している。
- Continuations により LLM のストリーミング出力を TTS に順次渡しつつ文脈を保てる点を重視している。
- 日本語音声の種類や Featured Voices の有無も確認し、用途に応じた音声選択が必要だと述べている。
- 入力チャンクを細かく渡しても自然なイントネーションに近づける用途が期待されている。

### Key Findings
- Sonic 3.5 は TTS Arena で Elo 1,218 とされ、Inworld と Gemini Flash TTS を上回ると紹介されている。 [^]
  - Footnote: 記事冒頭に「Eloスコア1,218」「Inworld Realtime TTS 1.5 Maxの1,194とGemini 3.1 Flash TTSの1,209を上回っています」とある。
- 価格は $39/1M 文字で、比較対象より高めのプレミアム価格とされる。 [^]
  - Footnote: 主なポイントで「Sonic-3.5は$39/1M文字」と記載し、Gemini と Inworld の価格と比較している。
- Sonic 3.5 は 42 言語、日本語、500 以上の声に対応すると整理されている。 [^]
  - Footnote: サービス概要に「42言語サポート（日本語含む）」、冒頭に「500以上の声がすぐに利用可能」とある。
- Cartesia の強みは出力だけでなく入力ストリーミングにも対応するリアルタイム性である。 [^]
  - Footnote: 本文に「出力のストリーミングだけでなく、当時は珍しい入力のストリーミングにも対応」と記載されている。
- Continuations はテキストチャンク間の文脈を維持し、自然さと低レイテンシーを両立するための要素である。 [^]
  - Footnote: 本文に「Continuations という機能で、コンテキストを維持することで自然で高速な音声生成」とある。
- Quickstart では Python SDK の cartesia 3.0.2 と websockets 15.0.1 を使っている。 [^]
  - Footnote: セットアップ出力に「cartesia==3.0.2」「websockets==15.0.1」と記載されている。
- サンプル実行では最初の音声チャンクをおよそ 400ms 程度で受信できたと観察している。 [^]
  - Footnote: ログ説明に「最初の音声は400msぐらいで受信できている」とある。
- 日本語音声は 22 種類あり、そのうち Featured アイコン付きは 7 種類だったと確認している。 [^]
  - Footnote: 音声選択の節に「日本語の音声は22種類」「Featuredアイコンが付いているものは7種類」とある。

### References
- https://zenn.dev/kun432/scraps/5e977a45ac90c4

## 「BitCPM-CANN」を試す
- Date: 2026-05-22T15:25:06+00:00

### Executive Summary
- BitCPM-CANN の概要、モデル種別、GGUF 推論、実行結果を確認した記事である。
- BitCPM-CANN は Ascend NPU 上の 1.58 ビット三値モデル訓練システムとして紹介されている。
- 0.5B、1B、3B、8B のモデルファミリーがあり、OpenBMB から公開されている。
- 著者は推論用途では GGUF の TQ2_0 を使うのが本来の省メモリ用途に近いと整理している。
- モデルカードでは 1B 以上がフル精度比 95.7% 以上の能力保持率とされる。
- Ubuntu 22.04 と RTX 4090 で llama.cpp を CUDA 有効でビルドして 8B GGUF を試している。
- 英語と日本語の生成は一応動作したが、速度は著者の期待ほど速くなかったようだ。
- 日本語対応はモデルカード上では明確でなく、英語・中国語中心の可能性が残る。

### Key Findings
- BitCPM-CANN はエッジ AI 向けにメモリ効率を重視した 1.58 ビット系モデルとして紹介されている。 [^]
  - Footnote: 冒頭に「エッジ対応」「BF16比で約6倍低いメモリフットプリント」と記載されている。
- モデルサイズは 0.5B、1B、3B、8B の 4 種類がある。 [^]
  - Footnote: 本文に「モデルは、0.5B / 1B / 3B / 8B の4つのパラメータサイズ」とある。
- 未量子化 QAT チェックポイントは直接推論向けではなく、疑似量子化版が推奨されている。 [^]
  - Footnote: 引用部に「このモデルは直接的な推論用途には適していません」「擬似量子化版のopenbmb/BitCPM4-CANN-8Bをご使用ください」とある。
- GGUF では BF16 と TQ2_0 があり、著者は TQ2_0 を試すべき形式と見ている。 [^]
  - Footnote: 本文に「GGUFには BF16 TQ2_0 の2つ」「試すとしたら、GGUFのTQ2_0 を使う」とある。
- 1B、3B、8B の三値モデルはフル精度性能の 95.7% から 97.2% を保持するとされる。 [^]
  - Footnote: モデルカード抜粋に「1B/3B/8Bモデルはいずれもフル精度時の性能の95.7%～97.2%を維持」と記載されている。
- 三値 QAT の訓練スループット低下は Ascend 910B 上で約 5% とされる。 [^]
  - Footnote: 概要に「QATの導入による訓練スループットのオーバーヘッドはわずか5%」とある。
- 実行環境では llama.cpp を GGML_CUDA=ON でビルドし、openbmb/BitCPM4-CANN-8B-gguf:TQ2_0 を指定している。 [^]
  - Footnote: コマンド例に「cmake -B build -DGGML_CUDA=ON」と「-hf openbmb/BitCPM4-CANN-8B-gguf:TQ2_0」がある。
- 英語生成では Prompt 47.3 t/s、Generation 21.6 t/s と表示され、著者は速くないと感じている。 [^]
  - Footnote: 実行結果に「[ Prompt: 47.3 t/s | Generation: 21.6 t/s ]」とあり、その後「むしろ遅い？」と述べている。

### References
- https://zenn.dev/kun432/scraps/9f0a86c12d7b94
