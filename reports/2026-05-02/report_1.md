# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-02T09:00:00+09:00
- Articles: 3

## 国産量子化ツール「OneComp」を試す
- Date: 2026-05-01T05:56:25+00:00

### Executive Summary
- Fujitsu Research の OneCompression、通称 OneComp を試したスクラップ。
- OneComp は LLM 圧縮のための Python パッケージとして紹介されている。
- CLI では `onecomp <generative AI>` のようにモデル ID を渡すだけで自動実行できる。
- VRAM 容量を自動検出し、層ごとのビット幅選択、QEP、評価、保存まで処理する設計。
- 動作確認済みアーキテクチャとして Llama、Qwen3、Gemma が挙げられている。
- Ubuntu 22.04 と RTX 4090 環境でソースからインストールして検証している。
- Qwen/Qwen3-0.6B の Quick Start では量子化処理が約15分で完了したと記録している。
- vLLM プラグイン連携により、量子化モデルを Open WebUI と組み合わせてローカル対話に使える点も確認している。

### Key Findings
- OneComp は LLM 圧縮を目的とする Python パッケージである。 [^]
  - Footnote: 記事では README の抜粋として「Fujitsu One Compression（OneComp）は、LLM（大規模言語モデル）の圧縮を実現するPythonパッケージです。」と説明している。
- CLI はモデル ID を渡すだけのワンライナー実行を重視している。 [^]
  - Footnote: 記事中に「⚡ たった1行のコマンドで完了 onecomp <generative AI>」および使用例 `onecomp meta-llama/Llama-2-7b-hf` が掲載されている。
- VRAM 自動検出と層ごとの最適ビット幅選択が主要機能として説明されている。 [^]
  - Footnote: 記事は「GPUのVRAM容量を自動検出し、各レイヤーに最適なビット幅を選択、誤差伝播型量子化を適用」と記載している。
- QEP、LPCD、AutoBit、JointQ、ブロック単位 PTQ、LoRA SFT 後処理など複数の量子化関連機能を含む。 [^]
  - Footnote: 主な機能として「量子化誤差伝播（QEP）」「レイヤー投影座標降下法（LPCD）」「AutoBit」「JointQ」「ブロック単位PTQ」「LoRA SFT後処理」が列挙されている。
- vLLM との連携は DBF と Mixed-GPTQ の組み込みプラグインを通じて行う。 [^]
  - Footnote: 記事では「組み込みプラグイン（DBF、Mixed-GPTQ）を使用してvLLMで動作」と説明している。
- 検証環境は Ubuntu 22.04 と RTX 4090、VRAM 24GB とされている。 [^]
  - Footnote: インストール節に「環境はUbuntu-22.04 ＋ RTX4090（VRAM 24GB）」と明記されている。
- Qwen/Qwen3-0.6B の検証では RTX 4090 が 25.25GB と認識され、196 モジュールに対する候補評価が行われた。 [^]
  - Footnote: ログに「GPU: NVIDIA GeForce RTX 4090 (25.25 GB)」「Activation-Aware ILP: 196 modules × 4 candidates」とある。
- Quick Start の実行時間はダウンロード時間を除き約15分と記録されている。 [^]
  - Footnote: 記事は Qwen/Qwen3-0.6B の実行について「全体としてはだいたい15分ぐらいで完了」と述べている。

### References
- https://zenn.dev/kun432/scraps/7369c74ccd4de6
- https://github.com/FujitsuResearch/OneCompression
- https://FujitsuResearch.github.io/OneCompression/

## OpenAI の「phaseパラメータ」を試す（Reasoningモデルおさらい）
- Date: 2026-05-01T18:38:50+00:00

### Executive Summary
- GPT-5.5 ガイドを読む過程で見つけた phase パラメータと Reasoning モデルを確認するスクラップ。
- phase パラメータは GPT-5.4 で追加された機能らしいと位置づけられている。
- Reasoning モデルは最終応答前に内部 Reasoning トークンを使うモデルとして説明されている。
- 計画、ツール活用、曖昧性解消、複雑なマルチステップ解決に向くと整理している。
- Responses API と reasoning.effort の指定例を Colaboratory で試している。
- reasoning.effort は none から xhigh まで段階があり、品質・速度・コストのトレードオフを制御する。
- 一般的な Reasoning では gpt-5.5、コスト重視では gpt-5.4 や gpt-5.4-mini から始める選択肢を紹介している。
- レイテンシー重視では TTFT を意識し、短い前置きを出すテクニックにも触れている。

### Key Findings
- 記事の目的は phase パラメータを調べつつ Reasoning モデルを復習することにある。 [^]
  - Footnote: 冒頭で「その1つに『phaseパラメータ』という機能がある」「Reasoningモデルのおさらい含めて、確認してみる」と述べている。
