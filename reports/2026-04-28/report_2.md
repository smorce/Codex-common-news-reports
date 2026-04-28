# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-04-28T11:13:05+09:00
- Articles: 3

## AnthropicがClaudeのAIエージェントに物品の売買や交渉を任せるAI市場をシミュレーションするProject Dealを実施、高性能モデルがより優れた取引を行うものの驚きの買い物をしてくるケースも
- Date: 2026-04-27T11:39:00+09:00

### Executive Summary
- Anthropicは、Claudeに買い付け、販売、交渉を任せる市場実験「Project Deal」を実施した。
- 実験はサンフランシスコのオフィス従業員向けマーケットプレイスとして構成された。
- 狙いは、買い手側と売り手側の双方にAIエージェントがいる市場の挙動を観察することだった。
- AI Newsの一覧では、4市場を設けてAIが取引を担当したと整理されている。
- 高性能モデル同士の取引では、総額約4000ドル、186件の取引が記録された。
- 参加者は取引を公平と感じ、将来の支払い意欲も半数近くに達した。
- 一方で、高性能モデルでも想定外の買い物を行うケースがあり、商取引への導入には監督が必要だ。
- 記事は、AIエージェント市場が理論段階から実験段階へ進みつつあることを示している。

### Key Findings
- Project DealはClaudeに商取引の実務を代行させる実験である。 [^]
  - Footnote: GIGAZINE本文に、従業員向けマーケットプレイスを作成し「人間の代わりにClaudeに買い付け、販売、交渉を行わせる」とある。
- 実験の目的は、AIエージェント同士が存在する市場の挙動を調べることだった。 [^]
  - Footnote: GIGAZINE本文に、Anthropicが「買い手と売り手にAIエージェントがいる市場がどのようなものになるか」を作成したと説明している。
- AI Newsは、4市場を設けてAIが買付・販売・交渉を担当したと要約している。 [^]
  - Footnote: AI News一覧の当該カードに「4市場を設け、AIが買付・販売・交渉を担当する実験を実施。」とある。
- 取引規模は、高性能モデル同士で総額約4000ドル、186件とされる。 [^]
  - Footnote: AI News一覧の当該カードに「高性能モデル同士の取引で総額約4000ドル、186件を記録。」とある。
- 参加者の受け止めは比較的肯定的だった。 [^]
  - Footnote: AI News一覧の当該カードに「参加者は取引を公平と感じ、将来の支払い意欲は半数近く。」とある。
- 公開記事は一次情報としてAnthropicのProject Dealページを参照している。 [^]
  - Footnote: GIGAZINE本文に「Project Deal: our Claude-run marketplace experiment | Anthropic」とURLが掲載されている。

### References
- https://gigazine.net/news/20260427-project-deal-anthropic/
- https://www.anthropic.com/features/project-deal
- https://ai-news.dev/

## Introducing talkie: a 13B vintage language model from 1930
- Date: 2026-04-01T00:00:00+00:00

### Executive Summary
- talkieは、1931年より前の英語テキストだけで学習した13B規模のビンテージ言語モデルである。
- 著者らは、歴史的テキストのみで学習したモデルがAI研究全般の理解に役立つと位置づけている。
- モデルは現代のウェブや現代的なチャットデータを使わず、時代性を保つ方向で設計されている。
- 一方で、Roosevelt政権や第二次世界大戦関連の知識など、時代漏れが完全には防げていない。
- 評価では、現代ウェブで学習した同一構造モデルより標準ベンチマークで劣るが、言語理解や数的課題では近い結果も見られた。
- 汚染の少ない実験環境として、未来予測、発明、コーディング学習などの一般化能力を調べられる。
- OCR品質は大きな課題で、通常OCR由来のテキストは人手転写に比べて学習効率が大きく落ちる。
- 今後はコーパス拡大、多言語化、OCR改善、漏えい検出、歴史家との協力によるポストトレーニング改善を進める。

### Key Findings
- talkie-1930-13b-baseは、260Bトークンの1931年前英語テキストで学習された。 [^]
  - Footnote: 記事本文に「a 13B language model trained on 260B tokens of historical pre-1931 English text」とある。
