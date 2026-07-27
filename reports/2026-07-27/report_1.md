# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-27T09:02:58+09:00
- Articles: 3

## 「MOSS-SoundEffect-v2.0」を試す

### Executive Summary
- MOSS-SoundEffect v2.0 は、テキストから非音声音響を生成するオープンモデルとして紹介されている。
- モデルは Diffusion Transformer と Flow Matching を基盤にし、DAC VAE と Qwen3 テキストエンコーダを組み合わせる。
- 生成対象は環境音、都市音、生物音、人間の動作音などで、最大30秒、48kHzまで制御できる。
- 筆者は Colaboratory L4 で試し、インストール後に protobuf の依存関係問題へ対処している。
- モデルロード時点の VRAM 消費は約10GB、複数回推論後は約15GBだった。
- 初回推論は torch.compile と Triton CUDA Graph の影響で時間がかかり、筆者環境では約3分だった。
- 生成自体は動作したが、プロンプトで狙い通りに制御するには試行錯誤が必要と評価している。
- オープンな効果音生成モデルとして貴重だが、リソース消費が大きく、量子化モデルへの期待が示されている。

### Key Findings
- MOSS-SoundEffect v2.0 は非音声の効果音生成に特化したモデルである。 [^]
  - Footnote: 記事では「テキストから非音声音響を生成する専用モデル」と説明され、環境音、都市音、生物音、人間の動作音などを対象にしている。
- v2.0 では旧来の自己回帰型から DiT + Flow Matching へ設計が変わっている。 [^]
  - Footnote: 記事中に、v1 の MossTTSDelay に代わり「連続潜在変数を用いたDiffusion Transformer + Flow Matching」を採用したとある。
- Colaboratory では依存関係の衝突が起き、protobuf の更新で回避している。 [^]
  - Footnote: モデルロード時に google.protobuf の runtime_version を import できないエラーが出て、`pip install -U "protobuf>=5.28,<6"` で動作したと記録されている。
- 推論には比較的大きな GPU メモリが必要だった。 [^]
  - Footnote: 筆者はモデルロード時点で VRAM 約10GB、数回推論後に約15GB消費した NVIDIA-SMI 出力を掲載している。
- 初回推論はコンパイル処理のため遅くなる。 [^]
  - Footnote: モデルカード由来の説明として初回呼び出し時に数分かかる場合があるとし、筆者環境では3分ほどで生成されたと書いている。
- 効果音生成の品質制御は簡単ではない。 [^]
  - Footnote: 複数のサンプルプロンプトを試した後、「プロンプトでの制御はなかなか難しい」と述べている。

### References
- https://zenn.dev/kun432/scraps/c15a8af84f93b2
- https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect-v2.0

## 「locate-anything.cpp」を試す

### Executive Summary
- locate-anything.cpp は NVIDIA の LocateAnything-3B を LocalAI が C++17 と ggml で移植した実装として紹介されている。
- Python ランタイムなしで、CPU または ggml バックエンド経由の GPU 上でオープン語彙物体検出を行える。
- モデル構成は Qwen2.5-3B、MoonViT、2層 MLP プロジェクタで、座標トークンをボックス座標へデコードする。
- README 由来のベンチマークでは、CPU で PyTorch 公式実装より 1.7～3倍程度高速とされている。
- 筆者は Apple Silicon Mac で Metal を有効化してビルドし、q8_0 の GGUF モデルを使って検証した。
- 単一カテゴリの tower 検出では5件の検出が返り、処理時間は約13.984秒だった。
- 複数カテゴリ指定では hybrid で sea が出ないケースがあり、slow モードでは sea も検出できた。
- 筆者は処理時間差が大きくないなら、精度重視では slow モードがよさそうだと見ている。

### Key Findings
- locate-anything.cpp は LocateAnything-3B の C++17 推論版である。 [^]
  - Footnote: 記事では「NVIDIAが開発したオープン語彙検出/視覚的接地VLM」である LocateAnything-3B の C++17 inference 版と説明されている。
- Python を使わず、依存関係を少なくして物体検出を実行できる。 [^]
  - Footnote: 本文に「Pythonランタイムを必要とせず、CPU上で高速かつ依存関係の少ないオブジェクト検出」とある。
