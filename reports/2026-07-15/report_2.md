# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-07-15T09:05:08.7458160+09:00
- Articles: 3

## Accretive Editing | Justin D Fuller
- Date: 2026-07-10T00:00:00+09:00

### Executive Summary
- AIツールが文章更新時に古い情報を削除せず、新情報へ注釈的に足す失敗を「accretive editing」と呼んでいる。
- 例として、Amazon Bedrock対応をLiteLLM対応へ変えた際、旧対応終了の文まで残る更新が挙げられている。
- 大きな仕様変更の告知自体は必要だが、本文中に旧情報を散在させるのは望ましくないと指摘している。
- 単に短く書けと指示しても、古い情報を短い形で残すだけで根本対策にならない。
- 文体指示でも、旧情報が別文に移動するだけで問題が解消しにくい。
- 人間は読者にとって正しい文書にするため古い記述を削除するが、LLMは旧情報と新指示を同時に出力しやすいと推測している。
- 対策として、古い文を保持せず正しい新文へ置き換え、最初から正しく書かれた文書のように仕上げる指示が推奨されている。

### Key Findings
- 失敗モードは、古い記述を残したまま新情報を付け足す形で現れる。 [^]
  - Footnote: 記事は、AIが「adds a parenthetical or some other type of addendum, rather than correcting the text」と説明している。
- 旧プロバイダーから新プロバイダーへの変更でも、旧情報が本文に残る具体例が示された。 [^]
  - Footnote: Bedrock対応削除とLiteLLM対応追加後に「This project can authenticate with LiteLLM but no longer supports Amazon Bedrock.」になった例が掲載されている。
- 仕様変更の履歴は本文に混ぜるより、変更履歴や告知で扱うべきだとしている。 [^]
  - Footnote: 記事は、changelog、announcement、docs内のcalloutが望ましいと述べている。
- 「短く書く」指示は、冗長な追記を短い追記に変えるだけである。 [^]
  - Footnote: 記事は「write less」では「This project can authenticate with LiteLLM, not Amazon Bedrock.」のような terse accretion になると説明している。
- 推奨される指示は、 obsolete text を正しい text に置換する考え方を明示すること。 [^]
  - Footnote: 記事は「replace obsolete text with accurate text rather than preserving the obsolete text and adding a correction」と提示している。

### References
- https://justindfuller.com/programming/accretive-editing

## AIの発展によって私たち「人間」に残される仕事は何か？人間とAIの「共同超知能」というビジョン
- Date: 2026-07-14T22:00:00+09:00

### Executive Summary
- GIGAZINEは、ICML 2026でのアルヴィンド・ナラヤナン氏の基調講演を紹介している。
- 講演の中心は、AIが仕事の多くを担う未来に人間がどう備えるかという問いである。
- ナラヤナン氏はAIを電気やインターネットと同様に、普及に長い時間を要する「Normal Technology」と位置付ける。
- AIの発明や導入が進んでも、組織や制度、人間の働き方が適応するには数十年単位の時間がかかるとされる。
- AIによる生産性向上がそのまま雇用減少を意味するわけではなく、需要拡大の可能性も示されている。
- 人間の役割は作業そのものから、目的地の設定や進路調整、評価へ移ると説明されている。
- ブラックボックス的なAI利用や専門外タスクの丸投げは、制御喪失やスキル低下につながる危険がある。
- 結論として、AIに依存するだけでなく、人間の能力を高める「共同超知能」の視点が提示されている。

### Key Findings
- AIは社会を即座に一変させる特別な存在ではなく、広く浸透するまで時間がかかる通常技術として扱われている。 [^]
  - Footnote: 記事は、AIも電気や蒸気機関、コンピューター、インターネットと同様に社会へ広く浸透するには長い時間がかかると説明している。
- ソフトウェア分野では、普及後の「適応」が最も遅い段階だとされる。 [^]
  - Footnote: 記事は「適応」は最も遅く、現代ではまだ本格的に始まってすらおらず、数十年かかると紹介している。
