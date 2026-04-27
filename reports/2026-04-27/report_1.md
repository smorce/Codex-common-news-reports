# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-04-27T09:18:53.2405645+09:00
- Articles: 3

## 「Soniox Text-to-Speech」を試す ③Real-time API
- Date: 2026-04-26T21:44:00+09:00

### Executive Summary
- Soniox TTS の Real-time API を中心に整理している。
- API は WebSocket ベースで双方向ストリーミングに対応する。
- 最初に音声タイプと出力形式を決め、その後はテキストをチャンク送信する。
- 入力は text と text_end を使って段階的に送る。
- 出力音声は base64 の audio チャンクとして順次返る。
- LLM のストリーミング出力と相性がよい構成として説明している。
- 実験コードでは sounddevice による再生とログ出力を追加している。

### Key Findings
- Real-time API は WebSocket で動作し、入力も出力もストリーミングできる。 [^]
  - Footnote: 本文で「リアルタイムAPIはWebSocketで行われ、入出力共にストリーミングに対応」と説明している。
- ストリーム開始時に音声タイプと音声出力形式を一度だけ設定する。 [^]
  - Footnote: 最初に voice と audio format を選び、その後は双方向ストリームとして扱う流れが示されている。
- テキストは小さなチャンクで送り、最後に text_end を立てる。 [^]
  - Footnote: コード例で text と text_end の組み合わせを使って段階送信する構成が示されている。
- 音声は audio ペイロードとして返り、逐次再生やバッファリングができる。 [^]
  - Footnote: 受信データは base64 の audio チャンクとして返り、デコードして再生できると書かれている。
- LLM のトークン列と組み合わせると、応答生成中に音声再生を先行できる。 [^]
  - Footnote: 「完全な応答をバッファリングすることなく音声出力」できる点が強調されている。
- 長時間無通信だと切断される可能性があり、Keep Alive が必要になる。 [^]
  - Footnote: 末尾で、送信が止まると接続が切れる可能性があるため Keep Alive が必要と述べている。

### References
- https://zenn.dev/kun432/scraps/1f0ddb4469b766
- https://soniox.com/docs/tts/rt/real-time-generation

## 「Soniox Text-to-Speech」を試す ②共通コンセプト
- Date: 2026-04-26T20:40:00+09:00

### Executive Summary
- Soniox TTS の共通前提をまとめた回。
- 音声は 12 種類あり、全言語で利用できる。
- 同じ音声モデルなら、言語が変わっても声質は一貫する。
- 現時点の主要モデルは tts-rt-v1-preview である。
- ハルシネーション抑制や英数字処理の強さを特徴としている。
- 音声フォーマットやサンプリング周波数、ビットレートを調整できる。
- ただし 1 リクエスト / 1 セッションで使える言語は 1 つに限られる。

### Key Findings
- 現時点で 12 種類の音声があり、全言語で使える。 [^]
  - Footnote: 本文で「現時点で12種類の音声」とし、全言語で利用可能と整理している。
- 同じ音声モデルなら、どの言語でも声や表現のスタイルが揃う。 [^]
  - Footnote: 「一貫した音声特性」として、言語間で特性が変わらないと述べている。
- 対応モデルは tts-rt-v1-preview のみで、プレビュー版扱いである。 [^]
  - Footnote: 「現時点でサポートしているモデルは tts-rt-v1-preview のみ」と明記している。
- 音声生成は文末を待たずにストリーミング開始できる。 [^]
  - Footnote: 特徴として「文の終了を待たずにストリーミングで生成」と説明している。
- 音声フォーマットは複数あり、サンプリングとビットレートを指定できる。 [^]
  - Footnote: 音声フォーマット表で、各形式の作成単位と調整可能項目が示されている。
- コードスイッチングには未対応で、同一リクエストやセッションでは 1 言語のみ。 [^]
  - Footnote: 本文で「同一のリクエストまたは同一セッション内で利用可能な言語は1つ」と説明している。

### References
- https://zenn.dev/kun432/scraps/c06d3eb045a8f0
- https://soniox.com/docs/tts/concepts/voices
- https://soniox.com/docs/tts/models
- https://soniox.com/docs/tts/concepts/supported-languages

## メモ: Qwen-Image-2.0-pro
- Date: 2026-04-25T22:20:00+09:00

### Executive Summary
- Qwen-Image-2.0-Pro の公開メモをまとめている。
- 画像品質、テキスト描画、指示追従が改善されたと紹介している。
- スタイル間の性能差も縮ましたと説明している。
- Text-to-Image の arena では世界 #9 とされる。
- 利用先として ModelScope と Alibaba Cloud の API を挙げている。
- 日本語化したサンプルを試し、かなり自然だと評価している。
- ただし一部に中国語表記が残るなど、まだ揺れはある。

### Key Findings
- 公開直後の情報として、画像品質と多言語テキスト描画の改善を強調している。 [^]
  - Footnote: 引用部分で「画像品質、多言語テキストのレンダリング、指示追従」を新たなレベルにしたと述べている。
- Text-to-Image の arena で世界ランキング #9 を獲得したと書いている。 [^]
  - Footnote: 本文に「@arena での Text-to-Image において世界ランキング #9」とある。
- 公開手段は ModelScope と Alibaba Cloud の API で、オープンモデルではないと見ている。 [^]
  - Footnote: コメントで「オープンモデルでなく、API提供」と整理している。
- 日本語化したサンプルでも、元の構図にかなり近い出力が得られた。 [^]
  - Footnote: 「だいぶそれっぽくになってる」とし、翻訳サンプルの再現性を評価している。
- 一方で、中国語の漢字表記が残るなど、完全な日本語化にはまだ課題がある。 [^]
  - Footnote: 結果の説明で「ところどころ中国語の漢字表記」と明言している。

### References
- https://zenn.dev/kun432/scraps/b3dd8c9b3ea9c2
- https://modelscope.ai/studios/Qwen/Qwen-Image-2.0-pro
- https://modelstudio.console.alibabacloud.com/ap-southeast-1?tab=doc#/doc/?type=model&url=2840914_2&modelId=qwen-image-2.0-pro-2026-04-22&serviceSite=international
