# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-12T10:46:35+09:00
- Articles: 3

## 音声を音素に変換する「Wav2Vec2Phoneme」 を試す
- Date: 2026-03-11T00:29:00+09:00

### Executive Summary
- 前回のphone認識から一歩進め、音声→音素の変換を試す方針を整理している。
- phoneとphonemeの違いを整理し、phoneは実音の単位、phonemeは意味弁別の抽象単位と説明。
- Allosaurusはphone認識器であり、本稿はphoneme側を扱う点を明確化。
- Wav2Vec2PhonemeはXu et al. 2021で提案されたゼロショット多言語音素認識の手法として紹介。
- 多言語wav2vec 2.0を微調整し、調音特徴量で音素をマッピングする点が要旨と記載。
- モデルは音素列を出力し、単語化には辞書と言語モデルが必要と注意。
- transformersとphonemizer、espeak-ngを用いた英日音声の推論例を示し、出力例も掲載。

### Key Findings
- Wav2Vec2PhonemeはXuらの論文（2021）で提案されたと明記している。 [^]
  - Footnote: 「Wav2Vec2Phonemeモデルは...論文...において提案されました。」
- 多言語wav2vec 2.0を微調整し、調音特徴量で音素を対象言語へマッピングする手法を採用。 [^]
  - Footnote: 「多言語事前学習済みwav2vec 2.0モデルをファインチューニング...調音特徴量を用いて訓練言語の音素を対象言語にマッピング」
- モデル出力は音素列であり、単語列化には辞書と言語モデルが必要とされる。 [^]
  - Footnote: 「デフォルトでは、このモデルは音素の連続列を出力します。これらの音素を単語列に変換するには、辞書と言語モデルを使用する必要があります。」
- 公開モデルは約30で、Facebook系モデルがよく使われる可能性があると述べている。 [^]
  - Footnote: 「公開されているモデルは30個ほどある。おそらくFacebookのこの辺が良く使われているものかな？」
- 実行にはtransformers 4系とphonemizerが必要で、espeak-ngも必要と記載。 [^]
  - Footnote: 「transformersは4系で。あと、phonemizer がないと怒られる。」「espeak-ngも必要。」
- 英語音声の推論出力例として音素列が提示されている。 [^]
  - Footnote: 「出力 ɡ ə d m ɔːɹ n ɪ ŋ ð ə w ɛ ð ɚ ...」

### References
- https://zenn.dev/kun432/scraps/6bef4ce2d17200

## 音声をphoneに変換する「Allosaurus」を試す
- Date: 2026-03-10T20:49:00+09:00

### Executive Summary
- Allosaurusを使ったphone認識の試行記録で、公式説明と実験手順を整理。
- Allosaurusは2000以上の言語に対応する汎用音声認識システムと記載。
- ICASSP 2020の多言語アロフォンシステム研究を基盤とする旨を引用。
- モデルはlatestを自動ダウンロードし、モデルIDが大きいほど性能が高いと説明。
- 汎用モデルuni2005と英語専用eng2102など言語依存モデルの位置づけを整理。
- WAVモノラルで推論し、初回はモデル取得、英日出力と時間計測を掲載。
- 言語指定でphone集合を絞り精度向上の可能性があるが、言語非依存性は薄れると所感。

### Key Findings
- Allosaurusは2000以上の言語に対応する汎用音声認識システムと説明されている。 [^]
  - Footnote: 「Allosaurusは事前学習済みの汎用音声認識システムです。2000以上の言語における音声認識に対応しています。」
- ICASSP 2020の多言語アロフォンシステム研究を基盤としている。 [^]
  - Footnote: 「本ツールはICASSP 2020で発表した研究論文多言語アロフォンシステムによる汎用音声認識を基盤として開発されました。」
- latestモデルが初回推論時に自動ダウンロードされ、モデルIDが大きいほど性能が高いとされる。 [^]
  - Footnote: 「デフォルト値はlatest...初回の推論時に自動的に最新モデルがダウンロード」「一般的にモデルIDが大きいほど性能が優れていると考えられます。」
