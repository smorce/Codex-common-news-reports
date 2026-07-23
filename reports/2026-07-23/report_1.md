# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-23T09:00:00+09:00
- Articles: 3

## 「APEX Quant」を試す
- Date: 2026-07-22T13:54:05+00:00

### Executive Summary
- APEX Quant は MoE モデル向けに量子化割り当てを最適化する手法として紹介されている。
- 記事では Qwen 系 35B MoE を念頭に、GGUF のサイズ、品質、速度のバランスを整理している。
- 通常の一律量子化ではなく、MoE の専門家重み、共有 expert、Attention/SSM を分けて扱う点が要点である。
- エッジ層を高精度に保ち、中間層を強く圧縮する layer-wise な設計が説明されている。
- I-Quality、Balanced、Compact、Mini など複数 tier があり、VRAM 容量と精度要求で選ぶ想定になっている。
- I 系バリアントは Wikipedia ではなくチャット、コード、推論、ツール呼び出し寄りの imatrix を使う。
- 作者公開の APEX 量子化済み GGUF を llama.cpp でそのまま起動し、コード変更なしで動作することを確認している。
- APEX Mini と TurboQuant の併用により、16GB GPU で 35B MoE と 8K コンテキストが視野に入る構成も示されている。

### Key Findings
- APEX Quant は MoE モデルの構造を前提にした混合精度量子化である。 [^]
  - Footnote: 記事では「MoEモデル専用の、超工夫された量子化ルール集」と説明している。
- APEX I-Quality は Q8_0 相当以上の精度を狙いつつ、モデルサイズを大幅に削る。 [^]
  - Footnote: F16 は 64.6GB、Q8_0 は 34.4GB、APEX I-Quality は 21.3GB と記載されている。
- Routed experts は強めに圧縮しやすい対象として扱われる。 [^]
  - Footnote: 1トークンごとに約8人しか呼ばれず、約97%はそのトークンにとって使われない専門家だと説明している。
- Shared expert は品質劣化に敏感なため高精度を維持する方針である。 [^]
  - Footnote: 毎トークン必ず通る重要パーツで、裾が重い分布を持つため最低でも Q8_0 必須という結論が示されている。
- レイヤー位置に応じて量子化精度を変える設計が重要視されている。 [^]
  - Footnote: 入力側 L0-L4 と出力側 L35-L39 は Q6_K、中間 L10-L29 は Q4_K や IQ4_XS まで落とす例が示されている。
- I 系モデルは実用タスク寄りのキャリブレーションを採用する。 [^]
  - Footnote: チャット、コード、推論、ツール呼び出しのデータで imatrix を作り、Wikipedia は使わないと説明されている。
- llama.cpp 側の変更なしで APEX 量子化済み GGUF を実行できる可能性が確認されている。 [^]
  - Footnote: 記事では README の「コードの変更は一切必要ありません」という説明を引用し、実際に llama-cli で起動している。

### References
- https://zenn.dev/kun432/scraps/77f4dd669bc319

## LocalAI のいろいろな C++ 実装
- Date: 2026-07-22T10:48:22+00:00

### Executive Summary
- 記事は LocalAI 周辺に存在する C++/GGML ベースのネイティブ推論エンジン群を整理している。
- LocalAI はテキスト生成だけでなく、ASR、TTS、画像認識、動画、物体検出など幅広いローカル AI タスクを対象にしている。
- 共通方針として Python、PyTorch、onnxruntime、CUDA toolkit を推論時に使わない from-scratch 実装が挙げられている。
- モデルを自己完結した GGUF ファイルとして配布し、GPU バックエンドにも対応する設計が多い。
- 音声認識、話者認識、TTS、音響処理、LLM、画像、3D生成、量子化などカテゴリごとに実装が列挙されている。
- parakeet.cpp、moss-transcribe.cpp、vibevoice.cpp、rf-detr.cpp、depth-anything.cpp などが具体例として紹介されている。
- vllm.cpp や apex-quant など、ggml 非使用またはエンジン本体ではない例外も注記されている。
- 低リソース環境では whisper.cpp や llama.cpp の思想に近い C++ 実装を探す価値がある、という見方で締めている。

### Key Findings
- LocalAI は多モダリティのローカル推論を扱う基盤として捉えられている。 [^]
  - Footnote: 記事ではテキスト生成、音声認識・音声合成、画像・動画認識、画像・動画生成、物体検出などを列挙している。
