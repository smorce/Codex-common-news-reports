# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-19T00:00:00+09:00
- Articles: 3

## メモ: Octen Embedding
- Date: 2026-07-18T09:42:42+00:00

### Executive Summary
- Octen の埋め込みモデル群が気になり、公開情報を整理したスクラップである。
- 著者は NVIDIA Nemotron 3 Embed の確認中に、Octen のモデルがリーダーボード上位に複数あることに注目している。
- Octen の公開モデルは複数あり、いずれも Apache-2.0 ライセンスとされている。
- モデル群は Qwen3-Embedding からのファインチューニングと見られている。
- Octen は一般検索サイトではなく、AI やエージェント向けの検索インフラ/API企業として整理されている。
- Web Search API、Broad Search、Extract、Embedding、画像・動画検索、Model Gateway などの機能が紹介されている。
- 性能訴求は魅力的だが、導入時は自社条件で実測検証する必要がある。

### Key Findings
- Octen のモデルがリーダーボード上位に複数入っている。 [^]
  - Footnote: Octenという会社のモデルが上位に並んでいる。
- 公開モデルは5つほどあり Apache-2.0 ライセンスとされる。 [^]
  - Footnote: モデルは5つほどあった。全部Apache-2.0ライセンス。
- モデル群は Qwen3-Embedding 由来のファインチューニングと見られる。 [^]
  - Footnote: 全てQwen3-Embeddingからのファインチューニングみたい。
- Octen は生成AIやエージェント向け検索インフラ/APIを提供する。 [^]
  - Footnote: 生成AIやAIエージェントに『最新のWeb情報を検索させる』ための検索インフラ／APIを提供するスタートアップです。
- 検索、抽出、埋め込み、マルチモーダル検索、モデル連携の機能が紹介されている。 [^]
  - Footnote: Web Search API、Broad Search、Extract、Embedding、画像・動画検索、Model Gateway。
- AIが検索結果を高速に取得し推論へ使う前提の設計である。 [^]
  - Footnote: AIが大量の検索結果を高速に取得し、そのまま推論に使うことを前提に設計されています。
- モデルカード上は sentence-transformers で利用できそうだと確認している。 [^]
  - Footnote: モデルカード見る限りは普通にsentence transformersで使えるみたい。

### References
- https://zenn.dev/kun432/scraps/5abdf28aed50f0

## 「NVIDIA Nemotron 3 Embed」を試す
- Date: 2026-07-18T08:30:14+00:00

### Executive Summary
- NVIDIA Nemotron 3 Embed の概要と Colaboratory L4 での試用結果をまとめている。
- Nemotron 3 Embed 8B は RTEB で全体1位に到達した埋め込みモデルとして紹介されている。
- 8B-BF16、1B-BF16、1B-NVFP4 の3系統で、精度、効率、高速運用の役割が分かれる。
- 良い埋め込みは RAG やエージェントで適切な文脈を拾いやすくし、検索回数や推論トークン削減につながる。
- 1B-NVFP4 は Blackwell 世代 GPU の 4bit フォーマットを活かす設計である。
- モデル設計では Ministral 系を retriever に改造し、蒸留や pruning を使って小型化している。
- 著者の 8B-BF16 試用では L4 環境で約15GBの VRAM を使い、英語・日本語の簡易検索で妥当な順位付けを確認している。

### Key Findings
- Nemotron 3 Embed 8B は RTEB で首位と紹介されている。 [^]
  - Footnote: RTEB で全体の #1 に到達しました。
- モデルは精度重視、実用バランス、高速省メモリの3用途に整理される。 [^]
  - Footnote: 8B、1B-BF16、1B-NVFP4 の説明で役割が分けられている。
- 埋め込み品質はエージェントの検索効率とコストに影響する。 [^]
  - Footnote: 検索回数も推論トークンも減って、エージェントが安く賢く動く。
- NVFP4 版は Blackwell GPU の 4bit フォーマットに最適化されている。 [^]
  - Footnote: Blackwell 世代 GPU には NVFP4 っていう 4bit フォーマットがある。
- 1B モデルは pruning と 8B teacher からの蒸留を経ている。 [^]
  - Footnote: 3B を ModelOpt の NAS で構造化 pruning、8B teacher から蒸留。
- 小型版でも 1.14B パラメータ、2048次元、32kコンテキストが示される。 [^]
  - Footnote: 1.14B パラメータ、埋め込み次元 2048、コンテキスト 32k。
- 著者の試用では VRAM 消費は約15GBだった。 [^]
  - Footnote: VRAM消費は約15GB程度。

### References
- https://zenn.dev/kun432/scraps/cf9f24660c6641

## メモ: How We Built Our Knowledge Base（Cerebras）
- Date: 2026-07-18T06:33:12+00:00

### Executive Summary
- Cerebras が社内ナレッジベースを構築した方法を整理している。
- Slack、Wiki、コード、ドキュメント、事故レポートなどを元の場所に残し、横断検索と回答のレイヤーを作る設計である。
- 全データソースは共通 schema の embeddings テーブルへ集約される。
- Slack はスレッド単位の要約、構造化、重要発言単位の burst 抽出で検索しやすくしている。
- 検索は full-text、embedding、IDF、age decay を組み合わせ、RRF でランキングを統合する。
- コード検索は ripgrep だけでなく semantic search も組み合わせ、CocoIndex でチャンク化と差分同期を行う。
- クエリ処理は Planner、Executor、Synthesizer の構成で、証拠収集から引用付き回答までを処理する。

### Key Findings
- 情報を一箇所に移さず既存ツール上に残す設計である。 [^]
  - Footnote: 情報は元の場所のままにしておいて、上から一気に検索＆回答できるレイヤーを作った。
- 全ソースを同じ形式の Postgres テーブルへ入れる。 [^]
  - Footnote: 最終的には同じフォーマットの1テーブルに入れる。
- Slack はスレッド単位で LLM に要約させてから embed する。 [^]
  - Footnote: スレッド単位で LLM に要約させてから embed する。
- 重要な発言を拾うため burst 単位も導入している。 [^]
  - Footnote: 長いスレッドだと、要約に入りきらない大事な一文がある。
- Slack 検索は複数手法を RRF で融合する。 [^]
  - Footnote: full-text search、embedding search、IDF、age decay、RRF。
- コード検索では意味検索も使い、名前を知らない実装探索に対応する。 [^]
  - Footnote: 関数名やファイル名を知らない人、意味的に近い実装を探したいときには semantic search が強い。
- 差分同期により大規模リポジトリでも再計算を抑える。 [^]
  - Footnote: 40GB級リポジトリでも、全再計算せずに最新状態を保てる。

### References
- https://zenn.dev/kun432/scraps/a207c3f2cc7f5c
