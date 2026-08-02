# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-08-02T09:01:54+09:00
- Articles: 3

## 「Qwen-Audio-3.0-ASR-Flash」を試す

### Executive Summary
- Alibaba の Qwen-Audio-3.0-ASR-Flash 系列を試したスクラップで、ASR の新モデル群の概要と実利用手順を整理している。
- モデルはリアルタイム向け、ファイル変換向け、短尺の非リアルタイム向けに分かれ、API 形式や話者ダイアライゼーション対応が異なる。
- 主な改善点として、文脈一貫性、専門用語認識、ホットワード、構造化テキスト化が挙げられている。
- 内部テストでは医療用語と工業用語の認識率が 90% 台半ばとされ、専門領域 ASR を意識した更新になっている。
- 著者は Alibaba Cloud の API キーとワークスペース ID を使い、HTTP API で日本語音声ファイルの文字起こしを試している。
- 5 分程度の音声では 15 から 20 秒程度で応答が返り、単語レベルのタイムスタンプを含む詳細な JSON が得られている。
- ただしファイルサイズ上限の記載に 2GB と 10MB の揺れがあり、著者は後者の可能性を疑っている。
- ホットワードとプロンプトコンテキストは、製品名、個人名、会話履歴、専門用語を使って認識精度を上げるための機能として整理されている。

### Key Findings
- Qwen-Audio-3.0-ASR-Flash は文脈理解と専門用語認識を強化した ASR モデルとして紹介されている。 [^]
  - Footnote: 記事冒頭で「より文脈理解力が向上し、専門分野特有の用語認識能力も強化」と説明されている。
- 内部テストでは医療用語 95.36%、工業用語 93.24% の認識率が示されている。 [^]
  - Footnote: 記事中の内部テスト結果に「医療用語の認識率：95.36%」「工業用語の認識率：93.24%」とある。
- モデルは streaming、filetrans、flash の 3 種類に分かれ、用途と API が異なる。 [^]
  - Footnote: 一覧表で streaming はリアルタイム WebSocket、filetrans と flash はオフライン HTTP と整理されている。
- 話者ダイアライゼーションは filetrans では対応、streaming と flash では非対応とされている。 [^]
  - Footnote: モデル表の話者ダイアライゼーション欄で filetrans のみ丸、他 2 モデルはバツになっている。
- ホットワードには事前コンパイル済みとインスタントの 2 種類があり、用途が異なる。 [^]
  - Footnote: 記事では安定した単語は事前コンパイル済み、セッション単位の一時語はインスタントホットワードと説明している。
- プロンプトコンテキストは会話履歴やドメイン固有テキストを認識精度向上に使う機能である。 [^]
  - Footnote: 機能説明表に、会話履歴やドメイン固有テキストをコンテキストとして利用して認識精度を高めるとある。
- 非リアルタイムの qwen-audio-3.0-asr-flash は同期 HTTP API で試されている。 [^]
  - Footnote: 著者は「HTTP APIを使った同期APIでの利用となるので curl で試す」と書いている。
- 実験では 5 分程度の日本語音声に対し 15 から 20 秒程度で応答が返っている。 [^]
  - Footnote: 試行結果として「15〜20秒程度で応答が返ってくる」と記載されている。

### References
- https://zenn.dev/kun432/scraps/310fca766482b2
- https://alibabacloud.com/help/en/model-studio/fun-asr-real-time-speech-recognition-api-reference
- https://alibabacloud.com/help/en/model-studio/fun-asr-recorded-speech-recognition-http-api
- https://alibabacloud.com/help/en/model-studio/non-real-time-speech-recognition-for-fun-asr-flash

## 「Audio8/Audio8-TTS-Preview-0.6b」を試す

### Executive Summary
- Audio8-TTS Preview 0.6B を Colaboratory L4 で試し、モデル仕様、性能、実行感を整理したスクラップである。
- モデルは 601M パラメータ規模で、11 言語、多言語音声生成、ゼロショット音声クローンに対応する。
- 44.1 kHz のニューラルオーディオコーデックが同梱され、追加のコーデックチェックポイントなしで参照音声のエンコードと波形デコードができる。
- ライセンスは Apache 2.0 で、著者は以前試した ASR モデルの CC-BY-NC-4.0 より扱いやすい点を評価している。
- Colab L4 では transformers を 4 系に調整して実行し、ロード直後の VRAM 消費は約 1.4GB と報告している。
- 参照音声なしの日本語 TTS は動作するが、再実行ごとに声が変わり、推論時間は 11 秒程度で速さには課題感がある。
- 参照音声を使った音声クローンの精度は良さそうだが、こちらも 10 数秒程度かかると述べている。
- クロスリンガルの音声クローンも生成できるものの、参照音声と言語を合わせた方が良さそうという所感が示されている。

### Key Findings
- Audio8-TTS Preview は 0.6B 級の小型 TTS モデルとして公開されている。 [^]
  - Footnote: 記事冒頭に「601Mパラメータ（コーデックを除く）」および「小型モデル。本格的な音声」とある。
- 対応言語は 11 言語で、日本語も含まれる。 [^]
  - Footnote: 対応言語一覧に広東語、中国語、英語、フランス語、日本語、韓国語など 11 言語が列挙されている。
- モデルは多言語音声生成とゼロショット音声クローンをサポートする。 [^]
  - Footnote: モデルカード抜粋に「多言語音声生成とゼロショット音声クローン機能をサポート」とある。
