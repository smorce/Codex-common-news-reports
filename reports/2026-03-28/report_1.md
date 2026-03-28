# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-28T10:51:47+09:00
- Articles: 3

## 増分処理フレームワーク「Retico」を試す

### Executive Summary
- MaAIというVAP実装をReticoに統合した話題を起点に調査している。
- MaAIはターンテイキングや相槌、頷きをリアルタイムに予測する点が特徴。
- Reticoは増分処理システム向けのオープンソースフレームワークとして説明される。
- 入力を単語など小さな単位で処理する増分処理の概念を再確認している。
- IUを基盤に複数モジュールを連結する構成で全体像を理解した。
- サンプルコードを通じてモジュールの購読チェーンの感触を掴んでいる。
- 依存関係の競合など運用面の難しさも感じた内容である。

### Key Findings
- MaAIはリアルタイムでターンテイキング・相槌・頷きを予測し、複数言語とCPU動作に対応する。 [^]
  - Footnote: 「MaAI は（１）ターンテイキング、（２）相槌、（３）頷き をリアルタイムかつ連続的に予測」「日本語・英語・中国語に対応」「CPUのみでも高速に動作」
- Reticoは増分処理システム構築のためのオープンソースフレームワークとして紹介されている。 [^]
  - Footnote: 「Retico は、最先端の増分処理システム（incremental processing system）を構築するためのオープンソースフレームワーク」
- 増分処理は入力を微細な単位で処理し、人間の会話に近いタイミングで理解や応答を進めるとされる。 [^]
  - Footnote: 「システムが入力データを微細な単位（通常は単語単位）で処理することを意味します」
- IUモデルを基盤に、ASRや言語理解、対話管理、TTSなどのモジュール間で情報単位をやり取りする。 [^]
  - Footnote: 「増分対話処理の『増分単位モデル（Incremental Unit）』を基盤」「音声認識モジュール、言語理解モジュール、対話管理モジュール、自然言語生成モジュール、音声合成モジュール」
- サンプルではMicrophoneModuleからTTSまでをsubscribeで接続し、runで動かす構成が示されている。 [^]
  - Footnote: 「m1 = MicrophoneModule()」「m2 = Wav2VecModule()」「m3 = TextDispatcherModule()」「m4 = GoogleTTSModule」「m1.subscribe(m2) ... run(m1)」
- retico-core周りで依存関係の競合が発生し、解決が難しいと記述されている。 [^]
  - Footnote: 「retico-googleasr 1.1.1.dev6... depends on retico-core>=2.0.0」「retico-googletts 0.1.3 depends on retico-core~=0.2」「これ解決できないよねぇ」

### References
- https://zenn.dev/kun432/scraps/04fdbbb23cb4da

## 「Takumi Guard」を試す

### Executive Summary
- LiteLLMのサプライチェーン攻撃を受け、Takumi Guardの有効性を確認している。
- Trivy侵害から連鎖した攻撃に対し、自衛策の必要性を強調している。
- Takumi GuardはPyPIプロキシとして悪意あるパッケージをブロックする。
- 新規公開版に72時間の検疫期間を設ける点が特徴とされる。
- pipやuvで使うためにPIP_INDEX_URLとUV_INDEX_URLを設定する。
- tf-nightly-cpuの検証で検疫によるバージョン固定が確認できた。
- uv add時のindex反映やpipのクールダウン事情にも触れている。

### Key Findings
- LiteLLMのマルウェア混入はTrivy侵害からKICS、LiteLLMへ波及した連鎖攻撃の文脈で語られている。 [^]
  - Footnote: 「Trivy侵害から始まったTeamPCPの連鎖攻撃は、KICS、そしてLiteLLMへと波及」
- Takumi GuardはGMO Flatt Security提供のレジストリプロキシで、悪意パッケージのブロックと通知機能を持つ。 [^]
  - Footnote: 「GMO Flatt Security）から、セキュアなレジストリプロキシ Takumi Guard の PyPI エンドポイント」「悪意あるパッケージがブロック」「後日の通知を行う仕組み」
