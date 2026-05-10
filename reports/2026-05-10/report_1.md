# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-10T09:01:02.5541065+09:00
- Articles: 3

## 「SenseNova-U1」を試す
- Date: 2026-05-10T00:47:00+09:00

### Executive Summary
- SenseNova-U1 は、理解・推論・生成を単一アーキテクチャで扱うネイティブマルチモーダルモデルとして紹介されている。
- 記事は GitHub README の内容を中心に、NEO-Unify アーキテクチャの特徴を日本語で整理している。
- 従来のアダプター型連携ではなく、言語情報と視覚情報を統一された複合体として処理する点が主張されている。
- Visual Encoder と VAE を排除し、ピクセル情報と単語情報の深い相関を前提にした設計が強調されている。
- 生成・理解ベンチマークでオープンソースモデルの最先端を達成したという説明がある。
- 公開モデルとして 8B MoT と A3B MoT 系列が示され、SFT モデルや LoRA、GGUF 量子化にも触れている。
- 低 VRAM 環境向けの GGUF 量子化チェックポイントとレイヤーオフローディングが最新情報として記録されている。
- 制約として 32K 文脈長、人間の細部表現、テキストレンダリング、交互生成の成熟度が課題に挙げられている。

### Key Findings
- SenseNova-U1 は理解・推論・生成を統合するネイティブマルチモーダルモデルである。 [^]
  - Footnote: 記事本文に「マルチモーダル理解・推論・生成を単一のアーキテクチャに統合」とある。
- 中核技術は NEO-Unify アーキテクチャである。 [^]
  - Footnote: 本文で「SenseNova U1の中核をなすのが NEO-Unify アーキテクチャ」と説明されている。
- VE と VAE を使わない設計が特徴として示されている。 [^]
  - Footnote: 本文に「Visual Encoder（VE）とVariational Auto-Encoder（VAE）を完全に排除」と記載されている。
- 言語情報と視覚情報をエンドツーエンドで処理する設計である。 [^]
  - Footnote: 特徴として「言語情報と視覚情報を統一された複合体としてエンドツーエンドで処理」とある。
- 8B MoT と A3B MoT の Lite シリーズが公開対象になっている。 [^]
  - Footnote: モデル欄に「SenseNova U1 Liteシリーズを2つのサイズでオープンソース化」とあり、8B MoT と A3B MoT が列挙されている。
- 2026年5月8日に GGUF 量子化チェックポイントとレイヤーオフローディングが追加された。 [^]
  - Footnote: 最新情報に「[2026.05.08] GGUF量子化チェックポイントとレイヤーオフローディングを追加」とある。
- 現行モデルには文脈長や人物表現、文字生成などの課題が残る。 [^]
  - Footnote: 改善事項として「最大32Kトークン」「人間の身体の微細なディテール」「誤表記や文字の歪み」が挙げられている。

### References
- https://zenn.dev/kun432/scraps/703fa1101e6347
- https://github.com/OpenSenseNova/SenseNova-U1

## 「HiDream-O1-Image」 を試す
- Date: 2026-05-09T17:50:00+09:00

### Executive Summary
- HiDream-O1-Image は、VAE や分離型テキストエンコーダを使わない画像生成基盤モデルとして紹介されている。
- 記事は GitHub README の抜粋に加え、実際のセットアップ、推論、Web UI 利用時の観察を記録している。
- モデルは生ピクセル、テキスト、条件情報を共有トークン空間で扱い、最大 2048x2048 の生成や編集に対応すると説明されている。
- 2026年5月8日に 8B モデルの未蒸留版と蒸留版 Dev バリアント、Reasoning-Driven Prompt Agent が公開された。
- 提供モデルには通常版、Dev 版、Prompt Agent、Web デモがあり、通常版は 50 ステップ、Dev 版は 28 ステップとされる。
- 筆者の BF16 実行では、画像生成時の VRAM 消費が約 18GB、編集や複数画像利用ではさらに増えることが記録されている。
- Web GUI では Text to Image、Edit、Subject の 3 機能を確認している。
- 最終的な所感として、VAE なしやプロンプト改善エージェントの流れ、日本語文字生成の健闘、量子化への期待が述べられている。

### Key Findings
- HiDream-O1-Image は外部 VAE や分離型テキストエンコーダを使わない。 [^]
  - Footnote: 本文に「外部のVAEや分離型テキストエンコーダを使用せず」とある。
- 最大 2048x2048 解像度で画像生成、編集、パーソナライゼーションをサポートする。 [^]
  - Footnote: 本文で「最大2,048×2,048ピクセルの解像度」における生成、編集、被写体主導型パーソナライゼーション対応が説明されている。
