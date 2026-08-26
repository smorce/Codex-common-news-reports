# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-08-26T09:01:32.4006078+09:00
- Articles: 3

## 「LLM-jp-4」 を試す（33B）
- Date: 2026-08-25T09:10:23+00:00

### Executive Summary
- LLM-jp-4 の新しい Dense 型 33B モデルについて、公開情報と実行手順を確認している。
- 公開モデルは base と thinking の 2 種類で、thinking は SFT と DPO による事後学習済みモデルとして紹介されている。
- アーキテクチャ上は 64 層、隠れ層サイズ 5120、40 ヘッド、コンテキスト長 65536、総パラメータ数約 332 億である。
- 学習は事前学習と中間学習の 2 段階で、総トークン数は 11.7T と説明されている。
- 評価では llm-jp-judge を使い、MT-Bench、AnswerCarefully、llm-jp-instructions などのタスクで比較している。
- GGUF 版も公式に公開されているが、llama.cpp は LLM-jp のフォーク版を使う必要がある点が重要な注意点である。
- 筆者は Ubuntu 22.04 と RTX4090、LLM-jp 版 llama.cpp、Q4_K_M の GGUF で実行を試している。
- 出力例では日本語回答に安心感があると評価し、reasoning_effort を llama-server 経由で指定できる点も確認している。

### Key Findings
- LLM-jp-4 33B は Dense 型モデルとして新たに公開された。 [^]
  - Footnote: 記事には「新たに約332億パラメータのDense型モデル『LLM-jp-4 33B』として、2種類のモデルを公開」とある。
- 公開モデルは base と thinking の 2 種類である。 [^]
  - Footnote: 記事では「llm-jp-4-33b-base」と「llm-jp-4-33b-thinking」が公開対象として列挙されている。
- thinking モデルは SFT と DPO によるアライメント処理済みで、強化学習は使っていない。 [^]
  - Footnote: モデルカード抜粋として「教師ありファインチューニング（SFT）と直接的選好最適化（DPO）によるアライメント処理を実施しており、強化学習は行っていません」と記載されている。
- 33B Dense のコンテキスト長は 65,536 で、総パラメータ数は 33,219,548,160 とされる。 [^]
  - Footnote: モデル詳細の表に「33B」「コンテキスト長 65,536」「総パラメータ数 33,219,548,160」とある。
- 学習パイプラインは事前学習と中間学習からなり、総トークン数は 11.7T である。 [^]
  - Footnote: 記事には「事前学習と中間学習の2段階からなるパイプライン方式で学習されており、総トークン数は11.7T」とある。
- GGUF 版の実行には通常の llama.cpp ではなく LLM-jp フォーク版が必要である。 [^]
  - Footnote: 記事では「元の ggml-org/llama.cpp には必要なトークナイザー処理の修正がまだ含まれていないため」と注意している。
- reasoning_effort は low、medium、high を指定でき、デフォルトは medium と確認されている。 [^]
  - Footnote: 筆者は「reasoning_effort を指定できるみたい。デフォルトは mediumで、low / high が指定できる」と記している。

### References
- https://zenn.dev/kun432/scraps/22c57c093bd516
- https://huggingface.co/llm-jp/llm-jp-4-33b-thinking
- https://huggingface.co/llm-jp/llm-jp-4-33b-thinking-gguf

## 「Ornith-1.5」を試す（35B-A3B / 9B）
- Date: 2026-08-19T16:03:03+00:00

### Executive Summary
- Ornith-1.5 は 9B Dense、35B MoE、397B MoE を含むオープンソース LLM ファミリーとして紹介されている。
- 記事では自己改善ループを中核に、タスク生成、スキャフォールド生成、ロールアウトをまとめて最適化するモデルとして説明している。
- ベンチマークでは Terminal-Bench 2.1、SWE-Bench、DeepSWE、HLE、ClawEval、Tool Decathlon などの値が示されている。
- 35B-A3B はトークンあたり約 3B パラメータを活性化する MoE で、同規模競合や Dense モデルを上回ると説明されている。
- 9B 版はモバイルやエッジデバイスへの展開を意識し、量子化版で 1.5GB まで圧縮されたと紹介されている。
- モデル配布形式は BF16、FP8、GGUF、MLX、NVFP4 など幅広く、Ollama、LM Studio、OpenCode などでの利用にも触れている。
- 筆者は Ubuntu 22.04 と RTX4090 で 35B-A3B の GGUF を llama.cpp から実行し、推奨サンプリング設定も確認している。
- 記事後半では出力例として日本語質問、競馬の楽しみ方、システムプロンプトによるペルソナ指定、画像説明などを試している。

### Key Findings
- Ornith-1.5 は 9B、35B、397B の 3 サイズを含むモデルファミリーである。 [^]
  - Footnote: 記事では「9B Dense、35B MoE、397B MoE を含むオープンソースLLMのファミリー」と紹介している。
