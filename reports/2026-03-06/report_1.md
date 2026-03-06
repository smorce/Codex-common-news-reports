# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-06T12:41:14+09:00
- Articles: 3

## Gemini-TTS で ストリーミング
- Date: 2026-03-06T12:12:00+09:00

### Executive Summary
- 過去検証でGemini TTSのストリーミングができず、再調査の記録。
- Google AI Studio経由では1チャンク返却でストリーミングにならないと明記。
- 短文でも約3秒かかり、リアルタイム用途には不向きと判断。
- Gemini 2.5 Flash/Proでも同様に1チャンクで変化なし。
- X投稿ではVertex AI経由ならストリーミングできた可能性が示唆された。
- 公式ドキュメントから、Gemini TTSはCloud Text-to-Speech APIとVertex AI APIの両方で利用可能と整理。
- API選定の指針を踏まえ、Vertex AI側での挙動確認を予定としている。

### Key Findings
- 以前の検証でもストリーミング不可で、今回も同様の問題意識で調査している。 [^]
  - Footnote: 本文: 「過去に以下で試したのだけど、」「ストリーミングできないな、と思って調べてみたけど、うーん・・・」
- Google AI Studioでは音声が1チャンクで返り、ストリーミングの意味がないと述べている。 [^]
  - Footnote: 本文: 「確かにまるっと1つのチャンクで返ってくるので、ストリーミングの意味がない。」
- 短い入力でも約3秒の待ちが発生し、遅延が問題になっている。 [^]
  - Footnote: 本文: 「以下のような短いものでもだいたい3秒ぐらいかかる。」
- Gemini 2.5 Flash/Proでもストリーミングは1チャンク返却のままだった。 [^]
  - Footnote: 本文: 「ストリーミングも試してみたけど、以前と変わらず1つのチャンクで返ってくる・・・・」
- Vertex AI経由ならストリーミングできる可能性があると推測している。 [^]
  - Footnote: 本文: 「確かに自分が試したのはGoogle AI Studioの方で、もしかしてVertexAIだとできるかも？」
- Gemini TTSは2つのAPI（Cloud Text-to-Speech / Vertex AI）から呼び出せると整理。 [^]
  - Footnote: 本文: 「ドキュメントを見ると、どうやら Gemini TTS は 2つのAPIから呼び出せるようになっているみたい。」
- Cloud Text-to-Speechは複数フォーマット指定が可能で、Vertex AIは固定1種と記載。 [^]
  - Footnote: 本文: 「複数の出力フォーマットに対応、これを指定できる（Vertex AI API は 固定の1つだけ）」

### References
- https://zenn.dev/kun432/scraps/7fcb7a51c8f8ad

## 「Phi-4-reasoning-vision」を試す
- Date: 2026-03-05T21:39:00+09:00

### Executive Summary
- MicrosoftのPhi-4-reasoning-vision-15Bを取り上げ、概要と所感をまとめたスクラップ。
- 画像・文字を見て推論するマルチモーダル推論モデルである点を強調。
- mid-fusion構成とSigLIP-2 + Phi-4-Reasoningの組み合わせが説明されている。
- 高解像度画像ではDynamic resolutionの有利さと最大トークン数の言及がある。
- 2000億トークン規模の学習やデータ品質改善（GPT-4o等による修正）を紹介。
- thinking_modeの挙動（hybrid/think/nothink）を実験し、出力差を確認。
- 自身の試用ではリソース増に見合う性能が確認できず、結果に不満を示している。

### Key Findings
- モデルは画像・文字を見て推論するマルチモーダル推論モデルと説明されている。 [^]
  - Footnote: 本文: 「画像や画面（スクショとか）を「見る」」「そのうえで「ちゃんと考える（推論する）」」「ってことができるマルチモーダル推論モデルだよ。」
- モデル規模は約150億パラメータと記載。 [^]
  - Footnote: 本文: 「サイズは 150億パラメータくらい」
- アーキテクチャはmid-fusionを採用し、SigLIP-2とPhi-4-Reasoningを組み合わせている。 [^]
  - Footnote: 本文: 「Phi-4-reasoning-vision-15B は mid-fusion を採用してる。」「画像側：まず「SigLIP-2」」「テキスト側：Phi-4-Reasoning」
- 高解像度対応ではDynamic resolutionのビジョンエンコーダが最良と述べている。 [^]
  - Footnote: 本文: 「動的解像度（Dynamic resolution）のビジョンエンコーダが一番良かった」
