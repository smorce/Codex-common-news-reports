# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-24T09:20:26+09:00
- Articles: 3

## LiveKit サーバ を Linux にインストールする
- Date: 2026-03-24T02:57:00+09:00

### Executive Summary
- Mac では Homebrew で簡単に導入できるが、Agents を同時に動かすと負荷が増える。
- SFU 自体より Agents がリソースを消費している可能性に触れている。
- Ubuntu 22.04 + RTX4090 の Linux サーバに移して運用する方針。
- Agents で VAD やターンテイキングモデルも動かすため Linux の方が有利と見ている。
- セルフホストの公式ドキュメントがあり、Mac/Linux/Windows に対応。
- Linux では curl のワンライナーでインストール可能で、既定は /usr/local/bin。
- INSTALL_PATH で配置変更でき、例では /opt/livekit/bin へ導入、--dev は本番非推奨。

### Key Findings
- Mac では Homebrew で簡単に入るが、Agents 同時実行でリソース要求が増える。 [^]
  - Footnote: 「Mac の場合は Homebrew で簡単にインストールできて便利」「Agents がリソースを消費する」
- Ubuntu 22.04 + RTX4090 の Linux サーバで動かす判断をしている。 [^]
  - Footnote: 「Linux サーバ（Ubuntu-22.04+RTX4090） があるので、そちらで動かすことにする」
- セルフホストのドキュメントがあり、Mac/Linux/Windows で導入可能と明記されている。 [^]
  - Footnote: 「セルフホストのドキュメントはこちら。Mac / Linux / Windows でインストールできる。」
- Linux は curl のワンライナーでインストールできる。 [^]
  - Footnote: 「Linux の場合は、curlでワンライナーでインストールできる。」
- 既定のインストール先は /usr/local/bin だが INSTALL_PATH で変更できる。 [^]
  - Footnote: 「デフォルトだと /usr/local/bin にインストール」「INSTALL_PATH で指定できる」

### References
- https://zenn.dev/kun432/scraps/3defcac3187b64

## LiveKit Agents の「EndToolCall」を試す
- Date: 2026-03-24T02:21:00+09:00

### Executive Summary
- LiveKit Agents の古いまとめが陳腐化したため、機能ごとに記録する方針。
- EndCallTool はまだベータ段階だが挙動を確認している。
- EndCallTool は通話を円滑に終了しルームから切断するツールと説明。
- end_call で最終応答→セッション終了、delete_room=True でルーム削除と参加者切断。
- 通常の終了はクライアント主導で、終了判定はエージェント側になる。
- EndCallTool を使えばエージェント側から音声で終了処理を走らせられる。
- 実験では RoomDeleted で切断されるが、プロセス終了にはイベント処理が必要。

### Key Findings
- 1.x まとめは現状に合わなくなったため、機能単位の記録に切り替えている。 [^]
  - Footnote: 「現在はバージョンが進んでもはや意味がないまとめになっていたので、気になった機能などを個別に書くことにした。」
- EndCallTool はベータ機能として扱われている。 [^]
  - Footnote: 「まだベータの機能ではあるけども。」
- EndCallTool は通話終了・切断のためのツールで、後処理やルーム削除/セッション終了を扱える。 [^]
  - Footnote: 「通話を円滑に終了してルームから切断」「自動的に後処理」「オプションでルームの削除やセッションの終了処理」
- end_call 呼び出し後は最終応答生成→セッション終了、delete_room=True ならルーム削除と参加者切断、ジョブ終了。 [^]
  - Footnote: 「最終的な応答を生成」「セッションは自動的に終了」「delete_room が True に設定されている場合、ルームが削除」「ジョブ処理が終了」
- RoomDeleted で切断されるが、クライアントのプロセス終了にはイベント検知が必要。 [^]
  - Footnote: 「disconnected from room with reason: RoomDeleted」「プロセスはそのまま生きている」「ルーム削除イベントを拾って終了」

### References
- https://zenn.dev/kun432/scraps/5b0893850f7873

## プライベートなDiscordサーバーを立てる
- Date: 2026-03-24T01:22:00+09:00

### Executive Summary
- Discord は参加のみだったが、招待制のプライベートサーバを立てたいという目的。
- 左下の「サーバーを追加」から作成を開始し、「オリジナルの作成」を選ぶ。
- サーバー用途の選択があり、種類の説明をドキュメントで確認している。
- サーバータイプはフレンドサーバーとコミュニティサーバーの2種類。
- コミュニティは大規模向けで管理機能や公開性の高い機能がある。
- 用途は招待制の私用なので「自分と友達のため」を選択。
- ロールは @everyone のみが初期状態で、管理者は権限フラグで扱う。

### Key Findings
- プライベートな Discord サーバを立て、設定をまとめていく方針。 [^]
  - Footnote: 「プライベートなDiscordサーバを立てたい。それに関して、設定などまとめていく。」
- 作成手順は「サーバーを追加」→「オリジナルの作成」→用途選択。 [^]
  - Footnote: 「左下から『サーバーを追加』」「『オリジナルの作成』を選択」「次に、サーバーの用途を聞かれる。」
- Discord のサーバータイプはフレンドサーバーとコミュニティサーバーの2種類と整理されている。 [^]
  - Footnote: 「Discordには主に2種類のサーバータイプがあり」
- コミュニティサーバーには多数管理、無期限招待リンク、検索で発見といった機能がある。 [^]
  - Footnote: 「多数のユーザーを管理するための機能」「有効期限なしの招待リンク」「サーバー検索で見つけれる」
- 招待制の私用目的なので「自分と友達のため」を選び、@everyone の権限で運用し招待は無効にする判断。 [^]
  - Footnote: 「招待されたユーザーしか使えないプライベートなものなので、『自分と友達のため』」「@everyone」「招待は無効にしておくほうが良さそう」

### References
- https://zenn.dev/kun432/scraps/a79a293e27d4ca
