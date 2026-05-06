# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-06T09:30:00+09:00
- Articles: 3

## llama.cpp の Speculative Decoding
- Date: 2026-05-06T02:43:00+09:00

### Executive Summary
- Speculative Decoding は、小さい高速なモデルが複数トークンを先読みし、大きいモデルがまとめて検証する生成高速化手法として説明されている。
- 通常の LLM 生成は大きいモデルが 1 トークンずつ次を考えるため、長い文章では計算時間がかかる。
- 先読みが正しければ、大きいモデルだけで生成した場合と同じ品質を保ちながら複数トークンを一気に進められる。
- 効果は小さいモデルの予測精度、モデルの組み合わせ、ハードウェアに依存し、常に速くなるわけではない。
- MTP は Speculative Decoding そのものではなく、複数トークンを先読みする能力や構造をモデル側に持たせる方法として整理されている。
- llama.cpp では投機的デコーディングをサポートし、ドラフトモデル方式だけでなく n-gram 系の方式も扱えると紹介されている。
- n-gram 系の実装は追加モデルなしで履歴パターンや統計を使い、コード書き換え、反復処理、要約生成などに向く可能性が示されている。

### Key Findings
- Speculative Decoding は小さいモデルの先読みと大きいモデルの検証で構成される。 [^]
  - Footnote: 記事では「小さくて速いモデルに『たぶん次はこう続く』と先読みさせて、大きくて賢いモデルがそれをまとめてチェックする方法」と説明している。
- 通常生成は 1 トークンずつ大きいモデルが計算するため遅くなりやすい。 [^]
  - Footnote: 記事では「通常のLLMは、文章を1トークンずつ順番に出します」「1回1回の計算が重い」と述べている。
- 検証が通れば品質を保ったまま高速化できることが狙いである。 [^]
  - Footnote: 記事では「大きいモデルが1トークンずつ生成した場合と同じ結果を保ちながら、複数トークンを一気に進められます」としている。
- 予測が外れる場合や小モデルの実行コストにより、高速化効果は限定される。 [^]
  - Footnote: 記事では「小さいモデルが外しまくると…あまり速くなりません」「小さいモデルを別に動かすコストもあります」と説明している。
- MTP は複数トークン予測を学習・モデル構造として持たせる考え方である。 [^]
  - Footnote: 記事では「MTPでは…2個先、3個先、4個先も予測させる」「モデルの学習方法・構造に近い話」と整理している。
- MTP で作った先読み部分は Speculative Decoding の draft model として利用できる。 [^]
  - Footnote: 記事では「MTPで作った『複数トークンを先読みする部分』は、Speculative Decoding の draft model、つまり下書き役として使えます」と述べている。
- llama.cpp は複数の投機的デコーディング実装をサポートする。 [^]
  - Footnote: 記事の llama.cpp ドキュメント抜粋では「llama-serverアプリケーションでは、複数の投機的デコーディング実装をサポートしています」とある。
- ngram-mod は軽量で、固定的な計算量・メモリ使用量の特徴を持つ。 [^]
  - Footnote: 記事では ngram-mod の主な特徴として「軽量（約16MBのメモリ使用量）」「メモリ使用量と計算量が一定」と記載している。

### References
- https://zenn.dev/kun432/scraps/65bfaedf2939bd
- https://docs.nvidia.com/nemo/megatron-bridge/latest/training/multi-token-prediction.html
- https://arxiv.org/pdf/2412.19437

## CPU推論特化フレームワーク「Trillim」を試す
- Date: 2026-05-05T01:23:00+09:00

### Executive Summary
- Trillim は CPU 向けのローカル AI スタックで、CLI、Python SDK、FastAPI サーバーを提供する。
- LLM だけでなく、オプションとして STT と TTS も扱える点が紹介されている。
- BitNet 形式の三値モデルと PrismML の Bonsai 形式モデルを、同じ管理モデルストアと実行環境で扱える。
- 内部では DarkNet と量子化ツール群が推論処理の大部分を担い、Python パッケージはオーケストレーション層になる。
- ライセンス面では Python SDK は MIT だが、同梱バイナリなど一部はプロプライエタリであり注意が必要とされている。
- 著者は Raspberry Pi 4B でも Bonsai 1ビット 1.7B を試し、出力速度は一定あるが TTFT が大きいと評価している。
- トークン進捗タイムアウトを 60 秒に変更する回避策で停止は避けられたが、低リソース環境では用途を選ぶという結論になっている。

### Key Findings
- Trillim は CPU でローカル AI を動かすための統合スタックである。 [^]
  - Footnote: 記事では「TrillimはCPU向けのローカルAIスタックです。CLIインターフェース、Python SDK、およびFastAPIサーバーを提供」と説明している。
- LLM 以外に音声認識と音声合成もオプションで備える。 [^]
  - Footnote: 記事には「オプションとして音声認識（speech-to-text）と音声合成（text-to-speech）の機能も備えています」とある。
