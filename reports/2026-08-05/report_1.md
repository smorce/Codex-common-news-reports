# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-08-05T09:01:39.7418789+09:00
- Articles: 3

## 「LFM2.5-2.6B」を試す
- Date: 2026-08-04T23:56:00+09:00

### Executive Summary
- Liquid AI の LFM2.5-2.6B は、オンデバイスで動くエージェント向け小型モデルとして紹介されている。
- 計画、ツール呼び出し、多段階タスク処理を端末上で実行できる点が主眼になっている。
- 事前学習は約 34T トークン、コンテキスト長と語彙サイズはいずれも 128K とされる。
- ポストトレーニングは SFT、教師専門化、MOPD、Agentic RL の 4 段階で説明されている。
- ベンチマークでは 4B から 10B クラスと比べ、指示追従やツール使用で強い結果が示されている。
- 推論環境は llama.cpp、MLX、vLLM、SGLang、ONNX など主要スタックに対応している。
- 筆者は Ubuntu 22.04 と RTX 4090 上で llama.cpp の llama-server を使い、Pi から OpenAI 互換エンドポイントとして利用する手順を試している。

### Key Findings
- LFM2.5-2.6B は端末内で動作するエージェントモデルとして位置づけられている。 [^]
  - Footnote: 記事本文に「完全にデバイス上で動作するエージェントモデル」「データはデバイスを離れることはなく」と記載。
- モデル仕様として約 34T トークンの事前学習、128K コンテキスト、128K 語彙が挙げられている。 [^]
  - Footnote: 本文に「~34Tトークンで事前学習」「コンテキスト長：128K」「語彙サイズ：128K」と記載。
- 小型ながらツール利用ベンチマークで上位モデルを上回る例が示されている。 [^]
  - Footnote: ToolSandbox 77.83 が Qwen3.5-9B の 76.44、IFStruct 85.49 が Qwen3.5-9B の 78.50 を上回ると記載。
- 学習後工程はドメイン別教師モデルを使った蒸留と実エージェント環境での RL が中心になっている。 [^]
  - Footnote: 「Teacher Specialization」「MOPD」「Agentic RL」の説明で、専門家モデル、トークンレベルのフィードバック、実際のエージェント環境のマルチターン RL が説明されている。
- CPU と GPU の両方で高速推論を狙うモデルとして整理されている。 [^]
  - Footnote: M5 Max で 220 tokens/s 以下、スマホで約 30 tokens/s、H100 で約 15K tokens/s と記載。
- 主要な推論フレームワークと複数ハードウェアへの対応が強調されている。 [^]
  - Footnote: llama.cpp、MLX、vLLM、SGLang、ONNX、および AMD、Qualcomm、Apple、NVIDIA、Intel が列挙されている。
- 筆者の実験では llama.cpp の Q8_0 GGUF を llama-server で配信し、Pi のモデル設定から接続している。 [^]
  - Footnote: 本文に `LiquidAI/LFM2.5-2.6B-GGUF:Q8_0`、`http://XXX.XXX.XXX.XXX:8080/v1`、Pi の `models.json` 設定例が掲載されている。

### References
- https://zenn.dev/kun432/scraps/dc34ccc88107f1
- https://twitter.com/liquidai/status/2084640701669613906
- https://twitter.com/liquidai/status/2084640706157486372

## メモ: How we built a realtime system for responsive voice AI in six months
- Date: 2026-08-04T20:23:00+09:00

### Executive Summary
- OpenAI の GPT-Live に関する記事をもとに、リアルタイム音声 AI の構成と運用上の論点が整理されている。
- GPT-Live は話しながら聞ける音声モデルとして紹介され、会話中の推論やツール利用を止めない設計が重視されている。
- 音声は専用の高速パスを通し、深い推論やツール利用は非同期に処理する構成とされる。
- 音声セッション開始時のネットワーク往復は 6 回から 1 回に削減されたと説明されている。
- 本番投入前には Advanced Voice Mode と GPT-Live に同じトラフィックを流すシャドーテストが行われたと整理されている。
- 容量設計では GPU 処理能力だけでなく、CPU、キュー、ネットワーク、地理的距離、長時間セッションの状態管理が重要とされる。
- 筆者はフルデュプレクス音声モデル、制御性、WebRTC 周辺技術が今後の実装上の重要点だと見ている。

### Key Findings
- GPT-Live は発話中にも聞き取れる音声体験を目指している。 [^]
  - Footnote: 本文に「GPT-Live は話しながら聞くことができます」と記載。
- 音声体験を自然にするため、クライアントからモデルまで音声スタックを再構築したと説明されている。 [^]
  - Footnote: 本文に「クライアントからモデルまで音声スタックを再構築しました」と記載。
