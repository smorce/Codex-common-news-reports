# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-02T00:00:00+09:00
- Articles: 3

## テキストから地名を抽出して位置情報を付与する「GeoNLP」を試す

### Executive Summary
- GeoNLP は、自然言語テキストから地名を抽出し、緯度経度などの地理情報に結び付けるためのオープンな地名情報処理プロジェクトである。
- 記事では公式ドキュメントを確認したうえで、PyGeoNLP の CLI と Python API を Colaboratory 環境で試している。
- インストールには MeCab や Boost などの OS パッケージと、PyPI の pygeonlp パッケージを利用している。
- 初回実行時には基本辞書セットのインストールが必要で、都道府県、市区町村、鉄道駅などの辞書が導入される。
- CLI の geoparse では、目黒駅、品川区、港区、京都市、伏見区などに緯度経度が付与される例が示されている。
- 一方で、京都競馬場のように基本辞書にない語は緯度経度が付かず、辞書カバレッジが結果を左右することが確認されている。
- Python API の出力は GeoJSON の Feature 形式で、node_type が GEOWORD の要素を抽出すると地名語だけを扱える。
- 高度な利用として、NEologd、Jageocoder、解析チューニング、カスタム辞書作成が候補に挙げられている。

### Key Findings
- GeoNLP は GIS と NLP を組み合わせ、地名を軸にテキストを空間文脈へ接続するプロジェクトである。 [^]
  - Footnote: 記事本文で「地理情報処理(GIS) と自然言語処理(NLP)を組み合わせ」「地名情報処理システムの構築を目指します」と説明されている。
- PyGeoNLP は CLI と Python API の両方で利用できる。 [^]
  - Footnote: CLI の `pygeonlp --help` には geoparse、search、list-dictionaries などのサブコマンドが示され、別途 `pygeonlp.api.geoparse` のコード例も掲載されている。
- Colaboratory では Ubuntu 環境として、MeCab、Boost、pygeonlp を導入して試している。 [^]
  - Footnote: 記事では `apt install build-essential libmecab-dev mecab-ipadic-utf8 libboost-all-dev` と `pip install pygeonlp` が実行されている。
- 基本辞書セットには都道府県、市区町村、鉄道駅の辞書が含まれる。 [^]
  - Footnote: 初回の辞書インストール説明で「日本の都道府県」「歴史的行政区域データセットβ版地名辞書」「日本の鉄道駅（2019年）」が列挙されている。
- 抽出された地名語には緯度経度が付与され、形態素解析結果と同時に確認できる。 [^]
  - Footnote: 目黒駅の出力に `139.71566,35.632485`、品川区の出力に `139.73025000,35.60906600` が含まれている。
- 辞書に登録されていない固有名は、地名語として位置情報が付与されない場合がある。 [^]
  - Footnote: 記事では「京都競馬場」について「緯度経度情報がない、つまり基本辞書セットに含まれる辞書には登録されていない」と述べている。
- Python API の結果は GeoJSON Feature 形式で、GIS アプリケーションでのプロットに向く。 [^]
  - Footnote: 記事では `type: Feature`、`geometry: Point`、`coordinates` を含む JSON を示し、「GeoJSON の Feature 形式」と説明している。
- 今後の発展先として、住所ジオコーダー連携やカスタム辞書の作成が実用上重要になりそうだと整理されている。 [^]
  - Footnote: 高度な使い方として「住所ジオコーダーJageocoder」「独自のカスタム辞書を作る」が挙げられ、筆者は「カスタム辞書を作ってみたい」と述べている。

### References
- https://zenn.dev/kun432/scraps/d79bdd752e0db2

## 「ModernBERT-ja」を試す ④ ベクトル

### Executive Summary
- この記事では ModernBERT-ja を使ったテキストベクトル化と、Embedding 用のファインチューニングを検証している。
- まず transformers の AutoModel と AutoTokenizer を使い、平均プーリングで 512 次元の文ベクトルを作成している。
- 未調整モデルでは「中華そばが食べたい」というクエリに対して、ラーメン以外の料理文も高スコアになり、精度は十分ではないと判断している。
- 長文入力の例として青空文庫の「走れメロス」を扱い、5638 トークンの入力がモデルの長文対応範囲に収まることを確認している。
- ファインチューニングには Livedoor ニュースコーパスを使い、タイトルをクエリ、本文を正例ドキュメントとする対照学習データを作っている。
- sentence-transformers と MultipleNegativesRankingLoss を使い、バッチ内の他データを自動的に負例として扱う構成で学習している。
- 1 エポックの学習後、recall@5 は未調整モデルの 0.12 からチューニング済みモデルの 0.95 に大きく改善している。
- 筆者は分類、NER、Embedding のユースケースを一通り試し、日本語 MIT ライセンスモデルとして ModernBERT-ja の有用性を評価している。

### Key Findings
- ModernBERT-ja の出力を平均プーリングすることで 512 次元の文ベクトルを得ている。 [^]
  - Footnote: 記事のコードでは `last_hidden_state` に attention mask を掛けて平均し、出力として `torch.Size([1, 512])` が示されている。
