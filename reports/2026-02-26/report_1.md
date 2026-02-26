# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-02-26T09:57:31.2189267+09:00
- Articles: 3

## Alibaba Cloud 「Coding Plan」を試す
- Date: 2026-02-26T00:05:00+09:00

### Executive Summary
- Alibaba Cloud Model Studioの「コーディングプラン」はAIコーディング向けの月額サブスク。
- Qwen CodeやClaude Codeなどのコーディングツールから利用する前提。
- 対応モデルにQwen系とMiniMax/GLM/Kimiなどのサードパーティが含まれる。
- ライト$10/月とプロ$50/月で、月間リクエスト上限が明示されている。
- APIでの自動利用は不可で、コーディングツール限定の利用。
- 上限到達後の従量課金・クレジット追加は不可。
- 契約には決済手段登録と本人確認が必要と書かれている。
- Model Studioのデータ利用・暗号化に関する説明があり、同意なしの学習利用はしないと明記。

### Key Findings
- コーディングプランはModel StudioのAIコーディング向けサブスクリプション。 [^]
  - Footnote: 「コーディングプラン」は、Alibaba Cloud Model Studioが提供するAIコーディングサービスのサブスクリプションプランです。
- Qwen系とサードパーティモデルが利用可能。 [^]
  - Footnote: qwen3.5-plus、qwen3-max-2026-01-23、qwen3-coder-next、qwen3-coder-plus、MiniMax-M2.5、glm-5、glm-4.7、kimi-k2.5
- 月間最大90,000リクエストの上限が提示されている。 [^]
  - Footnote: 月間最大90,000リクエストまで対応可能
- 対応ツールはQwen Code/Claude Code/Cline/OpenClawなど。 [^]
  - Footnote: 対応ツール: Qwen Code、Claude Code、Cline、OpenClawに対応しています。
- ライトプランは$10/月。 [^]
  - Footnote: $10/月
- プロプランは$50/月。 [^]
  - Footnote: $50/月
- API利用は不可でツール経由の利用前提。 [^]
  - Footnote: API利用は不可
- 上限到達後の追加課金はできない。 [^]
  - Footnote: 使用量を使い切っても、従量課金やクレジットでの追加はできない。
- 同意がない限り業務データは学習に使われないと明記。 [^]
  - Footnote: お客様が特に同意を提供されない限り、Alibaba Cloud Model Studioではお客様の業務上のデータをモデルの開発・改善に使用することはありません
- アカウント作成時に決済手段の登録が必須。 [^]
  - Footnote: 決済手段の登録はアカウント作成時に必須（クレカ or PayPal）
- 本人確認資料の提出が必須と記載。 [^]
  - Footnote: 本人確認資料の提出が必須（パスポート or 運転免許証。審査が行われる様子。）

### References
- https://zenn.dev/kun432/scraps/0a8c3645aa39a3

## 「LFM2-24B-A2B」を試す
- Date: 2026-02-25T17:23:00+09:00

### Executive Summary
- Liquid AIのLFM2-24B-A2Bリリース情報を試したメモ。
- 総パラメータ24Bで、トークンあたりアクティブ2.3BのMoE構成。
- 高速・メモリ効率設計にMoEを組み合わせたと説明。
- LFM2-350Mから24Bまでのファミリー拡張で品質向上を主張。
- 32GB RAMに収まる設計でコンシューマー機での実行を想定。
- 深さ増加やエキスパート倍増などスケーリング詳細が示される。
- アクティブパラメータ増加は約1.5倍と記載。
- 著者の印象では日本語自体は問題ないが知識面は限定的。

### Key Findings
- LFM2-24B-A2Bが最大モデルとしてリリースされた。 [^]
  - Footnote: 本日、当社最大のLFM2モデル「LFM2-24B-A2B」をリリースします
- 総パラメータは24B。 [^]
  - Footnote: 総パラメータ数24B
- トークンあたりアクティブ2.3B。 [^]
  - Footnote: トークンあたりアクティブ2.3B
