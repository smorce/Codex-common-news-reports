# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-02-15T09:01:40+09:00
- Articles: 3

## TP-Link Tapo C210 を Python で操作する
- Date: 2026-02-15T00:15:00+09:00

### Executive Summary
- TP-Link Tapo C210をPythonで操作するためのメモを開始。
- 自分でも試したいとしてカメラを購入した旨を記載。
- RTSPライブストリーミングの公式FAQを参考として挙げている。
- Tapo関連の他事例記事を参照リンクとして整理。
- ONVIF系のPythonライブラリ候補を列挙。
- Python3向けの派生実装にも触れて比較している。
- 最終的に非同期対応のライブラリを試す方針を示した。

### Key Findings
- Tapo C210を購入して試す前提を明示。 [^]
  - Footnote: 買った。Tapo C210というやつ。
- RTSPライブストリーミングの公式FAQを参考にしている。 [^]
  - Footnote: Tapoを使用したRTSPライブストリーミングの利用方法 | TP-Link 日本
- Python向けONVIF実装としてPython2版を挙げている。 [^]
  - Footnote: onvif（ただしPython2向け）
- Python3対応の派生版を候補にしている。 [^]
  - Footnote: python-onvif-zeep（上記のPython−3.0向け）
- 非同期対応版をより良さそうとして試す意向を示す。 [^]
  - Footnote: python-onvif-zeep-async（さらに非同期に対応したもの？）
- 有望と見て試す方針を述べている。 [^]
  - Footnote: ざっと見た感じ、python-onvif-zeep-async が良さそう？とりあえず試してみる。

### References
- https://zenn.dev/kun432/scraps/91312d13f7e79f

## OpenAI の「Shell」ツールを試す
- Date: 2026-02-14T19:13:00+09:00

### Executive Summary
- Responses APIの新しいプリミティブ群に関する引用を紹介。
- サーバーサイド圧縮で長時間エージェント実行を可能にする旨をメモ。
- ネットワーク付きコンテナで制御されたインターネットアクセスを提供と記載。
- Agent Skillsのネイティブサポートやスプレッドシートスキルにも触れている。
- コンテナ外部アクセスはリスクがあるため注意点として記録。
- ShellとCode Interpreterの違い・Usage計上の同一性に疑問を提示。
- 料金が同じ扱いである点とコンテナ料金表を確認している。

### Key Findings
- Responses APIに新しいプリミティブ導入が示されている。 [^]
  - Footnote: Responses API に新しい一連のプリミティブを導入します。
- サーバーサイド圧縮で長時間実行が可能になるとされる。 [^]
  - Footnote: コンテキスト制限に達することなく、数時間にわたるエージェント実行を可能にします。
- ネットワーク付きコンテナで制御されたインターネットアクセスを提供するとある。 [^]
  - Footnote: OpenAI がホストするコンテナに制御されたインターネットアクセスを提供し、ライブラリのインストールやスクリプトの実行を可能にします。
- Agent Skills標準のネイティブサポートとスプレッドシートスキルが言及されている。 [^]
  - Footnote: Agent Skills 標準のネイティブサポートと、最初の実装済みスプレッドシートスキル。
- コンテナからの外部アクセスはリスクがあるため注意点として記載。 [^]
  - Footnote: コンテナから外部へのアクセスはいろいろリスクがあるので注意。
- ShellとCode Interpreterの違いに疑問を示している。 [^]
  - Footnote: Code Interpreterと何が違うんだろうか？
- 料金は同じ扱いと見ている。 [^]
  - Footnote: 料金についてもどうやら同じ扱い
- コンテナ料金例として1GB $0.03/コンテナが示されている。 [^]
  - Footnote: 1 GB（デフォルト）：$0.03/コンテナ

### References
- https://zenn.dev/kun432/scraps/aa55b468ce18fb

## 「Ovis2.6-30B-A3B」を試す
- Date: 2026-02-14T00:26:00+09:00

### Executive Summary
- Ovis2.6-30B-A3Bの情報を試す記録。
- 公式告知前という前置きを明記。
- Alibaba AIDCの最新マルチモーダルLLMと紹介。
- 64Kコンテキストや2880x2880解像度など特徴を列挙。
- MoE 30B/3BアクティブやApache 2.0ライセンスにも触れる。
- 実行結果は遅めだがサンプル程度は動くと評価。
- モデル大型化やGGUF不在によるローカル活用の難しさを指摘。

### Key Findings
- 公式告知がまだ出ていないという前提が書かれている。 [^]
  - Footnote: まだ公式からは告知など出ていないが。
- Alibaba AIDCの最新マルチモーダルLLMとして紹介されている。 [^]
  - Footnote: AlibabaのAIDCチームによる最新のマルチモーダルLLM
- 64Kコンテキストと高解像度が特徴として挙げられている。 [^]
  - Footnote: 64Kコンテキスト + 2880×2880解像度
- MoE 30B/3Bアクティブが特徴として示されている。 [^]
  - Footnote: MoE 30B/3Bアクティブ
- Apache 2.0ライセンスであることが明記されている。 [^]
  - Footnote: Apache 2.0
- 回答は遅めだがサンプル程度なら動作する評価。 [^]
  - Footnote: 回答は2分弱ほどとちょっと遅くなったが、サンプル程度なら動いていそう。
- 日本語は問題なさそうという評価がある。 [^]
  - Footnote: 日本語は問題なさそうね。
- モデルサイズが大きくなっているとの所感が述べられている。 [^]
  - Footnote: モデルサイズがどんどん大きくなっているように思える。
- GGUFがないため量子化が課題という指摘がある。 [^]
  - Footnote: GGUFがないんだよね・・・

### References
- https://zenn.dev/kun432/scraps/f101213f318bb7