- 音声データと重い推論処理を分けることで、会話の継続性を保つ設計になっている。 [^]
  - Footnote: 本文に「オーディオは専用の高速パス」「深い推論とツールの使用は非同期的」と記載。
- セッション起動時の遅延削減が主要改善として扱われている。 [^]
  - Footnote: 本文に「ボイスセッションの起動を6回のネットワークラウンドトリップから1回に削減」と記載。
- 本番相当の検証にはシャドートラフィックが使われている。 [^]
  - Footnote: 本文に「Advanced Voice ModeとGPT-Liveの両方に流すテスト」「GPT-Liveにも読み取り専用モードで推論処理」と記載。
- キャパシティ指標は GPU 単体の処理能力から同時セッション処理能力へ移っている。 [^]
  - Footnote: 本文に「GPUは1秒間に何件」から「フレーム遅延なく同時に処理できるセッション数」への転換が記載。
- 長時間セッション、地理的距離、可観測性の不足が実運用上の問題として挙げられている。 [^]
  - Footnote: 本文に「長時間動かさないと見つからない障害」「エンドユーザとの地理的距離」「より詳細なテレメトリデータの収集」と記載。

### References
- https://zenn.dev/kun432/scraps/ffdd1170b4d967
- https://twitter.com/OpenAI/status/2084378415818579975
- https://twitter.com/OpenAI/status/2084378417320141196

## 「Irodori-TTS v4」を試す
- Date: 2026-08-03T21:09:00+09:00

### Executive Summary
- Irodori-TTS v4 のリリースを受け、筆者が概要、README、インストール、実行感を確認している。
- v4 ではテキストエンコーダが ModernBERT-ja ベースに置き換えられ、日本語発話精度向上が期待されている。
- 従来別系統だった Voice Design が v4-Small では単一チェックポイントに統合されたと説明されている。
- モデルは Flow Matching ベースの TTS で、Echo-TTS を基本に DACVAE の連続潜在変数を使う。
- 参照音声からのゼロショット音声クローン、絵文字によるスタイル制御、自動持続時間予測などを備える。
- Ubuntu 22.04 と RTX 4090 環境で `uv sync --extra cu128` などのバックエンド指定によりセットアップできることが確認されている。
- 筆者の実行では VRAM 5 から 6GB 程度で動きそうとされ、MIT ライセンスで公開されている点も高く評価されている。

### Key Findings
- v4 は日本語発話精度の改善を意図した更新として扱われている。 [^]
  - Footnote: 本文に「テキストエンコーダがModernBERT-jaベースのものに置き換えられ、日本語発話精度が向上」と記載。
- Voice Design と従来のベースファミリーが統合された単一チェックポイントになっている。 [^]
  - Footnote: 本文に「以前は別だった Voice Design も1つのモデル」「従来のbaseファミリーとVoiceDesignファミリーを統合した単一のチェックポイント」と記載。
- Irodori-TTS は Flow Matching ベースで DACVAE の連続潜在変数を生成対象にしている。 [^]
  - Footnote: README 抜粋として「Flow Matchingベースのテキスト音声合成モデル」「DACVAEの連続潜在変数を採用」と記載。
- v4-Small はテキスト、参照音声、キャプションテキストを条件として利用できる。 [^]
  - Footnote: 本文に「テキスト、参照音声、キャプションテキストの3種類の条件付け入力に対応」と記載。
- 音声クローン、長時間参照音声、絵文字スタイル制御、自動持続時間予測など実用機能が多い。 [^]
  - Footnote: 機能概要に「ゼロショット音声クローン生成」「最大120秒」「絵文字注釈」「出力音声の長さを自動推定」と記載。
- 環境構築では PyTorch バックエンドを `uv sync --extra` で明示選択する手順が示されている。 [^]
  - Footnote: 本文に CUDA 12.8、ROCm、XPU、CPU 向けの `uv sync --extra cu128/rocm/xpu/cpu` が列挙されている。
- 筆者の確認では VRAM 使用量は 5 から 6GB 程度と見積もられている。 [^]
  - Footnote: 本文に「VRAM5〜6GBぐらいで動きそう」とあり、NVIDIA-SMI 出力で Memory-Usage 4913MiB が示されている。
- ライセンス面ではコードとモデルの扱いやすさが評価されている。 [^]
  - Footnote: 本文に「コード: MITライセンス」「モデルのライセンスはどちらもMITライセンス」「MITライセンスで公開されてる」と記載。

### References
- https://zenn.dev/kun432/scraps/12f2b10a9d5e3e
- https://github.com/Aratako/Irodori-TTS
- https://huggingface.co/Aratako/Irodori-TTS-v4-Small
