# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-22T09:01:50.2845990+09:00
- Articles: 3

## Tencentの翻訳モデル「HY-MT2」

### Executive Summary
- Tencentが多言語翻訳モデルファミリーHy-MT2をオープンソース公開したことを紹介している。
- モデルは1.8B、7B、30B-A3Bの3サイズで、33言語間の翻訳に対応する。
- 1.8BモデルはAngelSlim 1.25ビット量子化により、ストレージ要件を440MBまで削減している。
- 7Bと30B-A3Bは高速思考モードで一部オープンソースモデルを上回る性能と説明されている。
- 翻訳指示追従評価用のIFMTBenchと、Hy-MT2-Translatorスキルも公開対象に含まれる。
- 推論フレームワークはTransformers、vLLM、SGLang、llama.cppへの対応が示されている。
- 筆者はライセンス制約が厳しく、オープンソースと呼ぶには微妙ではないかと懸念している。
- 過去バージョンへの不満と比較し、30B-A3B追加による実用性を見極めたいという見方で締めている。

### Key Findings
- Hy-MT2は翻訳向けの多言語モデルファミリーとして公開された。 [^]
  - Footnote: 本文に「Hy-MT2は『高速思考』型の多言語翻訳モデルファミリー」とある。
- 提供サイズは1.8B、7B、30B-A3Bの3種類である。 [^]
  - Footnote: 記事では「1.8B、7B、30B-A3B（MoE）の3つのモデルサイズ」と説明している。
- 対応言語は33言語とされ、翻訳指示にも対応する。 [^]
  - Footnote: 本文に「33言語間の翻訳をサポートし、複数言語での翻訳指示を効果的に実行」と記載されている。
- 1.8Bモデルは低ビット量子化でモバイル用途も意識されている。 [^]
  - Footnote: 記事には「1.8Bモデルのストレージ要件をわずか440MBまで削減」とある。
- IFMTBenchも同時にオープンソース公開される。 [^]
  - Footnote: 本文で「翻訳における指示追従能力を評価するベンチマークツールIFMTBenchもオープンソースとして公開」と述べている。
- 2026年5月21日に主要モデルとIFMTBenchが公開された。 [^]
  - Footnote: 最新情報欄に「2026年5月21日 HuggingFaceおよびModelScopeにて...オープンソース公開」とある。
- 利用可能なモデル配布形式にはFP8、GGUF、低ビットGGUFなどが含まれる。 [^]
  - Footnote: モデル配布リンクには「Hy-MT2-1.8B-FP8」「Hy-MT2-1.8B-GGUF」「Hy-MT2-1.8B-1.25bit-GGUF」などが並ぶ。
- 筆者はライセンス制約を実運用上の懸念として見ている。 [^]
  - Footnote: 本文に「EUでは使用不可・商用利用は一定のMAU以下に限定・他モデルの学習には使用禁止」とある。

### References
- https://zenn.dev/kun432/scraps/527e198418845c
- https://github.com/Tencent-Hunyuan/Hy-MT2

## OpenAI Python SDK を aiohttp で使う

### Executive Summary
- OpenAI Python SDKのHTTPバックエンド差し替えによる速度差を、MacとRaspberry Pi 4Bで簡易比較している。
- 標準のAsyncOpenAIではhttpxが使われ、RPiでは起動とTTFTが大きく遅くなることが確認された。
- httpxのkeep-aliveを無効化した構成では、チャンク間隔の改善は見えるが決定的な高速化ではない。
- aiohttpバックエンドは`openai[aiohttp]`を入れ、DefaultAioHttpClientを指定して利用できる。
- aiohttpでもRPiのTTFTは一定程度改善したが、Python SDK全体の起動負荷は残っている。
- SDKを使わずhttpxやaiohttp単体でも試し、結果のばらつきと測定条件の限界を確認している。
- OpenAI Go SDKではRPi 4Bの起動がほぼゼロに近く、TTFTも大幅に短くなった。
- 筆者は低リソース環境では、Python側の調整よりGo利用の方が速いという結論を示している。

### Key Findings
- Raspberry PiではPython SDK利用時の起動オーバーヘッドが大きい。 [^]
  - Footnote: 標準構成の結果で「Raspberry PI 4B startup: 3179.7 ms」と示されている。
