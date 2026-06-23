# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-06-23T00:00:00+09:00
- Articles: 3

## AgentSpace

### Executive Summary
- AgentSpace は、人間と AI エージェントを同じチーム、同じワークスペースで扱うための共同作業基盤として紹介されている。
- 既存のエージェント利用は個人端末や単発チャットに閉じがちで、組織利用では可視性、責任、権限管理が崩れやすいという問題意識が中心にある。
- AgentSpace はエージェントに役割、所有者、権限、スケジュール、責任を与え、デジタル従業員として管理する発想を取る。
- コア機能として、エージェント採用、マルチエージェント連携、スケジュール管理、権限と承認、監査ログ、部門間共有が挙げられている。
- AgentRouter により Claude Code、Codex、OpenClaw、Hermes、nanobot など複数ランタイムへ同じエージェントをルーティングできると説明されている。
- 導入方式はホスティングサービス型とセルフホスト型の 2 種類があり、どちらも同じ製品機能を使えるとされる。
- 筆者は、マルチユーザーとマルチエージェントを前提にしたワークスペースとしては良さそうだと評価している。
- 一方で、実際に試した結果として不具合が多く、Codex に修正させても修正量が多かったため一旦保留と述べている。

### Key Findings
- AgentSpace は人間とエージェントの共同作業を、共有ワークスペース上のチームとして扱う。 [^]
  - Footnote: 記事には「人間 + エージェント。一つのチーム。一つのワークスペース。」とあり、AgentSpace は人間とエージェントを一つのチームとして統合すると説明されている。
- 既存のエージェント利用は個人利用前提で、チーム運用には適しにくいという課題が示されている。 [^]
  - Footnote: 記事では「一人一端末、一回のチャットセッション」や「ほとんどのエージェントフレームワークは個人使用を想定」といった課題が挙げられている。
- エージェントをデジタル従業員として、役割、所有者、権限、責任を持つ存在にする設計である。 [^]
  - Footnote: 本文に「本物の役割、明確なオーナー、権限、スケジュール、責任を与え」とあり、「デジタル従業員であるべき」と説明されている。
- AgentRouter は複数のエージェント実行環境をまたいで、同じエージェントの文脈や権限を保つ役割を担う。 [^]
  - Footnote: 記事では AgentRouter が Claude Code、Codex、OpenClaw、Hermes、nanobot などへルーティングし、アイデンティティ、コンテキスト、スキル、権限を保持すると述べている。
- 権限管理、承認、監査ログは後付けではなく組み込み機能として位置づけられている。 [^]
  - Footnote: 本文に「権限と承認を強制 — ガバナンスは組み込み型で、後付けではない」および「すべてのアクション、出力量、決定を監査」とある。
- 導入はホスティングサービス型とセルフホスト型の二択で、利用機能に差はないとされる。 [^]
  - Footnote: 導入オプションの表で、ホスティングサービスとセルフホスト型が示され、「どちらのモードでも同じ製品を利用できます」と説明されている。
- 2026年6月22日の更新では、AgentRouter が複数ランタイムに対応したことが示されている。 [^]
  - Footnote: 最新情報に「2026年6月22日 ― AgentRouterがClaude Code、Codex、OpenClaw、Hermes、nanobotに対応しました」と記載されている。
- 筆者の試用感では、現時点では不具合が多く実用評価は保留になっている。 [^]
  - Footnote: 最後のコメントで「まだいろいろ不具合多いかな」「一旦ペンディング」と述べている。

### References
- https://zenn.dev/kun432/scraps/c8b1434e0470f5
- https://github.com/HKUDS/AgentSpace

## Goのエージェントフレームワークいろいろ

### Executive Summary
- 筆者は Go 入門中の文脈で、Go 向けの AI エージェントフレームワークを調査している。
- 取り上げられている主な候補は go-agent、Eino、Google の adk-go、Charmbracelet の fantasy、Google 系の Genkit である。
- go-agent は LLM プロバイダー、メモリ、ファイルコンテキスト、ガードレール、UTCP、マルチエージェント協調を備える Go フレームワークとして紹介されている。
- Eino は LangChain や Google ADK の知見を取り入れつつ、Go の標準的な書き方に沿った LLM アプリ開発フレームワークとして説明されている。
- adk-go は Google 製で、Go の並行処理や性能を活かしたクラウドネイティブなエージェントアプリ開発向けとされる。
- Genkit は Go だけでなく複数言語向け SDK を持ち、Google、OpenAI、Anthropic、Ollama などを統一インターフェースで扱えるとされる。
- 筆者のざっくりした所感では、安心感なら adk-go / genkit、OSS のスター数なら Eino が有力候補と整理されている。
- 最終的には、Go をもう少し書き慣れてから試してみたいという結論になっている。

### Key Findings
- 記事の目的は Go 向けエージェントフレームワークの概観である。 [^]
  - Footnote: 冒頭で「Go向けのエージェントフレームワークにどのようなものがあるのか、を調べてみた」と述べている。
- go-agent は多プロバイダー、メモリ、ガードレール、マルチエージェント協調を含むフレームワークである。 [^]
  - Footnote: 本文に「プラグイン可能なLLMプロバイダー、メモリ機能、ファイルコンテキスト、ガードレール、UTCPツールオーケストレーション、マルチエージェント協調機能」とある。
