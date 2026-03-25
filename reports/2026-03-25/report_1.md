# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-25T09:06:15+09:00
- Articles: 3

## OpenClawクローン「nanobot」を試す
- Date: 2026-03-25T02:37:00+09:00

### Executive Summary
- OpenClaw流行時に、セキュリティ面も含めてクローン調査を始めた。
- 判断のためにまず本家OpenClawを試す方針を取った。
- OpenClawは規模が大きく、追従やメンテが大変という所感。
- TypeScript製である点もネックとして挙げている。
- 軽量なPython製クローンとして「nanobot」を試用対象に選定。
- nanobotの開発元HKUDSはLightRAGの開発元でもあると記述。
- CLIリファレンスが提示され、主要コマンド群が列挙されている。
- スクラップ内には関連スクラップへのリンクも埋め込まれている。

### Key Findings
- OpenClaw流行とセキュリティ議論を受け、クローン調査を開始。 [^]
  - Footnote: 「OpenClawが流行りだした頃に、セキュリティなどの話もあって、OpenClawクローンなプロジェクトを色々調べた。」
- 本家OpenClawを先に試す判断を明記。 [^]
  - Footnote: 「本家を一度試してから判断するほうがいいかな、ということでOpenClawを試した。」
- OpenClawは大きすぎてキャッチアップやメンテが大変との評価。 [^]
  - Footnote: 「OpenClawはちょっと大きすぎてキャッチアップするのもメンテするのも大変、という感じ。」
- TypeScript製で慣れていない点がネック。 [^]
  - Footnote: 「自分があまり慣れていないTypeScript製っていうのもネック。」
- Python製で軽量を謳うnanobotを試す方針。 [^]
  - Footnote: 「Python製でかつ軽量を謳っている「nanobot」を試してみる。」
- nanobot開発元HKUDSはLightRAGの開発元でもあると説明。 [^]
  - Footnote: 「nanobotの開発元である「HKUDS」...過去に試したGraphRAGの軽量な実装「LightRAG」の開発元でもある。」
- CLIの主要コマンドとしてonboard等が示されている。 [^]
  - Footnote: 「onboard   Initialize nanobot configuration and workspace.」

### References
- https://zenn.dev/kun432/scraps/1209c2ad491647

## 音素変換の実装いろいろ
- Date: 2026-03-24T12:33:00+09:00

### Executive Summary
- 音素変換に関する実装のインデックス的まとめとして作成。
- 「音声から音素」「テキストから音素」の2カテゴリを明示。
- 各カテゴリに関連スクラップや外部リンクが並ぶ。
- VoPhoなど過去に試したものを再掲している。
- Wav2Vec2Phonemeなど音声→音素系の参照も含む。
- 筆者は試したことを忘れていた旨を追記。
- 新しいものを見つけたら更新する方針を明記。

### Key Findings
- 音素変換実装のインデックスとしての位置づけ。 [^]
  - Footnote: 「音素への変換に関する実装、過去いろいろ試しているので、インデックス的まとめ」
- カテゴリとして「音声から音素」を明示。 [^]
  - Footnote: 「音声から音素」
- カテゴリとして「テキストから音素」を明示。 [^]
  - Footnote: 「テキストから音素」
- VoPhoは過去に試したが忘れていた旨を記載。 [^]
  - Footnote: 「すっかり試したことを忘れていた」
- 新規発見や試行があれば更新する方針。 [^]
  - Footnote: 「違うものを見つけたり、試したりしたら更新する。」
- VoPhoが具体的な項目として列挙されている。 [^]
  - Footnote: 「VoPho」
- Wav2Vec2Phonemeが具体的な項目として列挙されている。 [^]
  - Footnote: 「Wav2Vec2Phoneme」

### References
- https://zenn.dev/kun432/scraps/b2d78204db29d6

## LiveKit サーバ を Linux にインストールする
- Date: 2026-03-24T02:57:00+09:00

### Executive Summary
- MacではHomebrewで容易に導入できるが、Agents同時稼働でリソースが必要。
- SFU自体は重くなく、主にAgentsがリソースを消費すると述べる。
- 余裕のあるLinuxサーバ（Ubuntu-22.04+RTX4090）で動かす方針。
- Agents側でVADやターンテイキングモデルも動かす前提を示す。
- セルフホストのドキュメント参照とOS別インストール可を明記。
- Linuxはcurlのワンライナーでインストール可能。
- スクリプトはGitHub Releasesから最新TARを取得し/usr/local/binに導入。
- INSTALL_PATHでパス変更でき、/opt/livekit/bin例を提示。
- インストール結果としてlivekit 1.10.0やバイナリ配置を確認。
- 開発用--devは固定キーになるため本番不可、--config運用推奨。

### Key Findings
- MacはHomebrewで簡単だが、Agents同時稼働でリソースを要求。 [^]
  - Footnote: 「Mac の場合は Homebrew で簡単にインストールできて便利なのだけど、Agentsなども同時に動かすとなると、それなりにリソースを要求される」
- SFU自体よりもAgentsがリソース消費の主因と推測。 [^]
  - Footnote: 「実際には、SFU自体はそうでもなくて、Agents がリソースを消費するのだと思う。」
- Ubuntu-22.04+RTX4090のLinuxサーバで動かす方針。 [^]
  - Footnote: 「リソースに余裕のある Linux サーバ（Ubuntu-22.04+RTX4090） があるので、そちらで動かすことにする。」
- AgentsでVADやターンテイキングモデルを動かす前提。 [^]
  - Footnote: 「AgentsではVADやターンテイキングモデルなども動かしたりするので、おそらくそちらのほうが有利なはず。」
- セルフホストのドキュメントがあり、Mac/Linux/Windowsに対応。 [^]
  - Footnote: 「セルフホストのドキュメントはこちら。Mac / Linux / Windows でインストールできる。」
- Linuxはcurlのワンライナーでインストール可能。 [^]
  - Footnote: 「Linux の場合は、curlでワンライナーでインストールできる。」
- インストールスクリプトはGitHub Releasesから最新TARを取得し/usr/local/binに入れる。 [^]
  - Footnote: 「GitHub レポジトリの Releases から 最新バージョンのTAR アーカイブを持ってきて、デフォルトだと /usr/local/bin にインストールされる様子。」
- INSTALL_PATHでインストール先を変更可能で、/opt/livekit/binの例が示される。 [^]
  - Footnote: 「INSTALL_PATH で指定できるようなので、例えばこんな感じで指定すれば他の場所にインストールできる」
- インストール結果としてlivekit 1.10.0が導入される例を示す。 [^]
  - Footnote: 「Installing livekit 1.10.0」
- --devは開発・検証用で固定キーになるため本番では使わない。 [^]
  - Footnote: 「--dev は開発時や検証時のモードで、APIキーやAPIシークレットが固定になる。当然本番環境などでは使用しない。」

### References
- https://zenn.dev/kun432/scraps/3defcac3187b64
