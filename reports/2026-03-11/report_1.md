# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-11T13:58:47+09:00
- Articles: 3

## 音声を音素に変換する「Wav2Vec2Phoneme」 を試す
- Date: 2026-03-11T02:10:00+09:00

### Executive Summary
- 音声から音素（phoneme）を抽出するモデルを試した記録。
- phone と phoneme の違いを整理し、Allosaurusはphone認識だと説明。
- Wav2Vec2Phonemeはゼロショット多言語音素認識の研究に基づくと紹介。
- 出力は音素列で、単語列化には辞書と言語モデルが必要と注意。
- transformers 4系とphonemizer、さらにespeak-ngが必要と手順化。
- facebook/wav2vec2-lv-60-espeak-cv-ftで推論を実施。
- 英語・日本語の音声で出力を比較し、別モデルも試す意向。

### Key Findings
- phoneは実際の音の単位、phonemeは意味を分ける抽象単位として区別している。 [^]
  - Footnote: 「音声の細かい音の単位（phone）...言語の区別に使う抽象的な単位が『音素（phoneme）』」
- Wav2Vec2PhonemeはXu et al. (2021) のゼロショット多言語音素認識研究に基づく。 [^]
  - Footnote: 「Wav2Vec2Phonemeモデルは...論文『シンプルで効果的なゼロショット多言語音素認識』（Xu et al., 2021）において提案」
- デフォルト出力は音素列で、単語化には辞書と言語モデルが必要。 [^]
  - Footnote: 「デフォルトでは、このモデルは音素の連続列を出力します。これらの音素を単語列に変換するには、辞書と言語モデルを使用する必要があります。」
- 実行にはtransformers 4系とphonemizer、さらにespeak-ngが必要。 [^]
  - Footnote: 「transformersは4系で。あと、phonemizer がないと怒られる。... espeak-ngも必要。」
- 推論モデルとしてfacebook/wav2vec2-lv-60-espeak-cv-ftを使用。 [^]
  - Footnote: 「model_id = "facebook/wav2vec2-lv-60-espeak-cv-ft"」

### References
- https://zenn.dev/kun432/scraps/6bef4ce2d17200

## 音声をphoneに変換する「Allosaurus」を試す
- Date: 2026-03-11T00:38:00+09:00

### Executive Summary
- Allosaurusで音声をphone（音）に変換する検証記録。
- 2000以上の言語に対応する汎用phone認識器で、ICASSP 2020論文が基盤。
- モデルはlatestが自動ダウンロードされ、モデルIDで新しさの目安を説明。
- 汎用モデルuni2005がデフォルトで、言語依存モデルは手動取得。
- WAVモノラル入力でCLI実行し、初回はモデルDLが発生。
- 日本語でも推論し、処理時間や出力例を提示。
- 言語指定でphone範囲が絞られ精度向上の可能性がある一方、音が落ちる懸念も記述。

### Key Findings
- Allosaurusは2000以上の言語に対応する汎用phone認識器として説明されている。 [^]
  - Footnote: 「Allosaurusは事前学習済みの汎用音声認識システムです。2000以上の言語における音声認識に対応しています。」
- latestモデルは初回推論時に自動DLされ、モデルIDが新しさの目安とされる。 [^]
  - Footnote: 「初回の推論時に自動的に最新モデルがダウンロード...モデル名にはその訓練日が示されているため、一般的にモデルIDが大きいほど性能が優れている」
- 汎用モデルuni2005が最新でデフォルト、言語依存モデルはdownload_modelと--model指定が必要。 [^]
  - Footnote: 「uni2005...最新モデル...allosaurusがデフォルトでダウンロード・使用するモデル...これらのモデルは自動ダウンロードされません。...--modelフラグ」
- デフォルトはIPAの230 phoneを使い、言語指定で範囲を絞ると精度向上の可能性がある。 [^]
  - Footnote: 「デフォルト（ipa）だと IPAで定義されている全 230 phoneを使用するが、言語を指定すると...認識精度が上がる場合がある」
- CLI実行では初回にモデルDLが発生し、出力ログにdownloadが表示されている。 [^]
  - Footnote: 「downloading model  latest」

### References
- https://zenn.dev/kun432/scraps/55734823dc0b52

## 「piper-plus」を試す
- Date: 2026-03-11T02:12:00+09:00

### Executive Summary
- piper-plus（日本語対応軽量TTS）を試した記録。
- README抜粋でVITS採用、日英マルチスピーカー、Piperフォークでの強化を整理。
- OpenJTalk統合や韻律情報、音素入力、WebUI/C++/WebAssemblyなどの機能を列挙。
- プラットフォームやPyPIインストール手段を確認。
- Docker推論はtorch欠如で失敗し、事前ビルドでも同様だった。
- Python環境で再挑戦し、パス問題を経て推論ログと実行速度を確認。
- まとめとしてRPi等の低スペック環境で有用、更新頻度が高いと所感を記載。

### Key Findings
- piper-plusはVITS採用の高速・高品質TTSで、日本語・英語のマルチスピーカーに対応する。 [^]
  - Footnote: 「高速・高品質なニューラルテキスト音声合成 (TTS) システム。VITS アーキテクチャを採用し、日本語・英語のマルチスピーカー音声合成に対応。」
- 対応プラットフォームはLinux x86_64/ARM64、macOS ARM64のみ、Windows x64、WebAssemblyのブラウザ。 [^]
  - Footnote: 「Linux x86_64 / ARM64 フルサポート」「macOS ARM64 (Apple Silicon) のみ」「Windows x64 フルサポート」「Web WebAssembly Chrome/Edge/Firefox/Safari」
- piper-plus-baseは60,164発話・20話者・22,050Hzで、韻律や拡張音素を含む。 [^]
  - Footnote: 「学習データ: 60,164発話 (20話者)」「サンプリングレート: 22,050 Hz」「拡張音素... (65音素)」
- Docker推論はtorch欠如で失敗し、事前ビルド済みイメージでも同じ結果。 [^]
  - Footnote: 「ModuleNotFoundError: No module named 'torch'」「ちなみに事前ビルド済みイメージでも同じ結果となった。」
- 推論ログでreal-time factor 0.377...、infer 0.893s / audio 2.368sが記録されている。 [^]
  - Footnote: [2026-03-10 20:18:58.333] [piper] [info] Real-time factor: 0.37712958721564793 (infer=0.893207055 sec, audio=2.36843537414966 sec)

### References
- https://zenn.dev/kun432/scraps/449c8261ec0a58
