# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-03-13T10:45:45+09:00
- Articles: 3

## gpt-ossの推論を6倍速に。Thinking OFF設定と、Ollamaで効かない理由
- Date: 2026-03-11

### Executive Summary
- gpt-ossの推論時間の大半はanalysisのreasoning tokensに起因する。
- chat_templateのgeneration promptを書き換えるだけでThink OFFにできる。
- Think OFFでgpt-oss:20bが12.4秒/件から2.0秒/件に短縮された。
- llama-serverとSGLangではThink OFFが有効だが、Ollamaでは無効と説明される。
- 速度改善はDecodeが全体の約79%を占めるためトークン削減が効く。
- 精度への影響はタスク依存で、単純抽出は維持できた。
- 多段階推論が必要な分類では精度が大きく低下した。
- explicit CoTで精度は回復するが速度メリットは消える。

### Key Findings
- chat_templateのgeneration promptを1箇所変更するだけでThink OFFが可能と説明されている。 [^]
  - Footnote: 「chat_templateを1箇所書き換えるだけで、gpt-oss:20bの推論が12.4秒から2.0秒に縮みます。」
- Think OFFはllama-serverとSGLangで有効だが、Ollamaでは無効と整理されている。 [^]
  - Footnote: 「llama-serverとSGLangで有効で、Ollamaでは効きません。」
- 推論時間の内訳ではDecodeが約79%で、reasoning tokens削減が最も効くと記載。 [^]
  - Footnote: 「トークン生成のDecodeが全体の79%を占めています。Think OFFにしてreasoningの500〜800 tokensを丸ごと消せば、ここが一気に縮みます。」
- Ollamaのnothinkは実質Think ONで、速度やcompletion_tokensの検証が必要と述べている。 [^]
  - Footnote: 「Ollamaのnothinkは裏でreasoningが動いているので、completion_tokensと速度で検証してから使ってください。」
- 精度はタスク依存で、メタデータ抽出は維持、レビュー分類は20pt低下と報告。 [^]
  - Footnote: 「メタデータ抽出（単純な構造化）…精度維持」「レビューコメント分類…96.5%→76.3%（-20pt）」
- explicit CoTで精度は上がるが、速度はThink ONと同等まで悪化した。 [^]
  - Footnote: 「Think OFF + explicit CoT…精度は76.3%から87.5%に上がりましたが…速度が2.1sから13.4sまで落ちました。Think ONの12.4sとほぼ同じです。」

### References
- https://qiita.com/ntaka329/items/35f156dbe526121e66f5

## 外出先の非力なノートPCで自宅の大型LLMを動かす「LM Link」登場
- Date: 2026-03-13T06:07:00+09:00

### Executive Summary
- LM LinkはLM Studio上のLLMをインターネット越しに使える仕組みとして紹介された。
- 同一LAN外からの利用は通常VPNが必要だが、LM Linkで不要になると説明される。
- lmstudio.aiのアカウントで接続デバイスを管理する方式とされる。
- 通信はTailscale（WireGuard系）で暗号化し、ピアツーピア接続と記載。
- 無料提供で2ユーザー・各5デバイスまでの制限がある。
- LM Studio 0.4.5で新機能として追加され、0.4.6でUIに表示される。
- 軽量ノートから大型モデルを扱える具体例としてQwen3.5-122b-a10bが挙げられる。

### Key Findings
- LM Linkは「LM Studio上のLLMをインターネット越しにリモート利用する仕組み」と定義されている。 [^]
  - Footnote: 「“LM Studio上で動作しているLLMを、インターネット越しでもリモートから使えるようにする仕組み”」
- 同一LAN外からの利用はVPNが必要だが、LM Linkでどこからでもアクセス可能と説明。 [^]
  - Footnote: 「同一LAN上ではないPC…VPNなどを経由しない限り利用は不可能…ところがこのLM Linkを使うと同一LAN上に限らず、どこからでも…アクセスできる」
