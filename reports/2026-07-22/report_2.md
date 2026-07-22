# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-07-22T09:05:29.1419984+09:00
- Articles: 3

## 「Agents-A1」を試す（4B）
- Date: 2026-07-21T00:00:00+09:00

### Executive Summary
- Agents-A1は長期探索、エンジニアリング、科学研究、指示追従、ツール呼び出しを対象にしたエージェント型モデルとして紹介されている。
- 記事では、当初の35B-A3B MoEモデルに加えて、2026年7月14日に4Bモデルがリリースされた点を中心に扱っている。
- 4B版はBF16、FP8、GGUFなど複数形式で提供され、ローカルAIアシスタント構築を高速かつ容易にする狙いが示されている。
- モデルカードの説明では、Agents-A1が長期視野の拡張と多様なエージェント機能の拡張を重視している。
- 性能評価ではBrowseComp、XBench-DS-2510、GAIA、IFEvalなどで同規模モデルを上回る結果が提示されている。
- 記事後半では、Mac M2 Pro上で4B GGUF Q8_0をllama.cppから試す手順と推奨サンプリング設定が記録されている。
- 実行例ではVision対応らしき表示や、回答中の長い思考過程、固有名詞の誤りなど、実用時に観察された挙動も共有されている。

### Key Findings
- Agents-A1は長期タスク向けのエージェント型モデルとして位置づけられている。 [^]
  - Footnote: 記事冒頭で「検索、エンジニアリング、科学研究、指示追従、ツール呼び出しにわたる長期的タスク向けに構築された、35B MoE エージェント型モデル」と紹介されている。
- 4Bモデルの公開が、記事作成時点で注目されている主な理由になっている。 [^]
  - Footnote: ニュース欄に「2026年7月14日: 4Bモデルをリリースしました」とあり、筆者も「どうやら4Bモデルが出たみたい」と述べている。
- 4B版と35B版は、BF16、FP8、GGUFなど複数の配布形式が用意されている。 [^]
  - Footnote: 記事のバリエーション一覧に「35B-A3B MoE BF16 FP8 GGUF」と「4B Dense BF16 FP8 GGUF」が列挙されている。
- モデルは関数呼び出しや外部ツール連携を標準的な特徴としている。 [^]
  - Footnote: 主な特徴の項目に「関数呼び出し機能とツール統合機能を標準搭載」「API、コードインタープリタ、検索エンジンなどの外部ツール」と記載されている。
- 4Bモデルでも複数ベンチマークで同規模モデルを大きく上回ると説明されている。 [^]
  - Footnote: 性能評価では「BrowseComp（66.8）、XBench-DS-2510（90.0）、GAIA（95.1）、FrontierScience-Research（33.3）、IFEval（94.8）」が挙げられている。
- 評価フレームワークも公開され、再現性や比較可能性が重視されている。 [^]
  - Footnote: 記事には「エージェントモデルの中核機能を評価するフレームワークもオープンソースとして公開」とある。
- 筆者はMac M2 Proで4B GGUF Q8_0をllama.cppから試している。 [^]
  - Footnote: 記事後半に「今回は Mac（M2 Pro）で、4B GGUF Q8_0 を試してみる」とあり、llama-cliの実行例が示されている。

### References
- https://zenn.dev/kun432/scraps/c070bfe51ac731

## "Drawing" the Mona Lisa with GPT-5.6, Claude, Gemini, and Grok · TryAI
- Date: 2026-07-21T00:00:00+00:00

### Executive Summary
- TryAIは、4つのフロンティアモデルに白紙キャンバスと色鉛筆ツールを与えて描画させる比較実験を行った。
- 対象モデルはGPT-5.6 Sol、Claude Fable 5、Grok 4.5、Gemini 3.6 Flashで、モナリザと星月夜の再現、5つの自由プロンプトを試している。
- 実験は合計28枚の描画で、ツール利用、コスト、トークン、所要時間、自己レビュー、SSIM/RMSEなどを比較している。
- 数値上はGemini 3.6 Flashがターゲット再現のSSIMで高い値を出したが、記事の主観評価ではGPT-5.6 Solが総合的に最も優れているとされた。
- Claude Fable 5は品質では2番手とされた一方、7枚で約160ドルと他モデルの約20倍のコストになった。
- Grok 4.5はツール呼び出しが多いにもかかわらず、視覚的な出力の安定性や判断力に課題があると評価されている。
- 全ターゲット実行で最終出力が途中のベストSSIMを下回り、モデルが自分の最良状態を超えて編集し続ける傾向も示された。

### Key Findings
- 実験は4モデル、2つのターゲット画像、5つの自由プロンプトで構成されている。 [^]
  - Footnote: 記事には「GPT-5.6 Sol, Claude Fable 5, Grok 4.5, and Gemini 3.6 Flash」「two targets」「five open-ended prompts」「28 drawings total」とある。
