# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-03-25T09:12:05+09:00
- Articles: 3

## Claude Code / CursorのHooksで実装した AIエージェントの3層プロンプトインジェクション対策
- Date: 2026-03-24

### Executive Summary
- Cursor 2.4のSkills追加を機に、Hooksでプロンプトインジェクション対策を設計した。
- LLMへの注意喚起ではなく、実行境界で止める方針でPythonフックスクリプトを実装した。
- プロンプトインジェクションが秘密情報漏洩や不正操作につながると整理している。
- フックは入力時・実行前・実行後の3層で介入する設計だ。
- 第1層は既知パターン検知の水際対策で、未知手口は通ると明記した。
- 第2層は危険コマンドや機密ファイルアクセスをブロックする主軸として位置づけた。
- 第3層は外部データ受領後にスキャンし、次の実行で確実に止める方式を採る。

### Key Findings
- LLMへの注意喚起ではなく実行境界で止める設計を採用した。 [^]
  - Footnote: LLM に「気をつけて」と指示するのではなく、LLM の外側にある実行境界で止める。
- プロンプトインジェクションは参照データ内の悪意指示で誤作動させる攻撃と説明している。 [^]
  - Footnote: プロンプトインジェクションは、AI が参照するデータの中に悪意ある指示を隠し込む攻撃手口です。
- 重大リスクとして秘密情報漏洩、AIの乗っ取り、破壊的操作を列挙した。 [^]
  - Footnote: 秘密情報の漏洩（API キーや認証情報が外部に送り出されるリスク）
- 第1層は入口での水際対策に限定し、補助的な役割と位置づけた。 [^]
  - Footnote: この層はあくまで「入口での水際対策」として位置づけています。
- 第2層はツール実行直前に毎回介入する主軸である。 [^]
  - Footnote: AI がコマンドやツールを実行しようとする直前に毎回割り込みます。ここが対策の主軸です。
- 第3層は危険フラグを立て、次のPreToolUseで確実に止める方針を採る。 [^]
  - Footnote: 危険フラグを立てて次の PreToolUse で確実に止める方針にしました。

### References
- https://creators.bengo4.com/entry/2026/03/24/080000

## Disney Exits OpenAI Deal After AI Giant Shutters Sora
- Date: 2026-03-24

### Executive Summary
- OpenAIがSoraの動画アプリを終了すると報じられている。
- OpenAIはSoraで制作した人々に感謝し、アプリとAPIのタイムラインや保存方法を案内すると述べた。
- 関係者によればDisneyはOpenAIとの投資・ライセンス契約から撤退する。
- Soraは昨秋にローンチし、IPや俳優の利用をめぐって数日後に方針修正したと説明されている。
- OpenAIはAI動画事業自体からは撤退しないが、単独アプリは犠牲になると記されている。
- DisneyはOpenAIの決定を尊重し、他のAIプラットフォームとも協力を続ける姿勢だ。
- 記事はSora終了でAI動画の勢力図が変わる可能性に触れている。

### Key Findings
- SoraのAI動画アプリを終了する方針が示された。 [^]
  - Footnote: OpenAI will shut down its Sora AI video app, just months after it was first launched.
- OpenAIはSora利用者に感謝し、アプリ/APIのタイムラインや作品保存の詳細を後日共有すると述べた。 [^]
  - Footnote: We’ll share more soon, including timelines for the app and API and details on preserving your work.
- Disneyは昨年のOpenAIとの契約から撤退し、10億ドル投資とキャラクターライセンスの枠組みを解消する。 [^]
  - Footnote: Disney is also exiting the deal it signed with OpenAI last year, in which it pledged to invest $1 billion in the company and agreed to license some of its characters for use in Sora.
- Soraは昨秋にローンチし、数日後にIP/肖像の扱いをめぐって方針修正を迫られた。 [^]
  - Footnote: Sora launched last fall ... The company had to backtrack a few days after it launched, giving Hollywood studios and talent more control over their IP and likenesses on the platform.
- OpenAIはAI動画事業自体から撤退せず、単独のSoraアプリが犠牲になると記されている。 [^]
  - Footnote: OpenAI, led by CEO Sam Altman, is not getting out of the AI video business ... but it appears the standalone Sora app will be a casualty of its evolving ambitions.
- DisneyはOpenAIの判断を尊重し、責任ある形で新技術を取り込む姿勢を示した。 [^]
  - Footnote: We respect OpenAI’s decision to exit the video generation business and to shift its priorities elsewhere ... we will continue to engage with AI platforms to find new ways to meet fans where they are while responsibly embracing new technologies that respect IP and the rights of creators.

### References
- https://www.hollywoodreporter.com/business/digital/openai-shutting-down-sora-ai-video-app-1236546187/

## Thoughts on LLMs - Psychological complications

### Executive Summary
- LLMは機械でも心でもなく、既存の語彙では説明しづらい存在だと述べる。
- 私たちは「思考」「幻覚」といった言葉で無意識に心を見てしまうと指摘する。
- 著者はLLMには正誤の概念がなく、思考や感情はないと断じる。
- 議論のための語彙として「entity」「artifact」などフィクション寄りの言葉を推奨する。
- AIという言葉の意味のずれが混乱を生み、LLMは推論心のシミュレーションに過ぎないと述べる。
- パレイドリアやチューリングテストの誤解が心の投影を助長すると論じる。
- チャットUIや“talking dog syndrome”が評価基準を甘くする心理効果を示す。

### Key Findings
- LLMは機械でも心でもない第三の存在で、語彙が不足していると述べる。 [^]
  - Footnote: LLMs are conceptually unlike anything we’re used to dealing with in either a technical or social context; they are neither machines nor minds, but some third thing
- 「思考」や「幻覚」といった語彙が心の存在を誤認させると指摘する。 [^]
  - Footnote: We speak of these artifacts “thinking” while they process. We blame “hallucination” when errors occur
- LLMには正誤の概念がなく、思考もしないと明言している。 [^]
  - Footnote: They’re not thinking. They’re not hallucinating ... They have no concept of true or false.
- LLMは論理的な機械ではなく、確率的で予測不能な存在だと説明する。 [^]
  - Footnote: They’re not machines, they’re not minds, they’re not programs. They’re a trillion numbers in a trenchcoat; not logical
- 議論にはフィクションの語彙を用い、「entity」「artifact」などを使うべきと提案する。 [^]
  - Footnote: we’re better served by the language of fiction ... we can use words like “entities” and “artifacts”
- パレイドリアが心の投影を強め、客観評価を妨げると論じる。 [^]
  - Footnote: Pareidolia is the strong, innate human tendency to see patterns, particularly faces, where none really exist.

### References
- https://parsingphase.dev/tech/LLMs/psychologicalFactors.html
