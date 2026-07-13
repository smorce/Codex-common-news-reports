# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-13T09:01:43.0747589+09:00
- Articles: 3

## Ubuntu の「snap」を試す

### Executive Summary
- Ubuntu の snap を実際に触りながら、基本概念と操作を確認している。
- snap は Linux ディストリビューションやハードウェア環境に依存しにくい自己完結型パッケージとして説明されている。
- Ubuntu 24.04 では snap が標準で入っており、snap --version や snap list で状態を確認している。
- Markdown 関連パッケージの検索、glow の詳細確認、インストールまでを具体的なコマンド出力付きで記録している。
- VLC を例に、stable や beta のチャネル切り替え、refresh、revert の挙動を試している。
- snap の隔離機能では、connections と connect によりカメラなどの権限接続を確認している。
- 削除時には snap data snapshot が保存され、saved、save、restore による復元系操作にも触れている。

### Key Findings
- snap は自己完結型のアプリケーションパッケージとして、複数の Linux 環境で一貫した配布を狙う仕組みである。 [^]
  - Footnote: 本文に「多様な Linux ディストリビューション間で動作する自己完結型のアプリケーションパッケージ」と記載されている。
- snapd はインストール、隔離環境、アップデート処理を管理する中心コンポーネントである。 [^]
  - Footnote: 本文に「snap デーモン snapd は、インストール、隔離環境の設定、アップデート処理を管理します」とある。
- 検証環境の Ubuntu 24.04 では snap と snapd が標準状態で利用可能だった。 [^]
  - Footnote: 本文に「Ubuntu-24.04でやってみる。snap はデフォルトでインストールされていた」とあり、snap 2.75.2+ubuntu24.04 の出力が示されている。
- snap find では Markdown 関連の多数のパッケージが見つかり、Publisher の記号は信頼度の目安として扱われている。 [^]
  - Footnote: 本文では markdown-editor、onlyoffice、glow などが列挙され、「✓」は認証済みパブリッシャー、「✪」はスター開発者と説明されている。
- snap info は説明、パブリッシャー、ライセンス、チャネルを確認する用途に使える。 [^]
  - Footnote: glow の例で summary、publisher、store-url、license、latest/stable などの channels が表示されている。
- チャネル更新と revert により、VLC の beta 版への更新と以前のリビジョンへの復帰を確認している。 [^]
  - Footnote: 本文に「vlc (beta) 3.0.21-1-74-g47e6c1b726 ... refreshed」および「vlc reverted to 3.0.20-1-g2617de71b6」とある。
- snap の隔離では plug と slot の接続状態を確認し、必要に応じて手動接続する。 [^]
  - Footnote: vlc の camera が未接続の例に続き、sudo snap connect vlc:camera 後に「camera vlc:camera :camera manual」と表示されている。
- snap remove は関連データをスナップショットとして保存する場合がある。 [^]
  - Footnote: 本文に「vlc removed (snap data snapshot saved)」とあり、snap saved の一覧で vlc の snapshot が表示されている。

### References
- https://zenn.dev/kun432/scraps/71c607ec770256

## OpenAI Responses API の「Programmatic Tool Calling」を試す

### Executive Summary
- OpenAI Responses API の Programmatic Tool Calling を公式ドキュメントに沿って整理し、通常の Tool Calling と比較している。
- この機能は、Responses API リクエスト内で JavaScript コードを生成・実行し、複数ツールを連携させるものとして説明されている。
- 予測可能な制御フロー、集計、重複除去、検証など、コードで小さく構造化できる処理に向いている。
- 一方で、単発呼び出し、都度モデル判断が必要な処理、承認が重要な書き込み操作、引用保持には従来の直接的 Tool Calling が適するとしている。
- 実行環境は隔離された V8 ランタイムで、Node.js、直接ネットワーク、汎用ファイルシステム、サブプロセスなどは提供されない。
- クライアント側関数を呼ぶ場合、function_call、function_call_output、caller、call_id を使って停止・再開を繰り返す実装が必要になる。
- ツール設計では小さな JSON、output_schema、冪等性、引数と権限のアプリ側確認、影響の大きい操作の承認が重要だと整理している。

### Key Findings
- Programmatic Tool Calling は Responses API 内でツール呼び出しを連携・実行する JavaScript を生成する仕組みである。 [^]
  - Footnote: 本文に「Responses API リクエスト内でツール呼び出しを連携・実行するための JavaScript コードを生成・実行」とある。
- 複数ツールの並列呼び出し、ループ、条件分岐、中間結果保持が主な用途として整理されている。 [^]
  - Footnote: 本文の「できること」に「プログラムからツールを並列呼び出し」「ループ・条件分岐を使用」「ホスト環境のランタイムに中間結果を保持」とある。
- 実行ランタイムは隔離された V8 であり、一般的な Node.js 実行環境ではない。 [^]
  - Footnote: 本文に「隔離されたV8ランタイム環境が毎回新しく用意」され、「Node.js環境」「パッケージのインストール」「直接的なネットワークアクセス」などは提供されないとある。
