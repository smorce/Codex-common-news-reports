# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-02-14T09:02:13+09:00
- Articles: 3

## OpenAI の「Shell」ツールを試す
- Date: 2026-02-14T03:58:00+09:00

### Executive Summary
- Responses APIに長時間エージェント向けの新プリミティブが導入された。
- サーバーサイド圧縮でコンテキスト制限を超えた長時間実行を狙う。
- ネットワーク付きコンテナで制御されたインターネットアクセスが提供される。
- API内スキルのネイティブサポートとスプレッドシートスキルが示された。
- 「Shell」ツールはモデルにコマンド実行環境を与える。
- 使い方はホスト型コンテナ実行とローカル実行の2種類。
- ShellはResponses API限定で、Chat Completions APIでは使えない。
- ホスト型Shellの環境や制約、プリインストール言語が具体的に列挙された。

### Key Findings
- Responses API向けに長時間エージェント実行の新プリミティブが追加された。 [^]
  - Footnote: 「Responses API に新しい一連のプリミティブを導入」
- サーバーサイド圧縮でコンテキスト制限を回避し長時間実行を可能にする。 [^]
  - Footnote: 「コンテキスト制限に達することなく、数時間にわたるエージェント実行を可能にします。」
- ネットワーク付きコンテナでOpenAIホストの環境に制御されたインターネットアクセスが提供される。 [^]
  - Footnote: 「OpenAI がホストするコンテナに制御されたインターネットアクセスを提供」
- API内スキルとしてAgent Skills標準とスプレッドシートスキルが言及された。 [^]
  - Footnote: 「Agent Skills 標準のネイティブサポートと、最初の実装済みスプレッドシートスキル。」
- Shellツールはモデルにコマンド実行環境を与えると説明されている。 [^]
  - Footnote: 「『Shell』ツールは、モデルにコマンド実行環境を与える」
- Shellの利用形態はホスト型コンテナ実行とローカル実行の2種類。 [^]
  - Footnote: 「2種類の使い方がある。」「OpenAIが提供するホスト型コンテナ上で実行」「ローカルで実行」
- ShellはResponses API専用でChat Completions APIでは使えない。 [^]
  - Footnote: 「Responses APIでのみ利用可能、Chat Completions APIでは使えない。」
- ホスト型ShellはDebian 12ベースで/mnt/dataを使い、TTYやsudoは不可。Python/Node/Java/PHP/Ruby/Goがプリインストール。 [^]
  - Footnote: 「Debian 12ベース」「/mnt/data」「インタラクティブなTTYセッション」「sudo」「Python: 3.11」「Node.js: 22.16」「Java: 17.0」「PHP: 8.2」「Ruby: 3.1」「Go: 1.23」

### References
- https://zenn.dev/kun432/scraps/aa55b468ce18fb

## 「Ovis2.6-30B-A3B」を試す
- Date: 2026-02-14T00:26:00+09:00

### Executive Summary
- Ovis2.6-30B-A3BはAlibaba AIDCの最新マルチモーダルLLMとして紹介されている。
- 公式からの告知はまだ出ていないとのコメントがある。
- 仕様として64Kコンテキストと2880×2880解像度が挙げられている。
- MoE 30B/3Bアクティブ構成とApache 2.0ライセンスが明記。
- 「画像で考える」アクティブな視覚推論が特徴として記載。
- 実行サンプルは2分弱で回答し、サンプル程度なら動作したとの所感。
- 日本語は問題なさそうとの評価がある。
- モデルサイズ増大でローカル利用は量子化が必要、GGUF不在を課題視。

### Key Findings
- 公式アナウンスは未確認とされている。 [^]
  - Footnote: 「まだ公式からは告知など出ていない」
- Alibaba AIDCの最新マルチモーダルLLMとして紹介。 [^]
  - Footnote: 「AlibabaのAIDCチームによる最新のマルチモーダルLLM」
- 64Kコンテキストと2880×2880解像度が特徴。 [^]
  - Footnote: 「64Kコンテキスト + 2880×2880解像度」
- MoE 30B/3Bアクティブ構成。 [^]
  - Footnote: 「MoE 30B/3Bアクティブ」