- 8B モデルの Dev 系列と Reasoning-Driven Prompt Agent が公開された。 [^]
  - Footnote: 更新情報に「2026年5月8日: 未蒸留版と蒸留版のDevバリアントを含む HiDream-O1-Image（8Bモデル）をオープンソース化」とある。
- 提供モデルの通常版は 50 ステップ、Dev 版は 28 ステップで推論する。 [^]
  - Footnote: 提供モデル表に HiDream-O1-Image は「50ステップ」、HiDream-O1-Image-Dev は「28ステップ」とある。
- Prompt Agent は生成前に知識、レイアウト、テキストレンダリングを解決する役割として説明されている。 [^]
  - Footnote: 主な特徴に「生成前に暗黙的な知識、レイアウト、テキストレンダリングを解決する」とある。
- 筆者の環境では BF16 画像生成の VRAM 消費が約 18GB だった。 [^]
  - Footnote: 実行結果の後に「BF16ならVRAM消費は18GBぐらいに抑えられる」とあり、NVIDIA-SMI で 18241MiB が示されている。
- Web GUI では画像生成、画像編集、複数画像からの主題ベース編集を試している。 [^]
  - Footnote: 本文に「画像生成（Text→Image）、画像編集（Edit）、複数画像からの主題ベースの画像編集（Subject）の3つがある」とある。
- 筆者は日本語文字生成を一定評価しつつ、品質判断には慎重な姿勢を示している。 [^]
  - Footnote: まとめに「日本語文字は思いのほか頑張ってる」「BF16にしてるので本来正しい結果ではないかもしれない」とある。

### References
- https://zenn.dev/kun432/scraps/bcb0dede82cb1a
- https://github.com/HiDream-ai/HiDream-O1-Image

## Hermes Agent 個人的セットアップメモ
- Date: 2026-05-08T20:16:00+09:00

### Executive Summary
- この記事は Hermes Agent を本格利用するための個人的なセットアップメモである。
- 主に Web Search & Extract 機能のバックエンドとして SearXNG と FireCrawl を設定する手順が記録されている。
- SearXNG では Docker Compose でローカルコンテナを起動し、8888 番ポートで公開する構成が示されている。
- SearXNG の settings.yml では search.formats に json を追加し、JSON 形式の検索結果を返せるようにしている。
- 確認コマンドでは localhost:8888 の検索 API を呼び、20 results と表示されれば OK としている。
- Hermes 側には .env の SEARXNG_URL と config.yaml の search_backend: searxng を設定する流れになっている。
- FireCrawl については API キーを .env に入れ、extract_backend: firecrawl を設定する例が示されている。
- 筆者は FireCrawl 自体の取得は数秒に見える一方、Hermes Agent 上では約2分かかるように見える点を未解決の観察として残している。

### Key Findings
- 記事の目的は Hermes Agent の実用向けセットアップを記録することである。 [^]
  - Footnote: 冒頭に「本格的に使うためのセットアップいろいろをメモ」とある。
- SearXNG は Docker Compose で searxng/searxng:latest を起動する構成である。 [^]
  - Footnote: docker-compose.yml 例に image: searxng/searxng:latest、container_name: searxng とある。
- SearXNG はホストの 8888 番ポートからコンテナの 8080 番へ公開される。 [^]
  - Footnote: ports に "8888:8080" と記載されている。
- JSON 検索結果を使うため、SearXNG の search.formats に json を追加する。 [^]
  - Footnote: 本文に「search.formats に json を追加」とあり、formats に html と json が並ぶ例がある。
- SearXNG の動作確認では検索 API から 20 results が返っている。 [^]
  - Footnote: 確認コマンドの出力として「20 results」と表示されている。
- Hermes 側では SEARXNG_URL と search_backend を設定する。 [^]
  - Footnote: .env に SEARXNG_URL=http://localhost:8888、config.yaml に search_backend: 'searxng' とある。
- FireCrawl は extract_backend として設定する例が示されている。 [^]
  - Footnote: config.yaml 例に search_backend: searxng と extract_backend: firecrawl が記載されている。
- FireCrawl 利用時、Hermes Agent 上の処理時間が長く見えるという課題が残っている。 [^]
  - Footnote: 追記に「Hermes Agent上だと2分ぐらいかかってるように見える」とある。

### References
- https://zenn.dev/kun432/scraps/2e2e18104937ee
- https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search#searxng-free-self-hosted
- https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search#firecrawl-default
