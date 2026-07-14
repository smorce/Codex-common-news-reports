# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-14T09:01:46+09:00
- Articles: 3

## 「AnimeGen」を試す
- Date: 2026-07-14T00:00:00+09:00

### Executive Summary
- AnimeGen の Text-to-Video と Image-to-Video を試したスクラップである。
- モデルカードは日本語版が用意され、デモも複数提示されている。
- 対象モデルには Text-to-Video、Image-to-Video、Frame Interpolation が含まれる。
- ライセンスはいずれも Apache-2.0 と記録されている。
- Ubuntu 22.04 と RTX 4090 の環境で Text-to-Video を検証している。
- uv で Python 3.12 環境を作り、torch、diffusers、transformers などを導入している。
- AnimeGen-T2V のモデルファイルは 60GB 強あり、初回準備に時間がかかる。
- 832x480、5 秒、16fps 相当の設定ではモデル取得を除き約 3 分で生成できた。
- VRAM 使用量は約 23GB とされ、RTX 4090 でも余裕は小さい。

### Key Findings
- AnimeGen は動画生成系として Text-to-Video と Image-to-Video のモデルを提供している。 [^]
  - Footnote: 本文に「モデル」「Text-to-Video」「Image-to-Video」とあり、それぞれ日本語版モデルカードが用意されていると記載されている。
- Frame Interpolation も対象機能として触れられている。 [^]
  - Footnote: 本文に「Frame Interpolation（画像と画像の間を生成するフレーム補間）」とある。
- ライセンスは Apache-2.0 と整理されている。 [^]
  - Footnote: 本文に「どちらも Apache−2.0ライセンス」と記載されている。
- 検証環境は Ubuntu 22.04 と RTX 4090 である。 [^]
  - Footnote: 本文に「Ubuntu-22.04 + RTX4090 で試す。」とある。
- 実行には大容量モデルの事前取得が必要である。 [^]
  - Footnote: 本文に「モデルをダウンロード。60GB強あるので気長に待つ。」と記載されている。
- 生成時間は設定次第で数分規模だが、VRAM 消費は大きい。 [^]
  - Footnote: 本文に「上記の設定で3分ぐらいで生成される。VRAMは23GBぐらい使う」とある。

### References
- https://zenn.dev/kun432/scraps/8f111401d4fe87

## 日本語テキストをひらがな・カタカナに変換する（Python）
- Date: 2026-07-13T00:00:00+09:00

### Executive Summary
- 日本語テキストから読みを取得し、ひらがな・カタカナへ変換する方法を比較している。
- 形態素解析ライブラリを使えば、多くの場合で読み取得は可能だと整理している。
- 候補として Sudachi、Mecab、fugashi、Janome、Vibrato が挙げられている。
- 用途特化のライブラリとして pykakasi と kanjiconv にも触れている。
- 精度は最終的に利用する日本語辞書へ依存しそうだと述べている。
- kanjiconv は Sudachi ベースで、UniDic やカスタム辞書も使える可能性がある。
- Sudachi 単体でも reading_form によってカタカナ読みを取得できる。
- Vibrato は軽量辞書だと発音寄りになり、要件によっては読み用途に合わない可能性がある。
- 筆者の用途では依存を増やさず Sudachi 単体でよいとの結論である。

### Key Findings
- 主題は日本語テキストから読みを得ることである。 [^]
  - Footnote: 本文冒頭に「つまり、日本語テキストから読みを得る。」とある。
- 汎用的には形態素解析ライブラリで実現できると見ている。 [^]
  - Footnote: 本文に「基本的に、形態素解析ライブラリを使えば、どれでもできるはず。」と記載されている。
- 変換精度は辞書に依存する可能性が高い。 [^]
  - Footnote: 本文に「どの場合でも結局は日本語辞書を使っているので、精度については日本語辞書に依存しそう。」とある。
- kanjiconv は Sudachi ベースで辞書差し替えやカスタム辞書に対応する選択肢である。 [^]
  - Footnote: 本文に「基本はSudachiベースで、UniDicに差し替えたり、カスタム辞書も使えるらしい。」とある。
- Vibrato の軽量辞書は発音寄りの出力になる場合がある。 [^]
  - Footnote: 本文に「読みじゃなくて発音に特化（『う』が『ー』になったり、『は』が『ワ』になったり）」と記載されている。
- 最終判断として、筆者の用途では Sudachi 単体が適している。 [^]
  - Footnote: 本文に「自分の用途的には、sudachi単体でよいかな。依存を増やさなくて済むし。」とある。

### References
- https://zenn.dev/kun432/scraps/2623d030baddcd

## Ubuntu の「snap」を試す
- Date: 2026-07-11T00:00:00+09:00

### Executive Summary
- Ubuntu の snap を初めて試し、基本概念から操作まで確認している。
- snap は複数の Linux ディストリビューションで動く自己完結型パッケージとして説明されている。
- snapd がインストール、隔離環境、アップデート処理を管理する。
- Ubuntu 24.04 では snap がデフォルトで入っており、snap --version で確認している。
- snap find で Markdown 関連パッケージを検索し、Publisher 記号の意味も整理している。
- glow を例に snap info、install、list、which、snap run の挙動を確認している。
- snap はデフォルトで自動更新され、refresh のタイミングや hold/unhold を設定できる。
- vlc を例にチャネル変更、refresh、revert、revision 指定の挙動を試している。
- snap には隔離の概念があり、アプリがアクセスできるリソース範囲を制御する仕組みがある。

### Key Findings
- snap は自己完結型の Linux アプリケーションパッケージである。 [^]
  - Footnote: 本文に「snap は、組み込みデバイスからデスクトップ、サーバー、クラウド環境に至るまで、多様な Linux ディストリビューション間で動作する自己完結型のアプリケーションパッケージ」とある。
- snapd はインストール、隔離環境、更新処理を担当する。 [^]
  - Footnote: 本文に「snap デーモン snapd は、インストール、隔離環境の設定、アップデート処理を管理します。」と記載されている。
- Ubuntu 24.04 では snap が最初から利用可能だった。 [^]
  - Footnote: 本文に「Ubuntu-24.04でやってみる。snap はデフォルトでインストールされていた。」とある。
- Publisher の記号は信頼度の目安だが、安全監査済みを意味するものではない。 [^]
  - Footnote: 本文に「Canonical / Snap Store の確認・審査によるもの」「そのパッケージが安全に監査された、ということではないよう」とある。
- snap の更新は自動で行われ、refresh や hold で制御できる。 [^]
  - Footnote: 本文に「snap は自動的に更新され、デフォルトでは snapd デーモンが1日4回更新をチェックします。」とあり、hold/unhold の例も示されている。
- revert は過去に取得済みのリビジョンへ戻す用途として確認されている。 [^]
  - Footnote: 本文に「過去にアップデートしたことがある、のが条件っぽく思える」「snap revert vlc」の実行例がある。
- snap パッケージは隔離とアクセス制御の概念を持つ。 [^]
  - Footnote: 本文に「snapパッケージにはサンドボックスのような『隔離』の概念がある。」と記載されている。

### References
- https://zenn.dev/kun432/scraps/71c607ec770256
