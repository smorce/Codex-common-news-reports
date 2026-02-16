# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-02-16T09:01:28+09:00
- Articles: 3

## 「FireRedVAD」を試す
- Date: 2026-02-16T03:47:00+09:00

### Executive Summary
- FireRedVAD を中心に FireRedASR2S 系モデルを確認したメモ。
- ASR・VAD・LID・Punc を統合した産業用ASRシステムと説明。
- FireRedASR2 は標準中国語で平均CER 2.89%などの数値が示されている。
- FireRedVAD は100以上の言語対応でF1 97.57%と記載。
- FireRedLID は82言語で97.18%の精度とされる。
- 2026年2月12日にモデル重みと推論コードを公開とある。
- ASRの入力長制限やApache-2.0ライセンスの注意点もメモされている。

### Key Findings
- FireRedASR2SはASR/VAD/LID/Puncを統合した産業用オールインワンASRとして説明されている。 [^]
  - Footnote: FireRedASR2Sは、最先端（SOTA）の性能を誇る産業用グレードのオールインワンASRシステムで、ASR（音声認識）、VAD（音声/非音声判定）、LID（言語識別）、Punc（句読点挿入）の各モジュールを統合しています。
- 標準中国語の4テストセット平均CER 2.89%など、FireRedASR2の指標が示されている。 [^]
  - Footnote: 標準中国語のテストセット4種類における平均CERは2.89%
- FireRedVADは100以上の言語対応でF1 97.57%を達成し、既存VADを上回ると記載。 [^]
  - Footnote: 100以上の言語に対応する音声/歌唱/音楽検出を行う音声活動検出システム。F1スコア97.57%を達成し、Silero-VAD、TEN-VAD、FunASR-VADを上回っています。
- FireRedASR2S一式は2026年2月12日に重みと推論コードが公開されたとされる。 [^]
  - Footnote: [2026年2月12日] FireRedASR2S（FireRedASR2-AED、FireRedVAD、FireRedLID、FireRedPunc）をモデル重みと推論コードとともにリリースしました。技術レポートおよびファインチューニング用コードは近日中に公開予定です。
- FireRedVADはFLEURS-VAD-102（102言語）で評価され、SOTAとされている。 [^]
  - Footnote: FireRedVADを多言語VADベンチマークであるFLEURS-VAD-102で評価しました。このベンチマークは102言語を対象としています。
- ASR入力長の制限が明記され、AEDは60秒、LLMは30秒までとされる。 [^]
  - Footnote: FireRedASR2-AEDは最大60秒までの音声入力に対応しています。FireRedASR2-LLMは最大30秒までの音声入力に対応しています。

### References
- https://zenn.dev/kun432/scraps/283e1a398d002f
- https://huggingface.co/FireRedTeam/FireRedASR2-AED
- https://huggingface.co/FireRedTeam/FireRedVAD

## 「FireRed-Image-Edit」を試す
- Date: 2026-02-15T22:24:00+09:00

### Executive Summary
- FireRed-Image-Edit-1.0の紹介と試行メモ。
- 一般画像編集でSOTAをうたう説明を引用。
- GEditベンチでNano-Banana/Seedream4.0超えと記載。
- テキストスタイル保持や複数画像編集など特徴を列挙。
- 2026年2月14日に重み公開、2月10日に技術レポート公開。
- A100 40GBでも厳しく4bit量子化+CPUオフロードで試すと記述。
- 日本語プロンプト/日本語文字はうまくいかない所感がある。

### Key Findings
- FireRed-Image-Edit-1.0は一般的な画像編集の新SOTAとして紹介されている。 [^]
  - Footnote: 一般的な画像編集の新しいSOTAとして正式に認定されました。
- GEditベンチマークでNano-BananaとSeedream4.0を上回るとされる。 [^]
  - Footnote: GEditベンチマークでNano-BananaおよびSeedream4.0を上回る性能。
- T2I基盤から構築され、既存モデルへのパッチではないと説明されている。 [^]
  - Footnote: T2Iの基礎から構築されており、既存モデルへの単なる「パッチ」ではありません。
- スタイル転送は4.97/5.0のスコアで、テキスト忠実度も高いとされる。 [^]
  - Footnote: スタイル転送で記録破りの4.97/5.0をスコア。
- 2026年2月14日に重みを、2月10日に技術レポートを公開したとある。 [^]
  - Footnote: 2026年2月14日: FireRed-Image-Edit-1.0モデルの重み付けデータをリリースしました。2026年2月10日: FireRed-Image-Edit-1.0の技術レポートを公開しました。
- 実行面ではA100 40GBでも不足し、4bit量子化+CPUオフロード前提と書かれている。 [^]
  - Footnote: とりあえず、普通にやるとColaboratory A100（40GB）でも足りない。よって今回はbitsandbytesで4ビット量子化+CPUオフロード前提でやる。

### References
- https://zenn.dev/kun432/scraps/e15cc9e5114a05
- https://modelscope.cn/models/FireRedTeam/FireRed-Image-Edit-1.0
- https://github.com/FireRedTeam/FireRed-Image-Edit
- https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0

## TP-Link Tapo C210 を Python で操作する
- Date: 2026-02-15T00:15:00+09:00

### Executive Summary
- TP-Link Tapo C210を買ってPython制御を試すメモ。
- ONVIFはメーカー違いでも操作可能にする共通規格と整理。
- ONVIFは制御系、映像はRTSPで送信と説明。
- ONVIFの通信はSOAP/WSDLで、ライブラリが読み込む。
- PythonのONVIFライブラリを比較し、async系を試す方針。
- ONVIFでの基本操作（名前、時刻、RTSP、PTZ、録画）を列挙。
- Codexでコードを書いたがズーム未実装とメモ。

### Key Findings
- Tapo C210を購入して試すと明記されている。 [^]
  - Footnote: 買った。Tapo C210というやつ。
- ONVIFはメーカーが違っても同じ操作を可能にする共通規格と説明されている。 [^]
  - Footnote: ONVIFは、ネットワークカメラや録画機器をメーカーが違っても同じ方法で操作できるようにするための共通規格
- ONVIFは主に制御系を担当し、映像はRTSPで送信するという整理。 [^]
  - Footnote: ONVIFは主に制御系を担当する。映像そのものは、RTSPを使って送信する。
- ONVIF通信はSOAPで命令を送信し、WSDLで定義する仕組みとされる。 [^]
  - Footnote: SOAP（XMLで命令を送信する）を使う。命令などを定義したものが WSDL（Web Services Description Language）
- Pythonライブラリはpython-onvif-zeep-asyncが良さそうとして試す方針。 [^]
  - Footnote: ざっと見た感じ、python-onvif-zeep-async が良さそう？とりあえず試してみる。
- Codexでコードを書いたがズームは未実装と記載されている。 [^]
  - Footnote: ズームだけ対応していないので未実装。

### References
- https://zenn.dev/kun432/scraps/91312d13f7e79f
- https://www.tp-link.com/jp/support/faq/2680/
- https://www.onvif.org/
