# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-08T09:01:28.1892532+09:00
- Articles: 3

## OmniRoute

### Executive Summary
- OmniRoute は、複数の AI プロバイダを 1 つの OpenAI 互換エンドポイントにまとめるローカルゲートウェイとして紹介されている。
- VS Code 拡張、Claude Code、Cursor、Copilot、Cline などを http://localhost:20128/v1 に向けるだけで利用できる構成が説明されている。
- 対応プロバイダは 237 社、無料枠ありは 90 以上、ほぼ永続無料とされるものは 11 とされている。
- コンボ機能により、有料サブスクリプション、低価格モデル、無料モデルを段階的に並べ、障害やクォータ切れ時に自動で切り替える。
- auto モデルはヘルス、クォータ、コスト、レイテンシ、成功率、モデル性能などを使って自動選択する仕組みとして説明されている。
- トークン圧縮は RTK、Caveman、Relevance、LLMLingua-2 など最大 10 エンジンで構成され、15 から 95% の削減を狙う。
- ローカル実行、AES-256-GCM による保存、テレメトリなし、MIT ライセンスが示され、セルフホスト志向の利用者に向くと整理されている。
- LiteLLM、OpenRouter、Portkey との比較では、プロバイダ数、MCP/A2A、圧縮、ガードレール、評価機能などの広さが強調されている。

### Key Findings
- OmniRoute は複数 AI を 1 つの OpenAI 互換 API に集約するゲートウェイとして位置づけられている。 [^]
  - Footnote: 本文では「あらゆるAIを1個の入り口からまとめて使えるゲートウェイ」「1つのOpenAI互換エンドポイント」と説明されている。
- クライアント側の設定はローカルの Base URL、API Key、Model 指定に集約される。 [^]
  - Footnote: 設定例として Base URL: http://localhost:20128/v1、API Key、Model: auto や kr/claude-sonnet-4.5 が挙げられている。
- コンボ機能はクォータ切れ、レートリミット、障害時の自動フェイルオーバーを担う。 [^]
  - Footnote: 本文では「上の段で『クォータ切れ』『レートリミット』『障害』が起きたら数ミリ秒で次の段に切り替わる」と説明されている。
- ルーティング戦略は priority、cost-optimized、headroom、lkgp、fusion など多様に用意されている。 [^]
  - Footnote: 本文では 17 種類のルーティング戦略として priority、cost-optimized、headroom、lkgp、fusion が例示されている。
- auto モデルは運用状態と性能の複数要素をスコアリングしてモデルを選ぶ。 [^]
  - Footnote: ヘルス、クォータ残量、コスト、レイテンシ、成功率、models.dev の情報など約 9 要素で最適なモデルを自動選択するとされている。
- トークン圧縮は構造化データを壊さないことと、圧縮後に長くなる場合の回避が重視されている。 [^]
  - Footnote: コードブロック、URL、JSON を保存し、圧縮結果が長くなりそうなら元のまま送るインフレガードがあると記載されている。
- 無料枠の統合管理はプロバイダ単位、プール単位、商用利用可否などの可視化を含む。 [^]
  - Footnote: ダッシュボードでプロバイダごとの今月使用量、残りトークン、プールごとの締め日、利用規約フラグを見える化すると説明されている。
- MCP と A2A により、エージェントが OmniRoute 自身の設定やプロバイダ管理を操作できる。 [^]
  - Footnote: MCP サーバと A2A を実装し、設定変更、プロバイダ追加削除、コンボ編集、キャッシュ・メモリ・圧縮制御まで可能とされている。

### References
- https://zenn.dev/kun432/scraps/ebf30f75f903c8

## 「Tau」を試す ④ Tau をライブラリとして使う

### Executive Summary
- この記事は、Tau を CLI としてではなく Python ライブラリとして使う方法を試した記録である。
- README に示される AgentHarness と AgentHarnessConfig が tau_agent の入口として紹介されている。
- AgentHarness の内部でエージェントループが動作し、prompt からイベントが非同期に返る構造だと読み取られている。
- 実行例では Colaboratory 上で tau-ai をインストールし、OpenAI 互換プロバイダを使ってハーネスを構築している。
- ツール呼び出しの例として get_weather が定義され、都市名に応じた固定の天気を返すダミーツールが用意されている。
- notebook 環境では nest_asyncio.apply() が必須として追加されている。
- 実行結果では agent_start、turn_start、message_start、tool_execution_start、tool_execution_end などのイベントが順に出力されている。
- 最終的に東京と札幌の天気を尋ねるプロンプトに対して、ツール実行結果を踏まえた日本語回答が生成されている。

### Key Findings
- Tau は CLI だけでなくライブラリとしても利用できる。 [^]
  - Footnote: 本文冒頭で「TauをCLIでそのまま使うことが前提だったが、GitHubのREADMEを見ると、ライブラリとしても使える様子」と述べられている。
