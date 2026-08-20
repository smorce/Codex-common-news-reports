# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-08-20T09:01:53.4506062+09:00
- Articles: 3

## 「Ornith-1.5」を試す（35B-A3B / 9B）
- Date: 2026-08-20T01:03:00+09:00

### Executive Summary
- Ornith-1.5 は 9B Dense、35B MoE、397B MoE を含むオープンソース LLM ファミリーとして紹介されている。
- 記事では、自己改善戦略で訓練されたモデルとして、推論・コーディング・エージェント用途の性能を中心に整理している。
- ベンチマーク例として Terminal-Bench 2.1、SWE-Bench、DeepSWE、HLE、ClawEval、Tool Decathlon が挙げられている。
- Ornith-1.0 の自己スキャフォールディングを、タスク提案、スキャフォールド生成、RL 用ロールアウト生成まで含むループへ拡張した点が重要とされている。
- MIT License でモデルと量子化版が公開され、商用・研究利用の自由度が高いと説明されている。
- 35B-A3B は同規模モデルや一部 Dense モデルに対する優位性が示され、HF モデルへのリンクも掲載されている。
- 筆者は llama-cli で 35B-A3B と 9B を実行し、画像説明や会話応答の品質を比較している。
- 9B 版については動作例を踏まえ、35B-A3B より多少粗さがあるという所感で締めている。

### Key Findings
- Ornith-1.5 は複数サイズのオープンソース LLM ファミリーである。 [^]
  - Footnote: 記事中に「9B Dense、35B MoE、397B MoE を含むオープンソースLLMのファミリー」とある。
- 自己改善型の学習ループがモデルの中心的な特徴である。 [^]
  - Footnote: 本文では「モデルは新しいタスクを提案し、タスク固有のスキャフォールドを生成し、強化学習のための解決策ロールアウトを生成」すると説明されている。
- 主要ベンチマークで高いスコアが列挙されている。 [^]
  - Footnote: Terminal-Bench 2.1 は 86.1、SWE-Bench は verified 86 / pro 65.1 / Multilingual 79.6、DeepSWE は 56 と記載されている。
- ライセンス面では利用しやすい公開形態が示されている。 [^]
  - Footnote: 「すべてのモデルとその量子化バージョン（FP8、GGUF、MLX、NVFP4）は、MIT Licenseの下でリリース」とある。
- 35B-A3B はトークンあたり 3B パラメータ活性でも強いとされる。 [^]
  - Footnote: 記事では「トークンあたりわずか3Bのパラメータしか活性化しないにもかかわらず」とした上で Gemma 4-31B や Muse Glimmer-30B への優位性を述べている。
- 筆者はローカル実行で画像説明タスクを試している。 [^]
  - Footnote: llama-cli の実行例に `--image kobe.jpg` と「この画像について詳しく説明して。」というプロンプトが掲載されている。
- 9B 版は実用例を示しつつも品質差があると評価されている。 [^]
  - Footnote: 末尾に「35B-A3Bに比べると多少アラがある感じかなぁ？」という所感がある。

### References
- https://zenn.dev/kun432/scraps/2d04d533e978c1
- http://ornith.ai/ornith_1_5.html
- https://huggingface.co/collections/ornith-ai/ornith-15

## メモ: COLD FUSION (GAIN+Unsloth) fine tuning
- Date: 2026-08-19T23:06:00+09:00

### Executive Summary
- この記事は Hugging Face 上の Qwen 系 COLD FUSION モデルを起点に、GAIN と Unsloth を組み合わせた微調整手法を整理している。
- 筆者はまず試用感が良さそうだったため、COLD FUSION が何を意味するのかを調べている。
- Unsloth は LoRA などを含む効率的な学習ツールチェーンとして位置づけられている。
- GAIN はサンプルごとに学習のかけ方を動的に変える仕組みとして紹介されている。
- COLD FUSION は GAIN の動的制御と Unsloth の効率的環境を組み合わせたものとまとめられている。
- 狙いは元モデルの性能や性格を大きく壊さず、思考トークン削減と性能維持・改善を両立することにある。
- 記事では 4bit/8bit 量子化でもフル精度に近い性能を維持するというモデルカード上の主張を紹介している。
- 一方で、蒸留元やデータセットの透明性に疑問があり、商用利用には慎重さが必要という見解も示されている。

### Key Findings
- COLD FUSION は軽い追加学習で元モデル性能を保ちつつ改善を狙う手法として説明されている。 [^]
  - Footnote: 本文に「軽い追加学習だけで、“ほぼ元モデルそのままの性能”を保ちつつ、思考トークン削減＆精度アップを狙う微調整レシピ」とある。
