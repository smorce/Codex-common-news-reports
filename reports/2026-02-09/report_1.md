# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-02-09T10:30:00+09:00
- Articles: 3

## 「NVIDIA Model Optimizer」を試す
- Date: 2026-02-08T22:58:00+09:00

### Executive Summary
- Model Optimizerは量子化・蒸留・プルーニング・投機的デコーディング等を統合した最適化ライブラリと説明されている。
- 入力はHugging Face、PyTorch、ONNX形式のモデルをサポートと記載されている。
- Python APIで最適化を組み合わせ、量子化チェックポイントをエクスポートできる。
- 生成された量子化チェックポイントはSGLang/TensorRT-LLM/TensorRT/vLLMへ展開可能と示されている。
- pipによるインストールやソースからの開発用インストール手順が提示されている。
- 著者はUbuntu 22.04（RTX4090）でTensorRT-LLMのDockerイメージ利用を選択した。
- コンテナ内のmodeloptは0.37.0で最新0.41.0との差を認識しつつ進めている。

### Key Findings
- Model Optimizerは量子化や蒸留など複数の最適化技術を統合したライブラリである。 [^]
  - Footnote: 「量子化、蒸留、プルーニング、推測的デコーディング、スパース性などの最先端のモデル最適化技術を統合したライブラリ」
- 入力形式としてHugging Face、PyTorch、ONNXのモデルをサポートする。 [^]
  - Footnote: 「Hugging Face、PyTorch、またはONNX形式のモデルを入力としてサポート」
- Python APIで最適化を組み合わせ、量子化チェックポイントを出力できる。 [^]
  - Footnote: 「Python APIを提供しており、...量子化チェックポイントをエクスポートできます」
- 量子化チェックポイントはSGLang/TensorRT-LLM/TensorRT/vLLMに展開可能。 [^]
  - Footnote: 「SGLang、TensorRT-LLM、TensorRT、あるいはvLLMといった下流の推論フレームワークで即座にデプロイ可能」
- pipで安定版をインストールする場合はnvidia-modelopt[all]を利用する。 [^]
  - Footnote: 「pip install -U nvidia-modelopt[all]」
- TensorRT-LLMのDockerイメージを直接利用できる選択肢が示されている。 [^]
  - Footnote: 「TensorRT-LLM Dockerイメージ...を直接使用することも可能」
- 著者はTensorRT-LLMのDockerイメージを使う判断をしている。 [^]
  - Footnote: 「TensorRT-LLMのDockerイメージで使えるみたい...そのイメージを使うことにする。」
- コンテナ内のmodeloptは0.37.0で、最新が0.41.0と記載されている。 [^]
  - Footnote: 「0.41.0が最新のようだが...含まれていたのは0.37.0だった」

### References
- https://zenn.dev/kun432/scraps/f13c9d22a572db

## 「TensorRT-LLM」を試す
- Date: 2026-02-07T19:32:00+09:00

### Executive Summary
- TensorRT LLMはLLMを定義できるPython APIとGPU向け最適化を提供すると説明されている。
- 推論向けのオープンソースライブラリで、カスタム注意カーネルやインフライトバッチなどを備える。
- 量子化（FP8/FP4/INT4/AWQ/INT8など）や投機的デコーディングにも対応とされる。
- PyTorch基盤で単一GPUからマルチGPU・マルチノードまで対応するLLM APIを提供する。
- Ubuntu 22.04（RTX4090）でDockerイメージを使うクイックスタートを実施している。
- trtllm-serveでOpenAI互換APIを起動し、--host 0.0.0.0を付与する必要があると記載。
- 量子化はGPUとモデル依存で、RTX4090はFP8系やGPTQ/AWQなど一部が利用可能と整理されている。

### Key Findings
- TensorRT LLMはLLM定義用のPython APIとNVIDIA GPU向け最適化を提供する。 [^]
  - Footnote: 「LLMを簡単に定義できるPython APIを提供し、NVIDIA GPU上で効率的に推論を実行」
- 推論最適化のための複数機能（カスタム注意、インフライトバッチ、ページングKVキャッシュなど）を備える。 [^]
  - Footnote: 「カスタム注意機構カーネル、インフライトバッチ処理、ページング方式のKVキャッシュ」
