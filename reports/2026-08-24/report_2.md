# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-08-24T09:05:27.7781693+09:00
- Articles: 3

## Training AI to Paint with Code
- Date: 2026-03-01T00:00:00+09:00

### Executive Summary
- この記事は、画像生成をプロンプトだけでなく編集可能なコード生成として扱う研究事例を紹介している。
- モデルは p5.brush の JavaScript スケッチを書き、Puppeteer で PNG に描画される。
- 強化学習では、主観的な美的品質をどう報酬に変換するかが中心課題になっている。
- 初期の9指標ルーブリックは冗長で、報酬は上がっても生成能力が伸びにくかった。
- ペアワイズ評価と手作業で選んだ参照プールを導入し、報酬設計を大きく変更した。
- 新しい4指標の報酬では、前回の停滞点に3倍速く到達し、その後も改善が続いた。
- 長い API 仕様をプロンプトに入れるより、短い許可リストの方が API 幻覚を抑えた。
- 結論として、創作タスクの RL はモデル訓練だけでなく、好みを一般化する報酬設計の問題だと位置づけている。

### Key Findings
- 研究の狙いは、AI画像生成の成果物を編集可能なコードとして扱うことだった。 [^]
  - Footnote: 記事は、通常の画像生成では参加方法がプロンプトに限られ、生成物を直接編集できないことが出発点だったと説明している。
- 訓練ループはプロンプト、モデル、レンダリング、判定、報酬更新の4段階で構成される。 [^]
  - Footnote: モデルが p5.brush JavaScript スケッチを書き、Puppeteer 環境で PNG を作り、参照画像との比較で報酬に変換して GRPO 更新する流れが示されている。
- 初期報酬設計は9指標を含んだが、実質的には重複が多かった。 [^]
  - Footnote: 記事では、品質ジャッジとプロンプト遵守の相関が 0.85 から 0.95 で、同じ内容を何度も測っていたと診断している。
- 旧設計では報酬が約0.65で停滞し、生成物が似た形に収束した。 [^]
  - Footnote: 旧ルーブリックでは、5枚の丸い花びらを持つ平坦なクリップアート風の花が繰り返され、報酬だけが上がったと述べている。
- 新設計ではペアワイズ判定が報酬の中心になった。 [^]
  - Footnote: 新ルーブリックは compile gate 0.05、length 0.05、HPSv3 0.30、reference pool との pairwise judge 0.60 に整理された。
- 参照プールは手作業評価を含む 581 枚で構成された。 [^]
  - Footnote: 記事は、1664世代から love 117、okay 266 を選び、別生成の補足198枚を加えた 581 枚の参照プールを使ったと説明している。
- 長い API リファレンスは、かえって存在しない API の幻覚を誘発した。 [^]
  - Footnote: 初期プロンプトには 400 行の p5.brush API 参照があり、モデルが存在しない API を自信ありげに作ったと記述されている。
- 短い許可リスト型のプロンプトが、生成の安定性を高めた。 [^]
  - Footnote: GEPA による 200 イテレーション後、8つの brush メソッドだけを許可する短いプロンプトに収束し、3回中3回で見える hibiscus blobs が出たとされる。

### References
- https://surya.website/rling-qwen-to-paint-with-code

## GitHub - AlpinDale/gpt2.cmake: Implementation of the GPT-2 model in pure CMake

### Executive Summary
- このリポジトリは、GPT-2 モデルを純粋な CMake で実装する実験的プロジェクトである。
- README は Q16.16 の整数演算で GPT-2 を実行すると説明している。
- フルモデル実行では、Hugging Face から model.safetensors、vocab.json、merges.txt を取得する手順が示されている。
- 生成用スクリプトとして tools/gen_full.py を実行し、その後 cmake -P gpt2_full.cmake で推論する流れになっている。
- トイモデル向けには gen_tables.py と gen_model.py を実行してから gpt2.cmake を実行する。
- リポジトリは初期コミットのみで、表示時点ではスター6、フォーク0だった。
- 言語構成は CMake が中心で、Python は生成ツール部分を担っている。
- 実用目的というより、ビルドツールだけで言語モデル推論を表現する技術デモとして読むべき内容である。

### Key Findings
- プロジェクトの主題は GPT-2 の CMake 実装である。 [^]
  - Footnote: GitHub の About と README に "Implementation of the GPT-2 model in pure CMake" と表示されている。
- 演算方式は Q16.16 固定小数点整数演算である。 [^]
  - Footnote: README 冒頭に "GPT-2 in pure CMake, executed with Q16.16 integer arithmetic." と記載されている。