- Audio8 TTS は Fish Audio S2 Pro に着想を得た DualAR アーキテクチャを採用している。 [^]
  - Footnote: モデル詳細で「Fish Audio S2 Proに着想を得たDualARアーキテクチャ」と説明されている。
- Seed-TTS 評価では EN WER 1.506、ZH CER 0.950 という値が示されている。 [^]
  - Footnote: 評価表に Audio8 TTS Preview の EN WER / SIM が 1.506 / 63.2、ZH CER / SIM が 0.950 / 73.1 とある。
- ライセンスは Apache License 2.0 で公開されている。 [^]
  - Footnote: ライセンス欄に「コードおよびモデルの重み付けデータは、Apache License 2.0の下で公開」とある。
- Colab L4 でのロード直後の VRAM 消費は約 1.4GB と軽量である。 [^]
  - Footnote: 著者の nvidia-smi 出力に Memory-Usage が 1414MiB / 23034MiB と示されている。
- 参照音声なしの推論は約 11.2 秒で、著者はあまり速くないと評価している。 [^]
  - Footnote: 計測結果に Wall time: 11.2 s とあり、直後に「あまり速くはないかなぁ」と書かれている。
- クロスリンガル音声クローンは可能だが、自然さの点で参照と言語を合わせる方が良いとされている。 [^]
  - Footnote: 著者はクロスリンガル結果について「日本人英語・アメリカ人日本語みたいな雰囲気」とし、言語を合わせた方が良さそうと述べている。

### References
- https://zenn.dev/kun432/scraps/ab7b0d1e2d9f6e
- https://huggingface.co/Audio8/Audio8-TTS-Preview-0.6b
- https://github.com/Audio8-AI/Audio8_TTS
- https://audio8-ai.github.io/Audio8_TTS/

## 「LFM2.5-Encoder-230M / LFM2.5-Encoder-350M」を試す

### Executive Summary
- Liquid AI の LFM2.5-Encoder-230M と 350M を調べ、公式ブログ、モデルカード、Colab 実験をまとめたスクラップである。
- 両モデルは LFM2 バックボーンを双方向エンコーダ化したマスク言語モデルで、8,192 トークンの長文入力に対応する。
- 230M は制約の厳しい環境や高スループット向け、350M は精度重視向けという位置づけで説明されている。
- 用途は分類、意図判定、ポリシー検査、トークン分類、PII 検出、検索、再ランキングなどの裏方 NLP 処理が中心である。
- 公式評価では 350M が 17 タスク平均で 14 モデル中 4 位、230M が 6 位とされ、同サイズ帯で高い効率を示している。
- 長文推論では CPU 上で ModernBERT-base より高速とされ、8k 入力で約 3.3 から 3.7 倍速いという説明がある。
- 著者の Colab L4 実験では Flash Attention 2 を使って 350M をロードし、VRAM 消費は 1GB 弱だった。
- fill-mask の日本語例では「日本の首都」に対して京都を高スコアで返しており、日本語利用ではトークナイザーや用途設計への注意が必要と見ている。

### Key Findings
- LFM2.5-Encoder は長いコンテキストでも高速な双方向エンコーダとしてリリースされている。 [^]
  - Footnote: 記事冒頭に「長いコンテキストでも高速を維持する双方向エンコーダー」とある。
- 230M は 8,192 トークンで CPU 上の ModernBERT-base より約 3.7 倍高速とされる。 [^]
  - Footnote: Liquid AI の投稿引用に「8,192トークンでCPU上のModernBERT-baseより約3.7倍高速」とある。
- 350M は GLUE、SuperGLUE、多言語分類の比較で 14 モデル中 4 位と説明されている。 [^]
  - Footnote: 記事冒頭の引用に「14モデル中4位」とあり、評価表でも LFM2.5-Encoder-350M が 4 位に置かれている。
- 両モデルは 8,192 トークンのコンテキスト長を持ち、約 13 から 15 ページを 1 回の forward で扱えるとされている。 [^]
  - Footnote: 公式ブログまとめに「コンテキスト：8,192トークン、1回のフォワードパスで約13〜15ページ」とある。
- アーキテクチャは LFM2 を基盤に、双方向アテンション、非因果ショート畳み込み、30% マスク率の MLM に変更している。 [^]
  - Footnote: アーキテクチャ説明に、双方向マスク、非因果の短い畳み込み、30% のマスク率が挙げられている。
- 対応言語は 15 言語で、日本語も含まれる。 [^]
  - Footnote: モデルカード抜粋の対応言語に英語、ドイツ語、日本語、中国語など 15 言語が列挙されている。
- モデルは LFM Open License v1.0 で提供され、独自ライセンスへの注意が必要である。 [^]
  - Footnote: 著者は「LFMは独自ライセンスというところには注意」と書き、表にも LFM Open License v1.0 とある。
- Colab L4 で 350M を Flash Attention 2 付きでロードした際、VRAM 消費は 916MiB と報告されている。 [^]
  - Footnote: 著者の nvidia-smi 出力に Memory-Usage が 916MiB / 23034MiB と示されている。
- 日本語の fill-mask 例では「京都」が 0.691、「東京」が 0.100 となり、期待と異なる上位候補が出ている。 [^]
  - Footnote: スコア出力に「0.691: 京都」「0.100: 東京」とあり、著者は日本語ではトークナイザーの考慮が必要と述べている。

### References
- https://zenn.dev/kun432/scraps/d50bb98289f0d2
- https://huggingface.co/LiquidAI/LFM2.5-Encoder-230M
- https://huggingface.co/LiquidAI/LFM2.5-Encoder-350M
- https://www.liquid.ai/blog/lfm2-5-encoders
