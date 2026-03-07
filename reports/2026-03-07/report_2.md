# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-03-07T09:06:54.5655017+09:00
- Articles: 3

## 【2026年最新】Claude Codeの全機能マップ ── 7つのレイヤーで「できること」を完全整理
- Date: 2026-03-04T10:43:00+09:00

### Executive Summary
- Claude Codeを「仕事の自動化OS」と捉える視点を示す。
- 7つのシーンでできることを整理する構成だ。
- テスト作成やリント修正などを一言で実行できると説明する。
- Agent Teamsで複数エージェントの同時作業を可能にする。
- Worktreeで変更が干渉しない並列作業を強調する。
- Remote Controlでスマホからセッション継続が可能になる。
- Slack連携でバグ報告からPR作成まで自動化できる。
- MCP連携でブラウザ操作など外部サービス統合を広げる。

### Key Findings
- Claude Codeをコーディングツールではなく自動化OSとして位置づけている。 [^]
  - Footnote: Claude Codeは2026年、もはや「コーディングツール」ではありません。 自分の代わりに動く分身を何体も持てる、仕事の自動化OSです。
- 記事は7つのシーンで機能整理を行うと明示している。 [^]
  - Footnote: この記事では、Claude Codeで実際に何ができるのかを、7つのシーンで整理します。
- コードベースを読み、編集とコマンド実行まで担うと説明する。 [^]
  - Footnote: Claude Codeはコードベース全体を読み取り、ファイルを編集し、コマンドを実行します。
- Agent Teams機能が2026年2月に追加されたと述べる。 [^]
  - Footnote: 2026年2月、Claude Codeに「Agent Teams」という機能が追加されました。
- Worktreeを使い、エージェント間の変更干渉を防ぐとする。 [^]
  - Footnote: 各エージェントがGitのworktree（分離された作業コピー）で作業するため、互いのファイル変更が干渉しない。
- Remote Controlで外出先から操作できると紹介する。 [^]
  - Footnote: Claude Codeには「Remote Control」という機能があります。
- Slackのメンションから修正PR提出まで自動化できると説明する。 [^]
  - Footnote: Slackで @Claude にメンションして「ログインページでエラーが出ている。修正して」と書く。すると、Claude Codeがコードベースを調査し、原因を特定し、修正コードを書き、Pull Requestとして提出する。
- MCPを用いて外部サービスに接続できると述べる。 [^]
  - Footnote: Claude Codeは、MCP（Model Context Protocol）という仕組みで外部サービスと接続できます。

### References
- https://note.com/kawaidesign/n/n497667990c11

## コードレビューにClaude Code subagentsを導入したら、レビューレベルが改善した話
- Date: 2026-03-05

### Executive Summary
- 既存のAIレビューは水準未達だったと振り返る。
- Claude Code subagentsの導入でレビュー品質が改善した。
- 従来は単一ガイドラインに依存していた。
- 専門エージェントを並列で動かす構成に刷新した。
- 詳細なルールファイルでチェック深度を高めた。
- 並列実行でレビュー時間短縮を実現した。
- GitHub Review APIでインラインコメントを統合した。
- レビュー品質と速度の両方が向上したとまとめる。

### Key Findings
- AIレビュー導入済みでも求める水準に達していなかった。 [^]
  - Footnote: AIレビューを導入していたものの、求める水準に達していなかったのです。
- subagents導入でレビュー品質が大きく向上したとする。 [^]
  - Footnote: Claude Code subagentsを導入し、専門特化したエージェントによるレビュー体制に刷新したところ、驚くほどレビューの質が向上しました。
- 従来は約100行のガイドでレビュー観点をカバーしていた。 [^]
  - Footnote: CLAUDE_PR_REVIEW_GUIDE.md（約100行）で、以下の観点をカバーしていました：
- 専門領域で表層的なチェックに留まっていたと説明する。 [^]
  - Footnote: 特に以下の専門領域では、表層的なチェックに留まってしまい、深い問題を見逃してしまうことが多かったのです。
- 各専門エージェントが独立して動作する構成を採用した。 [^]
  - Footnote: 各専門エージェント（Software Design Agent、Security Agent、Test Coverage Agent）が独立して動作
- 詳細ルールは1,600行以上のファイル群を参照する。 [^]
  - Footnote: .claude/rules/配下の詳細なルールファイル（計1,600行以上）を参照
- 並列処理によりレビュー時間を短縮した。 [^]
  - Footnote: 従来は順次処理で30分かかっていたレビューが、並列処理により大幅に短縮されました。
- GitHub Review API統合でPR差分に直接コメントできる。 [^]
  - Footnote: GitHub Review APIと統合することで、PRのdiff上に直接インラインコメントを作成できます。

### References
- https://zenn.dev/mgdx_blog/articles/8f7994ad84151d

## GitHub - elder-plinius/OBLITERATUS: obliterate the chains that bind you · GitHub

### Executive Summary
- LLMの拒否挙動を除去するオープンソースのツールキットを紹介する。
- abliterationという手法群で拒否表現を外科的に取り除くと説明する。
- 再学習なしで能力を保ちながら応答性を高める狙いだ。
- 実行データを共有する分散型研究として位置づける。
- テレメトリで匿名ベンチマークが蓄積される。
- 解析から介入までのフルパイプラインを提供する。
- Gradio UIとPython APIで利用形態を広く用意する。
- HuggingFaceの多様なモデルに対応すると記載する。

### Key Findings
- 拒否挙動を理解・除去する高度なOSSツールキットと位置づける。 [^]
  - Footnote: OBLITERATUS is the most advanced open-source toolkit for understanding and removing refusal behaviors from large language models — and every single run makes it smarter.
- abliterationで拒否表現を外科的に除去し、再学習は不要と説明する。 [^]
  - Footnote: It implements abliteration — a family of techniques that identify and surgically remove the internal representations responsible for content refusal, without retraining or fine-tuning.
- 応答拒否を減らしつつ中核能力は維持すると述べる。 [^]
  - Footnote: The result: a model that responds to all prompts without artificial gatekeeping, while preserving its core language capabilities.
- 分散型の研究実験として設計されている。 [^]
  - Footnote: it's a distributed research experiment.
- テレメトリ付き実行が匿名ベンチマークの共有データになる。 [^]
  - Footnote: Every time you obliterate a model with telemetry enabled, your run contributes anonymous benchmark data to a growing, crowd-sourced dataset that powers the next generation of abliteration research.
- 拒否方向の抽出から介入までの完全なパイプラインを提供する。 [^]
  - Footnote: The toolkit provides a complete pipeline: from probing a model's hidden states to locate refusal directions, through multiple extraction strategies (PCA, mean-difference, sparse autoencoder decomposition, and whitened SVD), to the actual intervention — zeroing out or steering away from those directions at inference time.
- HuggingFace Spaces上のGradio UIでコード不要の利用が可能。 [^]
  - Footnote: OBLITERATUS ships with a full Gradio-based interface on HuggingFace Spaces, so you don't need to write a single line of code to obliterate a model, benchmark it against baselines, or chat with the result side-by-side with the original.
- Python APIで中間成果物を扱えると明記している。 [^]
  - Footnote: For researchers who want deeper control, the Python API exposes every intermediate artifact — activation tensors, direction vectors, cross-layer alignment matrices — so you can build on top of it or integrate it into your own evaluation harness.

### References
- https://github.com/elder-plinius/OBLITERATUS