- AgentHarness が tau_agent の主要なエントリポイントとして扱われている。 [^]
  - Footnote: README の例として from tau_agent import AgentHarness, AgentHarnessConfig が示され、「AgentHarness ってのが tau_agent の入口」と説明されている。
- AgentHarness は非同期イベントストリームを返す。 [^]
  - Footnote: サンプルでは async for event in harness.prompt("Explain this package") と書かれ、実行後に「イベントが返ってきている」と確認されている。
- Colaboratory での実行には tau-ai、nest_asyncio、OpenAI 互換プロバイダ設定が使われている。 [^]
  - Footnote: コード例に !pip install tau-ai、import nest_asyncio、OpenAICompatibleProvider、DEFAULT_OPENAI_COMPATIBLE_BASE_URL が含まれている。
- ツールは AgentTool と executor で定義し、AgentToolResult を返す構成になっている。 [^]
  - Footnote: get_weather_executor が AgentToolResult を返し、tools 配列に AgentTool(name="get_weather", input_schema=..., executor=...) が定義されている。
- サンプルでは gpt-5.5 をモデルとして指定している。 [^]
  - Footnote: AgentHarnessConfig の model に "gpt-5.5" が指定されている。
- ツール呼び出しは複数都市に対して個別に発生している。 [^]
  - Footnote: 出力では get_weather が Tokyo と Sapporo の 2 回呼び出され、それぞれ tool_execution_start と tool_execution_end が出ている。
- 最終応答はツール結果を反映した自然文としてストリーミングされている。 [^]
  - Footnote: message_delta が文字単位で続き、最後に東京は晴れ 28°C、札幌は雨 18°C という AssistantMessage が出力されている。

### References
- https://zenn.dev/kun432/scraps/d8ca7bc1d62e8b

## 日本語形態素解析ライブラリ「Vibrato」を試す

### Executive Summary
- この記事は、日本語形態素解析ライブラリ Vibrato を Python ラッパー経由で試した記録である。
- 著者は Sudachi、MeCab、Janome、Lindera、Kuromoji などは知っていたが、Vibrato は未経験だったため検証している。
- Vibrato は Viterbi アルゴリズムを基盤とする高速なトークン化または形態素解析ツールとして紹介されている。
- GitHub README の説明では、Vibrato は MeCab を Rust で再実装し、簡素化と最適化で高速化したものとされている。
- Python ラッパーは pip install vibrato で導入でき、記事中の環境では vibrato-0.2.3 と Vibrato 本体 0.5.2 が確認されている。
- 辞書は GitHub Releases から取得し、今回は v0.5.0 の mecab-ipadic v2.7.0 を使っている。
- 辞書は zstd 圧縮されており、Vibrato に渡す前に zstandard で展開する必要がある。
- 短文や Wikipedia 冒頭文を使った試行では、辞書によってトークン数や固有名詞の分割結果が変わることが示されている。

### Key Findings
- Vibrato は高速な日本語トークン化・形態素解析ツールとして紹介されている。 [^]
  - Footnote: 本文では「Viterbiアルゴリズムを基盤とした高速なトークン化（または形態素解析）ツール」と説明されている。
- MeCab と同じ辞書を参照する場合、Vibrato の結果は MeCab と大差ないとされている。 [^]
  - Footnote: 引用記事の要約として「Mecabの結果とvibratoの結果は参照する辞書が同じ場合大差がなかった」と記載されている。
- 速度が重要な処理では Vibrato の利用検討が妥当とされている。 [^]
  - Footnote: 本文では「速度を気にする処理を実装する場合はvibratoの利用を検討するべき」と引用されている。
- Vibrato は MeCab の Rust 再実装であり、大規模な行列データでキャッシュ効率の利点がある。 [^]
  - Footnote: README 抜粋では Rust で再実装し、459 MiB の行列データを持つ unidic-cwj-3.1.1 などで ID マッピング機構により高速に動作すると説明されている。
- Python からは pip install vibrato で利用できる。 [^]
  - Footnote: 記事中の実行例では !pip install vibrato の結果として Successfully installed vibrato-0.2.3 と表示されている。
- 辞書は zstd 圧縮形式で配布され、利用前に展開してから Vibrato に渡している。 [^]
  - Footnote: system.dic.zst を zstandard.ZstdDecompressor の stream_reader で読み込み、vibrato.Vibrato(dict_reader.read()) に渡している。
- mecab-ipadic を使った短文例では 5 トークンに分割されている。 [^]
  - Footnote: 「社長は火星猫だ」の出力でトークン数 5、社長・は・火星・猫・だ が表示されている。
- 辞書の種類によって固有名詞や読みの分割結果が変わる。 [^]
  - Footnote: Wikipedia 冒頭文の例では mecab-ipadic がトークン数 90、bccwj-suw+unidic-cwj-3_1_1 がトークン数 95 と出力されている。

### References
- https://zenn.dev/kun432/scraps/e6833d0bb59161
