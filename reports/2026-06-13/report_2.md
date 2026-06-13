# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-06-13T09:04:35.4899679+09:00
- Articles: 3

## Why are cached input tokens cheaper with AI services? - Xe Iaso
- Date: 2026-06-12

### Executive Summary
- この記事は、AI API のキャッシュ済み入力トークンが安くなる理由を、計算量の削減として説明している。
- 長い会話では、過去の system prompt、ユーザー発話、AI 応答、ツール呼び出しが毎回入力に含まれる。
- モデルは通常、会話全体を再処理して次の応答を生成するため、会話が長いほどコストが増える。
- 同じ入力に対する推論は決定的に扱えるため、中間状態を保存する KV cache が有効になる。
- prefix cache により、既に処理済みの会話部分を再計算せず、新しい末尾だけを処理しやすくなる。
- キャッシュはモデル提供者側の時間と計算資源を減らし、その節約が利用者向けの安い料金に反映される。
- アプリ開発では、過去メッセージや推論設定を不用意に変えないことがキャッシュヒット率を高める実務上の要点になる。

### Key Findings
- DeepSeek の例では、cache hit と cache miss の入力単価に大きな差がある。 [^]
  - Footnote: deepseek-chat は cache hit が 100万トークンあたり $0.07、cache miss が $0.27 と示されている。
- 入力トークンの多くがキャッシュされると、利用者は大きなコスト削減を得られる。 [^]
  - Footnote: 記事は「in this case $0.20 per million tokens」として、100万トークンあたり $0.20 の差を例示している。
- 会話型 API では messages 配列が蓄積し、入力全体が肥大化する。 [^]
  - Footnote: 記事は system prompt、user request、AI responses、tool use requests/responses が配列に追加され続けると説明している。
- 長い会話では、モデルが内部状態を毎回再計算するため高コストになる。 [^]
  - Footnote: 記事は会話が長くなるほど、モデルが internal state を再計算する必要があり expensive になると述べている。
- KV caching は同じ入力から得られる中間状態を保存して再利用する仕組みである。 [^]
  - Footnote: 記事は deterministic な推論を前提に、key-value caching で intermediate state を保存して次回使うと説明している。
- 実運用では prefix cache が多く、会話末尾への追加に適している。 [^]
  - Footnote: 記事は多くの場合 cache は prefix cache であり、末尾にメッセージを追加しやすいと述べている。
- キャッシュ活用は料金だけでなく、速度や環境負荷にも影響する。 [^]
  - Footnote: 記事は設定や過去メッセージを変えないことで cache を読みやすくなり、faster、environmental impact reduction、money saving につながるとまとめている。

### References
- https://xeiaso.net/notes/2026/why-llm-cached-token-cheaper/

## MCP連携でOpus 4.8超え、1兆パラメータLLM「Kimi K2.7 Code」無償公開 - PC Watch
- Date: 2026-06-12T21:33:50+09:00

### Executive Summary
- Moonshot AI がコーディング特化のオープンソースエージェント AI モデル「Kimi K2.7 Code」を公開した。
- モデルは総 1 兆パラメータ、アクティブ 320 億パラメータの MoE アーキテクチャを採用している。
- 重みは Modified MIT ライセンスで無償公開され、Hugging Face から入手できる。
- vLLM や SGLang などのローカル推論ツールで使えるほか、Kimi API と Kimi Code からも利用可能である。
- Kimi K2.6 からトークン効率が改善され、推論時のトークン使用量を約 30% 削減した。
- コーディング系ベンチマークと MCP 連携評価で Kimi K2.6 から性能が上がり、MCP Mark Verified では Claude Opus 4.8 を上回った。
- API 料金は入力・出力・キャッシュヒットで分かれ、キャッシュヒット時の入力単価が低く設定されている。

### Key Findings
- Kimi K2.7 Code はコーディング用途に特化したエージェント AI モデルとして提供された。 [^]
  - Footnote: 記事本文は「コーディングに特化したオープンソースのエージェントAIモデル」と説明している。
- モデル規模は総 1 兆パラメータ、アクティブ 320 億パラメータである。 [^]
  - Footnote: 記事は「総パラメータ数1兆でアクティブパラメータ数320億のエキスパート混合モデル(MoE)」と記載している。
- 重みは Modified MIT ライセンスで無償公開されている。 [^]
  - Footnote: 記事は「モデルの重みはModified MITライセンスのもと無償公開」としている。