- go-agent は Apache-2.0 ライセンスである。 [^]
  - Footnote: go-agent の説明末尾に「Apache-2.0ライセンス」と記載されている。
- Eino は Go の標準的なコーディング規約に沿った LLM アプリ開発フレームワークとして位置づけられている。 [^]
  - Footnote: Eino の説明で「Go言語の標準的なコーディング規約に準拠して設計」と書かれている。
- Eino にはコンポーネント、ADK、グラフやワークフロー構成、サンプルコードが含まれる。 [^]
  - Footnote: 記事では ChatModel、Tool、Retriever、ChatTemplate、ADK、グラフやワークフロー、動作可能なコード例が列挙されている。
- adk-go は Gemini 向けに最適化されつつ、モデル非依存かつデプロイ環境非依存と説明されている。 [^]
  - Footnote: adk-go の説明に「Gemini向けに最適化されていますが、モデル非依存・デプロイ環境非依存」とある。
- Genkit は JavaScript/TypeScript と Go が本番環境対応、Python はベータ、Dart はプレビューという整理で紹介されている。 [^]
  - Footnote: Genkit の説明で各 SDK の安定性として「JavaScript/TypeScript」「Go」は本番環境対応、「Python」はベータ、「Dart」はプレビューと記載されている。
- 筆者は候補選びの観点として Google 製の安心感と OSS スター数を挙げている。 [^]
  - Footnote: 記事末尾で「開発元がGoogleで安心かも: adk-go / genkit」「OSSでstarが一番大そう: eino」と整理している。

### References
- https://zenn.dev/kun432/scraps/d070aa4b1b3fc9
- https://github.com/Protocol-Lattice/go-agent
- https://github.com/cloudwego/eino
- https://github.com/google/adk-go
- https://github.com/genkit-ai/genkit

## 「UpSkill」を試す

### Executive Summary
- UpSkill は、低コストな Flash モデルを継続的なスキル改善によって Pro モデル級の性能へ近づける軽量フレームワークとして紹介されている。
- 背景には、Pro モデルは高品質だが高コスト、Flash モデルは安価だが信頼性に課題があるというトレードオフがある。
- ベンチマークとして Terminal-Bench 2.0 が使われ、25 の訓練タスクで抽出したスキルを 64 の未学習テストタスクに適用したと説明されている。
- 結果では Flash + UpSkill がテスト合格率 51.6% となり、Pro モデルの 50.0% を上回ったとされる。
- コスト面では Flash + UpSkill がタスクあたり $0.04、Pro モデルが $0.06 とされ、41% 低いコストで上回ったと主張されている。
- 仕組みとして Daily モデル、Pro モデル、Flash モデルの 3 役割があり、失敗時に Pro モデルが分析し、Flash モデルで検証されたスキルだけを残す。
- Ralph ループは、弱いモデルが実際に従える指示へスキルを調整するための検証ループとして説明されている。
- 筆者は Quickstart を見た上で、Claude Code 前提、プロバイダー切り替え、Flash と Daily の使い分けに疑問を示している。

### Key Findings
- UpSkill は Flash モデルを Pro モデル級に近づけることを狙うフレームワークである。 [^]
  - Footnote: 記事冒頭に「スキルを継続的に進化させ続ける軽量フレームワーク」「FlashモデルをProモデルに進化」とある。
- 問題意識は、高性能モデルのコストと低コストモデルの信頼性不足の両立にある。 [^]
  - Footnote: 本文では「Proモデルはコストが高すぎる」「Flashモデルは信頼性に欠ける」として、既存のトレードオフを説明している。
- Terminal-Bench 2.0 の 89 タスクを使った検証が紹介されている。 [^]
  - Footnote: 性能検証に「Terminal-Bench 2.0」「16分野にわたる89種類の実際のターミナル操作タスク」と記載されている。
- 評価では Flash + UpSkill が Pro モデルの合格率を上回ったとされる。 [^]
  - Footnote: 結果表では Flash 45.3%、Pro 50.0%、Flash + Upskill 51.6% と示されている。
- Flash + UpSkill は Pro モデルより低コストで高い性能を達成したという主張がある。 [^]
  - Footnote: 本文に「タスクあたり$0.04」「タスクあたり$0.06のProモデルを41%低いコストで上回る性能」とある。
- UpSkill はセッションフックとして統合され、インフラ変更不要と説明されている。 [^]
  - Footnote: 仕組みの説明で「エージェントのハーネスに軽量なセッションフックとして統合」「インフラストラクチャの変更は不要」と記載されている。
- Ralph ループは、Pro モデルの助言を Flash モデルが実際に使えるスキルへ検証・改良するための仕組みである。 [^]
  - Footnote: 記事では、第1ラウンドで Pro モデルが失敗を分析し、第2ラウンド以降で Flash モデルが再試行し、機能するまで改良すると説明されている。
- 筆者は現状の実装が Claude Code 前提で、他のコーディングエージェントではそのまま使えない可能性を指摘している。 [^]
  - Footnote: Quickstart への所感で「Claude Code が前提」「そのままだとCodexやらOpenCodeなど他のコーディングエージェントでは使えない」と述べている。

### References
- https://zenn.dev/kun432/scraps/4217f31bcb231c
- https://github.com/HKUDS/UpSkill
- https://github.com/HKUDS/UpSkill/blob/main/tb_harbor_2.0/RESULTS.md
