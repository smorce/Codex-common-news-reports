# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-06-17T00:00:00+09:00
- Articles: 3

## コーディングエージェント用プロキシ「CLIProxyAPI」を試す
- Date: 2026-06-15T13:39:03+00:00

### Executive Summary
- GLM-5.2 と GLM Coding Plan を Codex から使う方法として CLIProxyAPI を検証している。
- CLIProxyAPI は OpenAI、Gemini、Claude、Codex、Grok 互換の API インターフェースを提供する CLI 向けプロキシとして紹介されている。
- インストールは Ubuntu 24.04 上で公式インストールスクリプトを使い、バージョン 7.2.5 が導入された。
- インストール後は systemd user service、設定ファイル、生成 API キーなどがホームディレクトリ配下に作成された。
- OpenCode Go と GLM Coding Plan は標準対応が明記されていないため、OpenAI 互換または Anthropic 互換として設定する方針になっている。
- config.yaml に残っていた例示 API キーが原因で通常 API サーバーが無効化される問題があり、例示キー削除で起動できた。
- Codex 側では model_provider と base_url を CLIProxyAPI に向ける設定を試しており、利用可否と互換性を検証する流れになっている。

### Key Findings
- CLIProxyAPI は複数 CLI モデルを OpenAI 互換などの API として扱うためのプロキシである。 [^]
  - Footnote: 記事では「OpenAI/Gemini/Claude/Codex/Grok 互換のAPIインターフェースを提供するCLI用プロキシサーバー」と説明している。
- OAuth 経由で OpenAI Codex と Claude Code にも対応している。 [^]
  - Footnote: README 抜粋として「現在はOAuth経由でOpenAI Codex（GPTモデル）およびClaude Codeにも対応」と記載されている。
- Ubuntu 環境ではインストールスクリプトで CLIProxyAPI 7.2.5 が導入された。 [^]
  - Footnote: 実行ログに「Latest version: 7.2.5」「CLIProxyAPI 7.2.5 installed successfully」とある。
- インストール時に systemd user service と config.yaml が生成された。 [^]
  - Footnote: ログに「Created config.yaml from example」「Systemd service installed: /home/kun432/.config/systemd/user/cliproxyapi.service」とある。
- OpenCode Go はモデルによって OpenAI 互換と Anthropic 互換を使い分ける必要がある。 [^]
  - Footnote: 記事では「Qwen / Minimax は Anthropic互換」「GLM / Kimi / DeepSeek / MiMo は OpenAI互換」と整理している。
- 例示 API キーが残っていると通常 API サーバーが無効化される。 [^]
  - Footnote: 起動ログに「normal API server disabled: example API key values are configured」と出ており、your-api-key-3 の削除で解消したと説明している。
- CLIProxyAPI の利用が各プロバイダーの公認利用に当たるかは不明で、規約リスクに注意が必要である。 [^]
  - Footnote: 記事では「公式に許可されたコーディングエージェント・ツールしか利用できない」という記載に触れ、リスクの可能性を指摘している。

### References
- https://zenn.dev/kun432/scraps/71f4d8cdff3fb7

## メモ: wakewordlab
- Date: 2026-06-15T06:10:25+00:00

### Executive Summary
- wakewordlab は Python 向けのデバイス内蔵型ウェイクワード検出機能として紹介されている。
- Silero VAD による事前フィルタで音声フレームだけを推論対象にし、無音時の CPU 使用率と誤検知を抑える設計である。
- モデルサイズは openWakeWord パイプラインより大幅に小さく、記事では約 15 倍小さい出荷時モデルサイズとして扱われている。
- Raspberry Pi 3 の単一コア測定では wakewordlab の CPU 負荷相当値が 15.3% とされ、openWakeWord より低い。
- Home Assistant 環境では openWakeWord の埋め込みモデルが高負荷要因で、HA Green の 1 コアの 26-53% を占有しうると説明されている。
- wakewordlab は自己完結型の畳み込みモデルで外部埋め込みに依存せず、ストリーミング経路の計算量が約 24MMAC/秒とされる。
- 一方でカスタムウェイクワードのトレーニング方法が公開されていない可能性があり、筆者は実用面の懸念を示している。

### Key Findings
- wakewordlab はオンデバイスのウェイクワード検出を目的にした Python 向け機能である。 [^]
  - Footnote: 記事では「Python向けのデバイス内蔵型ウェイクワード検出機能」と説明している。
