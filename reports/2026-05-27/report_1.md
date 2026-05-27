# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-27T00:00:00+09:00
- Articles: 3

## 「SFace」で顔認識を試す

### Executive Summary
- OpenCV の SFace を使った顔認識の検証メモである。
- 顔検出には前回試した YuNet を使い、SFace では検出済みの顔から特徴量を抽出している。
- Colaboratory では OpenCV 4.13.0 が利用でき、YuNet と SFace の ONNX モデルを Hugging Face から取得している。
- 同一画像の比較ではコサイン類似度が 1.0000 となり、同一人物と判定された。
- 複数人物画像から特定人物を探す例では、10件の顔検出結果のうち1件だけが閾値を超えた。
- 判定には OpenCV デモで使われる COSINE_THRESHOLD 0.363 を採用している。
- 実装は alignCrop、feature、match を組み合わせるシンプルな流れで整理されている。

### Key Findings
- SFace 単体ではなく、YuNet による顔検出結果を前処理として使っている。 [^]
  - Footnote: 記事では「YuNetで顔を検出する」として detector.detect の結果を SFace の alignCrop に渡している。
- Colaboratory 環境では OpenCV 4.13.0 が利用されていた。 [^]
  - Footnote: cv2.__version__ の出力として 4.13.0 が示されている。
- SFace の標準 ONNX モデルとして face_recognition_sface_2021dec.onnx を利用している。 [^]
  - Footnote: リポジトリ内に3種類の ONNX があり、FaceRecognizerSF.create の model に標準ファイルを指定している。
- 同一画像同士の比較では完全一致に近い結果が得られた。 [^]
  - Footnote: cosine score: 1.0000、same person: True と出力されている。
- 複数人物画像では10件の顔が検出され、クエリ画像では1件の顔が検出された。 [^]
  - Footnote: target faces: 10、query faces: 1 の出力が掲載されている。
- 閾値 0.363 を超えた index 8 のみが同一人物と判定された。 [^]
  - Footnote: comparison_results で index 8 の score が 0.5280203695378987、same_person が True とされている。

### References
- https://zenn.dev/kun432/scraps/f58a2069165e38

## 「LLM-jp-4-VL / Jagle-VL」 を試す

### Executive Summary
- LLM-jp-4-VL 9B beta と Jagle-VL 系モデルを調べ、Colaboratory で試した記録である。
- LLM-jp-4-VL は llm-jp-4-8b-instruct を基盤に、SigLIP2 と2層 MLP プロジェクタで構成されている。
- 学習データは FineVision 2420万サンプルと Jagle 920万サンプルの混合である。
- 日本語タスクでは Qwen3-VL-8B-Instruct と同等程度の平均性能とされ、使用トークン量は大幅に少ないと説明されている。
- Colaboratory L4 では LLM-jp-4-VL 9B beta のロード後に約17.6GBの VRAM を消費した。
- Jagle-VL-2.2B 系は約4.3GBの VRAM で動いたが、当初 config の不整合や出力ループが見られた。
- モデル自体は Apache License 2.0 だが、FineVision 由来データのライセンス解釈には注意が必要だと整理している。

### Key Findings
- LLM-jp-4-VL 9B beta は日本語向けの視覚言語モデルとして紹介されている。 [^]
  - Footnote: モデルカード抜粋として「LLM-jpが開発した視覚言語モデル」と説明されている。
- アーキテクチャは InternVL3.0 に着想を得ている。 [^]
  - Footnote: 言語モデル、視覚エンコーダ、軽量プロジェクタから構成されると記載されている。
- LLM-jp-4-VL の構成要素は 8.6B LLM、0.4B 視覚エンコーダ、2層 MLP である。 [^]
  - Footnote: LLM: llm-jp/llm-jp-4-8b-instruct、視覚エンコーダ: google/siglip2-so400m-patch16-512、プロジェクタ: 2層MLP と示されている。
- 学習データは FineVision と Jagle の2系統で、Jagle は日本語マルチモーダルデータセットである。 [^]
  - Footnote: FineVision 2420万サンプル、Jagle 920万サンプルと記載されている。
- LLM-jp-4-VL は Qwen3-VL より少ない後学習トークンで日本語タスク同等性能を狙っている。 [^]
  - Footnote: Qwen3-VL が2兆トークン以上、本モデルは1800億トークンと説明されている。
- Colaboratory L4 での LLM-jp-4-VL 実行時、VRAM 消費は約17.6GBだった。 [^]
  - Footnote: NVIDIA-SMI の出力で Memory-Usage が 17636MiB / 23034MiB と示されている。
- Jagle-VL-2.2B 系は軽量だが、出力ループや設定修正の必要性が観察された。 [^]
  - Footnote: VRAM 約4.3GB、富士山説明で同じ文が繰り返される出力、2026/05/25追記で config 修正不要と記載されている。
- FineVision 由来データのライセンス扱いには注意が必要だと述べている。 [^]
  - Footnote: FineVision に OpenAI や Anthropic などのクローズドソースモデル出力が含まれる可能性への疑問が書かれている。

### References
- https://zenn.dev/kun432/scraps/9094e75e32e740
- https://huggingface.co/llm-jp/llm-jp-4-vl-9b-beta
- https://huggingface.co/llm-jp/Jagle-VL-2.2B-Jagle-FineVision

## メモ: human-in-the-loop を OpenAI Chat Completions API でやってみる

### Executive Summary
- OpenAI Chat Completions API で human-in-the-loop の承認処理を試したメモである。
- 最初の例では get_weather ツールを呼び出し、ユーザーに y/N で実行可否を確認している。
- 次にツールごとに ask 属性を持たせ、天気取得は自動、メール送信は承認必須に分けている。
- 自然言語の承認判定では、別の LLM 呼び出しで approve、reject、unclear に分類している。
- ただし自然言語承認は自由度が高く、堅牢性が下がる可能性があると問題提起している。
- 拒否や保留を単なるツールエラーとして扱うと、以後の会話で恒久的な権限不足のように誤解される例が示されている。
- 改善案として approval_state を持ち、ツール呼び出しID、引数、判定、理由を保存する構成を試している。

### Key Findings
- Chat Completions API の tools と tool_choice="auto" を使ってツール呼び出しを発生させている。 [^]
  - Footnote: client.chat.completions.create に model、messages、tools、tool_choice="auto" を渡すコードが掲載されている。
- ツール実行前にユーザー確認を挟む基本形を実装している。 [^]
  - Footnote: ツール要求の名前と引数を表示し、「このツールを実行しますか？ [y/N]」で確認している。
- 承認しない場合でも tool メッセージとして結果を返す設計にしている。 [^]
  - Footnote: 拒否時には error: tool_execution_denied、tool_name、arguments を content に入れて messages に追加している。
- ツールごとに承認要否を切り替える構造を試している。 [^]
  - Footnote: tool_mapping に get_weather は ask: False、send_email は ask: True と定義されている。
- 自然言語承認は別スレッド的な分類器で approve、reject、unclear に変換している。 [^]
  - Footnote: classify_approval が response_format の json_schema で decision と reason を返す設計になっている。
- 拒否や一時保留を単純な失敗として会話履歴に残すと、その後の応答が悪化する例がある。 [^]
  - Footnote: 一時保留後に「メール送信の権限がないため」と返し、再依頼しても送信できない前提で応答した例が示されている。
- 改善策として approval_state に承認情報を保存する方式を試している。 [^]
  - Footnote: ApprovalState に tool_call_id、tool_name、arguments、decision、reason を持たせるコードが示されている。

### References
- https://zenn.dev/kun432/scraps/fd750c03716a5e