- フルモデル実行には GPT-2 の重みとトークナイザ関連ファイルが必要である。 [^]
  - Footnote: README の Full model 手順には model.safetensors、vocab.json、merges.txt を checkpoint に取得する curl コマンドが並ぶ。
- フルモデルの CMake スクリプトは生成ステップを経て作られる。 [^]
  - Footnote: Full model 手順では python3 tools/gen_full.py の後に cmake -P gpt2_full.cmake を実行する。
- サンプル推論では PROMPT と N を CMake 実行時に渡す。 [^]
  - Footnote: README は cmake -P gpt2_full.cmake -DPROMPT="Hello" -DN=2 という形式を示している。
- トイモデルには別の生成手順が用意されている。 [^]
  - Footnote: Toy model セクションには python3 tools/gen_tables.py、python3 tools/gen_model.py、cmake -P gpt2.cmake が記載されている。
- ライセンスは BSD 3-Clause で公開されている。 [^]
  - Footnote: README の License セクションに BSD 3-Clause とあり、LICENSE ファイルへのリンクが表示されている。
- 表示時点では小規模な初期公開リポジトリである。 [^]
  - Footnote: GitHub 画面には initial commit、1 Commit、6 stars、0 forks、No releases published と表示されている。

### References
- https://github.com/AlpinDale/gpt2.cmake

## 米Amazon、同意なくTwitch動画をAI学習に使用。集団訴訟を起こされる
- Date: 2026-08-24T07:15:00+09:00

### Executive Summary
- この記事は、Twitch の配信アーカイブやコンテンツを生成AI学習に使う方針をめぐる集団訴訟を報じている。
- Twitch は 8月12日に、Amazon 全体の生成AIモデル訓練への利用を拒否する設定を追加したと説明した。
- 問題視されたのは、設定がデフォルトで利用許可になっていた点である。
- Twitch 幹部は、オプトイン方式なら誰も選ばないだろうと述べ、反発を招いた。
- オプトアウトは自分のチャンネルにだけ適用され、他チャンネルで表示された自分のコンテンツには効かない可能性がある。
- 原告側は、配信者を商用AI製品の無料学習素材として使う判断が契約違反だと主張している。
- 訴状では、承認なしの大量複製、暗黙の合意違反、不正競争防止法違反が挙げられている。
- 記事は、同種の訴訟が Apple や Meta、NVIDIA、ByteDance、Snap にも広がっていることを補足している。

### Key Findings
- Twitch は配信者コンテンツを Amazon 全体の生成AIモデル訓練に使う方針を示した。 [^]
  - Footnote: 記事は、Twitch が生成型AIモデルのトレーニングに配信アーカイブやコンテンツを利用すると発表したと報じている。
- 反発の中心は、デフォルト設定が利用許可だった点にある。 [^]
  - Footnote: 記事冒頭で、チャンネル設定がデフォルトでコンテンツ使用を許可する状態だったことが反発を招いたと説明している。
- Twitch は拒否オプションを設定に追加した。 [^]
  - Footnote: 8月12日の Twitch 投稿として、チャンネルコンテンツの AI 学習利用を拒否するためのオプションを設定に追加したと紹介されている。
- Twitch 幹部はオプトイン方式では参加者が集まらないという趣旨の発言をした。 [^]
  - Footnote: 記事は、CPO のマイク・ミントン氏が、オプトイン方式なら誰もオプトインしないだろうと返答したと記している。
- オプトアウトの効力は限定的である可能性がある。 [^]
  - Footnote: 記事は、自分がオプトアウトしても、自分のコンテンツが他の非オプトアウトチャンネルで表示された場合は、そのチャンネル設定が適用され得ると説明している。
- 原告側は契約違反を主張している。 [^]
  - Footnote: 訴訟では、配信者を別の商用AI製品の無料トレーニング素材として利用する決定が契約違反だと主張されている。
- 訴状は承認なしの複製と不正競争を問題にしている。 [^]
  - Footnote: 訴状による主張として、適切な承認なしの大量映像複製、暗黙の合意違反、州の不正競争防止法違反が挙げられている。
- 動画コンテンツの AI 学習利用をめぐる訴訟は Amazon だけに限らない。 [^]
  - Footnote: 記事は、今年4月に YouTube チャンネルが Apple を相手取って同様の集団訴訟を起こし、Meta、NVIDIA、ByteDance、Snap に対しても類似訴訟があると補足している。

### References
- https://www.techno-edge.net/article/2026/08/24/5417.html