- アカウント管理はlmstudio.aiで行い、Tailscaleで暗号化されたP2P接続を使うと記載。 [^]
  - Footnote: 「lmstudio.aiにアカウントを作り…Tailscaleを使用…暗号化し、デバイス同士が直接ピアツーピア接続」
- 無料で利用可能だが、2ユーザー・各5デバイスまでで、将来課金オプション予定とされる。 [^]
  - Footnote: 「現在は無料で利用可能…制限は2ユーザー、各5デバイス(計10デバイス)まで。プレビュー終了後、追加の課金オプションを導入予定」
- LM Studio 0.4.5の新機能としてLM Linkが追加されたと明記されている。 [^]
  - Footnote: 「2月26日のバージョン0.4.5の新機能の1つとして、LM Linkがあった。」
- 重いモデルを軽量ノートから使える例としてQwen3.5-122b-a10bのリモート動作が示される。 [^]
  - Footnote: 「試しにQwen3.5-122b-a10bをロードすると…普通のノートPCでは作動不可能…LM Linkを使えば…入力と出力のみローカルPCを使う」

### References
- https://pc.watch.impress.co.jp/docs/column/nishikawa/2092683.html

## ネット詐欺のターゲットは人間ではなく、AIエージェントに？　F-Secureの予測を紹介
- Date: 2026-03-13T06:00:00+09:00

### Executive Summary
- F-Secureの2026年2月レポートを基にAIエージェントが新たな標的になると解説。
- AIエージェントは人間の代理としてファイル操作や予約、金融取引まで行う。
- 詐欺の焦点は人間ではなくAIをだます方向に移行していると指摘。
- AIは文脈的な判断力が弱く、欺瞞やソーシャルエンジニアリングに脆い。
- プロンプトインジェクションやアドバーサリアル攻撃で意思決定が狙われる。
- 重要情報や金融タスクをAIに任せるのは現時点では避けるべきと述べる。
- AIを使った投資詐欺の事例としてOPCOPRO手口が紹介されている。

### Key Findings
- F-SecureのレポートではAIエージェントが2026年の新たな標的になると示される。 [^]
  - Footnote: 「F-Secureが2月に発表したレポート…2026年のサイバー空間では、自律的に判断を下す『AIエージェント』が攻撃の新たな標的になることなどが指摘」
- AIエージェントは人間の代理でPC操作や金融取引まで自律的に行えると説明。 [^]
  - Footnote: 「ファイルの読み書きをはじめ、レストランの予約から金融取引まで、自律的に判断し…サービスと直接やり取りを行うことができる」
- 詐欺の対象が人間からAIに移行しているとF-Secure CEOが述べたと引用。 [^]
  - Footnote: 「『人間をだますことから、人間の代わりに決定を下すAIシステムの方をだますことへ手口が移行した』と…述べています。」
- AIエージェントは文脈判断が弱く、欺瞞を見抜けないと指摘されている。 [^]
  - Footnote: 「現在のAIエージェントには…文脈的な判断力がないのだと、同氏は指摘しています。」
- 攻撃手法としてプロンプトインジェクションやアドバーサリアル攻撃が挙げられる。 [^]
  - Footnote: 「プロンプトで悪意ある指示を行う『プロンプトインジェクション』や、悪意ある例示データでAIをだます『アドバーサリアルアタック』」
- 重要情報や金融関連タスクをAIに任せるのは現時点で控えるべきと結論づけている。 [^]
  - Footnote: 「現時点では、AIエージェントに重要な情報や金融関連のタスクを任せるのは控えるべきでしょう。」
- OPCOPRO手口ではAIとボットで偽のコミュニティを作り投資詐欺に誘導する。 [^]
  - Footnote: 「AIとボットを使って数週間かけて偽のコミュニティを作り上げ…投資に誘います。」

### References
- https://internet.watch.impress.co.jp/docs/column/netliteracy/2091933.html