- Silero VAD によって無音時の推論を避け、CPU 使用率と誤検知を減らす。 [^]
  - Footnote: 「Silero VADによる事前フィルタを搭載」「無音時のCPU使用率を削減し、誤検知を大幅に低減」とある。
- パッケージモデルは openWakeWord パイプラインより大幅に小さい。 [^]
  - Footnote: wakewordlab の .wkw モデルが 244,541 バイト、openWakeWord パイプラインが 3,685,906 バイトとして示されている。
- Raspberry Pi 3 では wakewordlab のコア負荷が openWakeWord より低い。 [^]
  - Footnote: 表では wakewordlab が「コアの15.3%負荷」、openWakeWord が「コアの40.6%負荷」とされている。
- Home Assistant Green では openWakeWord の埋め込み処理が大きな負荷になる。 [^]
  - Footnote: 記事は openWakeWord が「26～53%のCortex-A55コアを占有」し、UI や自動化処理と競合すると説明している。
- wakewordlab のストリーミング処理は openWakeWord より低い計算量で動作する。 [^]
  - Footnote: 「完全なストリーミング処理経路の計算量は約24MMAC/秒」「openWakeWordの約22分の1」とある。
- カスタムウェイクワードの自己学習ができない場合、採用上の制約になる。 [^]
  - Footnote: 筆者は「カスタムウェイクワードのトレーニングが自分でできないのであれば、ちょっと厳しい」と述べている。

### References
- https://zenn.dev/kun432/scraps/36e3840eaac24a

## メモ: OpenRouter Fusion API
- Date: 2026-06-15T04:34:54+00:00

### Executive Summary
- OpenRouter Fusion API は複数モデルの回答を統合する複合モデル API として紹介されている。
- Fusion は複数モデルに同じ課題を投げ、判定モデルが合意点や矛盾点を抽出し、合成モデルが最終回答を作る仕組みである。
- DRACO ベンチマークを使い、法律、医療、金融、製品比較など 10 分野の 100 種類の高度な調査課題で評価された。
- 複数モデルのパネルは単一モデルより高い性能を示すことが多く、安価なモデルの組み合わせでも高性能モデルに迫るとされている。
- Gemini 3 Flash、Kimi K2.6、DeepSeek V4 Pro の節約パネルは Fable 5 に 1% 差まで迫り、コストは約半分と説明されている。
- Fusion は openrouter/fusion というモデルスラッグで単一モデルのように呼び出せるほか、サーバーツールとして他モデルに渡す使い方も示されている。
- 筆者は、自前でマルチエージェントを組まず API 一つで統合できる点にメリットを見つつ、推論コストとレイテンシーのトレードオフを指摘している。

### Key Findings
- Fusion API は複数モデルの出力を判定・合成して最終回答を作る仕組みである。 [^]
  - Footnote: 記事では判定用モデルが「合意点、矛盾点、部分的なカバー範囲、独自の洞察、盲点」を抽出し、合成モデルが回答を作ると説明している。
- 評価には DRACO の 100 種類の高度なリサーチ課題が使われた。 [^]
  - Footnote: 「法律・医療から金融、製品比較まで、10の専門分野にわたる100種類の高度なリサーチ課題」と記載されている。
- 複数モデルのパネル構成は単一モデルを上回る傾向がある。 [^]
  - Footnote: 記事には「複数モデルを組み合わせたパネル構成は、単一モデルを一貫して上回る性能」とある。
- Fusion の性能向上は合成処理とモデル多様性の両方に由来する。 [^]
  - Footnote: 「性能向上効果の約4分の3は合成処理」「残りの4分の1は多様性」と説明されている。
- 低コストモデルの組み合わせでも高級モデル単体に近い性能を達成できる。 [^]
  - Footnote: 節約パネルは「Fable 5の性能からわずか1%以内」「コストは約半分」と紹介されている。
- Fusion は API 上では単一モデルのように扱える。 [^]
  - Footnote: 「openrouter/fusion」というモデルスラッグで利用可能と記載されている。
- Web 検索付き評価ではベンチマーク情報の取得を防ぐため除外設定が必要だった。 [^]
  - Footnote: DRACO 評価基準をオンラインで提示する問題に対し、該当ドメインを除外して再テストしたと説明している。
- 筆者は高品質化の代償としてレイテンシーと推論コストを考慮すべきだと見ている。 [^]
  - Footnote: 「それぞれの推論コストは発生する」「正確性のトレードオフとしてレイテンシーもありそう」と述べている。

### References
- https://zenn.dev/kun432/scraps/7b58c479bac0bc