- Apache 2.0ライセンス。 [^]
  - Footnote: 「Apache 2.0」
- 『画像で考える』アクティブ視覚推論が特徴。 [^]
  - Footnote: 「『画像で考える』: アクティブな視覚推論」
- 回答は2分弱でサンプル程度は動作。 [^]
  - Footnote: 「回答は2分弱ほどとちょっと遅くなったが、サンプル程度なら動いていそう。」
- 日本語は問題なさそうとの所感。 [^]
  - Footnote: 「日本語は問題なさそうね。」
- モデルが大きくなり量子化が必要で、GGUFがない点が課題。 [^]
  - Footnote: 「モデルサイズがどんどん大きく」「ローカルで動かすには量子化が必要」「GGUFがない」

### References
- https://zenn.dev/kun432/scraps/f101213f318bb7
- https://huggingface.co/AIDC-AI/Ovis2.6-30B-A3B

## メモ: 生成AIチャットボット向けAmazon DynamoDBデータモデル
- Date: 2026-02-13T13:39:00+09:00

### Executive Summary
- 生成AIチャットボットの会話履歴をDynamoDBに保存するデータモデル設計のメモ。
- 参照元はAWSブログ記事で、やや古いが参考にしたいという立場。
- フレームワークが持つ場合もあるがユースケース次第で独自設計が必要と述べる。
- Diaによる要約で、アクセスパターンの決定が最重要と整理。
- 1アイテム詰め込みは400KB制限とWCUコストで破綻すると説明。
- 会話メタデータとメッセージを垂直分割し、TTLで古い会話を削除。
- 想定API/RPSが列挙され、書き込みが多いワークロードを前提に設計する。
- PKをユーザー、SKでCONV/CHAT/MSG/ULIDを区別する設計例。
- GLM-4.7とCodexでチュートリアル作成を試し、Codexの整理力を評価。

### Key Findings
- DynamoDBでチャット履歴を保存するデータモデル設計についてのメモ。 [^]
  - Footnote: 「LLMチャットボットの会話履歴の永続ストレージとしてDynamoDBを使う場合のデータモデル設計」
- フレームワークで吸収されることもあるが独自設計が必要な場合がある。 [^]
  - Footnote: 「ユースケース次第ではそのまま使えなかったり、独自の設計が必要になったり」
- 要点はアクセスパターンの決定、1アイテム詰め込み回避、垂直分割、TTL。 [^]
  - Footnote: 「アクセスパターンをちゃんと決める」「1アイテムに全部詰め込むとすぐ詰む」「垂直分割」「TTLで古い会話を自動削除」
- アクセスパターンからスキーマ設計を始めるのが重要と明記。 [^]
  - Footnote: 「どんなクエリを投げるか（アクセスパターン）から決めるのが大事」
- 想定APIとRPSが提示され、書き込みが多いワークロード。 [^]
  - Footnote: 「PutMessage: メッセージ追加（ユーザー＆ボット）（書き込み、1000 RPS）」「書き込みがかなり多い」
- 会話を1アイテムにまとめると400KB制限とWCUコストで破綻。 [^]
  - Footnote: 「『会話まるごと1アイテム』は 400KB 制限と WCU コストで破綻する」
- 会話メタデータとメッセージを垂直分割して保存する。 [^]
  - Footnote: 「会話メタデータとメッセージを分けて垂直分割する」
- PKはユーザー、SKはCONVとCHAT#...#MSG#ULIDで区別。 [^]
  - Footnote: 「PK はユーザー」「CONV#」「CHAT#...#MSG#ULID」
- ULIDで一意性と時系列ソート性、TTLで90日後自動削除。 [^]
  - Footnote: 「ULID でメッセージの一意性＋時系列ソート性」「TTL で 90 日後に自動削除」
- GLM-4.7は途中で混乱し、Codexで再整理したとの比較。 [^]
  - Footnote: 「GLM-4.7…途中で…しっちゃかめっちゃか」「Codexに再整理してもらった」

### References
- https://zenn.dev/kun432/scraps/20bbccec8d75ed
- https://aws.amazon.com/jp/blogs/database/amazon-dynamodb-data-models-for-generative-ai-chatbots/
- https://www.diabrowser.com/
