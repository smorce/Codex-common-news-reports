# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-24T09:01:44.1264427+09:00
- Articles: 3

## 「APEX Quant」を試す

### Executive Summary
- APEX Quant は MoE モデル向けに量子化割り当てを細かく最適化する手法として紹介されている。
- 目的は、llama.cpp 用 GGUF モデルを精度を大きく落とさず小型化し、推論速度も改善することにある。
- 記事では Qwen3.6-35B-A3B の APEX I-Quality GGUF を使い、Ubuntu 22.04 と RTX4090 環境で llama.cpp から動作確認している。
- APEX は Routed experts、Shared expert、Attention/SSM などテンソル種別ごとに量子化精度を変える点を特徴としている。
- レイヤー位置も考慮し、入力側・出力側の重要層を高精度に保ち、中間層を強く圧縮する方針が説明されている。
- I-variants は Wikipedia ではなくチャット、コード、推論、ツール呼び出しなど実用タスク寄りの imatrix を使う設計とされる。
- 記事後半では自前で F16 GGUF を作成し、APEX Quant の scripts/quantize.sh で量子化する流れを確認している。
- 全体として、16GB から 24GB 程度の GPU で大きな MoE モデルをローカル運用したいユーザー向けの実用的な検証になっている。

### Key Findings
- APEX Quant は MoE モデル専用の量子化ルール集として位置づけられている。 [^]
  - Footnote: 記事本文に「APEX は『MoEモデル専用の、超工夫された量子化ルール集』」と記載されている。
- I-Quality は Q8_0 同等以上を狙いつつ、モデルサイズを大きく削減する例として示されている。 [^]
  - Footnote: F16 64.6GB、Q8_0 34.4GB、APEX I-Quality 21.3GB、APEX Mini 12.2GB という比較が掲載されている。
- MoE の Routed experts は利用頻度が低いため、強めの量子化対象になりやすい。 [^]
  - Footnote: 「256人の専門家のうち、1トークンごとに 8人くらいしか呼ばれない」「97% くらいは...死んでる専門家」と説明されている。
- Shared expert は毎トークン通る重要部分で、低精度化に慎重な扱いが必要とされている。 [^]
  - Footnote: Shared expert について「毎トークン必ず通る重要パーツ」「最低でも Q8_0 必須」と記載されている。
- APEX はレイヤー位置に応じて、エッジ層を高精度、中間層を低精度にする設計を採る。 [^]
  - Footnote: L0-L4 と L35-L39 は Q6_K、L10-L29 は Q4_K や IQ4_XS まで落とす例が説明されている。
- I 系モデルは実用タスク寄りのキャリブレーションを重視している。 [^]
  - Footnote: I 系は「チャット」「コード」「推論」「ツール呼び出し」などのデータでキャリブレーションすると説明されている。
- 記事では llama.cpp を改変せず APEX 量子化済 GGUF が動作することを確認している。 [^]
  - Footnote: 「すべての処理は標準のllama.cppを使用しており、コードの変更は一切必要ありません」とし、llama-cli 実行例を掲載している。

### References
- https://zenn.dev/kun432/scraps/77f4dd669bc319

## LocalAI のいろいろな C++ 実装

### Executive Summary
- 記事は LocalAI に統合または関連する C/C++/GGML 系の推論エンジン群を整理している。
- LocalAI はテキスト生成だけでなく、音声認識、音声合成、画像・動画認識、生成、物体検出など広いタスクをローカルで扱うものとして紹介されている。
- 共通方針として、Python、PyTorch、onnxruntime、CUDA toolkit に依存せず、C/C++/GGML で推論する設計が挙げられている。
- モデル配布は自己完結した GGUF ファイルを基本とし、多くが参照実装との bit-exact 一致を検証しているとされる。
- 音声分野では parakeet.cpp、moss-transcribe.cpp、voice-detect.cpp、vibevoice.cpp、moss-tts.cpp などが紹介されている。
- ビジョン分野では rf-detr.cpp、locate-anything.cpp、depth-anything.cpp、face-detect.cpp などが整理されている。
- 3D 生成や量子化にも範囲が広がっており、free-splatter.cpp、trellis2cpp、apex-quant などが取り上げられている。
- 筆者は低リソース環境では whisper.cpp や llama.cpp 系の C++/ggml 実装を探す価値があると結論づけている。

### Key Findings
- LocalAI は多様なローカル AI タスクの実行基盤として捉えられている。 [^]
  - Footnote: 本文で「LLMのテキスト生成はもちろん、それ以外の幅広いタスク...をローカルで簡単に動かそうというもの」と説明されている。
- LocalAI には既存モデルを C++/ggml で再実装した推論エンジンが多数ある。 [^]
  - Footnote: 「このような既存の実装を C++/ggmlで再実装したプロジェクトがLocalAIには多数ある」と記載されている。
