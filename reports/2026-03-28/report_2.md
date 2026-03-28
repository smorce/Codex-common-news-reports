# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-03-28T09:03:22+09:00
- Articles: 3

## Solving Semantle With the Wrong Embeddings
- Date: 2026-03-16

### Executive Summary
- Semantleのスコアの相対順位だけを使う解法を提案している。
- モデルの埋め込みやコサイン類似度の数値は不要とする。
- 順位比較は埋め込み空間の半空間制約として扱える。
- 制約を積み重ねて候補を絞るアルゴリズムを説明した。
- 同一モデル前提なら10〜15回程度で解けると述べる。
- 異なる埋め込み同士ではハード制約が破綻するため確率的更新へ切替。
- 確率版は100〜200回で到達し、人間の推論に近いと結論づける。

### Key Findings
- 順位比較は半空間制約となり、候補領域を大きく削れる。 [^]
  - Footnote: Each ordered comparison of two guesses immediately lets us eliminate roughly half of the embedding sphere.
- 数値の類似度を使わなくても10〜15回程度で解けると報告。 [^]
  - Footnote: this solver finds the answer in about 10-15 guesses.
- 別モデルではハード制約がターゲットを除外し得る。 [^]
  - Footnote: hard-constraint approach above doesn’t work here... the solver will eliminate the target.
- ターゲットを除外しない確率的更新方式へ移行した。 [^]
  - Footnote: switched from a hard binary constraint to a probabilistic approach where no words are ever eliminated.
- 確率版は100〜200回で到達するとしている。 [^]
  - Footnote: takes between 100-200 guesses to find the target this way.

### References
- https://victoriaritvo.com/blog/robust-semantle-solver/

## Google TurboQuant入門 — KVキャッシュ3ビット圧縮でLLM推論を8倍高速化
- Date: 2026-03-26

### Executive Summary
- KVキャッシュのメモリが推論コストのボトルネックと説明する。
- TurboQuantは3ビット圧縮で精度損失ゼロを掲げる。
- PolarQuantとQJLの2段階アルゴリズムを解説している。
- 再学習不要で既存モデルに適用できる点を強調。
- H100でメモリ6倍削減・最大8倍高速化と紹介。
- LongBench等の長文ベンチで劣化なしと記載。
- MITライセンスのコミュニティ実装が公開済み。

### Key Findings
- 3ビット圧縮で精度損失ゼロ、メモリ6倍削減・最大8倍高速化と説明。 [^]
  - Footnote: 3ビットに圧縮しながら精度損失ゼロを実現し、メモリ使用量を6倍削減、NVIDIA H100上で注意機構の計算を最大8倍高速化
- TurboQuantはPolarQuantとQJLの2段階で構成される。 [^]
  - Footnote: TurboQuantはPolarQuant（極座標変換+Lloyd-Max量子化）とQJL（1ビット誤差補正）の2段階でKVキャッシュを3ビットに圧縮
- 再学習やファインチューニングは不要と明記。 [^]
  - Footnote: モデルの再学習やファインチューニングが一切不要
- 長文ベンチ全体で精度劣化が観測されなかったとする。 [^]
  - Footnote: これらのベンチマーク全体で精度劣化が観測されなかった
- コミュニティのPyTorch実装がMITライセンスで公開済み。 [^]
  - Footnote: コミュニティによるPyTorch実装がMITライセンスで公開

### References
- https://qiita.com/kai_kou/items/a411215806322af68a73

## 200種以上のAIから最大50種を選んで同じ質問に回答＆6種のAI同士で議論させて結論を導きだせる「AI Roundtable」 - GIGAZINE
- Date: 2026-03-27T19:00:00+09:00

### Executive Summary
- Opper AIのAI Roundtableは多数のモデル比較と議論を提供する。
- 200種類以上から最大50モデルで同一質問を投票形式で評価可能。
- 討論モードは最大6モデルで議論し結論を収束させる。
- 各モデルの回答要約や強い意見の抜粋が表示される。
- 洗車テスト例では投票で意見が割れ、討論後に車派へ収束。
- 結果はPNGで共有でき、投票理由やモデル決定も確認できる。
- セッションは既定で非公開で、一般ユーザーは無料利用可能と説明。

### Key Findings
- AI Roundtableは200種類以上のAIから最大50種を選んで投票でき、討論ラウンドも可能。 [^]
  - Footnote: 200種類以上のAIモデルから最大50種類を選んで同じ質問をし...討論ラウンドを実施することもできます。
- 投票モードではAIモデルが213種類あり最大50モデルまで追加可能。 [^]
  - Footnote: AIモデルは213種類あり、投票モードでは最大50モデルまで追加できます。
- Debateモードは選択できるAIモデルが6つまで。 [^]
  - Footnote: Debateモードの場合、選択できるAIモデルは6つまでです。
- 洗車テスト例で10モデル中5モデルが「歩いていく」と誤答。 [^]
  - Footnote: 今回選択した10種のAIモデルのうち5種は...「歩いていく」と間違った回答をしています。
- 討論後は全てのモデルが「車で行く」と結論付けた。 [^]
  - Footnote: 討論が行われ...最終的に全てのモデルが「車で行く」と結論付けています。

### References
- https://gigazine.net/news/20260327-ai-roundtable/