- 量子化済み GGUF モデルが公開され、q8_0 が推奨されている。 [^]
  - Footnote: モデル一覧で q8_0 は約6.3GB、ほぼ損失のない変換、f32 とボックス位置が完全一致、推奨と記載されている。
- Mac M2 Pro では Metal 有効化ビルドで実行されている。 [^]
  - Footnote: 筆者は `LA_GGML_METAL=ON` を指定して CMake ビルドし、Apple M2 Pro の Metal ログを掲載している。
- tower の単独検出では5件の検出結果が得られた。 [^]
  - Footnote: 出力例に tower の bounding box が5件並び、`5 detections` と表示されている。
- 複数カテゴリ指定ではデコードモードが結果に影響した。 [^]
  - Footnote: tower と sea を同時指定した hybrid では sea が検出されず、slow モードでは sea のボックスが返ったと記録されている。

### References
- https://zenn.dev/kun432/scraps/c58d4da4e480f6
- https://github.com/mudler/locate-anything.cpp

## メモ: DSPy / GEPA / optimize_anything / optimize_anything omni

### Executive Summary
- この記事は DSPy、GEPA、optimize_anything、omni の関係を整理するメモである。
- 背景として、LLM システムのプロンプトや設定は従来人間が手作業で調整してきた課題が示されている。
- DSPy は LLM 処理をプログラムとして構築し、評価関数を使って最適化可能にするフレームワークとして説明されている。
- GEPA は実行結果の振り返りを使い、プロンプトなどを進化的に改善する最適化手法として整理されている。
- optimize_anything は、プロンプトだけでなくコード、SQL、設定、Skill など任意の文字列成果物を評価関数で改善する仕組みとして扱われている。
- 新しい optimize_anything では GEPA、AutoResearch、Meta-Harness などの最適化エンジンを共通インターフェースで交換できる。
- omni は複数のオプティマイザを小予算で試し、最良候補を新しいオプティマイザに渡すメタ最適化戦略として説明されている。
- 同じ20ドル予算の比較では、omni 系が単独方式を上回る結果が紹介されている。

### Key Findings
- DSPy は長いプロンプト文字列ではなく、入出力と処理構造をプログラムとして定義する。 [^]
  - Footnote: 記事では Signature、Module、Program、Metric、Optimizer を構成要素として挙げ、DSPy がモデルへ渡す指示を組み立てると説明している。
- GEPA はスコアだけでなく、失敗例やフィードバックを LLM に見せて改善候補を作る。 [^]
  - Footnote: 本文では「現在のプロンプト、実際の入出力、スコア、フィードバック」を LLM に見せる流れを示している。
- optimize_anything は文字列として表現でき、評価関数で測れる成果物を最適化対象にする。 [^]
  - Footnote: 記事では Python コード、SQL、設定ファイル、エージェントの Skill、シェルスクリプト、SVG などを例に挙げている。
- Actionable Side Information は次の修正方針を LLM に伝える重要な診断情報である。 [^]
  - Footnote: スコアだけでなく CompilerError、FailedTests、Runtime などを返すほうが、LLM が変更点を判断しやすいと説明されている。
- GEPA、AutoResearch、Meta-Harness は同じ問題群でも得意なタスクが異なる。 [^]
  - Footnote: Frontier-CS の10問では GEPA が3問、AutoResearch が3問、Meta-Harness が4問で最高スコアを出したと記載されている。
- omni は単独最適化器を選ぶより、複数方式を組み合わせる発想を採る。 [^]
  - Footnote: 記事では $5 × 3 + $5 の同じ20ドル予算で、複数方式の候補から最良を選び新しい最適化器へ渡す流れが説明されている。
- omni の比較結果は単独方式より高い平均スコアを示している。 [^]
  - Footnote: 表では GEPA が43.8から61.8、AutoResearch が55.4から63.2、Meta-Harness が50.9から59.3へ改善したとされている。

### References
- https://zenn.dev/kun432/scraps/2386dace3b19df
- https://gepa-ai.github.io/gepa/blog/2026/07/22/optimize-anything-omni/