- 最大3600程度のビジュアルトークン設定が高解像度画面で有効と記載。 [^]
  - Footnote: 本文: 「最大 3600 トークンくらいビジュアルトークン使える設定が、高解像な画面でかなり効く」
- 学習データは約2000億トークン規模で、品質改善にGPT-4o等を使っている。 [^]
  - Footnote: 本文: 「マルチモーダル 2000億トークンくらい」「回答がダメなやつは GPT-4o や o4-mini で回答を修正」
- 思考モードの切り替え（hybrid/think/nothink）の使い分けが示されている。 [^]
  - Footnote: 本文: 「基本は "hybrid"」「"think" で Reasoning強制、"nothink" で Reasoningさせない」
- 試用結果として、リソース増に見合う性能が確認できず失望感を示している。 [^]
  - Footnote: 本文: 「サイズは大きくなって求められるリソースが厳しくなった」「それに見合うだけの性能を全然確認できない」「かなり残念。」

### References
- https://zenn.dev/kun432/scraps/2a7889fb91d3bf
- https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/

## GSV-TTS-Lite
- Date: 2026-03-05T17:25:00+09:00

### Executive Summary
- GPT-SoVITS向けの高性能推論エンジンとしてGSV-TTS-Liteを紹介。
- RTX 3050環境での遅延問題を背景に、V2Proベースで最適化した経緯が説明されている。
- 低メモリ環境でミリ秒単位のリアルタイム応答を実現すると主張。
- 音声トーン/スタイル分離、字幕タイムスタンプ同期、トーン転移などの機能を列挙。
- PyPIの`gsv-tts-lite`として公開され、日中英対応・V2Pro系モデルをサポート。
- TTFT/RTF/VRAMの比較で2.9〜3.3倍高速化、メモリ半減と記載。
- v2Pro系列のみ対応で、モデル構成の不確実性や検証保留点にも触れている。

### Key Findings
- GPT-SoVITS専用の高性能推論エンジンとして位置付けられている。 [^]
  - Footnote: 本文: 「GPT-SoVITSテキスト音声合成モデル専用に設計された高性能推論エンジン」
- RTX 3050ノートでの遅延問題が開発動機となった。 [^]
  - Footnote: 本文: 「RTX 3050 (ノートPC) の計算リソースの制約により、推論遅延がリアルタイムインタラクションの要件を満たすのが困難」
- GPT-SoVITS V2Proをベースにした推論バックエンドと明記。 [^]
  - Footnote: 本文: 「GPT-SoVITS V2Pro をベースとした推論バックエンド」
- 低メモリ環境でもミリ秒単位のリアルタイム応答を実現したと記載。 [^]
  - Footnote: 本文: 「低メモリ環境下でもミリ秒単位のリアルタイム応答を実現しました。」
- トーン/スタイル分離、字幕同期、トーン転移などの機能を搭載。 [^]
  - Footnote: 本文: 「音声トーンとスタイルの分離制御」「字幕のタイムスタンプ同期」「音声トーンの転移」
- PyPIで`gsv-tts-lite`として公開され、pipで導入可能。 [^]
  - Footnote: 本文: 「gsv-tts-lite ライブラリとして PyPI で公開」「pip コマンドで簡単にインストール可能」
- 対応言語は日本語・中国語・英語で、V2Pro/V2ProPlus対応。 [^]
  - Footnote: 本文: 「日本語・中国語・英語」「対応するモデルは V2Pro、V2ProPlus」
- 性能比較でTTFTやRTF、VRAMが改善し、2.9〜3.3倍高速化と示している。 [^]
  - Footnote: 本文: 「436 ms」「150 ms」「133 ms」「0.381」「0.125」「0.108」「⚡ 2.9倍」「🔥 3.3倍」
- Flash Attentionの有効化を強く推奨している。 [^]
  - Footnote: 本文: 「Flash Attention 機能の有効化を強く推奨します。」
- ライセンスはMITと明記。 [^]
  - Footnote: 本文: 「ライセンスはMITライセンス。」
- GSV-TTS-Liteはv2Pro系列のみ対応で、v2Proがv4より良いとの所感を記載。 [^]
  - Footnote: 本文: 「GSV-TTS-Lite でサポートしているのは v2Pro シリーズ（v2Pro / v2Pro Plus）のみ」「v2Pro は v4 よりも良い様子。」

### References
- https://zenn.dev/kun432/scraps/7e3ca20615d5f3
- https://github.com/chinokikiss/GSV-TTS-Lite?tab=readme-ov-file
