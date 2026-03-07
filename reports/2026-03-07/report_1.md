# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-07T09:01:59.9846539
- Articles: 3

## 「sherpa-onnx」を試す
- Date: 2026-03-07T08:37:00

### Executive Summary
- ウェイクワード/キーワード検出を試す動機で、軽量な sherpa-onnx を調査している。
- sherpa-onnx は Kaldi 後継の k2-fsa 系プロジェクト群の一部という位置づけ。
- k2 は基盤、icefall は学習レシピ、sherpa/sherpa-onnx は推論実行という役割分担が示されている。
- 「next-gen Kaldi」と表現されるが、Kaldi そのものとは同一ではないと整理している。
- sherpa-onnx は ONNX Runtime を使い、オフラインで音声認識や音声合成などを動かせる旨が記載されている。
- 用途によって icefall と sherpa-onnx を見分けるべき、という整理が中心。
- 関連リポジトリとして k2-fsa/sherpa-onnx の GitHub が引用されている。

### Key Findings
- ウェイクワード/キーワード検出のために sherpa-onnx の軽量性に注目している。 [^]
  - Footnote: 「ウェイクワード / キーワード検出を試したくて、いろいろ調べてみたら、sherpa-onnxが軽量で良いらしく」
- sherpa-onnx は Kaldi 後継の k2-fsa プロジェクト群の一部と捉えている。 [^]
  - Footnote: 「どうやらKaldiの後継である k2-fsa の中の1つのプロジェクトらしい？」
- k2 が基盤、icefall がレシピ、sherpa/sherpa-onnx が推論実行という分担が説明されている。 [^]
  - Footnote: 「k2 は基盤、icefall は学習や実験のためのレシピ集、sherpa や sherpa-onnx は学習済みモデルを実際に動かすための実行側」
- 「next-gen Kaldi」と呼ばれるが、Kaldi と同一ではないと整理している。 [^]
  - Footnote: 「“next-gen Kaldi” という表現が使われています。ただし、Kaldi そのものと同一ではなく」
- sherpa-onnx は ONNX Runtime を用い、オフラインでASR/TTSなどを動かせると案内されている。 [^]
  - Footnote: 「sherpa-onnx は、ONNX Runtime を使い、インターネット接続なしでも音声認識、音声合成、話者分離、音声区間検出などを」

### References
- https://zenn.dev/kun432/scraps/1fdc08e096e8b7

## Gemini-TTS で ストリーミング（Vertex AI）
- Date: 2026-03-06T13:51:00

### Executive Summary
- 過去の試行ではストリーミングできず、調査しても芳しくない印象だった。
- Google AI Studio では 1 チャンクで返るためストリーミングの意味がないと記述している。
- 短い入力でも応答が遅く、体感で数秒かかると述べている。
- ストリーミング再試行でも 1 チャンクの挙動は変わらなかった。
- その結果、リアルタイム用途では使いにくいという結論になっている。
- 一方で Vertex AI では期待どおりにストリーミングが動作するとまとめている。
- 従来との差分確認の観点で、ストリーミング可否が焦点になっている。

### Key Findings
- 以前の試行でストリーミングできず、調べても納得感が薄かった。 [^]
  - Footnote: 「ストリーミングできないな、と思って調べてみたけど、うーん・・・」
- Google AI Studio では 1 チャンク返却でストリーミングの意味がないと記述している。 [^]
  - Footnote: 「まるっと1つのチャンクで返ってくるので、ストリーミングの意味がない」
- 短い入力でも体感で約3秒かかると述べている。 [^]
  - Footnote: 「以下のような短いものでもだいたい3秒ぐらいかかる。」
- ストリーミングを再試行しても 1 チャンクの挙動は変わらない。 [^]
  - Footnote: 「ストリーミングも試してみたけど、以前と変わらず1つのチャンクで返ってくる・・・・」
- リアルタイム用途には使いにくいという評価になっている。 [^]
  - Footnote: 「実質非ストリーミングでリアルタイム用途では使いにくかった」
- Vertex AI では期待どおりにストリーミングが動作するとまとめている。 [^]
  - Footnote: 「Vertex AI なら 期待したとおりに ストリーミングが動作する」

### References
- https://zenn.dev/kun432/scraps/7fcb7a51c8f8ad

## 「Phi-4-reasoning-vision」を試す
- Date: 2026-03-05T21:39:00

### Executive Summary
- Phi-4-reasoning-vision-15B について試した結果の所感をまとめている。
- モデルサイズが大きく、必要リソースが厳しくなったと述べている。
- 性能がそれに見合うほど確認できないという評価を示している。
- 日本語対応は Hugging Face に記載があると触れつつ、結果が悪いことに疑念を持っている。
- Transformers 以外に vLLM や Azure Foundry でも利用できるらしいと記載。
- 結果が正しいなら残念、という結論で締めている。
- VLM は高価で遅く展開しにくいが、Phi-4-reasoning-vision はそれを緩和する狙いが引用されている。

### Key Findings
- サイズが大きくなり、必要リソースが厳しくなったと述べている。 [^]
  - Footnote: 「サイズは大きくなって求められるリソースが厳しくなった」
- 性能がそれに見合うほど確認できないと評価している。 [^]
  - Footnote: 「にも関わらず、それに見合うだけの性能を全然確認できない」
- 結果が悪すぎるため、自分のミスを疑うほどだと述べている。 [^]
  - Footnote: 「あまりにもダメな結果なので、自分がなにかミスってるんじゃなかろうか？」
- 日本語対応は Hugging Face に書いてあると触れている。 [^]
  - Footnote: 「日本語にも対応、というのはHuggingFaceにも書いてあるし」
- Transformers 以外に vLLM や Azure Foundry でも使えるらしいと記載。 [^]
  - Footnote: 「Transformers以外にもvLLMと、あとAzure Foundry でも使えるらしい」
- 結果が正しいならかなり残念という結論に至っている。 [^]
  - Footnote: 「この結果が正しい結果だと、かなり残念。」
- VLM は遅く高価で展開しにくいが、Phi-4-reasoning-vision-15B はそれを緩和する狙いが引用されている。 [^]
  - Footnote: 「ビジョン言語モデルは…遅く、高価で、展開しにくく…Phi-4-reasoning-vision-15B…限界を軽減する」

### References
- https://zenn.dev/kun432/scraps/2a7889fb91d3bf
