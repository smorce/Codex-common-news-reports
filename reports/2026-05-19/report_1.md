# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-19T00:00:00+09:00
- Articles: 3

## 「Colima」を試す

### Executive Summary
- Colima は macOS と Linux 向けのコンテナランタイムとして紹介されている。
- 最小限の設定で利用できることが主な目的として示されている。
- Intel Mac、Apple Silicon、Linux の複数環境に対応する。
- Docker、Containerd、Incus など複数のランタイムを扱える。
- Kubernetes 利用や複数インスタンス実行にも対応する。
- 自動ポートフォワードやボリュームマウントなど開発用途の機能が含まれる。
- 実装面では Lima 上に VM を立て、その中でコンテナを動かす構成と理解されている。

### Key Findings
- Colima は macOS と Linux 向けの軽量なコンテナ実行環境として位置付けられている。 [^]
  - Footnote: 記事本文に「Colima - macOS（およびLinux）向けの最小限の設定で動作するコンテナランタイム」とある。
- macOS では Intel と Apple Silicon の両方を対象にしている。 [^]
  - Footnote: 主な機能として「IntelプロセッサおよびApple Silicon搭載のmacOS、およびLinux環境に対応」と記載されている。
- CLI とデフォルト設定は導入しやすさを意識した設計になっている。 [^]
  - Footnote: 機能一覧に「直感的なCLIインターフェースと合理的なデフォルト設定」とある。
- 開発時に必要になりやすいポート転送とボリューム共有が標準機能として挙げられている。 [^]
  - Footnote: 機能一覧に「自動ポートフォワード機能」「ボリュームマウント機能」とある。
- Docker、Containerd、Incus を含む複数ランタイムをサポートする。 [^]
  - Footnote: 本文に「複数のコンテナランタイムをサポート」「Docker」「Containerd」「Incus」と列挙されている。
- プロジェクトの狙いは、macOS でコンテナランタイムを簡単に使えるようにすることにある。 [^]
  - Footnote: プロジェクトの目的として「macOS環境において、最小限の設定でコンテナランタイムを利用できるようにすること」と説明されている。
- 内部的には Lima を使って VM を起動し、その中でコンテナを動かす構成と筆者は捉えている。 [^]
  - Footnote: 筆者コメントに「裏ではLimaを使ってVMを立ち上げてそこでコンテナを動かすという感じみたい」とある。

### References
- https://zenn.dev/kun432/scraps/7e0becc836485f
- https://github.com/abiosoft/colima

## プロバイダ・フレームワーク等のResponses API 対応状況

### Executive Summary
- Responses API への互換対応状況を複数プロバイダと実装で比較している。
- 筆者は OpenAI 互換 API の多くが Chat Completions API 中心だと見ている。
- Responses API はサーバサイド処理が多く、完全互換が難しいという見立てが示されている。
- エージェント用途では Responses API の方が望ましいと評価されている。
- OpenRouter、Ollama、LiteLLM、llama.cpp などは対応範囲や制限に差がある。
- Fireworks AI、LM Studio、Oracle OCI、Portkey などは比較的 Responses API らしい機能を備える候補として扱われている。
- 結論として、完全準拠には Chat Completions 互換より幅広い実装対応が必要だと整理している。

### Key Findings
- Responses API 互換は Chat Completions API 互換より難度が高いと見られている。 [^]
  - Footnote: 冒頭に「Responses API はサーバサイドでの処理も多いので、完全互換が難しいのだと思う」とある。
- エージェント向けには Responses API の利点が大きいとされている。 [^]
  - Footnote: 本文に「エージェント向けにはResponses APIのほうが色々望ましい」と記載されている。
- OpenRouter はベータ扱いで、ステートフル非対応と整理されている。 [^]
  - Footnote: OpenRouter の項目に「ベータ扱い」「ステートレスのみで、ステートフルには非対応」とある。
- Fireworks AI はステートフルやサーバサイド MCP への対応がある候補として評価されている。 [^]
  - Footnote: Fireworks AI の項目に「ステートフルにも対応」「サーバサイドMCPや previous_response_id に対応」とある。
- Ollama は Responses API をサポートするが、previous_response_id や conversation には非対応とされている。 [^]
  - Footnote: Ollama の項目に「一応サポート」「ただしステートフルには非対応（previous_response_id / conversation）」とある。
