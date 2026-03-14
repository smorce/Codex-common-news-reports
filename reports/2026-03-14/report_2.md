# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-03-14T09:02:17.9967017+09:00
- Articles: 3

## JEPA-v0: a self-supervised audio encoder for real-time speech translation
- Date: 2026-02-23

### Executive Summary
- 従来のASR→MT→TTSのカスケードは感情や声色を捨てるという課題を指摘している。
- 音声翻訳に必要なのは、意味とパラ言語情報を同時に保持する表現だと説明する。
- JEPA-v0は自己教師ありで音声表現を学習し、ラベル依存を回避する設計だ。
- マスク再構成や対照学習の欠点を避け、表現そのものを予測するのが中核。
- JEPAは音響構造や感情の手掛かりを捉える一方、音素や意味の整合は弱い。
- 時間解像度や周波数構造の保持が今後の改良点として挙げられている。
- 最終的な評価軸は翻訳音声が元話者の特徴を保てるかに置かれている。

### Key Findings
- 従来のカスケード翻訳は音声の感情や韻律を失うため、音声表現を直接扱う必要がある。 [^]
  - Footnote: The cascade pipeline of ASR → MT → TTS treats audio as a container for text... Everything that made the original speech human, like pitch and rhythm, gets discarded at step one.
- JEPA-v0は自己教師ありで大量の未ラベル音声から表現を学習する方針を採る。 [^]
  - Footnote: For JEPA-v0, this means we can train on millions of audio samples... all without needing a single label.
- JEPAは「隠れた部分そのもの」ではなく「表現」を予測する設計で、意味重視の学習を促す。 [^]
  - Footnote: JEPA ... predict the representation of the hidden parts, not the hidden parts themselves.
- CREMA-Dで情動認識スコア0.456を得ており、感情関連の音響特徴を捉えている。 [^]
  - Footnote: JEPA-v0 gets a 0.456 score on CREMA-D emotion recognition.
- GTZANでは音楽キャプションで0.481の競争的スコアを得たと報告している。 [^]
  - Footnote: helps JEPA-v0 to get a competitive score of 0.481 for music captioning.
- 10秒クリップで32フレーム出力という時間解像度が主要ボトルネックと述べている。 [^]
  - Footnote: The most direct bottleneck is the 32-frame output for a 10-second clip.
- 周波数方向の平均化で母音・子音やピッチ情報が失われるため、2D出力等が必要とされる。 [^]
  - Footnote: We also need to preserve frequency structure... average over the frequency axis... collapses information that distinguishes vowels from consonants (formant structure), pitch (fundamental frequency), and timbral details.

### References
- https://www.startpinch.com/research/en/jepa-encoder-translation/

## Claude CodeやCodexのスキルの管理を楽にするツール「faceted-prompting」
- Date: 2026-03-12

### Executive Summary
- 長大化したプロンプトは保守性が下がるという課題を起点に議論している。
- 役割・規約・知識・指示・出力形式が混ざることが混乱の原因だと説明する。
- Faceted Promptingで関心ごとに分割し、部品として扱う考え方を紹介する。
- faceted-promptingはその考え方を運用するためのnpmツールとして位置づけられる。
- Markdownの部品をcompositionで組み合わせ、system/userプロンプトを生成できる。
- Claude CodeやCodexのスキルとしても使える点を強調している。
- facet initやサンプル取得から始め、部品運用へ移行する手順を提示している。

### Key Findings
- 長いプロンプトが増えると保守性が下がるという問題意識が出発点になっている。 [^]
  - Footnote: プロンプトが長く、そして増えてくると、どんどんと保守性が下がってきます。
- 混在する要素として役割・ルール・知識・作業指示・出力形式を挙げている。 [^]
  - Footnote: 役割、ルール、知識、作業指示、出力形式。
- Faceted Promptingは混ざったプロンプトを関心ごとに分けて扱う考え方だと定義している。 [^]
  - Footnote: Faceted Prompting は、そうした混ざったプロンプトを関心ごとに分けて扱う考え方です。
- faceted-promptingは部品を管理し、組み合わせて使うための道具として説明されている。 [^]
  - Footnote: faceted-prompting は、その部品を実際に管理し、組み合わせて使うための道具です。
- persona/policy/knowledgeをMarkdownで置き、compositionで組み合わせる方式を示す。 [^]
  - Footnote: persona や policy や knowledge を Markdown ファイルとして置く。 それらを composition で組み合わせる。
- 組み合わせ結果をsystem promptとuser promptに分けて出力できるとしている。 [^]
  - Footnote: すると、その結果を system prompt と user prompt に分けて出力できます。
- 導入手順として facet init と facet pull-sample を提示している。 [^]
  - Footnote: まずは facet init して、 facet pull-sample してみてください。

### References
- https://zenn.dev/nrs/articles/88f158aca0505b

## Nyne, founded by a father-son duo, gives AI agents the human context they’re missing
- Date: 2026-03-13

### Executive Summary
- AIエージェントは人間の代わりに意思決定するが、文脈理解が不足していると指摘する。
- 創業者Michael Fanousは、複数サービスのデータが同一人物に紐づくか判別が難しいと述べる。
- 父のEmad Fanousと共同でNyneを立ち上げ、デジタル足跡全体の理解層を目指す。
- Nyneは人間理解のためのインテリジェンスレイヤー構築を掲げている。
- 同社はシードで5.3百万ドルを調達し、主要投資家が明示されている。
- Googleの広告ターゲティングに見える優位は独占的データに依存し外部には提供されないとする。
- 既存の機械学習で解決済みという見方に対して反論している。

### Key Findings
- AIエージェントは購買やスケジュールなど自律的判断を行う時代が近いと説明している。 [^]
  - Footnote: AI agents are expected to soon start making autonomous purchasing and scheduling decisions on behalf of humans.
- 人間理解のための「完全な文脈」が欠けているという指摘が中心主張になっている。 [^]
  - Footnote: agents are currently missing a critical piece of the puzzle: the full context required to truly understand the people they are programmed to serve.
- 複数のオンラインプロフィールが同一人物かどうかの識別が難しいと述べている。 [^]
  - Footnote: machines currently struggle to discern whether a person’s professional profile on LinkedIn, their activity on Instagram, and their public government records all belong to the same human being.
- Michael FanousとEmad FanousがNyneを共同で立ち上げたと記されている。 [^]
  - Footnote: he teamed up with his father, Emad Fanous, a veteran CTO, to build Nyne
- Nyneはエージェントが人間を理解するためのインテリジェンスレイヤーを目指す。 [^]
  - Footnote: a startup aiming to become the intelligence layer that helps agents understand humans across their entire digital footprint.
- シード資金5.3百万ドルを調達し、Wischoff VenturesとSouth Park Commonsが主導した。 [^]
  - Footnote: raised $5.3 million in seed funding led by Wischoff Ventures and South Park Commons
- Googleの優位は検索履歴など独占的データに依存し、外部エージェントには共有されないと主張する。 [^]
  - Footnote: Google’s “secret sauce” is its exclusive access to users’ search histories and cross-platform activity... the tech giant will never share with external agents

### References
- https://techcrunch.com/2026/03/13/nyne-founded-by-a-father-son-duo-gives-ai-agents-the-human-context-theyre-missing/