- 自己改善ループが主要な特徴で、タスクや評価環境もモデルが生成する。 [^]
  - Footnote: 記事のまとめでは「タスクも評価の仕組みも、自分で考えて作る」と説明されている。
- タスク生成、スキャフォールド・ハーネス生成、ロールアウトの 3 ステージを最適化する。 [^]
  - Footnote: 記事には「タスク生成」「スキャフォールド・ハーネス生成」「ロールアウト」の 3 ステージ構成が示されている。
- 35B-A3B はトークンあたり約 3B のみを活性化する MoE として説明されている。 [^]
  - Footnote: モデルカード抜粋に「トークンあたり約30億パラメータのみを活性化」とある。
- 同規模モデルに対する優位性を、推論、コーディング、エージェント関連ベンチマークで主張している。 [^]
  - Footnote: 記事には「Qwen 3.6-35B を、すべての推論、コーディング、およびエージェント関連のベンチマークで大幅に上回って」とある。
- 9B Mobile 版は 1.5GB まで圧縮され、スマートフォンやエッジデバイス向け展開を意識している。 [^]
  - Footnote: 記事には「モデルのサイズを1.5 GBに圧縮」「スマートフォン、iPad、その他のエッジデバイスに容易に展開」とある。
- 商用・研究利用に広く使える MIT License として公開されている。 [^]
  - Footnote: 記事では「MIT Licenseの下でリリースされており、無制限の商用および研究利用が可能」と説明している。

### References
- https://zenn.dev/kun432/scraps/2d04d533e978c1
- https://ornith.ai/ornith_1_5.html
- https://huggingface.co/collections/ornith-ai/ornith-15

## メモ: COLD FUSION (GAIN+Unsloth) fine tuning
- Date: 2026-08-19T14:06:33+00:00

### Executive Summary
- この記事は COLD FUSION (GAIN+Unsloth) fine tuning について、モデルカードや関連 URL をもとに概念を整理している。
- 筆者は、軽い追加学習で元モデルの性能を保ちながら思考トークン削減と精度向上を狙う微調整レシピとして捉えている。
- 構成要素として、効率的な学習基盤の Unsloth、サンプルごとに学習制御を変える GAIN、それらを組み合わせた COLD FUSION を挙げている。
- GAIN は学習中にモデルの状態を見て、サンプルごとの重みやタスクの強め方を動的に変える仕組みとして説明されている。
- COLD FUSION は 4bit や 8bit 量子化でも BF16 に近い性能を維持し、thinking モードの思考トークンを削減する狙いがある。
- 筆者は ThinkingCap と似た印象を持ちつつ、モデル配布元のコレクションから創作やロールプレイ用途の色も感じ取っている。
- 商用利用については、データセットや蒸留元の不透明さを理由に慎重な見方を示している。
- 最後に Qwen3.8-27B Cold Fusion GAIN の GGUF と mmproj を使い、神戸の風景画像に対する詳細説明の実行例を記録している。

### Key Findings
- COLD FUSION は思考トークン削減と精度向上を両立させる微調整レシピとして紹介されている。 [^]
  - Footnote: 記事では「思考トークン削減＆精度アップを狙う微調整レシピ」と要約している。
- Unsloth は効率的に既存モデルをチューニングする土台として位置づけられている。 [^]
  - Footnote: 記事には Unsloth について「安く・速く・壊さず」に既存モデルをチューニングしやすくする土台とある。
- GAIN はサンプルごとに学習のかけ方を変える動的な学習制御手法として説明されている。 [^]
  - Footnote: 記事はモデルカードの引用として「automatically (and dynamically) changes training on a per sample basis」と記している。
- COLD FUSION は GAIN と Unsloth を組み合わせたものとして整理されている。 [^]
  - Footnote: 記事では「GAIN（動的トレーニング制御）」「Unsloth の効率的トレーニング環境・実装」をセットで回したものと説明している。
- 4bit と 8bit 量子化でも BF16 の 99% の性能維持を狙う点が強調されている。 [^]
  - Footnote: 記事には「元の BF16（フル精度）と比べて、4bit/8bit 量子化でも 性能の 99% を維持」とある。
- thinking モードの思考トークンを 1/10 から 1/2 程度まで削減する狙いがある。 [^]
  - Footnote: 記事では「いわゆる thinking モードの 1/10 ～ 1/2 くらいまで思考トークンを削減」と説明している。
- 筆者は商用用途ではデータセットや蒸留元の不透明さが懸念になると見ている。 [^]
  - Footnote: 記事には「使用しているデータセットなども記載されていないようなので、さすがに商用に絡む用途では厳しそう」とある。

### References
- https://zenn.dev/kun432/scraps/33358f57e2c777
- https://huggingface.co/DavidAU/Qwen3.8-27B-Cold-Fusion-GAIN-V1.1
- https://huggingface.co/DavidAU/Qwen3.8-27B-Cold-Fusion-GAIN-V1.1-NM-DAU-NEO-MAX-MTP-GGUF