- 各モデルは同一の色鉛筆ツールセットで描画した。 [^]
  - Footnote: ツール欄で「Every model worked with the exact same colored-pencil toolset」と説明され、draw、smudge、erase、view_canvasなどが列挙されている。
- GPT-5.6 Solは少ないコストと時間で高い主観品質を出したと評価されている。 [^]
  - Footnote: headline numbersではGPT-5.6 Solが平均6.2分、総コスト7.74ドルで、Our takeでは「runaway leader」と評されている。
- Claude Fable 5はコストと時間の面で不利だった。 [^]
  - Footnote: 記事はClaude Fable 5について「$160 for its seven drawings, roughly 20x GPT-5.6 Sol」とし、平均時間も12.5分と示している。
- Grok 4.5は多数のツール呼び出しを行ったが、描画品質の評価は低い。 [^]
  - Footnote: ツール利用ではGrokが1,349 tool callsの65%をset系に使ったとされ、Our takeでは「rarely produced anything usable」と評価されている。
- Gemini 3.6 Flashは自己レビューが多く、ターゲット再現のSSIMでは高い値を出した。 [^]
  - Footnote: 記事はGeminiについて「about 23 self-reviews per drawing」とし、Mona Lisaでbest SSIM 0.449、final SSIM 0.337を示している。
- 全ターゲット実行で最終出力は途中の最高スコアを下回った。 [^]
  - Footnote: 記事には「in all eight target runs, the final drawing scored below the best the model reached mid-run」とある。
- SSIMは人間の見た目の品質を直接測るものではないと注意されている。 [^]
  - Footnote: 方法メモに「SSIM/RMSE ... measure structural/pixel closeness, not artistic quality」と明記されている。

### References
- https://www.tryai.dev/blog/ai-drawing-arena-colored-pencils-claude-gpt-grok

## 音楽理論がわからない？　ならば自分で教材を作ってしまおう。ChatGPTとGeminiによる自分専用教科書構築メソッド（CloseBox）
- Date: 2026-07-22T07:25:00+09:00

### Executive Summary
- 記事は、音楽理論を体系的に学びたい筆者が、ChatGPTとGeminiを使って自分専用教材を作る過程を紹介している。
- 筆者はバークリーメソッドやコード・スケール理論への理解を深めるため、まずChatGPTに自分向け教材の作成を依頼した。
- ChatGPTはギター、鍵盤、Logic Proで音を確かめる学習方針を提案し、コード機能、テンション、ボイスリーディングなどを整理した。
- ChromeのGemini相談機能は、教材を読んでいる最中の疑問を文脈付きで解消する補助役として使われている。
- 筆者は音のフィードバックが必要だと考え、Web Audio APIで試聴できるインタラクティブ教材の作成へ発展させた。
- 完成した教材には全12課、譜例、鍵盤図、ギター指板図、Logic Pro課題、解答、Geminiで得た疑問回答のコラムが含まれる。
- 一方で、画像生成AIが鍵盤の白鍵と黒鍵の位置関係を正しく描けない問題も指摘されている。

### Key Findings
- 筆者の出発点は、音楽制作を続ける中で音楽理論の基礎不足を感じたことだった。 [^]
  - Footnote: 本文冒頭で「音楽関連のヴァイブ・コーディングをやってきた」「やはり根本的なところを学んでいないのです。音楽理論」と述べている。
- ChatGPTは筆者専用の学習対象として、ギター、鍵盤、Logic Proを中心に教材を構成した。 [^]
  - Footnote: ChatGPTの返答に「あなた向けなら、『ギターと鍵盤で音を確かめ、Logic Proで曲に使う』ことを中心にします」とある。
- 教材の中核にはコード機能、コード・スケール、テンション、ボイスリーディングなどが置かれている。 [^]
  - Footnote: ChatGPTは「コードを機能で捉える」「コードと使用可能なスケールを結びつける」「ボイスリーディングを重視する」などを列挙している。
- Geminiは、読んでいるページの文脈を保ったまま疑問に答える補助ツールとして使われている。 [^]
  - Footnote: 本文ではChromeの「Geminiに相談」機能について「読んでいる場所からは動かずに、疑問点だけを聞き出せるので便利」と説明している。
- 最終教材は音を鳴らせるインタラクティブ教材に拡張された。 [^]
  - Footnote: ChatGPTは「音は外部音源を使わず、HTML内のWeb Audio APIで生成するため、インターネット接続なしでも鳴らせます」と説明している。
- 全12課の教本形式に、譜例、鍵盤図、ギター指板図、Logic Pro課題、解答を付ける構成が提案された。 [^]
  - Footnote: 本文中に「教材を全12課の教本形式に拡張し、各課に譜例、鍵盤図、ギター指板図、Logic Pro課題、解答を付ける」とある。
- AI生成画像には、鍵盤を正しく描けないという残課題がある。 [^]
  - Footnote: 筆者はスケール入門マンガについて「白鍵と黒鍵の位置関係がめちゃくちゃ」と述べている。

### References
- https://www.techno-edge.net/article/2026/07/22/5318.html
