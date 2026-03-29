# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-29T09:02:01+09:00
- Articles: 3

## 「Hermes Agent」を試す
- Date: 2026-03-29T00:54:00+09:00

### Executive Summary
- XやRedditの評判を見てHermes Agentに興味を持ったという背景が書かれている。
- メモリー機能が良いという声やOpenClaw代替としての位置づけが示されている。
- Hugging Face統合でモデル選択が拡充された点が引用されている。
- Hermes Agentは学習ループと永続メモリを持つ自己進化型エージェントとして説明される。
- 多様なモデル/プロバイダ対応やTUI、メッセージング対応などの特徴が列挙されている。
- cronやサブエージェントなど自動化・並列処理の機能が紹介されている。
- 公式ドキュメントに従って進める方針とインストール方法が記載されている。

### Key Findings
- XのポストやRedditのスレで評判が良さそうという印象から調査が始まっている。 [^]
  - Footnote: 「X のポストや Reddit のスレで、評判が良さそうな雰囲気を感じた。」
- メモリー機能の評判やOpenClaw代替として捉えられている点に言及している。 [^]
  - Footnote: 「メモリー機能が良いという声がちらほら見えるのと、OpenClawの代替として捉えられているように見える。」
- Hugging Faceを推論プロバイダとして統合し、28のキュレートモデルと100+モデルが利用可能とされている。 [^]
  - Footnote: 「Hugging Face... 28 curated models... 100+ other models」
- Hermes Agentはオープンソースで、マルチレベルメモリと永続的な専用マシンアクセスを持つと説明されている。 [^]
  - Footnote: 「Hermes Agent is open-source and remembers... multi-level memory system and persistent dedicated machine access」
- Nous PortalやOpenRouterなど複数のモデル/プロバイダに対応し、切り替えもコマンドで可能とされている。 [^]
  - Footnote: 「Nous Portal、OpenRouter（200種類以上のモデル）、z.ai/GLM、Kimi/Moonshot、MiniMax、OpenAI」
- インストールはcurlワンライナーで実行可能で、gitのみが事前条件とされている。 [^]
  - Footnote: 「curlでワンライナーでインストールスクリプト実行」「事前に必要なのは git のみ」

### References
- https://zenn.dev/kun432/scraps/8b231b40b0a15f

## 増分処理フレームワーク「Retico」を試す
- Date: 2026-03-26T16:35:00+09:00

### Executive Summary
- ReticoにMaAIが統合されたという投稿を起点に調査している。
- MaAIは会話AI向けの非言語行動生成をリアルタイムかつ軽量に行うソフトとして紹介される。
- Reticoは増分処理システムを構築するためのOSSフレームワークと説明される。
- IU（Incremental Unit）モデルとモジュール間の増分処理の流れが解説されている。
- サンプルコードでマイク/スピーカーやASR→LLM→TTSの増分パイプラインが示される。
- uvでretico-coreを導入し動作確認する手順と出力が記載されている。
- 依存関係の衝突やメンテナンスの古さが課題として挙げられている。

### Key Findings
- MaAIがReticoに統合されたことが共有されている。 [^]
  - Footnote: 「MaAI is now integrated with retico」
- MaAIはターンテイキング・相槌・頷きをリアルタイムかつ連続的に予測する非言語行動生成ソフトと説明されている。 [^]
  - Footnote: 「ターンテイキング、相槌、頷きをリアルタイムかつ連続的に予測するソフトウェア」
- Reticoは増分処理システム構築のためのオープンソースフレームワークと定義されている。 [^]
  - Footnote: 「増分処理システム（incremental processing system）を構築するためのオープンソースフレームワーク」
- 増分処理の基盤としてIUモデルを採用し、複数モジュールで処理する流れが説明されている。 [^]
  - Footnote: 「増分対話処理の『増分単位モデル』（Incremental Unit）を基盤」
- uvでretico-coreを導入し、pyaudioとretico-coreのバージョンがインストールされたと記録されている。 [^]
  - Footnote: 「+ pyaudio==0.2.14」「+ retico-core==0.2.10」
- retico-coreのバージョン制約が衝突し、依存関係の解決が難しいと述べられている。 [^]
  - Footnote: 「retico-googleasr 1.1.1... depends on retico-core>=2.0.0」「retico-googletts 0.1.3 depends on retico-core~=0.2」

### References
- https://zenn.dev/kun432/scraps/04fdbbb23cb4da

## 「Takumi Guard」を試す
- Date: 2026-03-26T01:38:00+09:00

### Executive Summary
- LiteLLMの特定バージョンにマルウェアが混入したサプライチェーン攻撃が起点になっている。
- 詳細記事を参照しつつTakumi Guardの紹介と検討が進められている。
- Takumi GuardはPyPIとクライアントの間に置くセキュリティプロキシと説明される。
- 新規公開パッケージに72時間の検疫期間を設ける方針が述べられている。
- ダウンロード追跡や感染可能性通知など登録ユーザー向け機能が挙げられている。
- クールダウンはリスク低減に有効だが万能ではなく他の監査と併用すべきと整理している。
- メリット・デメリットを比較し、まずは取れる自衛策を優先すべきと結論づけている。

### Key Findings
- LiteLLMの1.82.7/1.82.8にSSHキーやクラウドクレデンシャルを盗むマルウェアが混入したと警告されている。 [^]
  - Footnote: 「SSHキーやクラウドクレデンシャルをぶっこ抜くマルウェア...1.82.7、1.82.8が影響範囲」
- Takumi GuardのPyPIエンドポイントがGMO Flatt Securityからリリースされたと説明されている。 [^]
  - Footnote: 「筆者が所属する組織（GMO Flatt Security）から、セキュアなレジストリプロキシ Takumi Guard の PyPI エンドポイントをリリース」
- Takumi Guardはpip/uv/poetryとPyPIの間に置くセキュリティプロキシで、悪意あるパッケージをブロックするとされている。 [^]
  - Footnote: 「pip/uv/poetry と PyPI（レジストリ）の間に位置するセキュリティプロキシで、悪意あるパッケージがブロックされます。」
- 新規公開バージョンに72時間の検疫期間を設け、公開直後のインストールを防ぐ方針が示されている。 [^]
  - Footnote: 「72時間の検疫期間」「新規公開バージョンが 72 時間はインストールできない仕組み」
- 機能として悪性パッケージのブロック、ダウンロード追跡、感染可能性通知が列挙されている。 [^]
  - Footnote: 「悪意のあるパッケージのブロック」「ダウンロード追跡」「感染可能性の通知」
- デメリットとして外部依存や情報送信、将来の無料提供が不明点として挙げられている。 [^]
  - Footnote: 「外部依存要因が増える」「外部に少なからず情報が送信」「将来的にも無料で利用できるかは不明」

### References
- https://zenn.dev/kun432/scraps/b52d4907bf3195
