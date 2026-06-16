# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-06-16T10:09:44.7786383+09:00
- Articles: 3

## 「CLIProxyAPI」を試す

### Executive Summary
- GLM Coding Plan を Codex から使いやすくする目的で、CLIProxyAPI を試している。
- CLIProxyAPI は OpenAI、Gemini、Claude、Codex、Grok 互換の API インターフェースを提供する CLI 用プロキシサーバーとして紹介されている。
- OAuth 経由で OpenAI Codex と Claude Code を扱える点が、Codex 利用者にとって重要な評価対象になっている。
- OpenAI Responses、Gemini、Claude 互換クライアントや SDK から複数アカウントの CLI アクセスを扱える構成が説明されている。
- Ubuntu 24.04 環境ではインストールスクリプトで 7.2.5 が導入され、config.yaml と systemd user service が作成された。
- 生成された API キーや OAuth ログインコマンドを使い、Gemini、Codex、Claude、Qwen、iFlow などの認証を行う流れになっている。
- help 出力では Codex OAuth、Codex device flow、Claude、Kimi、xAI、Antigravity など複数プロバイダー向けログインが確認されている。

### Key Findings
- CLIProxyAPI は複数プロバイダー互換の API プロキシとして位置づけられている。 [^]
  - Footnote: 記事では「OpenAI/Gemini/Claude/Codex/Grok 互換のAPIインターフェースを提供するCLI用プロキシサーバー」と説明されている。
- Codex 連携は OAuth を通じてサポートされる。 [^]
  - Footnote: README 抜粋に「OAuth経由でOpenAI Codex（GPTモデル）およびClaude Codeにも対応」とある。
- 複数アカウントの負荷分散が主要機能の一つになっている。 [^]
  - Footnote: 概要に「ラウンドロビン方式による複数アカウントの負荷分散」や「OpenAI Codexのマルチアカウント負荷分散」と記載されている。
- インストールスクリプトは Linux 環境でバイナリ、設定、systemd service まで作成する。 [^]
  - Footnote: 出力では「Latest version: 7.2.5」「Created config.yaml」「Systemd service installed」と報告されている。
- インストール後には複数プロバイダー向けの認証コマンドを実行する必要がある。 [^]
  - Footnote: Quick Start には「./cli-proxy-api --login」「--codex-login」「--claude-login」「--qwen-login」「--iflow-login」が並んでいる。
- CLI の help では Codex device flow や Antigravity など追加のログイン手段も確認できる。 [^]
  - Footnote: Usage 出力に「-codex-device-login」「-antigravity-login」「-kimi-login」「-xai-login」などが含まれている。

### References
- https://zenn.dev/kun432/scraps/71f4d8cdff3fb7

## メモ: wakewordlab

### Executive Summary
- wakewordlab は Python 向けのオンデバイス型ウェイクワード検出ライブラリとして紹介されている。
- Silero VAD による事前フィルタで、音声フレームのみ推論することで無音時の CPU 使用率と誤検知を下げる設計になっている。
- 記事では openWakeWord と比較して、小さいモデルサイズ、低い計算量、高い認識率を主な利点として整理している。
- hey_jarvis の比較では wakewordlab の .wkw モデルが約 240 KB、openWakeWord パイプラインが約 3.5 MB とされている。
- Raspberry Pi 3 の比較では wakewordlab が 48.1 MMAC/秒、openWakeWord が 530.3 MMAC/秒とされ、計算量差が大きい。
- Home Assistant Green の文脈では、openWakeWord が 1 コアの 26-53% を占める可能性がある一方、wakewordlab は約 1-2% とされる。
- 一方で、カスタムウェイクワードのトレーニング方法が公開されていない可能性があり、実利用上の懸念として挙げられている。

### Key Findings
- wakewordlab は常時稼働向けの軽量ウェイクワードエンジンとして設計されている。 [^]
  - Footnote: 記事では「小型ハードウェア上で常時動作させるのに十分な低コストなウェイクワードエンジン」と説明されている。
- Silero VAD により無音時の推論を避ける設計が採られている。 [^]
  - Footnote: 本文に「Silero VADによる事前フィルタを搭載」「音声フレームのみを対象に推論」とある。