- 量子化や投機的デコーディングなどの最先端最適化も含む。 [^]
  - Footnote: 「量子化技術（FP8、FP4、INT4 AWQ、INT8 SmoothQuantなど）、投機的デコーディング」
- PyTorch基盤で、LLM APIは単一GPUからマルチGPU・マルチノードまで対応する。 [^]
  - Footnote: 「PyTorchを基盤として構築...単一GPUからマルチGPU・マルチノード環境まで対応可能な、高水準のPython LLM API」
- Dockerでの起動例としてTensorRT-LLMの公式イメージが指定されている。 [^]
  - Footnote: 「nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc2」
- trtllm-serveでOpenAI互換APIを起動し、外部から使うために--host 0.0.0.0が必要と記載。 [^]
  - Footnote: 「trtllm-serve...--host 0.0.0.0 を付与する」
- 量子化の対応可否はGPUとモデルに依存し、RTX4090ではFP8系やGPTQ/AWQが列挙されている。 [^]
  - Footnote: 「RTX4090（Ada Lovelace）だと、FP8 Per Tensor、FP8 KV Cache、W4A16 GPTQ、W4A8 GPTQ、W4A16 AWQ、W4A8 AWQ」
- モデルの量子化作業はModel Optimizerで行うと整理されている。 [^]
  - Footnote: 「モデルの量子化作業はModel Optimizerというツールで行うことになる。」

### References
- https://zenn.dev/kun432/scraps/00e7ec6855aa0d

## 「MegaQwen」を試す
- Date: 2026-02-07T18:14:00+09:00

### Executive Summary
- MegaQwenはQwen3-0.6Bの1トークン生成を徹底最適化するプロジェクトとして紹介されている。
- 28層のトランスフォーマーブロックを1つの巨大CUDAカーネルに統合する設計を採用。
- 短いコンテキストで530 tok/sを達成し、HuggingFace実装の約3.9倍とされる。
- TensorRT-LLMより短コンテキストで速い一方、条件が限定的であることが示される。
- grid.syncによる全体同期を多用し、1トークンあたり140〜225回規模と説明されている。
- 実効メモリ帯域は47GB/sでピーク936GB/sの5%に留まると計測されている。
- ボトルネックはgrid.syncレイテンシで、アーキテクチャ的な天井があるという結論。

### Key Findings
- 28層のトランスフォーマーブロックを単一の巨大CUDAカーネルに統合している。 [^]
  - Footnote: 「28層ぶんのトランスフォーマーブロックを『1つの巨大 CUDA カーネル（メガカーネル）』に全部詰め込んだ」
- 短いコンテキストで530 tok/sを達成し、HuggingFace実装の約3.9倍と記載。 [^]
  - Footnote: 「短いコンテキストだと 530 tok/s を達成して、HuggingFace 実装の約 3.9 倍」
- 短コンテキストではTensorRT-LLMより速いとの比較が示されている。 [^]
  - Footnote: 「TensorRT-LLM よりも短コンテキストだけなら速い（530 vs 355 tok/s）」
- 1トークンあたりのgrid.sync回数は約225回と説明されている。 [^]
  - Footnote: 「1 トークンあたりの grid.sync は、約 225 回」
- 実効メモリ帯域は47GB/sでピーク936GB/sに対し利用率5%と報告されている。 [^]
  - Footnote: 「実効メモリ帯域: 約 47 GB/s」「GPU のピーク帯域: 936 GB/s」「利用率: わずか 5%」
- ボトルネックはメモリではなくgrid.syncのレイテンシと結論づけている。 [^]
  - Footnote: 「ボトルネックはメモリじゃなくて grid.sync() のレイテンシだった。」
- CUDA Graphで225カーネルに分割した場合の計測値が示されている。 [^]
  - Footnote: 「CUDA Graph で 225 カーネルに分割: 186.9 μs」
- 本番利用はTensorRT-LLMやvLLMを推奨する締めになっている。 [^]
  - Footnote: 「本番なら TensorRT-LLM や vLLM を使え。」

### References
- https://zenn.dev/kun432/scraps/48aef3d94ffb11