- 共通設計として、推論時に Python や PyTorch などを使わないことが強調されている。 [^]
  - Footnote: 共通の設計哲学として「推論時に Python・PyTorch・onnxruntime・CUDA toolkit を使わない」と列挙されている。
- parakeet.cpp は NVIDIA Parakeet ASR の C++/GGML ポートとして紹介されている。 [^]
  - Footnote: parakeet.cpp について「NVIDIA NeMo Parakeet 音声認識モデル群の C++ ポート」と説明されている。
- moss-transcribe.cpp は長時間音声の書き起こしと話者分離を 1 パスで行う。 [^]
  - Footnote: moss-transcribe.cpp の概要に「長時間音声の書き起こし + 話者分離(diarization)+ タイムスタンプ付を1パスで実行」とある。
- vllm.cpp は ggml を使わない例外的な純 C++ 実装として扱われている。 [^]
  - Footnote: 注記に「vllm.cpp は例外的に ggml を使わない独自の純 C++ 実装」とある。
- APEX は推論エンジン本体ではなく GGUF を生成する量子化手法として整理されている。 [^]
  - Footnote: 注記で「apex-quant は GGUF を生成する量子化手法(エンジン本体ではない)」と明記されている。
- 低リソース環境では C++/ggml 実装を探す実用的価値があるとされる。 [^]
  - Footnote: 末尾で「低リソース環境ではそういうのを探してみると良いかも」とコメントしている。

### References
- https://zenn.dev/kun432/scraps/66dc2af219472a

## 「Agents-A1」を試す（4B）

### Executive Summary
- 記事は InternScience の Agents-A1 について、特に 4B モデルのリリースとローカル実行を確認している。
- Agents-A1 は検索、エンジニアリング、科学研究、指示追従、ツール呼び出しなど長期タスク向けのエージェント型モデルとして紹介されている。
- モデルカードでは 35B-A3B のほか、4B Dense の BF16、FP8、GGUF など複数形式が整理されている。
- 4B モデルは 2026年7月14日にリリースされたとされ、より高速かつ簡単にローカル AI アシスタントを構築する狙いが説明されている。
- 記事では Agents-A1 が 256K コンテキスト長、エージェント型推論、関数呼び出しとツール統合を特徴とするとまとめている。
- 性能面では BrowseComp、GAIA、IFEval など複数ベンチマークで同規模モデルを大きく上回る結果が引用されている。
- 筆者は Mac M2 Pro 上で 4B GGUF Q8_0 を llama.cpp から起動し、推奨サンプリングパラメータで試している。
- 実行ログでは Q8_0 モデルが text、vision、video の modalities を持つと表示され、Vision 対応の可能性にも触れている。

### Key Findings
- Agents-A1 は長期的タスク向けに設計されたエージェント型モデルとして紹介されている。 [^]
  - Footnote: 冒頭で「検索、エンジニアリング、科学研究、指示追従、ツール呼び出しにわたる長期的タスク向け」と説明されている。
- 4B モデルのリリースが記事の主な確認対象になっている。 [^]
  - Footnote: モデルカードのニュースとして「2026年7月14日: 4Bモデルをリリースしました」と引用されている。
- モデルには 35B-A3B MoE と 4B Dense の複数バリエーションがある。 [^]
  - Footnote: バリエーションとして「35B-A3B MoE」「4B Dense」「BF16」「FP8」「GGUF（Q4_K_M / Q8_0 / F16）」が列挙されている。
- Agents-A1 はツール活用を標準機能として扱う。 [^]
  - Footnote: 主な特徴に「関数呼び出し機能とツール統合機能を標準搭載」と記載されている。
- 4B モデルは一部ベンチマークで大規模 MoE モデルに匹敵または上回るとされる。 [^]
  - Footnote: 本文に「一部のスコアではNex-N2-miniやQwen3.6といった大規模MoEモデルに匹敵または上回る」とある。
- BrowseComp、XBench、GAIA、IFEval などの数値が強みとして引用されている。 [^]
  - Footnote: Agents-A1-4B の BrowseComp 66.8、XBench-DS-2510 90.0、GAIA 95.1、IFEval 94.8 が掲載されている。
- 筆者は Mac M2 Pro で GGUF Q8_0 を llama.cpp から試している。 [^]
  - Footnote: 「今回は Mac（M2 Pro）で、4B GGUF Q8_0 を試してみる」とし、llama-cli の実行コマンドを示している。
- 推奨サンプリングパラメータがモデルカードから引用されている。 [^]
  - Footnote: temperature 0.85、top_p 0.95、top_k 20、min_p 0.0、presence_penalty 1.1、repetition_penalty 1.0 が列挙されている。

### References
- https://zenn.dev/kun432/scraps/c070bfe51ac731
