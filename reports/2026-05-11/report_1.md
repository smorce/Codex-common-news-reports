# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-11T09:01:30.3302520+09:00
- Articles: 3

## 「SenseNova-U1」を試す

### Executive Summary
- SenseNova-U1 は、理解・推論・生成を単一アーキテクチャに統合するネイティブマルチモーダルモデルとして紹介されている。
- 中核は NEO-Unify アーキテクチャで、Visual Encoder と VAE を排除し、言語と視覚を同じ表現空間で扱う点が強調されている。
- 公開モデルには 8B MoT 系と A3B MoT 系があり、SFT 版、LoRA 版、GGUF 量子化版など複数の選択肢が示されている。
- 筆者は Ubuntu 22.04 と RTX 4090 で Text-to-Image 推論を試し、通常の Transformers 経路では VRAM 不足に遭遇した。
- GGUF 量子化チェックポイントを使うと推論が成立し、Q6_K では約1分40秒で画像生成できたと記録している。
- GGUF と vram_mode balanced を組み合わせると VRAM 消費は約 7171MiB まで下がったが、完了まで約12分かかり速度面の課題が残った。
- 8ステップ蒸留版の GGUF は 30〜40秒程度まで高速化し、SFT 版は通常の Q6_K と同程度の約1分40秒だった。
- 筆者は、GPUに収められる環境なら量子化モデル単独の利用が現実的で、VRAM削減モードは時間とのトレードオフが大きいと見ている。

### Key Findings
- SenseNova-U1 はモダリティ間の連携ではなく統合を狙うモデルとして位置づけられている。 [^]
  - Footnote: 記事では「マルチモーダル理解・推論・生成を単一のアーキテクチャに統合」「モダリティ間の連携から真の統合へ」と説明されている。
- NEO-Unify は Visual Encoder と VAE を排除する設計である。 [^]
  - Footnote: 本文に「Visual Encoder（VE）とVariational Auto-Encoder（VAE）を完全に排除」とある。
- 公開モデルは 8B MoT、A3B MoT、LoRA、SFT など複数構成で提供されている。 [^]
  - Footnote: モデル表に「SenseNova-U1-8B-MoT」「SenseNova-U1-A3B-MoT」「LoRA-8step」「SFT」などが列挙されている。
- 通常の Transformers 推論では RTX 4090 でも VRAM 不足になった。 [^]
  - Footnote: 筆者は RTX4090 で実行し、「torch.OutOfMemoryError: CUDA out of memory」と記録している。
- GGUF 量子化を使うと推論が成立し、実測で約1分40秒だった。 [^]
  - Footnote: Q6_K の GGUF を指定した実行について「だいたい1分40秒ぐらいで生成された」とある。
- GGUF と balanced の併用は VRAM を大きく減らす一方で時間が長くなる。 [^]
  - Footnote: 併用時は「だいたい12分ぐらいで完了」「Memory-Usage 7171MiB / 24564MiB」と記載されている。
- 8ステップ蒸留版 GGUF は速度面で有利だった。 [^]
  - Footnote: 8step-Q6_K について「30〜40秒ぐらいとやはり速くなった」と記録されている。
- 筆者は、VRAMに収まるなら量子化モデル単独が現実的と判断している。 [^]
  - Footnote: 本文末尾に「GPUに収めれるなら量子化モデルを使うだけでいいかも」とある。

### References
- https://zenn.dev/kun432/scraps/703fa1101e6347
- https://github.com/OpenSenseNova/SenseNova-U1

## 「HiDream-O1-Image」 を試す

### Executive Summary
- HiDream-O1-Image は、外部 VAE や分離型テキストエンコーダを使わないピクセルレベル統一 Transformer ベースの画像生成モデルとして紹介されている。
- テキストから画像生成、画像編集、被写体主導のパーソナライゼーションなどを単一モデルで扱う点が特徴である。
- 最大 2048×2048 ピクセルの高解像度生成に対応し、Artificial Analysis Text to Image Arena で第8位に入ったことが引用されている。
- 筆者は VAE なしの意味を整理し、細部、文字、模様、レイアウトの劣化を減らせる可能性がある一方、計算や設計は重くなると理解している。
- 実験環境は Ubuntu 22.04 と RTX 4090 で、依存関係として PyTorch、Transformers、Diffusers、Flash Attention などを導入している。
- Reasoning 駆動型プロンプトエージェントを OpenAI 互換 API と gpt-5.5 で試し、入力プロンプトを詳細な英語プロンプトへ拡張している。
- 初回推論では VRAM 不足に遭遇し、蒸留版や解像度変更でも改善しなかったが、モデル読み込みを bfloat16 に修正すると実行できた。
- 実行結果では 1024×1024 指定が 2048×2048 に丸められ、Dev 版は 28 ステップで生成完了している。