- LiteLLM は Responses エンドポイントを Chat Completions に変換する対応を含む。 [^]
  - Footnote: LiteLLM の項目に「Responses エンドポイントへのアクセスをChat Completions に変換するような対応がある」とある。
- LM Studio は 0.3.39 以降で Open Responses 互換をうたっている。 [^]
  - Footnote: LM Studio の項目に「0.3.39 以降で対応」「Open Resoponses 準拠っぽいことを謳っている」とある。
- Portkey は AI Gateway で Open Responses フル準拠をうたうが、ネイティブ処理と内部変換が分かれる。 [^]
  - Footnote: Portkey の項目に「Open Responsesフル準拠」「ネイティブにResponses APIで処理するものと、内部でChat Completionsに変換するものがある」とある。
- 筆者はローカル実行候補として LiteLLM、teabranch/open-responses-server、llama.cpp の PR を挙げている。 [^]
  - Footnote: まとめに「ローカルでやるなら以下あたりかな？ LiteLLM teabranch/open-responses-server llama.cppはPRに期待」とある。

### References
- https://zenn.dev/kun432/scraps/f47b43e1b9f845

## 「Irodori-TTS-Server」を試す

### Executive Summary
- Irodori-TTS-Server は Irodori-TTS を OpenAI Text-to-Speech API 互換で使うためのサーバとして紹介されている。
- アプリへの組み込みやすさを理由に API サーバ利用が取り上げられている。
- 対象モデルは Irodori-TTS 500M v3 ベースモデルと説明されている。
- リファレンス音声によるボイスクローンや長文テキスト分割をサポートする。
- ストリーミング合成は未実装で、リクエストごとに完全な音声応答を返す。
- 筆者は Docker と Ubuntu 22.04、RTX4090 環境で試している。
- モデル取得後の curl 実行では短時間で応答し、SDK 利用時はややオーバーヘッドがあると見ている。

### Key Findings
- このサーバは OpenAI Text-to-Speech API 互換のインターフェースを提供する。 [^]
  - Footnote: README 抜粋に「Irodori-TTS に対応したOpenAI Text-to-Speech API互換サーバー」とある。
- Irodori-TTS 500M v3 ベースモデルが対象とされている。 [^]
  - Footnote: 本文に「本サーバーはIrodori-TTS 500M v3ベースモデルを対象」と記載されている。
- ボイスクローン、OpenAI 風レスポンス、長文分割が主要機能として挙げられている。 [^]
  - Footnote: 説明に「リファレンス音声によるボイスクローン機能、OpenAIスタイルの応答フォーマット、長文テキストの自動分割処理をサポート」とある。
- ストリーミング合成には対応していない。 [^]
  - Footnote: 本文に「ストリーミング合成機能は実装していません」と明記されている。
- POST /v1/audio/speech エンドポイントで OpenAI 互換の呼び出しができる。 [^]
  - Footnote: 機能概要に「OpenAI互換のPOST /v1/audio/speechエンドポイント」とある。
- wav、mp3、flac、opus、aac、pcm など複数の出力形式に対応する。 [^]
  - Footnote: 機能概要に「対応出力フォーマット：wav、mp3、flac、opus、aac、pcm」と列挙されている。
- 実用的な推論では NVIDIA GPU の利用が推奨されている。 [^]
  - Footnote: 動作要件の説明に「実用的な推論を行うには、NVIDIA GPUの使用を推奨」とある。
- Docker での起動時は Uvicorn が 8088 番ポートで起動している。 [^]
  - Footnote: 起動ログに「Uvicorn running on http://0.0.0.0:8088」とある。
- モデルダウンロード後の curl 再実行では約0.473秒の実行時間が記録されている。 [^]
  - Footnote: 本文の出力例に「real 0m0.473s」とある。
- OpenAI Python SDK では curl よりオーバーヘッドが気になると筆者は述べている。 [^]
  - Footnote: SDK 実行例の後に「SDKだとちょっとオーバーヘッドが気になるかな」とある。

### References
- https://zenn.dev/kun432/scraps/27a96c1a3d3f7e
- https://github.com/Aratako/Irodori-TTS-Server