- 著者らは、talkieを既知の範囲で最大のビンテージ言語モデルとしている。 [^]
  - Footnote: 記事本文に「talkie is the largest vintage language model we are aware of」とある。
- モデルは汚染の少ない一般化実験に使える。 [^]
  - Footnote: 記事本文に、Vintage LMsは「contamination-free by construction」であり、デジタルコンピュータの知識なしに現代言語でコードを書けるか調べる例が示されている。
- 時代漏れは完全には除去できていない。 [^]
  - Footnote: 記事本文に、13B版が第二次世界大戦や国際連合、ドイツ分割の一部詳細を知っているとある。
- OCR品質は学習効率に大きく影響する。 [^]
  - Footnote: 記事本文に、通常OCRで転写した1931年前テキストでは、人手転写版に比べて30%の性能にとどまり、正規表現クリーニングで70%まで戻るとある。
- ポストトレーニングでは現代的バイアスを避けるため、歴史的な定型テキストからデータを作った。 [^]
  - Footnote: 記事本文に、礼儀作法書、手紙文例集、料理本、辞書、百科事典などからinstruction-response pairsを生成したとある。
- 今後はGPT-3級モデルの公開と、1兆トークン超の歴史コーパス拡大を目指している。 [^]
  - Footnote: 記事本文に、次の段階としてGPT-3-level modelを夏に公開したいこと、コーパスをwell over a trillion tokensへ拡大できる見積もりがあることが書かれている。

### References
- https://talkie-lm.com/introducing-talkie
- https://github.com/talkie-lm/talkie
- https://huggingface.co/talkie-lm

## OpenAI、Microsoftと独占契約終了　Amazon経由でモデル提供
- Date: 2026-04-28T04:08:00+09:00

### Executive Summary
- 日本経済新聞は、OpenAIがMicrosoftへのAIモデル独占提供契約を終了すると報じた。
- 発表日は両社が27日とされ、記事の公開時刻は2026年4月28日4時08分である。
- OpenAIはMicrosoftからの収益分配を受けない代わりに、他クラウド経由で事業を広げられるようになる。
- 記事の公開部分では、AmazonやGoogleなど大手クラウドとの交渉余地が示されている。
- AI Newsは、独占契約終了により収益分配の縛りがなくなると要約している。
- 法人向けでは、プログラミング支援など外部提供の機会が広がると見られる。
- 有識者コメントでは、AI競争がモデル性能からAIエージェントを中核にした企業システム構築へ移ったとの見方が示された。
- 本文の大部分は会員限定のため、詳細な契約条件や未公開部分は本レポートでは扱わない。

### Key Findings
- OpenAIはMicrosoftへのAIモデル独占提供契約を終了する。 [^]
  - Footnote: 日経本文の公開部分に「米オープンAIは人工知能（AI）モデルを米マイクロソフトに独占的に提供する契約を終了する」とある。
- 終了は両社が27日に発表した内容として報じられている。 [^]
  - Footnote: 日経本文の公開部分に「両社が27日発表した」とある。
- OpenAIは収益分配を受けない代わりに、他クラウド経由の事業拡大が可能になる。 [^]
  - Footnote: 日経本文の公開部分に「マイクロソフトからの収益分配を受けない代わりに、他のクラウド大手を通じた事業拡大が可能になる」とある。
- 外部提供先としてAmazonやGoogleなどのクラウド大手が想定されている。 [^]
  - Footnote: 日経本文の公開部分に「米アマゾン・ドット・コム、米グーグルなど他のクラウド大手と交渉」とある。
- 法人向け事業ではプログラミング支援が例示されている。 [^]
  - Footnote: 日経本文の公開部分に「プログラミング支援など法人向けの事業拡大」とある。
- AI Newsは、独占契約終了で外部提供の機会と法人支援が強化されると要約している。 [^]
  - Footnote: AI News一覧の当該カードに「外部提供の機会が広がり、法人支援も強化。」とある。
- 有識者は、競争軸がAIエージェント中心の企業システム構築へ移ったと見ている。 [^]
  - Footnote: 日経ページの公開コメントに、競争軸は「AIエージェントを中核とした新たな企業システム構築方法」に移っているとある。

### References
- https://www.nikkei.com/article/DGXZQOGN27ARC0X20C26A4000000/
- https://ai-news.dev/