- Programmatic Tool Calling は、複数結果の絞り込み、結合、リランキング、重複除去、集計、検証に向く。 [^]
  - Footnote: 本文の比較表で「複数の結果をコードで絞り込み / 結合 / リランキング / 重複除去 / 集計 / 検証」は Programmatic Tool Calling とされている。
- 承認が重要な書き込み操作では、原則として直接的 Tool Calling が適する。 [^]
  - Footnote: 本文に「書き込み操作・承認が重要な操作」は「（原則として）直接的ツール呼び出し」とあり、認可境界を明確に保つためと説明されている。
- クライアント所有ツールでは、プログラムが途中で一時停止し、アプリが関数実行結果を返してから再開する。 [^]
  - Footnote: 本文に、JavaScript が get_inventory に到達して一時停止し、function_call が返り、アプリが function_call_output を返して実行が再開する流れが示されている。
- Programmatic Tool Calling では call_id だけでなく caller も一致させて結果を紐づける必要がある。 [^]
  - Footnote: 本文に「Programmatic Tool Calling の場合はさらに、caller も揃える必要がある」とある。
- 評価では効率だけでなく、最終回答の品質、安全性、失敗時の復旧も見るべきだとしている。 [^]
  - Footnote: 本文に「トークン数やツール呼び出し回数だけで評価するのではなく、求められる最終回答の品質なども重要」とあり、正確性、レイテンシ、コスト、安全性などが列挙されている。

### References
- https://zenn.dev/kun432/scraps/201825ebcae84f

## メモ: GPT-Live

### Executive Summary
- GPT-Live を OpenAI 公式記事ベースで整理し、新しい ChatGPT 音声体験の特徴をまとめている。
- GPT-Live は実際の会話に近い音声モデルとして、全二重アーキテクチャにより聞く・話すを同時に扱う。
- 相槌、素早い応答、静かに待つ挙動など、会話の自然さを高める挙動が重視されている。
- 検索、深い推論、複雑な作業はバックグラウンドで GPT-5.5 などのフロンティアモデルに委任する構成として説明されている。
- 従来のカスケード型やターン制音声モデルの制約に対し、継続的な対話と深い作業の分離で対応する。
- 安全性面では音声特有の評価、レッドチーム、安全応答への誘導、危機支援、10代向け保護が整理されている。
- 提供状況として、iOS、Android、ChatGPT.com で順次展開され、GPT-Live-1 と GPT-Live-1 mini の使い分けが示されている。

### Key Findings
- GPT-Live は人間との自然な会話に近づける新世代の音声モデルとして位置づけられている。 [^]
  - Footnote: 本文に「AI との会話を、実際の会話により近く感じられる新世代の音声モデル」とある。
- 全二重アーキテクチャにより、話しながら聞く、待つ、割り込む、ツールを呼ぶ判断を継続的に行う。 [^]
  - Footnote: 本文に「全二重アーキテクチャが基盤、聞く・話すを同時に行える」および「出力を生成しながら、入力を継続的に処理」とある。
- フロンティアモデルへの委任により、会話を続けながら検索や複雑な推論を進められる。 [^]
  - Footnote: 本文に「検索、推論、よりエージェント的な機能が必要な場合は、GPT‑5.5 のような別のモデルに委任」とある。
- 従来のカスケード型音声システムは、複数モデルの連結により情報欠落や遅延の課題があった。 [^]
  - Footnote: 本文に初代 ChatGPT 音声モードは Speech-to-Text、LLM、Text-to-Speech の 3 モデルを連結し、「モデル間で情報が欠落する」「応答は遅くぎこちない」とある。
- ターン制音声モデルは滑らかさを改善したが、話し終わり待ちや沈黙検出に起因する硬直性が残る。 [^]
  - Footnote: 本文に「モデルが応答する前に、ユーザーが話し終えるのを待つ必要がある」「短い間・背景ノイズがターン終了と誤認され」とある。
- GPT-Live は高度な音声モードより、人間評価や複数ベンチマークで優位とされている。 [^]
  - Footnote: 本文に「GPT‑Live‑1 と GPT‑Live‑1 mini は高度な音声モードよりも強く好まれた」および GPQA、BrowseComp、τ³-Voice Telecom が挙げられている。
- 安全性では音声特有のリスク評価とリアルタイム応答中の安全機能が追加されている。 [^]
  - Footnote: 本文に「音声特有の評価項目を新たに追加」「モデルが応答している最中にも作動可能な安全機能も実装」とある。
- 提供は iOS、Android、ChatGPT.com で順次展開され、プラン別に GPT-Live-1 と mini が使われる。 [^]
  - Footnote: 本文に「iOS、Android、ChatGPT.com で、GPT‑Live をグローバルに順次展開中」「GPT‑Live‑1: Go / Plus / Pro ユーザー向け」「GPT‑Live‑1 mini: Free ユーザー向け」とある。

### References
- https://zenn.dev/kun432/scraps/2aec01b6e299aa