- 素のモデルによる類似検索では、意味的に近い文が必ずしも上位に安定しない。 [^]
  - Footnote: 「中華そばが食べたいなぁ」の検索結果で、豚骨ラーメンが 0.882 で首位だが、チーズ、ピッツァ、カレーも 0.870 台で並んでいる。
- ModernBERT-ja は長文入力に対応し、走れメロスの 5638 トークンも処理対象にできる。 [^]
  - Footnote: 記事では青空文庫テキストのトークン数を `5638` と表示し、その後にベクトル化結果を出している。
- Livedoor ニュースコーパスはタイトルと本文のペアを作りやすく、Embedding 学習の正例ペアに利用されている。 [^]
  - Footnote: 記事では各ファイルが「1行目: URL、2行目: 記事公開日時、3行目: 記事タイトル、4行目以降: 記事本文」と説明されている。
- 学習時は最大 8192 トークン全体ではなく、VRAM 制約から 1024 トークンに切り詰めている。 [^]
  - Footnote: 筆者は「最大8192トークンの入力に対応」するが「VRAMが足りなくなるので、今回は1024トークンで後ろを切り捨てる」と記載している。
- MultipleNegativesRankingLoss により、明示的な負例データを用意せずに対照学習を行っている。 [^]
  - Footnote: 記事では「バッチ内の他のデータを自動的に不正解として扱ってくれる」と説明している。
- 学習は 1 エポック、455 step、約 699 秒で完了している。 [^]
  - Footnote: 学習結果として `global_step=455`、`train_runtime: 699.3025`、`epoch: 1.0` が示されている。
- ファインチューニング後の検索性能は recall@5 で大幅に改善した。 [^]
  - Footnote: 記事の評価出力では「オリジナルモデルの recall@5: 0.12」「チューニングモデルの recall@5: 0.95」とされている。

### References
- https://zenn.dev/kun432/scraps/814a7c95899cdf

## 「ModernBERT-ja」を試す ③ 固有表現抽出（NER）

### Executive Summary
- この記事では ModernBERT-ja を使い、日本語の固有表現抽出（NER）をファインチューニングで試している。
- 冒頭では NER を、人名、地名、組織名などの語句とラベルを文中から抽出するタスクとして説明している。
- ModernBERT-ja のユニグラム言語モデル系トークナイザーでは、語境界とトークン境界が一致しない問題があることを確認している。
- メイショウタバルが複数トークンに分割され、日本のが 1 トークンになる例から、BIO ラベルによる境界表現の必要性を整理している。
- データセットには stockmark/ner-wikipedia-dataset を使い、5343 件の学習データと 8 種類の固有表現タイプを扱っている。
- 文字単位のラベルを作成し、tokenizer の offset_mapping を使ってトークン単位のラベルに変換する実装を示している。
- AutoModelForTokenClassification と Trainer で 3 エポック学習し、約 105 秒で完了している。
- 推論では pipeline により人名、地名、イベント名などを抽出できる一方、「日本の」のような境界問題は残るため、事前分かち書きも検討している。

### Key Findings
- NER は文中の固有表現とその種類を抽出するタスクとして整理されている。 [^]
  - Footnote: 記事では「人名」「地名」「組織名」などを抽出し、例文から「武豊」「日本」「宝塚記念」などを取り出す説明がある。
- ModernBERT-ja のトークナイザーは語境界と一致しないことがあり、NER では追加対応が必要になる。 [^]
  - Footnote: 記事では「メイショウタバル」が4トークンに分割され、「日本の」が1トークンになる例を示している。
- BIO ラベルは、複数トークンにまたがる固有表現を表現するために使われている。 [^]
  - Footnote: 記事では B-X を固有表現の先頭、I-X を続き、O を固有表現以外として説明している。
- stockmark/ner-wikipedia-dataset は 5343 件の train データを持ち、span と type で固有表現を表す。 [^]
  - Footnote: 出力例に `num_rows: 5343` があり、サンプルでは `entities` に `name`、`span`、`type` が含まれている。
- 対象ラベルは人名、法人名、政治的組織名、その他の組織名、地名、施設名、製品名、イベント名に分けられている。 [^]
  - Footnote: 記事中の表で、人名 2980、法人名 2485、地名 2157、イベント名 1009 などの固有表現数が示されている。
- 文字範囲と offset_mapping を使い、文字単位ラベルからトークン単位ラベルを作成している。 [^]
  - Footnote: 実装では `return_offsets_mapping=True` を指定し、各トークンの開始位置 `s` から `char_labels[s]` を採用している。
- NER の学習では可変長ラベルを扱うため、DataCollatorForTokenClassification を使っている。 [^]
  - Footnote: 記事では「labels もトークンごとのリストで文ごとに長さが変わるため、-100 で埋める専用のコレクタを使う」と説明している。
- 学習後の pipeline 推論では、製品名、地名、人名、イベント名を抽出できている。 [^]
  - Footnote: 推論例では `メイショウタバル` が製品名、`日本の` が地名、`武豊` が人名、`宝塚記念` がイベント名として出力されている。
- 事前に分かち書きして `is_split_into_words=True` を使うと、推論時の境界制御を改善できる可能性がある。 [^]
  - Footnote: 記事では分割済みトークン列を tokenizer に渡し、`日本` と `の` が別トークンになる例を示している。

### References
- https://zenn.dev/kun432/scraps/80657369f35ed7