- Unsloth は効率的に既存モデルを調整する土台として扱われている。 [^]
  - Footnote: 記事では Unsloth について「LoRA みたいな手法や効率的な学習テク」をまとめ、「安く・速く・壊さず」にチューニングしやすくすると説明している。
- GAIN は学習中にサンプル単位で制御を変える動的手法である。 [^]
  - Footnote: 記事中でモデルカードの説明として「automatically (and dynamically) changes training on a per sample basis」と引用されている。
- GAIN の効果としてベンチ改善と能力崩壊の抑制が期待されている。 [^]
  - Footnote: 本文では「ベンチスコアが上がる」一方で「過学習で性格変わる」や「元の能力崩壊」を起こしにくいと整理している。
- 量子化後の性能維持が大きな訴求点になっている。 [^]
  - Footnote: 記事では「4bit/8bit 量子化でも 性能の 99% を維持」と記載されている。
- 思考トークン削減が COLD FUSION の実用的な利点として挙げられている。 [^]
  - Footnote: 本文に「1/10 ～ 1/2 くらいまで思考トークンを削減」とある。
- KoboldCpp や Silly Tavern 向け設定がモデルカードにある点を珍しいと評価している。 [^]
  - Footnote: 記事では「KoboldCpp」「Silly Tavern」向け設定が記載されていることに触れ、「これはなかなか珍しい」と述べている。
- 商用利用にはデータ透明性の観点で懸念が残る。 [^]
  - Footnote: 本文では「使用しているデータセットなども記載されていないようなので、さすがに商用に絡む用途では厳しそう」としている。

### References
- https://zenn.dev/kun432/scraps/33358f57e2c777
- https://huggingface.co/DavidAU/Qwen3.8-27B-Cold-Fusion-GAIN-V1.1

## 「ZCode」を試す ④ タスクとファイルの管理
- Date: 2026-08-18T01:06:00+09:00

### Executive Summary
- この記事は ZCode 試用シリーズの4本目で、前回の Goal モードに続いてタスクとファイル管理を扱っている。
- 本文自体は短く、ZCode 公式の Task & File Management ドキュメントへの参照が主内容になっている。
- 公式ドキュメントでは、左サイドバーでタスクをグループ、ワークスペース、タイムラインの各ビューで整理できると説明されている。
- タスクビューでは作成時刻や更新時刻による並び替え、キーワード検索、アーカイブ操作が提供される。
- グループ機能では New Group、色分け、名前変更、ドラッグ操作、コンテキストメニューでの移動が可能とされる。
- Workspace File Tree では ZCode を離れずにファイルを閲覧し、変更確認やチャットへのファイル参照追加ができる。
- Git 状態の表示や変更ファイルのみの絞り込みにより、レビューやコミット前確認の作業導線が用意されている。
- Repo wiki と Git Graph も同じ文脈で紹介され、リポジトリ理解や履歴確認を補助する機能として整理されている。

### Key Findings
- 記事は ZCode のタスクとファイル管理を扱う回である。 [^]
  - Footnote: 本文に「今回は『タスクとファイルの管理』について」と記載され、ZCODE Docs の Task & File Management にリンクしている。
- ZCode はタスク一覧を複数ビューで整理できる。 [^]
  - Footnote: 参照先ドキュメントには task views が group、workspace、timeline でタスクリストを整理できるとある。
- Grouped ビューはトピック、優先度、フェーズ別の管理に向いている。 [^]
  - Footnote: 公式ドキュメントで Grouped は「custom groups」で整理し、topics、priorities、phases に有用と説明されている。
- Workspace ビューはタスクを所属プロジェクト単位で扱う。 [^]
  - Footnote: 公式ドキュメントに Workspace は「keep tasks under the project they belong to」とある。
- Timeline ビューは最近の作業を逆時系列で確認できる。 [^]
  - Footnote: 公式ドキュメントに Timeline は「browse recent work in reverse chronological order」とある。
- タスク管理には検索、並び替え、アーカイブが組み込まれている。 [^]
  - Footnote: 公式ドキュメントでは Sort order、Search、Archive が view menu 付近の共通操作として説明されている。
- ファイルツリーは変更確認とチャット連携を同じ導線にまとめる。 [^]
  - Footnote: 公式ドキュメントでは workspace file tree が browse files、review changes、reference files in chat を ZCode 内で可能にすると説明されている。
- Repo wiki はリポジトリ構造を読みやすい文書に変換する機能として紹介されている。 [^]
  - Footnote: 公式ドキュメントでは Repo wiki が「current repository structure into a readable document」にし、各主張をソースにリンクするとある。

### References
- https://zenn.dev/kun432/scraps/fb7fffbd177760
- https://zcode.z.ai/en/docs/task-management
