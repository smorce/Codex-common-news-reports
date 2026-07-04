# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-04T09:01:14.1013292+09:00
- Articles: 3

## OpenWiki
- Date: 2026-07-03T14:55:51+00:00

### Executive Summary
- OpenWiki はコードベース向けの wiki を自動生成し、更新し続けるツールとして紹介されている。
- 狙いは、人間とコーディングエージェントが巨大なリポジトリを迷わず理解できる状態を作ることにある。
- README や AGENTS.md に全情報を詰め込むのではなく、リンクされた小さな wiki ページ群として知識を整理する。
- CLI で初期生成でき、GitHub Actions によってコード変更に追従する差分更新も想定されている。
- AGENTS.md や CLAUDE.md には wiki への参照を置き、エージェントが必要なページだけ参照する構成を取る。
- DeepWiki、AutoWiki、Karpathy の LLM Wiki 構想などが思想的な背景として挙げられている。
- 古いドキュメントを避け、エージェントが最新に近いリポジトリ理解を持てる運用を重視している。

### Key Findings
- OpenWiki はリポジトリから wiki 形式のドキュメントを自動生成する。 [^]
  - Footnote: 記事には「リポジトリから wiki 形式のドキュメントを自動生成する」と説明されている。
- 生成された wiki はエージェントの参照先として使う想定である。 [^]
  - Footnote: 記事では「その wiki をエージェントに教えて、参照させる」と書かれている。
- GitHub Actions による自動更新で、コード変更への追従を狙っている。 [^]
  - Footnote: 記事には「GitHub Action でコード変更に合わせて wiki を自動更新する」とある。
- wiki 形式は巨大な単一ファイルよりもトークン効率と保守性に優れるとされている。 [^]
  - Footnote: 記事では「毎回全部をコンテキストに読み込むとトークンの無駄」「全体をメンテするのダルすぎ」と課題が挙げられている。
- AGENTS.md や CLAUDE.md には wiki 本体ではなく参照を追加する設計である。 [^]
  - Footnote: 記事には「でかい wiki 本体は AGENTS.md の中に直書きしない」と説明されている。
- 差分更新はフル再生成を避け、大規模リポジトリでも運用しやすくする。 [^]
  - Footnote: 記事では「デカいリポでも毎回フル再生成しなくていい」と述べられている。

### References
- https://zenn.dev/kun432/scraps/c4d2f75eb7e493

## 「Tau」を試す ② Tau はどう動くのか？
- Date: 2026-07-03T13:28:07+00:00

### Executive Summary
- この記事は Tau の 2 本目のスクラップで、前回の Quickstart 後にアーキテクチャ文書を見る導入として書かれている。
- 本文で確認できる内容は短く、具体的な検証結果や詳細な設計解説はまだ掲載されていない。
- テーマは Tau の動作原理やアーキテクチャを追うことに置かれている。
- 記事タイトルとタグから、Python、pip、Agent、tau に関する技術メモであることが分かる。
- 状態は Open で、一覧上はコメント追加から 11 時間前の新しいスクラップとして表示されている。
- 前回記事を受けた続編であり、Quickstart からドキュメント確認へ進む流れを示している。
- 要約時点では、本文にない Tau の内部仕様は不明として扱う必要がある。

### Key Findings
- 本記事は前回の Quickstart の続編である。 [^]
  - Footnote: 本文に「前回」「とりあえず Quickstart を試したので」とある。
- 記事の次の目的は Tau のアーキテクチャ関連ドキュメントを確認することにある。 [^]
  - Footnote: 本文では「Tau のアーキテクチャなどのドキュメントを見ていこうと思う」と書かれている。
- 記事は Tau を対象にしたスクラップである。 [^]
  - Footnote: タイトルは「『Tau』を試す ② Tau はどう動くのか？」で、タグにも「tau」がある。
- 記事は Agent 関連の文脈で分類されている。 [^]
  - Footnote: ページ上のタグとして「Agent」が表示されている。
- 取得時点で本文は導入文中心で、詳細な検証内容は確認できない。 [^]
  - Footnote: 取得本文は「前回」と「とりあえず Quickstart を試したので...」の短い説明に留まっている。

### References
- https://zenn.dev/kun432/scraps/489be3c6b00b83

## 「Tau」を試す ① Quickstart
- Date: 2026-07-03T08:23:41+00:00

### Executive Summary
- Tau はターミナルで動作するコーディング支援エージェントとして紹介されている。
- この記事では Tau の概要、名前の由来、公式ドキュメントの内容、Quickstart の実行結果がまとめられている。
- Tau は実用的な TUI エージェントであると同時に、コーディングエージェントの仕組みを学ぶための教育用プロジェクトとされる。
- インストールは uv tool install tau-ai で行い、記事内では tau-ai 0.1.0 が導入されている。
- モデルプロバイダーは OpenAI、Anthropic、OpenRouter、Hugging Face などに対応し、OpenAI 互換 API も使えそうだとされている。
- ChatGPT サブスク利用時は /login openai-codex による OAuth 認証が試されている。
- セッション再開やワンショット実行も確認され、--provider openai-codex を指定するとプロンプト実行できたと報告されている。
- まとめでは、サンドボックス確認は Codex や Claude Code ほど強くなく、Pi に近いミニマムな印象だと述べられている。

### Key Findings
- Tau はターミナル環境で動作するコーディング支援エージェントである。 [^]
  - Footnote: 公式ドキュメント抜粋として「Tau はターミナル環境で動作するコーディング支援エージェントです」とある。
- Tau は実用ツールと学習用プロジェクトの両面を持つ。 [^]
  - Footnote: 本文には「Tau は同時に2つの機能を備えています」として「実用的なツール」「学びを得られるプロジェクト」が挙げられている。
- ファイル操作、シェルコマンド、会話を組み合わせて作業できる。 [^]
  - Footnote: 機能説明に「プロジェクト内でファイルの読み取り/書き込み/編集を行いながら、シェルコマンドを実行しながら会話を進める」とある。
- 複数のモデルプロバイダーと OpenAI 互換エンドポイントを利用できる。 [^]
  - Footnote: 本文では「OpenAI、Anthropic、OpenAI Codex、OpenRouter、Hugging Faceなどの OpenAI互換エンドポイント」と説明されている。
- 記事の検証環境では uv tool install tau-ai で tau 0.1.0 が入っている。 [^]
  - Footnote: インストール出力に「+ tau-ai==0.1.0」「Installed 1 executable: tau」、バージョン確認に「tau 0.1.0」とある。
- ChatGPT サブスクの場合、openai-codex ログインで認証を行っている。 [^]
  - Footnote: 本文には「ChatGPTサブスクの場合は以下を入力。/login openai-codex」とある。
- ワンショット実行では provider 指定が必要だったと報告されている。 [^]
  - Footnote: 本文では「--provider で設定したプロバイダーを指定できる様子」「tau --provider openai-codex -p ...」とある。
- 筆者は Tau を教育用でミニマムなものかもしれないと評価している。 [^]
  - Footnote: まとめに「教育用と銘打ってあるのでコード読んで自分でカスタマイズしていく、という感じなのかも」とある。

### References
- https://zenn.dev/kun432/scraps/9f9b79238dff5d
- https://twotimespi.dev
