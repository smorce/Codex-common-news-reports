# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-04T09:02:13+09:00
- Articles: 3

## 「VibeVoice-ASR」を試す

### Executive Summary
- MicrosoftがHugging FaceでVibeVoice-ASRを公開した点を確認。
- 60分音声を1回の処理で扱える長時間ASRとして紹介されている。
- 話者識別・タイムスタンプ・ホットワードを統合し、構造化文字起こしを生成する。
- 50以上の言語に対応し、言語設定不要・コードスイッチ対応と説明されている。
- モデルカード由来の主要特徴とOpen ASRリーダーボード結果が整理されている。
- Transformers互換版として公開され、以前の公開版との差分にも触れている。
- Colab L4での試行では7B規模・VRAM約16GB消費など実行メモが記載されている。

### Key Findings
- VibeVoice-ASRはMicrosoftからHugging Faceで公開された。 [^]
  - Footnote: MicrosoftがHugging Face上でVibeVoice-ASRを公開しました
- 60分の長時間音声を一括で書き起こせる設計とされる。 [^]
  - Footnote: 60分間の音声データを1回の処理で書き起こし可能です。
- 話者識別・タイムスタンプ・ホットワード検出を搭載する。 [^]
  - Footnote: 話者識別機能＋タイムスタンプ＋ホットワード検出機能を搭載。
- 50以上の言語に対応し、言語設定が不要と明記されている。 [^]
  - Footnote: 50以上の言語に対応しており、言語設定は不要です。
- ASR・ダイアライゼーション・タイムスタンプを統合し、誰が・いつ・何を発言したかの構造化出力を生成する。 [^]
  - Footnote: 本モデルはASR、ダイアライゼーション、タイムスタンプ処理を統合的に実行し、誰が、何を、いつ発言したかを示す構造化された出力を生成します。
- Open ASRリーダーボードでの平均WERやRTFxが示されている。 [^]
  - Footnote: 平均	7.77
RTFx	51.80
- ライセンスはMIT Licenseと記載されている。 [^]
  - Footnote: 本プロジェクトは MIT License に基づいて提供されています。

### References
- https://zenn.dev/kun432/scraps/98c5183492ab09
- https://huggingface.co/microsoft/VibeVoice-ASR-HF

## 「Qwen3-VL-Video-Grounding」を試す

### Executive Summary
- Qwen3-VL-Video-Groundingのデモ概要が紹介されている。
- ポイント追跡・テキスト指示検出・動画QAをQwen3-VL-4Bで実現する構成。
- Hugging Face Spacesにデモがあると記載されている。
- GradioベースのWebアプリとして動画追跡とQAを提供する。
- テキスト指示のバウンディングボックスとマスク、ポイント軌跡の描画が特徴。
- ZeroGPUは負荷が高く結果が出ない可能性があり複製推奨と注意喚起。
- CUDA GPU 16GB以上推奨など、ローカル要件と制限がまとめられている。

### Key Findings
- Qwen3-VL-4Bでポイント追跡・テキスト誘導検出・動画QAを実行するデモだと説明されている。 [^]
  - Footnote: Qwen3-VL-Video-Grounding デモ。ポイント追跡、テキストガイド付き検出、ビデオ質問応答を実行し、全てQwen3-VL-4B ビジョン言語モデルによって実現され、リアルタイムバウンディングボックス検出とフレーム間オブジェクトマッチングを備えています。
- Hugging Face Spacesにデモが用意されている。 [^]
  - Footnote: HuggingFace Spacesにデモが用意されている。
- GradioベースのWebアプリとして動画オブジェクト追跡、ポイント追跡、動画QAに対応する。 [^]
  - Footnote: Qwen3-VLマルチモーダル視覚言語モデルを活用した動画オブジェクト追跡、ポイント追跡、動画質問応答に対応したGradioベースのウェブアプリケーションです。
- ZeroGPUの制約で結果が出ない場合があり、複製して試すよう注意がある。 [^]
  - Footnote: [HFデモについて] 注意：本アプリケーションはZeroGPUコンピューティングリソースを多く消費する場合があり、場合によっては結果が得られないことがあります。より安定した動作を確認するため、ご自身の環境でアプリケーションを複製してお試しください。
- 処理はクライアント側で実行し、SpacesではZeroGPU対応Gradioを使うと説明されている。 [^]
  - Footnote: すべての処理はクライアント側で実行され、Hugging Face Spacesへのデプロイ時にはZeroGPU対応のGradioインターフェースを使用します。
- CUDA対応GPUで16GB以上のVRAMが推奨と明記されている。 [^]
  - Footnote: CUDA対応GPUで十分なVRAMを搭載していること（推奨16GB以上）
- 最大動画再生時間はデフォルト3秒、最大20秒とされる。 [^]
  - Footnote: 最大動画再生時間の制御 -- 各タブごとにスライダーで設定可能で、処理する動画の長さを制限します（デフォルト3秒、最大20秒）。

### References
- https://zenn.dev/kun432/scraps/e44009451f9f01
- https://github.com/PRITHIVSAKTHIUR/Qwen3-VL-Video-Grounding

## 「Qwen3.5 Smallモデル」を試す

### Executive Summary
- Qwen3.5の小型モデル0.8B/2B/4B/9Bの紹介が中心。
- 同一のQwen3.5基盤でネイティブマルチモーダル等の特徴を共有する。
- サイズごとの想定用途（エッジ・軽量エージェント・大型との差縮小）が記載されている。
- Baseモデルも同時リリースと明記されている。
- 全モデルVision対応でコンテキスト長は262,144トークン。
- 4B/9BはRoPE(YaRN)で1,010,000トークンまで拡張可能とある。
- Reasoningのデフォルトや推論フレームワーク対応、GGUF配布情報が整理されている。

### Key Findings
- 小型モデルは0.8B/2B/4B/9Bの4サイズで構成される。 [^]
  - Footnote: Qwen3.5-0.8B · Qwen3.5-2B · Qwen3.5-4B · Qwen3.5-9B
- 同じQwen3.5基盤でネイティブマルチモーダル等の改良を共有する。 [^]
  - Footnote: これらの小型モデルは、同じQwen3.5基盤に基づいて構築されています — ネイティブマルチモーダル、改良されたアーキテクチャ、スケーラブルなRL
- 0.8B/2Bは小型高速でエッジデバイス向けとされる。 [^]
  - Footnote: 0.8B / 2B → 小型で高速、エッジデバイスに最適
- 4Bは軽量エージェント向けの強力なマルチモーダル基盤と説明される。 [^]
  - Footnote: 4B → 軽量エージェント向けに驚くほど強力なマルチモーダル基盤
- 9Bは大型モデルとの差を縮めつつあると記載されている。 [^]
  - Footnote: 9B → コンパクトながら、はるかに大規模なモデルとのギャップをすでに埋めつつある
- 全モデルVision対応でネイティブのコンテキスト長は262,144トークン。 [^]
  - Footnote: 全モデル Vision 対応。コンテキスト長はネイティブで262,144トークン。
- 4B/9BはRoPE(YaRN)で1,010,000トークンまで拡張可能と記載。 [^]
  - Footnote: 4B / 9B
RoPE スケーリング（YaRN）で 1,010,000トークンまで拡張化。
- 0.8B/2BはReasoningがデフォルト無効、4B/9Bはデフォルト有効とされる。 [^]
  - Footnote: 0.8B / 2B はデフォルトで無効（non-thinking）
4B / 9B はデフォルトで有効（thinking）

### References
- https://zenn.dev/kun432/scraps/bd7e1b67833834
- https://huggingface.co/collections/Qwen/qwen35