- 新規公開バージョンに72時間の検疫期間を設ける設計が採用されている。 [^]
  - Footnote: 「72時間の検疫期間を設けています。新規公開バージョンが 72 時間はインストールできない」
- Python側はPIP_INDEX_URLとUV_INDEX_URLを設定するとTakumi Guard経由になる。 [^]
  - Footnote: 「export PIP_INDEX_URL=https://pypi.flatt.tech/simple/」「export UV_INDEX_URL=https://pypi.flatt.tech/simple/」
- 検証ではTakumi Guard経由だとtf-nightly-cpuが3日前の版になり、解除すると最新版が入る。 [^]
  - Footnote: 「Would install ... tf_nightly_cpu-2.22.0.dev20260322」「Takumi Guardなし... tf_nightly_cpu-2.22.0.dev20260325」
- uv addではインデックスURLがpyproject.tomlに残らないためdefault-index設定が必要と示される。 [^]
  - Footnote: 「Indexes specified via `--index-url` will not be persisted to the `pyproject.toml` file; use `--default-index` instead」
- pip 26.0で--uploaded-prior-toが追加されたが絶対指定のみで、OS標準pipでは未対応例がある。 [^]
  - Footnote: 「pip-26.0 から --uploaded-prior-to」「日付は『絶対指定のみ』」「python3-pip... 24.0... 対応していなかった」

### References
- https://zenn.dev/kun432/scraps/b52d4907bf3195

## 「hf-mount」を試す

### Executive Summary
- hf-mountでHugging FaceのバケットやリポジトリをローカルFSとして扱う。
- ダウンロード不要で遅延取得し、大きなストレージをマウント可能とされる。
- NFSとFUSEのバックエンドがあり、NFSが推奨されている。
- 用途と不向き用途が明確に整理され、強い一貫性は期待できない。
- インストールはinstall.shでバイナリ取得する簡易方式。
- バケットをHF_TOKENでマウントし、読み書きや遅延ロードを確認した。
- リポジトリは読み取り専用で、llama.cppからモデルを試している。

### Key Findings
- hf-mountはHugging Faceのバケットやリポジトリをローカルファイルシステムとしてマウントする。 [^]
  - Footnote: 「Hugging Face のストレージバケットとリポジトリをローカルファイルシステムとしてマウントします」
- NFSが推奨でルート不要、FUSEはより緊密だがmacOSでは権限やmacFUSEが必要とされる。 [^]
  - Footnote: 「NFS（推奨） -- あらゆる環境で動作し、ルート権限やカーネル拡張は不要」「FUSE -- ... macOS ではルート権限またはmacFUSEが必要」
- 強い一貫性はなく、ポーリングによる最終的整合性で、ファイルが最大10秒古くなる可能性がある。 [^]
  - Footnote: 「最終的な整合性を提供」「すべての鮮度保持はクライアント側のポーリング」「ファイルが最大10秒間古くなる可能性」
- 汎用NFSや遅延に敏感なランダムI/O、強い一貫性が必要なワークロードには不向きとされる。 [^]
  - Footnote: 「汎用的なネットワークファイルシステムとしての使用」「遅延に敏感なランダム I/O 操作」「強い一貫性が求められるワークロード」
- install.shはアーキテクチャ判別後に3つのバイナリを取得し$HOME/.local/binへ配置する。 [^]
  - Footnote: 「アーキテクチャを判別」「3コマンド（hf-mount、hf-mount-nfs、hf-mount-fuse）の最新版を取得」「$HOME/.local/bin（デフォルト）に配置」
- バケットのマウントにはHF_TOKENが必要で、デーモン起動とログ出力が示される。 [^]
  - Footnote: 「HF_TOKEN を環境変数」「hf-mount start bucket kun432/hf-mount-test」「Starting daemon (pid=...) ready」
- リポジトリは読み込み専用としてマウントし、hf-mount start repoでモデル群を参照している。 [^]
  - Footnote: 「リポジトリのマウント。こちらはバケットと異なり、読み込み専用」「hf-mount start repo unsloth/Qwen3.5-0.8B-GGUF」

### References
- https://zenn.dev/kun432/scraps/5299232ff623dc