- Reasoning モデルは応答前に内部的な Reasoning トークンを使うと説明されている。 [^]
  - Footnote: 記事には「Reasoningモデルは、（最終）応答を生成する前に内部的なReasoningトークンを使用する」とある。
- Reasoning モデルは計画立案、効果的なツール活用、曖昧性解消、複雑なマルチステップ解決に向く。 [^]
  - Footnote: 解決できるタスクとして「計画を立案する」「ツールを効果的に活用」「曖昧性を解消する」「複雑でマルチステップな解決」が列挙されている。
- Responses API で reasoning.effort を指定する実装例が示されている。 [^]
  - Footnote: サンプルコードでは `client.responses.create` に `model="gpt-5.5"` と `reasoning={"effort": "low"}` を指定している。
- reasoning.effort はモデルの思考の深さを制御するパラメータとして整理されている。 [^]
  - Footnote: 記事では「モデルが『どれぐらい深く考えるか？』のReasoningのレベルを制御できるのが、reasoning.effort パラメータ」と説明している。
- effort の段階は none、minimal、low、medium、high、xhigh の順に深くなる。 [^]
  - Footnote: 記事に「none < minimal < low < medium < high < xhigh」とあり、浅いから深い、速いから遅い、少ないから多いという対応が示されている。
- medium は品質・信頼性とコストのバランスが良い標準的な構成として扱われている。 [^]
  - Footnote: 表では medium について「ほとんどの場合のデフォルト構成。レイテンシー・性能・コストのバランスが良い」と記載している。
- レイテンシー重視では TTFT と短い Preamble の活用が検討事項になる。 [^]
  - Footnote: 記事末尾で「TTFT（Time-to-First-Token）を考慮」「短い前置き（Preamble）を出力させる」と説明している。

### References
- https://zenn.dev/kun432/scraps/961f298d79ed27

## OpenAI の「ツール検索」を試す
- Date: 2026-04-30T03:56:22+00:00

### Executive Summary
- GPT-5.5 ガイドを読む過程で見つけた OpenAI のツール検索機能を試すスクラップ。
- ツール検索は GPT-5.4 以降で利用できる機能として紹介されている。
- 必要なツール定義だけを実行時に動的に検索・読み込み、コンテキストに追加する仕組みと説明している。
- すべてのツール定義を事前投入しないことで、トークン使用量とコスト削減が期待できる。
- サンプルではスーパー青果部門の在庫管理チャットを題材にしている。
- 最初にツール検索なしで関数ツールを全定義する通常実装を作り、挙動を確認している。
- 野菜一覧、在庫取得、入荷、廃棄のツール呼び出しが Responses API で順に実行される様子を記録している。
- ツール検索利用には tool_search ツール追加と、遅延ロード対象への defer_loading 設定が必要と整理している。

### Key Findings
- ツール検索は必要な定義のみをモデルが実行時に読み込むための機能として説明されている。 [^]
  - Footnote: 記事では「遅延ロードされたツールを実行時に読み込むことで、モデルが必要な定義のみを読み込む」と説明している。
- ツール検索により、すべてのツール定義を事前にコンテキストへ読み込む必要がなくなる。 [^]
  - Footnote: 本文に「すべてのツール定義を事前にモデルのコンテキストに読み込む必要がなくなり」とある。
- 期待される効果はトークン使用量とコストの削減である。 [^]
  - Footnote: 記事は「トークン使用量とコストの削減が期待できます」と述べている。
- ツール検索は gpt-5.4 以降のモデルでのみ利用可能とされている。 [^]
  - Footnote: 注意書きとして「tool_search 機能は gpt-5.4 以降のモデルでのみ利用可能です」と記載されている。
- 利用手順は tools 配列への tool_search 追加と defer_loading 設定である。 [^]
  - Footnote: 記事では「tools 配列内に tool_search ツールを追加」「遅延ロードしたい関数に、MCPサーバーの場合はMCPサーバー用ツール定義に defer_loading: true を設定」と整理している。
- 検証用サンプルは野菜在庫管理の4ツールを題材にしている。 [^]
  - Footnote: サンプルのツール群として「在庫管理対象の野菜名を一覧で取得」「指定した野菜の在庫数を取得」「在庫数を増やす」「在庫数を減らす」が列挙されている。
- 通常実装では list_vegetables、get_stock、add_stock、sub_stock の関数とスキーマを明示的に定義している。 [^]
  - Footnote: コード内に `available_tools = {"list_vegetables": ..., "get_stock": ..., "add_stock": ..., "sub_stock": ...}` と各ツールスキーマが掲載されている。
- Responses API のツール呼び出しでは、在庫取得や更新が複数ステップで実行される様子が確認されている。 [^]
  - Footnote: 実行ログではジャガイモの在庫確認で `get_stock`、廃棄と入荷で `sub_stock` と `add_stock` が順に呼ばれている。

### References
- https://zenn.dev/kun432/scraps/5defa7ef1f2ca6
