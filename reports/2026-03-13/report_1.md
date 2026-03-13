# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-13T10:38:46.9244810+09:00
- Articles: 3

## 「ibm-granite/granite-4.0-1b-speech」を試す
- Date: 2026-03-12T23:17:00+09:00

### Executive Summary
- IBMのGranite-4.0-1b-speechのモデルカード要約を日本語訳で整理している。
- 多言語ASRと双方向音声翻訳(AST)に特化した小型音声言語モデルと位置付け。
- 公開コーパスと日本語ASR/キーワード/音声翻訳向け合成データで学習。
- 英語ASR精度や推論速度の改善、パラメータ削減などの改良点を列挙。
- Open ASRリーダーボードのWERやRTFxなど評価値を掲載。
- リリース日・ライセンス・対応言語・想定用途を明記。
- アーキ構成、学習データ、インフラ、倫理的配慮と安全策も記載。

### Key Findings
- 多言語ASR/AST向けの小型音声言語モデルとして設計。 [^]
  - Footnote: 多言語対応の自動音声認識（ASR）と双方向自動音声翻訳（AST）に特化
- 公開コーパスと日本語ASR/キーワード/音声翻訳の合成データで学習。 [^]
  - Footnote: 公開コーパス群、および日本語 ASR、キーワード重視型 ASR、音声翻訳をサポートするために特別に作成された合成データセット
- 改良点は多言語対応、英語ASR精度・推論速度向上、パラメータ半減、キーワードバイアス追加。 [^]
  - Footnote: 多言語音声入力に対応 / 半分のパラメータ数 / キーワードリストバイアス機能
- Open ASRリーダーボードで平均WER 5.52、RTFx 280.02などの数値を提示。 [^]
  - Footnote: 平均WER 5.52 / RTFx 280.02
- リリース日は2026年3月6日、ライセンスはApache 2.0。 [^]
  - Footnote: リリース日: 2026年3月6日 / ライセンス: Apache 2.0
- 英仏独西葡日などを対象に音声→テキストや音声翻訳を想定。 [^]
  - Footnote: 英語、フランス語、ドイツ語、スペイン語、ポルトガル語、日本語
- 音声エンコーダは16層ConformerのCTC、q-formerで10倍ダウンサンプル。 [^]
  - Footnote: 16個の conformer ブロック / 総合的な時間軸ダウンサンプリング係数は10倍
- H100搭載のBlue Velaで学習、8台GPUで30日と記載。 [^]
  - Footnote: H100 GPU / 8台の H100 GPU / 30日間

### References
- https://zenn.dev/kun432/scraps/1a1f9362662e9d
- https://huggingface.co/ibm-granite/granite-4.0-1b-speech
- https://arxiv.org/abs/2505.08699

## 音声を音素に変換する「Wav2Vec2Phoneme」 を試す
- Date: 2026-03-12T23:58:00+09:00

### Executive Summary
- phoneとphonemeの違いを整理し、音声→音素抽出を試すスクラップ。
- Wav2Vec2Phonemeはゼロショット多言語音素認識の論文に基づくと説明。
- モデルは音素列を出力し、単語化には辞書と言語モデルが必要と述べる。
- Hugging Faceの音素認識モデル一覧や代表モデルを参照。
- Colabでtransformers/phonemizer/espeak-ngを使った実行手順を記載。
- 英語・日本語の推論例と出力を比較し、欠落があると所感。
- まとめでphone/phonemeの使い分け、IPAの扱いの難しさに言及。

### Key Findings
- phoneは言語非依存の音、phonemeは言語依存の抽象単位として区別。 [^]
  - Footnote: phone と phoneme は違う / phoneme は言語に依存するが、phoneは基本的に依存しない
- Wav2Vec2PhonemeはXu et al. 2021のゼロショット多言語音素認識論文に基づく。 [^]
  - Footnote: 「シンプルで効果的なゼロショット多言語音素認識」（Xu et al., 2021）
- 音素列→単語列には辞書と言語モデルが必要。 [^]
  - Footnote: 音素の連続列を出力 / 辞書と言語モデルを使用する必要
- 実行にはtransformers 4系とphonemizer、espeak-ngの導入が必要と記載。 [^]
  - Footnote: transformers==4.57.6 / phonemizer / espeak-ng
- 公開モデルは約30件で、Facebookのモデルがよく使われる印象と述べる。 [^]
  - Footnote: 公開されているモデルは30個ほどある / Facebookのこの辺が良く使われているものかな？
- 日本語例では冒頭や途中が欠ける印象、短く切ると改善した。 [^]
  - Footnote: 冒頭とあと途中が抜けているような感 / duration 2.0
- Qiita記事の結果も踏まえると精度は高くない印象とまとめ。 [^]
  - Footnote: そこまで精度が良さそうという感はなさそう

### References
- https://zenn.dev/kun432/scraps/6bef4ce2d17200
- https://huggingface.co/docs/transformers/model_doc/wav2vec2_phoneme
- https://huggingface.co/papers/2109.11680
- https://qiita.com/shimajiroxyz/items/818ee21afbf6214e4e53

## 音声をphoneに変換する「Allosaurus」を試す
- Date: 2026-03-11T00:38:00+09:00

### Executive Summary
- Allosaurusで音声をphoneに変換する手順と所感をまとめた。
- 2000+言語対応の汎用phone recognizerで、ICASSP 2020論文が基盤。
- モデルは初回推論で最新を自動DLし、汎用モデルと言語特化モデルがある。
- WAVモノラル入力でCLI実行し、英語/日本語のIPA出力例を掲載。
- Python APIでの推論例と実行時間計測も示す。
- 言語指定でIPAの範囲を絞れるが、出力差や欠落の可能性に触れる。
- IPAから音声生成の難しさやespeak-ngの制約にも言及。

### Key Findings
- Allosaurusは2000以上の言語向け汎用phone recognizer。 [^]
  - Footnote: pretrained universal phone recognizer for more than 2000 languages
- ICASSP 2020の研究に基づく。 [^]
  - Footnote: ICASSP 2020で発表した研究論文
- デフォルトlatestが自動DL、モデル名は訓練日で大きいIDが高性能と説明。 [^]
  - Footnote: デフォルト値は latest / モデル名にはその訓練日
- 汎用モデルuni2005、英語特化eng2102など言語依存モデルがある。 [^]
  - Footnote: uni2005 / eng2102
- 入力はWAVモノラルで実行し、初回はモデルDLで時間がかかる。 [^]
  - Footnote: 入力はWAVファイル・モノラル / 初回はモデルがダウンロード
- 言語指定でIPA 230 phoneから言語別に絞り、精度向上の可能性がある。 [^]
  - Footnote: IPAで定義されている全 230 phone / 言語を指定すると言語ごとにこの範囲を絞る
- 言語指定で出力が変わり、音が落ちる可能性もあると所感。 [^]
  - Footnote: ちょっと違っている / いくつか音が落ちてるような気がする
- IPAから音声生成は限定的で、espeak-ngは記号未対応や自然さ課題がある。 [^]
  - Footnote: IPA記号を全てカバーしていない / 自然な発話には足りない

### References
- https://zenn.dev/kun432/scraps/55734823dc0b52
- https://github.com/xinjli/allosaurus
- https://arxiv.org/pdf/2002.11800.pdf