- 汎用モデルuni2005が既定で、言語依存モデルは自動ダウンロードされず--model指定が必要。 [^]
  - Footnote: 「この汎用モデルは言語に依存しない音素を予測...デフォルトでダウンロード・使用」「これらのモデルは自動ダウンロードされません...--modelフラグ」
- ライセンスはGPL-3.0と明記されている。 [^]
  - Footnote: 「ライセンスはGPL-3.0。」
- 入力はWAVモノラルが必要で、初回はモデル取得に時間がかかると記載。 [^]
  - Footnote: 「入力はWAVファイル・モノラルである必要がある。」「初回はモデルがダウンロードされるので少し時間がかかる。」
- 言語指定でphone集合を絞れるが、言語非依存の利点が薄れる可能性に言及。 [^]
  - Footnote: 「言語を指定すると言語ごとにこの範囲を絞る→認識精度が上がる場合がある」「これを指定しちゃうと言語に依存しないっていうメリットが薄れる」

### References
- https://zenn.dev/kun432/scraps/55734823dc0b52

## 「piper-plus」を試す
- Date: 2026-03-10T14:44:00+09:00

### Executive Summary
- ayousanz作成の軽量日本語TTS「piper-plus」を試用した記録。
- VITS採用のPiperフォークで、日本語/英語TTSやマルチスピーカー等の機能を列挙。
- 学習面ではWavLM DiscriminatorやFP16などの改善点をREADME抜粋で整理。
- Docker推論はtorch不足で失敗し、Python環境でもモジュール不足が続いた。
- torch追加後にONNX推論が成功し、CUDAプロバイダとリアルタイム係数をログで確認。
- WebUIはJSON命名とprosody_features不足でエラーに遭遇。
- Raspberry Pi 4Bでバイナリ推論が成功し、低スペック環境向けに有望とまとめ。

### Key Findings
- piper-plusはVITS採用のPiperフォークで、高速・高品質TTSと日英マルチスピーカー対応をうたう。 [^]
  - Footnote: 「高速・高品質なニューラルテキスト音声合成...VITS アーキテクチャを採用し、日本語・英語のマルチスピーカー音声合成に対応。Piper のフォーク」
- 日本語TTSはOpenJTalk統合と韻律情報、英語TTSはGPL-free G2Pなどの機能が列挙されている。 [^]
  - Footnote: 「日本語 TTS — OpenJTalk統合、韻律情報 (A1/A2/A3)...」「英語 TTS — GPL-free G2P...」
- 学習面ではWavLM DiscriminatorでMOS +0.15-0.25向上、FP16で速度2-3倍と記載。 [^]
  - Footnote: 「WavLM Discriminator — MOS +0.15-0.25 向上」「FP16 Mixed Precision — 学習速度2-3倍、メモリ約50%削減」
- プラットフォームはLinux x86_64/ARM64、macOS ARM64、Windows x64、WebAssembly対応と整理。 [^]
  - Footnote: 「Linux x86_64 / ARM64... macOS ARM64... Windows x64... Web WebAssembly」
- Docker推論はtorch不足で失敗し、事前ビルド済みイメージでも同様のエラーだった。 [^]
  - Footnote: 「ModuleNotFoundError: No module named 'torch'」「ちなみに事前ビルド済みイメージでも同じ結果」
- Python推論はモジュール不足が続いたが、torch追加後にCUDAプロバイダで実行できた。 [^]
  - Footnote: 「ModuleNotFoundError: No module named 'piper_train'」「ModuleNotFoundError: No module named 'torch'」「providers: ['CUDAExecutionProvider', 'CPUExecutionProvider']」
- WebUIではonnx.jsonの不足とprosody_features不足でエラーが発生した。 [^]
  - Footnote: 「Synthesis failed: ...onnx.json」「Required inputs (['prosody_features']) are missing」
- Raspberry Pi 4Bのバイナリ推論で辞書ダウンロード後に実行でき、速度面で有望と評価。 [^]
  - Footnote: 「Downloading OpenJTalk dictionary...」「[piper] [info] Real-time factor: 0.377...」「RPi でこの速度ならかなり使いやすそう。」

### References
- https://zenn.dev/kun432/scraps/449c8261ec0a58