- AIによる生産性向上が雇用を単純に10分の1へ減らすという見方は否定されている。 [^]
  - Footnote: 記事は「ソフトウェアエンジニアの生産性が10倍向上するなら、必要なソフトウェアエンジニアの数は10分の1で済む」という考えはデータと矛盾すると述べている。
- AI時代の人間の役割は、作業実行から評価・目的設定・調整へ移る可能性がある。 [^]
  - Footnote: 記事は、人間の役割が「目的地を決めて進路を調整する役割」になる変化を今後10年か20年で予測している。
- AIエージェントをブラックボックスとして使う誘惑には注意が必要とされる。 [^]
  - Footnote: 記事は、指示だけで勝手に動くものとして使うことは「制御を手放してしまう危険なワナ」だと紹介している。
- 専門外タスクをAIへ任せ続けると、わずかなスキルすら失う依存の悪循環が起こり得る。 [^]
  - Footnote: 記事は、そのタスクに関して持っていたわずかなスキルすら失う「依存のスパイラル」に陥ると警告している。

### References
- https://gigazine.net/news/20260714-ai-left-work/
- https://www.normaltech.ai/p/what-will-be-left-for-us-to-work

## OpenAI's first hardware device is reportedly a screenless speaker that can move
- Date: 2026-07-14T15:22:00-07:00

### Executive Summary
- TechCrunchは、OpenAI初のハードウェア製品が画面なしのモバイル型スマートスピーカーになる可能性を報じている。
- Bloomberg報道によれば、製品は開発中で、ChatGPTと同期し家庭向けAIサービスを提供する構想である。
- 社内では家庭内に存在する人間らしいAIコンパニオンとして位置付けられている。
- 従来のスマートスピーカーとは異なり、所有者を時間とともに学習し、個別化したサービスを提供することが想定されている。
- デバイスはユーザーのメールなどデジタル生活へアクセスする可能性があるとされる。
- 自律的に動く機械要素を含み、ChatGPTの物理的な表現として設計されている点が特徴とされる。
- 一方で、OpenAIはAppleから営業秘密侵害で訴えられており、ハードウェア展開には法的リスクも伴う。
- 消費者向けAIハードウェアへの投資が広がる中、製品形状が未確定でも大規模資金が集まる市場環境が示されている。

### Key Findings
- OpenAIの初ハードウェアは、AI機能を統合したモバイル型スマートスピーカーと報じられている。 [^]
  - Footnote: 記事は「mobile smart speaker with integrated AI capabilities that can sync with ChatGPT」と説明している。
- 製品はまだ開発中で、画面なしの家庭内AIコンパニオンとして売り込まれている。 [^]
  - Footnote: Bloomberg報道として、デバイスは「still currently under development」で「screen-free」とされている。
- 所有者を学習し、より個別化されたサービスを提供する構想がある。 [^]
  - Footnote: 記事は、デバイスが「proactively learn about its owner over time, providing more personalized service」と記している。
- ユーザーのデジタル生活にアクセスする可能性が、利便性とプライバシーの両面で重要な論点になる。 [^]
  - Footnote: 記事は、機械が「access to a user's digital life」を持ち、emails などを参照し得ると述べている。
- デバイスは動く機械要素を持ち、ChatGPTの物理的な表現を狙うものとされる。 [^]
  - Footnote: 記事は「mechanical elements that can move on their own」および「physical manifestation of OpenAI's ChatGPT」と説明している。
- OpenAIのハードウェア展開は、Appleとの営業秘密訴訟というリスクの中で進んでいる。 [^]
  - Footnote: 記事は、AppleがOpenAIを訴え、営業秘密を盗んだと非難した一方で、OpenAIは不正行為を否定していると記している。

### References
- https://techcrunch.com/2026/07/14/openais-first-hardware-device-is-reportedly-a-screenless-speaker-that-can-move/