- MoEにより実行ごとの活性パラメータは2.3Bに抑えられる。 [^]
  - Footnote: Mixture of Experts構成を組み合わせることで、実行ごとにわずか2.3Bのパラメータのみが活性化します。
- LFM2ファミリーは350Mから24Bまで拡張された。 [^]
  - Footnote: LFM2ファミリーはほぼ2桁の規模に広がりました：LFM2-350MからLFM2-24B-A2Bまで。
- 32GB RAMでコンシューマー機での実行を想定。 [^]
  - Footnote: 32 GBのRAMに収まるよう設計されており、統合グラフィックスプロセッサ（iGPU）および専用ニューラル処理ユニット（NPU）を搭載したコンシューマー向けラップトップやデスクトップで実行可能にしています。
- 24→40層とエキスパート32→64でスケーリング。 [^]
  - Footnote: LFM2-24B-A2B を深くする（24→40 層）ことでスケーリングし、MoE ブロックごとにエキスパートを倍増（32→64）
- アクティブパラメータは1.5B→2.3Bに増加。 [^]
  - Footnote: アクティブパラメータ数は約 1.5 倍に増加（1.5B→2.3B）
- 日本語の知識は十分でないとの印象が示されている。 [^]
  - Footnote: 日本語自体は問題ないのだけど、24Bだけど日本・日本語の知識はそこまでないかなぁ。

### References
- https://zenn.dev/kun432/scraps/d286fc3299f8c1

## メモ: Dockerのネットワークについて（iptablesとか）
- Date: 2026-02-25T12:40:00+09:00

### Executive Summary
- OpenClawを安全に試すためDockerとiptables周りを整理したメモ。
- ホストOSはUbuntu 24.04を想定。
- nftablesより情報量の多いiptablesでまず理解する方針。
- filter/natテーブルと各チェーンの役割、パケット経路を整理。
- ufw/iptables/nftはいずれもnf_tablesに収束する関係を解説。
- ツール併用は非推奨で、混在するとルールが見えにくいと注意。
- Docker導入でdocker0やvethが増え、iptablesチェーンが追加される。
- OpenClaw向けにDOCKER-USERで通信制限を入れる案を提示。

### Key Findings
- OpenClawを安全に試すためにネットワーク制御を検討している。 [^]
  - Footnote: OpenClaw的なものを安全に試したい、ということで、VMやDockerを駆使しつつ、かつネットワークも制御して、ということを考えた。
- ホストOSはUbuntu 24.04を前提としている。 [^]
  - Footnote: なお、ホストOSは Ubuntu-24.04 を想定。
- 当面はiptablesで理解を進める方針。 [^]
  - Footnote: iptables のほうが情報量が多いので、一旦そちらで。
- filterテーブルはパケットの許可/拒否を判断する。 [^]
  - Footnote: filterテーブル: パケットの許可/拒否を判断
- natテーブルはアドレス変換を行う。 [^]
  - Footnote: natテーブル: アドレス変換
- ufw/iptables/nftはnf_tablesを操作する関係にある。 [^]
  - Footnote: ufw / iptables / nft はすべて最終的にカーネル内の nf_tables を操作する。Ubuntu 24.04 では iptables コマンドの実体は iptables-nft（nf_tables バックエンド）。
- ツールの併用は避けて統一するのが望ましい。 [^]
  - Footnote: ツールの併用には注意が必要。統一するのが望ましい。
- Docker導入でdocker0ブリッジが追加される。 [^]
  - Footnote: docker0 のブリッジが追加される。
- Dockerのフィルタを追加するならDOCKER-USERが推奨されている。 [^]
  - Footnote: DOCKER-USER にルールを追加すればいいみたい。
- OpenClawコンテナからLiteLLMコンテナへのアクセスは許可する案。 [^]
  - Footnote: OpenClaw コンテナから LiteLLMコンテナへのアクセスを許可
- OpenClawコンテナからLAN内へのアクセスは拒否する案。 [^]
  - Footnote: OpenClaw コンテナから LANへのアクセスを拒否

### References
- https://zenn.dev/kun432/scraps/1551c3bd980c15
