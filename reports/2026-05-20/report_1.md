# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-20T09:08:56+09:00
- Articles: 3

## 「Colima」を試す

### Executive Summary
- Colima は macOS と Linux 向けのコンテナランタイムとして紹介されている。
- 最小限の設定で動くことを重視し、CLI と既定値が扱いやすい点が強調されている。
- Intel Mac、Apple Silicon Mac、Linux の各環境に対応する。
- Docker、Containerd、Incus など複数のランタイムを扱える。
- Docker と Containerd では Kubernetes の利用も選択肢として示されている。
- ポートフォワード、ボリュームマウント、複数インスタンス実行など日常利用向けの機能がある。
- 内部的には Lima で VM を起動し、その上でコンテナを動かす構成だと筆者は理解している。

### Key Findings
- Colima は macOS と Linux で使える軽量なコンテナランタイムとして位置づけられている。 [^]
  - Footnote: 記事内で「macOS（およびLinux）向けの最小限の設定で動作するコンテナランタイム」と説明されている。
- 対応環境は Intel Mac、Apple Silicon Mac、Linux を含む。 [^]
  - Footnote: 主な機能として「IntelプロセッサおよびApple Silicon搭載のmacOS、およびLinux環境に対応」と記載されている。
- 複数ランタイムをサポートし、用途に応じた選択ができる。 [^]
  - Footnote: Docker、Containerd、Incus がサポート対象として列挙されている。
- Docker と Containerd では Kubernetes もオプションで利用できる。 [^]
  - Footnote: 記事では「Docker（オプションでKubernetesも利用可能）」「Containerd（オプションでKubernetesも利用可能）」とされている。
- 開発時に便利なネットワークとファイル共有機能を備えている。 [^]
  - Footnote: 主な機能に「自動ポートフォワード機能」「ボリュームマウント機能」が含まれている。
- Colima の実体は Lima 上に VM を立ててコンテナを動かす方式だと説明されている。 [^]
  - Footnote: 筆者は「裏ではLimaを使ってVMを立ち上げてそこでコンテナを動かす」と述べている。

### References
- https://zenn.dev/kun432/scraps/7e0becc836485f
- https://github.com/abiosoft/colima

## プロバイダ・フレームワーク等のResponses API 対応状況

### Executive Summary
- OpenAI 互換 API の多くは Chat Completions API 中心で、Responses API への完全対応は限定的だと整理している。
- 筆者は Responses API をエージェント用途で望ましい API と見ている。
- Chat Completions 的なステートレス API と同じ感覚で理解すると難しいという所感が述べられている。
- Open Responses は Responses API の標準化を目指す取り組みとして紹介されている。
- Fireworks AI、OpenRouter、Ollama、LiteLLM、llama.cpp、AWS Bedrock など複数実装の対応状況が比較されている。
- ステートフル対応、サーバサイド MCP、ビルトインツール対応の有無が重要な比較軸になっている。
- 筆者は Fireworks AI、LiteLLM、teabranch/open-responses-server、llama.cpp の今後に注目している。
- LM Studio、Oracle OCI、Portkey など後続コメントで Open Responses 準拠や Responses API 対応の追加情報もまとめられている。

### Key Findings
- Responses API の完全互換は Chat Completions API より難しいと見られている。 [^]
  - Footnote: 冒頭で「Responses API はサーバサイドでの処理も多いので、完全互換が難しい」と述べている。
- Responses API はエージェント向けには有利な選択肢と評価されている。 [^]
  - Footnote: 記事内に「エージェント向けにはResponses APIのほうが色々望ましい」とある。
- Open Responses は Responses API の標準化を目指す動きとして紹介されている。 [^]
  - Footnote: Open Responses について「Responses API の標準化を目指すもの」と説明している。
- OpenRouter はベータ扱いで、ステートフルには非対応と整理されている。 [^]
  - Footnote: OpenRouter の項目で「ベータ扱い」「ステートレスのみで、ステートフルには非対応」と記載されている。
- Fireworks AI はステートフルやサーバサイド MCP 対応があり、有力候補として見られている。 [^]
  - Footnote: Fireworks AI の項目に「ステートフルにも対応」「サーバサイドMCPや previous_response_id に対応」とあり、まとめで「一番それっぽさがありそう」と述べている。
- Ollama は Responses API をサポートするが、previous_response_id や conversation は非対応とされている。 [^]
  - Footnote: Ollama の項目で「一応サポート」「ただしステートフルには非対応（previous_response_id / conversation）」と書かれている。
- LiteLLM は Responses エンドポイントを Chat Completions に変換する形の対応もある。 [^]
  - Footnote: LiteLLM の項目で「Responses エンドポイントへのアクセスをChat Completions に変換するような対応がある」と記載されている。
- Portkey は全プロバイダーで Open Responses フル準拠をうたいつつ、ネイティブ処理と内部変換を使い分ける。 [^]
  - Footnote: Portkey の項目で「全てのプロバイダーで機能」「ネイティブにResponses APIで処理するものと、内部でChat Completionsに変換するものがある」と説明されている。

### References
- https://zenn.dev/kun432/scraps/f47b43e1b9f845

## 「Irodori-TTS-Server」を試す

### Executive Summary
- Irodori-TTS-Server は Irodori-TTS を OpenAI Text-to-Speech API 互換で使うためのサーバとして紹介されている。
- アプリへ組み込みやすくする目的で API サーバが用意されていると説明されている。
- 対象モデルは Irodori-TTS 500M v3 ベースモデルである。
- リファレンス音声によるボイスクローン、OpenAI 形式の応答、長文分割に対応する。
- ストリーミング合成は未実装で、リクエストごとに完全な音声応答を返す。
- Docker とソースインストールの二通りがあり、記事では Ubuntu 22.04 と RTX 4090 の Docker 環境で試している。
- 初回はモデルダウンロードで時間がかかるが、再実行時の curl 例では約0.473秒の実行時間が示されている。
- OpenAI Python SDK からも利用できるが、筆者は SDK のオーバーヘッドがやや気になると述べている。

### Key Findings
- Irodori-TTS-Server は OpenAI TTS API 互換サーバとして提供されている。 [^]
  - Footnote: README 抜粋として「Irodori-TTS に対応したOpenAI Text-to-Speech API互換サーバー」と記載されている。
- リファレンス音声を使ったボイスクローンに対応する。 [^]
  - Footnote: 機能説明で「リファレンス音声によるボイスクローン機能」をサポートするとある。
- 出力形式は複数の音声フォーマットに対応している。 [^]
  - Footnote: 機能概要に「wav、mp3、flac、opus、aac、pcm」が対応出力フォーマットとして列挙されている。
- 長文入力は自動分割処理できる。 [^]
  - Footnote: 機能概要に「長文テキストの自動分割処理機能」とある。
- ストリーミング合成は実装されていない。 [^]
  - Footnote: 記事では「ストリーミング合成機能は実装していません」と明記されている。
- 実用的な推論には NVIDIA GPU の利用が推奨されている。 [^]
  - Footnote: 動作要件の説明で「実用的な推論を行うには、NVIDIA GPUの使用を推奨」と記載されている。
- Docker での起動例では Uvicorn が 8088 番ポートで立ち上がる。 [^]
  - Footnote: 起動ログに「Uvicorn running on http://0.0.0.0:8088」とある。
- モデル取得後の curl 実行は記事の例で約0.473秒だった。 [^]
  - Footnote: 再実行時の出力として「real 0m0.473s」が示されている。

### References
- https://zenn.dev/kun432/scraps/27a96c1a3d3f7e
- https://github.com/Aratako/Irodori-TTS-Server