- ローカル推論環境では Hugging Face からダウンロードし、vLLM や SGLang で利用できる。 [^]
  - Footnote: 記事は Hugging Face からダウンロードして vLLM や SGLang などのローカル推論ツールで利用できると述べている。
- Kimi K2.6 比で推論時のトークン使用量を約 30% 削減した。 [^]
  - Footnote: 記事は「Kimi K2.6と比べて推論時のトークン使用量を約30%削減」と明記している。
- Kimi Code Bench v2 と Program Bench の両方で前世代から改善した。 [^]
  - Footnote: 記事は Kimi Code Bench v2 が 50.9% から 62.0%、Program Bench が 48.3% から 53.6% に向上したと示している。
- MCP 連携評価では Kimi K2.6 と Claude Opus 4.8 を上回った。 [^]
  - Footnote: 記事は MCP Mark Verified が 72.8% から 81.1% に向上し、Claude Opus 4.8 の 76.4% も上回ったと記載している。
- API 料金は入力 100 万トークンあたり 0.95 ドル、出力 100 万トークンあたり 4 ドル、キャッシュヒット時 0.19 ドルである。 [^]
  - Footnote: 記事は Kimi API の料金として、入力 0.95 ドル、出力 4 ドル、キャッシュヒット時 0.19 ドルを挙げている。

### References
- https://pc.watch.impress.co.jp/docs/news/2116913.html

## 無料のAI音楽検出ツールを音楽配信サービスのDeezerがリリース、YouTube MusicやSpotifyなどのプレイリストをスキャン可能 - GIGAZINE
- Date: 2026-06-12T20:00:00+09:00

### Executive Summary
- Deezer が、他サービスのプレイリスト内にある AI 生成音楽を検出できる無料ツールを公開した。
- 対象には YouTube Music、Spotify、Apple Music などのプレイリストが含まれる。
- 生成 AI により高品質な音楽作成が容易になった一方、配信サービス上で大量の AI 生成楽曲が流通している。
- Deezer の調査では、AI 音楽の除外やラベル表示を求めるリスナーが多い。
- 2026 年 4 月時点で Deezer には 1 日約 7 万 5000 曲の AI 生成音楽がアップロードされていた。
- Deezer は AI 生成音楽を検出してタグ付けし、おすすめ掲載から外すことで再生時間比率を抑えている。
- 新ツールは 27 言語に対応し、Tune my music 経由でプレイリストを Deezer に読み込んでスキャンする仕組みである。

### Key Findings
- Deezer は他社サービスのプレイリストも対象にした無料の AI 音楽検出サービスをリリースした。 [^]
  - Footnote: 記事は YouTube Music、Spotify、Apple Music などで作成したプレイリストをスキャンできる無料サービスと説明している。
- AI 生成音楽に対するリスナーの抵抗感は数値として示されている。 [^]
  - Footnote: 2025 年調査では 45% が AI 生成音楽をプラットフォームから除外したい、40% が 100% AI 音楽ならスキップすると回答した。
- 多くのリスナーは AI 製であることの明示を求めている。 [^]
  - Footnote: 記事は 80% が AI 製であることを明示するラベルが必要だと考えていると記載している。
- 主要チャートで AI 生成音楽を人間制作曲と同等に扱うことへの支持は低い。 [^]
  - Footnote: 記事は「主要チャートではAI生成音楽を人間が作った音楽と同等に扱うべき」と回答した人は 11% にとどまったと述べている。
- Deezer では AI 生成音楽のアップロード量が大きな比率を占めている。 [^]
  - Footnote: 2026 年 4 月時点で 1 日約 7 万 5000 曲、1 日のアップロード数の約 44% が AI 生成音楽とされている。
- Deezer は検出・タグ付けとおすすめ除外により、AI 音楽の再生比率を抑えている。 [^]
  - Footnote: 記事は対策により AI 生成音楽が占める再生時間が総再生時間の 1% から 3% 程度に抑えられていると説明している。
- 新ツールは 27 言語と 20 種類の音楽ストリーミングサービスに対応する。 [^]
  - Footnote: 記事は 2026 年 6 月 11 日に 27 言語対応ツールをリリースし、20 種類の音楽ストリーミングサービスのプレイリストを確認できると述べている。
- 利用には Deezer アカウントが必要で、Tune my music を介してプレイリストを読み込む。 [^]
  - Footnote: 記事は Tune my music を使ってプレイリストを Deezer に読み込んでスキャンする仕組みであり、Deezer アカウントが必要だとしている。

### References
- https://gigazine.net/news/20260612-deezer-ai-generated-music-detector/