- モデルサイズは openWakeWord より大幅に小さいとされる。 [^]
  - Footnote: hey_jarvis の比較で「.wkw形式: 244,541バイト」「openWakeWordパイプライン: 3,685,906バイト」と示されている。
- Raspberry Pi 3 では wakewordlab の CPU 負荷が openWakeWord より低い。 [^]
  - Footnote: 表では wakewordlab が「コアの15.3%負荷」、openWakeWord が「コアの40.6%負荷」とされている。
- Home Assistant 環境では openWakeWord の埋め込みモデルが大きな負荷要因と整理されている。 [^]
  - Footnote: 本文では openWakeWord が「Google音声埋め込みモデル（4200万MACs）」を 80ms ごとに実行すると説明されている。
- wakewordlab は低いベースライン計算量により複数モデル運用でも優位性があるとされる。 [^]
  - Footnote: 記事では wakewordlab の 2 モデルが「openWakeWordの1インスタンスの10分の1以下の計算量」と説明されている。
- 公開モデルの商用利用やカスタム学習には制約がある可能性がある。 [^]
  - Footnote: 本文に「公開モデルは商用利用を目的としない場合に限り」および「カスタムウェイクワードの学習方法は公開されてなくて」とある。

### References
- https://zenn.dev/kun432/scraps/36e3840eaac24a

## メモ: OpenRouter Fusion API

### Executive Summary
- OpenRouter Fusion API は複数モデルの回答を統合し、単一 API として利用できる仕組みとして紹介されている。
- Fusion は複数モデルに同じプロンプトを投げ、判定モデルが合意点、矛盾点、独自の洞察、盲点を整理する流れになっている。
- その分析をもとに合成モデルが最終回答を作るため、ユーザーからは通常の単一モデル呼び出しに近く見える。
- DRACO の 100 種類の高度なリサーチ課題で評価され、複数モデル構成が単一モデルを上回る傾向が示されたとされる。
- Gemini 3 Flash、Kimi K2.6、DeepSeek V4 Pro の節約パネルは、Fable 5 に 1% 以内まで迫り、コストは約半分と説明されている。
- 利用方法は model に openrouter/fusion を指定する方法と、server tool として Fusion を渡す方法が示されている。
- 用途としては、医療、法律、金融、製品比較など、多面的な調査や正確性が重要なタスクに向く一方、レイテンシーや推論コストはトレードオフになる。

### Key Findings
- Fusion は複数モデルのパネル構成で回答品質を高めるアプローチである。 [^]
  - Footnote: 本文に「複数モデルを組み合わせたパネル構成は、単一モデルを一貫して上回る性能」とある。
- 性能向上は合成処理とモデル多様性の両方から生じるとされる。 [^]
  - Footnote: 記事では「性能向上効果の約4分の3は合成処理」「残りの4分の1は多様性」と説明されている。
- 低コストモデルの組み合わせでも高級モデル級の性能に迫る結果が示されている。 [^]
  - Footnote: 本文に「低コストパネルがClaude Fable 5と同等の性能」および「コストは約半分」とある。
- Fusion はサーバー側で動作し、単一モデルのように呼び出せる。 [^]
  - Footnote: 記事では「サーバー側で動作するため、開発者は単一モデルのように直接呼び出すことができます」と説明されている。
- DRACO 評価では検索による評価基準の露出を防ぐため、該当ドメインを除外して再テストしている。 [^]
  - Footnote: 本文に「該当ドメインを除外しました。その後、すべてのテストを再度実施」とある。
- 同一モデルを複数回使う構成でも改善が確認されたとされる。 [^]
  - Footnote: まとめ部分では「Opus 4.8 × Opus 4.8」で「58.8% → 65.5%にアップ」と説明されている。
- 著者はマルチエージェント的な構成を単一 API で抽象化したものとして理解している。 [^]
  - Footnote: コメントに「複数のエージェントがいて、それをチェックするエージェントがいて、最終回答を出すエージェントがいる、みたいなのを、単一APIで抽象化」とある。

### References
- https://zenn.dev/kun432/scraps/7b58c479bac0bc