### Key Findings
- HiDream-O1-Image は VAE と分離型テキストエンコーダを使わない統合型設計である。 [^]
  - Footnote: 本文に「外部のVAE（変分自己符号化器）や分離型テキストエンコーダを使用せず」とある。
- 生ピクセル、テキスト、条件情報を共有トークン空間で扱う。 [^]
  - Footnote: README 抜粋として「生のピクセルデータ、テキストデータ、およびタスク固有の条件情報を単一の共有トークン空間にネイティブに符号化」と記載されている。
- 最大 2048×2048 の高解像度生成が想定されている。 [^]
  - Footnote: 本文に「最大2,048×2,048ピクセルの解像度」「ネイティブ高解像度対応」とある。
- Reasoning 駆動型プロンプトエージェントは、生成前に知識や構図を補完する。 [^]
  - Footnote: 特徴説明に「生成前に暗黙的な知識、レイアウト、テキストレンダリングを解決する」とある。
- 筆者は OpenAI 互換 API の gpt-5.5 をバックエンドにしてプロンプトエージェントを試した。 [^]
  - Footnote: 実行例に「--backend api」「--base_url https://api.openai.com/v1」「--model_name gpt-5.5」とある。
- 初期推論では RTX 4090 でも CUDA OOM が発生した。 [^]
  - Footnote: 本文に「torch.OutOfMemoryError: CUDA out of memory」と記録されている。
- bfloat16 指定への修正で推論が進むようになった。 [^]
  - Footnote: 筆者は「torch_dtype=torch.bfloat16」に修正し、「一応いけたみたい」と記している。
- 解像度指定は 1024×1024 から 2048×2048 に丸められた。 [^]
  - Footnote: 出力ログに「Resolution snapped from 1024x1024 to 2048x2048」とある。

### References
- https://zenn.dev/kun432/scraps/bcb0dede82cb1a
- https://github.com/HiDream-ai/HiDream-O1-Image

## Hermes Agent 個人的セットアップメモ

### Executive Summary
- この記事は Hermes Agent を本格的に使うための個人的セットアップメモである。
- 最初に SearXNG を Docker Compose でセルフホストし、ローカルの 8888 番ポートで起動する手順が示されている。
- SearXNG の設定では search.formats に json を追加し、JSON 形式の検索結果を取得できるようにしている。
- 確認コマンドでは localhost の検索 API に format=json を付け、結果件数が表示されれば動作確認完了としている。
- Hermes 側では .env に SEARXNG_URL を設定し、config.yaml で search_backend を searxng にする。
- 筆者は SearXNG 自体は動くものの、使用する検索エンジンの細かな設定は追加で調整したほうがよいと見ている。
- 続いて FireCrawl の無料枠を使う構成として FIRECRAWL_API_KEY を .env に入れ、extract_backend を firecrawl にしている。
- FireCrawl はコンテンツ取得自体は数秒に見える一方、Hermes Agent 上では約2分かかるように見え、原因は未確定としている。

### Key Findings
- Hermes Agent の Web 検索バックエンドとして SearXNG を使う構成が示されている。 [^]
  - Footnote: config.yaml の例に「search_backend: 'searxng'」が記載されている。
- SearXNG は Docker Compose で localhost:8888 に公開する。 [^]
  - Footnote: docker-compose.yml の例に「ports: - "8888:8080"」とある。
- SearXNG で JSON 結果を使うため search.formats に json を追加する必要がある。 [^]
  - Footnote: 設定例に「formats: - html - json」と記載されている。
- 動作確認は SearXNG の search API に format=json を付けて実施している。 [^]
  - Footnote: 確認コマンドに「http://localhost:8888/search?q=test&format=json」が使われている。
- Hermes の環境変数には SEARXNG_URL を設定する。 [^]
  - Footnote: ~/.hermes/.env の例に「SEARXNG_URL=http://localhost:8888」とある。
- FireCrawl を抽出バックエンドとして使う構成も記録されている。 [^]
  - Footnote: config.yaml の例に「extract_backend: firecrawl」とある。
- FireCrawl 利用時は API キーを .env に設定する。 [^]
  - Footnote: ~/.hermes/.env の例に「FIRECRAWL_API_KEY=XXXXXXXXXX」とある。
- FireCrawl は Hermes Agent 上で処理時間が長く見えるという未解決メモがある。 [^]
  - Footnote: 追記に「Hermes Agent上だと2分ぐらいかかってるように見える。ちょっとよくわからない」とある。

### References
- https://zenn.dev/kun432/scraps/2e2e18104937ee