- BitNet 三値モデルと Bonsai 1ビット・三値モデルを同じワークフローで扱える。 [^]
  - Footnote: 記事では「BitNet形式の三値バンドルとPrismMLのBonsai形式バンドル（1ビットおよび三値形式）の両方」をサポートするとしている。
- DarkNet は CPU 推論の実行エンジンとして中心的な役割を担う。 [^]
  - Footnote: 記事では「DarkNetはCPUでローカルAIをガチ速く回すための推論エンジン本体」と要約している。
- インストール要件として Python 3.12 以降、Linux ホイールは glibc 2.27 以上が示されている。 [^]
  - Footnote: 記事のインストール方法では「Python 3.12以降のバージョンが必要」「Linux用のホイールパッケージはglibc >= 2.27」と記載されている。
- ライセンスは SDK と同梱バイナリで扱いが分かれる。 [^]
  - Footnote: 記事では「Python SDK自体はMITライセンス」「内部で利用される一部のファイルは、バイナリ提供かつプロプライエタリライセンス」と整理している。
- Raspberry Pi 4B では TTFT が 5 秒前後から 7 秒台になり、低リソース環境では厳しさが残る。 [^]
  - Footnote: 記事の実測では「TTFT=5.132s」「TTFT=5.178s」「TTFT=7.610s」と記録し、「RPi 4B だとTTFTが大きくてなかなか厳しい」と述べている。
- 進捗タイムアウトは内部定数を書き換えることで伸ばせる可能性が示された。 [^]
  - Footnote: 記事では `TOKEN_PROGRESS_TIMEOUT_SECONDS = 60.0` に変更するコードを示し、「止まることはなくなった」と述べている。

### References
- https://zenn.dev/kun432/scraps/f1fe4de36e63b6
- https://trillim.com/
- https://github.com/Trillim/Trillim?tab=readme-ov-file

## 「Codex App Server」を試す
- Date: 2026-05-04T20:55:00+09:00

### Executive Summary
- この記事は Codex App Server と Codex SDK の違いを、OpenAI 公式ドキュメントや関連投稿を元に整理している。
- Codex App Server は Codex をリッチクライアントへ組み込むための低水準プロトコル/サーバーとして説明されている。
- App Server は認証、会話履歴、承認、エージェントイベントのリアルタイムストリーミングなどを扱える。
- 一方、Codex SDK はローカル Codex エージェントをプログラムから制御する高水準ライブラリとして整理されている。
- CI/CD やジョブ自動化では App Server より SDK、codex exec、GitHub Action の方が扱いやすいとされている。
- ChatGPT サブスクリプションを活かした独自 UI やユーザー単位の認証体験を作る場合に App Server の価値がある。
- 著者は、個人用途なら自作アプリから ChatGPT アカウントのサブスク範囲で呼び出せる点がメリットだが、公開バックエンド用途は不適切だろうと述べている。

### Key Findings
- Codex App Server は Codex を製品やリッチクライアントへ組み込むための仕組みである。 [^]
  - Footnote: 記事の翻訳では「app-serverプロトコルを使用して、Codexを製品に組み込みます」と記載されている。
- App Server は認証、会話履歴、承認、イベントストリーミングなどを扱える。 [^]
  - Footnote: 記事では「認証、会話履歴、承認処理、エージェントイベントのリアルタイムストリーミングなどが可能」と説明している。
- ジョブ自動化や CI では Codex SDK の利用が推奨される。 [^]
  - Footnote: 記事では「ジョブの自動化やCI環境でCodexを実行する場合は、代わりに Codex SDK をご利用ください」と引用している。
- Codex SDK はローカル Codex エージェントをプログラムから制御する用途に向く。 [^]
  - Footnote: 記事では「Codex SDK は、ローカル Codex エージェントをプログラムから制御するための API」と整理している。
- App Server は SDK より低水準で、JSON-RPC、状態管理、イベント処理を自前実装する必要がある。 [^]
  - Footnote: 記事ではデメリットとして「SDK より低水準」「JSON-RPC メッセージ、状態管理、イベント処理を自分で実装する必要がある」としている。
- 各ユーザーの ChatGPT サブスクリプションを活かす独自 UI には App Server が向く。 [^]
  - Footnote: 記事では選び方として「各ユーザーの ChatGPT サブスクリプションを活かしたい」「Codex App Server」と整理している。
- CI やサーバー側自動実行では API キー運用が安定するとされる。 [^]
  - Footnote: 記事では「CI/CD なら API キー + codex exec、Codex GitHub Action、または Codex SDK」としている。
- 公開アプリのバックエンドで ChatGPT サブスクを利用する使い方は避けるべきと著者は見ている。 [^]
  - Footnote: 記事では「パブリックに公開するアプリのバックエンドで使う、というケースはNGなはず」と述べている。

### References
- https://zenn.dev/kun432/scraps/9fe862943fb00e
- https://developers.openai.com/codex/app-server
- https://developers.openai.com/codex/sdk