- 標準httpx構成ではRPiのTTFTがMacより大きく悪化した。 [^]
  - Footnote: 標準構成ではMacのTTFTが793.6 ms、Raspberry Pi 4Bが8209.6 msと記録されている。
- httpxのkeep-alive無効化はチャンク間隔には影響したが、劇的な改善ではなかった。 [^]
  - Footnote: 筆者は結果後に「そんなに変わらないかな」とコメントしている。
- OpenAI Python SDKはaiohttpバックエンドを指定できる。 [^]
  - Footnote: 記事に「HTTPバックエンドとしてaiohttpを使用することも可能」とあり、`uv add "openai[aiohttp]"` が示されている。
- aiohttp構成ではRPiのTTFTが標準構成より短くなった例がある。 [^]
  - Footnote: aiohttpの結果では「Raspberry Pi 4B time to first chunk: 7449.6 ms」と掲載されている。
- SDKなしの比較でも、httpxとaiohttpの差は測定条件によるばらつきがある。 [^]
  - Footnote: 単体比較ではhttpx no keep-aliveとaiohttpの複数結果が並び、MacとRPiで異なる傾向が出ている。
- Go SDKは低リソース環境で明確に有利な結果を示した。 [^]
  - Footnote: OpenAI Go SDKのRPi 4B結果は「startup: 0.2 ms」「time to first chunk: 1045.8 ms」とある。
- 筆者は厳密なベンチマークではなく大まかな傾向確認だと断っている。 [^]
  - Footnote: 記事冒頭に「ちゃんと調べてない雑な比較なので参考にしないように」とある。

### References
- https://zenn.dev/kun432/scraps/220122eee7ce36

## 「llama-benchy」を試す

### Executive Summary
- OpenAI互換LLMエンドポイント向けベンチマークツール`llama-benchy`のREADME内容を紹介している。
- llama.cpp専用のllama-benchに似た統計を、vLLMやSGLangなど別エンジンでも測れることが狙いである。
- プロンプト処理速度、トークン生成速度、TTFR、推定プロンプト処理時間、E2E TTFTなどを出力できる。
- HuggingFaceトークナイザーによる正確なトークンカウントやProject Gutenberg由来のテキスト利用にも対応する。
- uvx、uv run、仮想環境インストール、システムインストールなど複数の実行方法が示されている。
- コンテキスト深度、プロンプト長、生成長、同時実行数を組み合わせて測定できる。
- プレフィックスキャッシュ性能を測る2段階ベンチマークも用意されている。
- 結果はMarkdown、JSON、CSVで保存でき、時系列データも追加保存できる。

### Key Findings
- `llama-benchy`はOpenAI互換エンドポイントを対象にしたベンチマークツールである。 [^]
  - Footnote: 本文に「OpenAI互換のLLMエンドポイントをベンチマーク」と記載されている。
- llama-benchでは扱いにくい推論エンジンの測定を補う目的がある。 [^]
  - Footnote: 記事では「llama.cpp専用に設計されており、vllmやSGLangといった他の推論エンジンでは使用できません」と説明している。
- TTFTだけでなくTTFRや推定PPTも測る。 [^]
  - Footnote: 主な機能に「初回応答までの時間（データチャンク）（TTFR）、推定プロンプト処理時間（est_ppt）、およびエンドツーエンドのTTFTを報告」とある。
- 複数回実行して平均値と標準偏差を報告できる。 [^]
  - Footnote: 機能一覧に「複数の反復処理（--runs）を実行可能で、平均値±標準偏差を報告」とある。
- uvxを使えばインストール不要で実行できる。 [^]
  - Footnote: インストール方法に「インストール不要でuvxを使用して実行」としてコマンド例が掲載されている。
- プロンプト長、生成長、コンテキスト深度、同時実行数をパラメータ化できる。 [^]
  - Footnote: 引数一覧に`--pp`、`--tg`、`--depth`、`--concurrency`が示されている。
- プレフィックスキャッシュの影響を測定する専用オプションがある。 [^]
  - Footnote: 本文に「--enable-prefix-cachingオプションを使用し...2段階のプロセスを実行」とある。
- 結果保存形式はMarkdown、JSON、CSVに対応する。 [^]
  - Footnote: 機能一覧と引数一覧に「結果をMarkdown、JSON、またはCSV形式でファイルに保存可能」とある。

### References
- https://zenn.dev/kun432/scraps/91f1e0413c0a66
- https://github.com/eugr/llama-benchy