- LocalAI には C++/ggml で既存モデルを再実装したプロジェクトが多数ある。 [^]
  - Footnote: parakeet.cpp を例に、NVIDIA の ASR Parakeet を C++/ggml にポートしたものと説明している。
- 多くの実装は推論時の重量級依存を避ける設計を掲げている。 [^]
  - Footnote: 共通の設計哲学として、推論時に Python、PyTorch、onnxruntime、CUDA toolkit を使わないと記載されている。
- GGUF による自己完結配布が複数エンジンの共通パターンになっている。 [^]
  - Footnote: モデルは自己完結した1個の GGUF ファイルとして配布されると説明している。
- ASR 分野では parakeet.cpp や moss-transcribe.cpp が取り上げられている。 [^]
  - Footnote: parakeet.cpp は CTC/RNNT/TDT/hybrid に対応し、moss-transcribe.cpp は長時間音声の書き起こし、話者分離、タイムスタンプ付与を1パスで実行するとされている。
- 画像・ビジョン分野でも C++/GGML 化の対象が広がっている。 [^]
  - Footnote: rf-detr.cpp、locate-anything.cpp、depth-anything.cpp、face-detect.cpp が画像・ビジョンカテゴリに列挙されている。
- apex-quant は推論エンジンではなく、GGUF を生成する量子化手法として分類される。 [^]
  - Footnote: 注記で apex-quant は GGUF を生成する量子化手法で、エンジン本体ではないと明記されている。

### References
- https://zenn.dev/kun432/scraps/66dc2af219472a

## 「Agents-A1」を試す（4B）
- Date: 2026-07-20T17:28:23+00:00

### Executive Summary
- 記事は InternScience の Agents-A1 について、特に 4B 版のリリースとローカル実行を扱っている。
- Agents-A1 は検索、エンジニアリング、科学研究、指示追従、ツール呼び出し向けの長期視野型エージェントモデルとして紹介されている。
- 35B-A3B MoE に加えて 4B Dense 版が公開され、BF16、FP8、GGUF など複数形式がある。
- モデルカードでは 256K コンテキスト、エージェント型推論、関数呼び出しとツール統合が主な特徴として示されている。
- 4B 版は BrowseComp、XBench、GAIA、IFEval などで同規模モデルを上回る性能が示されている。
- トレーニング面では、全ドメイン SFT、ドメイン別教師モデル、マルチ教師マルチドメインのオンポリシー蒸留が説明されている。
- 記事では Mac M2 Pro 上で 4B GGUF Q8_0 を llama.cpp から起動し、推奨パラメータも確認している。
- 出力例からは Vision 対応表示や、通常会話でツールを使わず自然に返すシステムプロンプトの挙動が観察されている。

### Key Findings
- Agents-A1 は長期タスク向けのエージェントモデルとして位置付けられている。 [^]
  - Footnote: 検索、エンジニアリング、科学研究、指示追従、ツール呼び出しにわたる長期的タスク向けと紹介されている。
- 4B モデルの公開が記事の注目点になっている。 [^]
  - Footnote: モデルカードのニュースとして 2026年7月14日に 4B モデルをリリースしたと記載されている。
- Agents-A1 には 35B-A3B MoE と 4B Dense の複数バリエーションがある。 [^]
  - Footnote: 記事では 35B-A3B MoE の BF16、FP8、GGUF と、4B Dense の BF16、FP8、GGUF を列挙している。
- モデルの特徴はエージェント的推論とツール活用に置かれている。 [^]
  - Footnote: 複雑なタスクをサブステップに分解し、関数呼び出しや API、コードインタープリタ、検索エンジンなどと連携できると説明されている。
- 4B 版は複数ベンチマークで高い競争力を示すとされている。 [^]
  - Footnote: BrowseComp 66.8、XBench-DS-2510 90.0、GAIA 95.1、IFEval 94.8 などの値が掲載されている。
- 学習方法はドメイン横断とドメイン特化を組み合わせる設計である。 [^]
  - Footnote: 全ドメイン SFT、ドメインレベル教師モデル、マルチ教師マルチドメインオンポリシー蒸留の3段階が説明されている。
- llama.cpp で 4B Q8_0 GGUF をローカル実行している。 [^]
  - Footnote: Mac M2 Pro で InternScience/Agents-A1-4B-Q8_0-GGUF を llama-cli の -hf オプションから起動している。

### References
- https://zenn.dev/kun432/scraps/c070bfe51ac731
