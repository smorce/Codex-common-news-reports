# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-22T09:01:52+09:00
- Articles: 3

## 「Agents-A1」を試す（4B）

### Executive Summary
- Agents-A1 の 4B モデル公開を受け、モデルカードや関連情報を確認している。
- Agents-A1 は長期探索、科学研究、指示追従、ツール呼び出しを重視したエージェント型モデルとして紹介されている。
- 4B Dense と 35B-A3B MoE の両系統があり、BF16、FP8、GGUF など複数形式が用意されている。
- 4B 版は小規模ながら BrowseComp、GAIA、IFEval などで高い評価値を示している。
- 筆者は Mac の llama.cpp で 4B GGUF Q8_0 を試し、推奨サンプリングパラメータを確認している。
- 実行ログ上は text、vision、video の modalities が表示され、視覚入力にも対応している様子がある。
- 一方で出力例ではキャラクター名の混乱などが見られ、実利用では応答品質の確認が必要とされる。
- 開発元 InternScience と InternLM、OpenGVLab など上海AI研究所系組織の関係性には筆者が疑問を残している。

### Key Findings
- Agents-A1 は長期タスク向けのエージェント型モデルとして位置付けられている。 [^]
  - Footnote: 記事では「検索、エンジニアリング、科学研究、指示追従、ツール呼び出しにわたる長期的タスク向けに構築された、35B MoE エージェント型モデル」と紹介されている。
- 4B モデルは 2026年7月14日にリリースされたとされる。 [^]
  - Footnote: モデルカード抜粋の最新情報に「2026年7月14日: 4Bモデルをリリースしました」とある。
- 配布形態は 35B-A3B MoE と 4B Dense の両方で、量子化形式も含まれる。 [^]
  - Footnote: 記事には「35B-A3B MoE BF16 FP8 GGUF」と「4B Dense BF16 FP8 GGUF」のバリエーションが列挙されている。
- 4B 版は長期検索や指示追従など複数ベンチマークで同規模モデルを上回る値が示されている。 [^]
  - Footnote: 性能評価で BrowseComp 66.8、XBench-DS-2510 90.0、GAIA 95.1、IFEval 94.8 が挙げられている。
- ツール利用と関数呼び出しはモデルの主な特徴として扱われている。 [^]
  - Footnote: 主な特徴に「関数呼び出し機能とツール統合機能を標準搭載」とあり、API、コードインタープリタ、検索エンジンとの連携が説明されている。
- 筆者は Mac M2 Pro 上で 4B GGUF Q8_0 を llama.cpp から試している。 [^]
  - Footnote: 記事には「今回は Mac（M2 Pro）で、4B GGUF Q8_0 を試してみる」とあり、llama-cli の実行例が掲載されている。
- 推奨パラメータとして temperature 0.85、top_p 0.95、top_k 20 などが示されている。 [^]
  - Footnote: 推奨サンプリングパラメータ欄に temperature: 0.85、top_p: 0.95、top_k: 20、presence_penalty: 1.1 などが列挙されている。
- 実行ログでは text、vision、video の modality が表示されている。 [^]
  - Footnote: llama-cli の出力に「modalities : text, vision, video」とあり、筆者も「Visionにも対応している様子」と書いている。

### References
- https://zenn.dev/kun432/scraps/c070bfe51ac731
- https://huggingface.co/InternScience/Agents-A1-4B
- https://huggingface.co/InternScience/Agents-A1-4B-Q8_0-GGUF

## 「audio.cpp」を試す

### Executive Summary
- audio.cpp は ggml を基盤にした C++ オーディオ推論フレームワークとして紹介されている。
- TTS、ASR、音声クローン、音声変換、VAD、音源分離などを共通インターフェースで扱うことを狙う。
- Python 環境や依存関係の複雑さを避け、ローカルのネイティブランタイムで複数モデルを試せる点が強調されている。
- CUDA では TTS パスで Python リファレンス比 1.8倍から5.0倍高速、レイテンシ 45%から80%削減という性能値が示されている。
- 筆者は Mac M2 Pro で Metal 向けビルドスクリプトを使い、CLI バイナリを作成している。
- CLI は task、family、model、backend を基本指定し、モデルやタスクごとに追加オプションを使う構成になっている。
- README の情報量が多く、対応モデルごとの差分も大きいため、使うモデルごとに都度確認するのがよいと筆者は見ている。
- ライセンスは Apache-2.0 と見られるが、利用モデルごとのライセンス確認は別途必要とされる。

### Key Findings
- audio.cpp はローカルオーディオモデル向けの高性能 C++ 推論フレームワークである。 [^]
  - Footnote: 記事では「ggmlを基盤として構築された高性能なC++オーディオ推論フレームワーク」と説明されている。
- Python 依存の複雑さを減らし、複数モデルを共通ランタイムで扱うことを目的にしている。 [^]
  - Footnote: README 抜粋に「10種類以上のConda環境」や「数百ものPythonパッケージ」を避け、共通のネイティブランタイムで共有可能とある。
- CUDA の TTS では Python リファレンス比で大幅な高速化が報告されている。 [^]
  - Footnote: 記事には「1.8倍～5.0倍の高速化」および「エンドツーエンドのレイテンシも45%～80%削減」とある。
- Supertonic 3 では RTX5090 上で約10時間分の音声を3分で生成できるとされる。 [^]
  - Footnote: 性能例として「RTX5090上で約10時間分のオーディオを3分で生成可能」と記載されている。
- ASR でも TranscrIA ベンチマークで同等 WER のまま実行時間を約4分の1に短縮したとされる。 [^]
  - Footnote: 記事には「他の実装と同等の単語誤り率（WER）を達成しつつ、実行時間を約1/4に短縮」とある。
- 対応タスクは TTS、ASR、ダイアライゼーション、VAD、音源分離など広い。 [^]
  - Footnote: 本文で「テキスト読み上げ（TTS）、音声クローン、音声変換、自動音声認識（ASR）、話者ダイアライゼーション、音声活動検出（VAD）、音源分離」などが列挙されている。
- Mac では Metal 向けビルドスクリプトで CLI バイナリを作成できることを筆者が確認している。 [^]
  - Footnote: 筆者は `scripts/build_metal.sh --target audiocpp_cli` を実行し、`audiocpp_cli` の生成結果を掲載している。
- CLI の基本形は task、family、model、backend の指定である。 [^]
  - Footnote: Usage に `audiocpp_cli --task <task> --family <family> --model <path> --backend <backend>` と表示されている。

### References
- https://zenn.dev/kun432/scraps/cf1b98613e30e0
- https://github.com/0xShug0/audio.cpp
- https://github.com/0xShug0/audio.cpp/blob/main/docs/usage.md

## 「AutoArk-AI/Audio8-ASR-0.1B」を試す

### Executive Summary
- Audio8-ASR-0.1B は小規模なプロダクション対応 ASR モデルとして紹介されている。
- 100M パラメータ級、ピークメモリ 200MB 未満の iOS 版など、オンデバイス利用を強く意識している。
- 対応言語は中国語、英語、フランス語、ドイツ語、日本語、韓国語、広東語の7言語とされる。
- Hugging Face Transformers 形式に加え、ONNX Runtime 版と iOS ANE 版が用意されている。
- 筆者は Mac M2 Pro で ONNX 版の Web UI と PyTorch 版のサンプル推論を試している。
- ONNX 版では 30秒音声制限と 512トークンのキャッシュ制限により、長い音声ではエラーや切り詰めが発生した。
- PyTorch 版でも長時間音声向けのパラメータ調整では安定した文字起こし感が得られなかったと報告している。
- 筆者の結論は、デフォルトの30秒制約を活かせる用途なら軽量に使える可能性があるが、適合ユースケースはまだ判断しにくいというもの。

### Key Findings
- Audio8-ASR-0.1B はクラウド不要のオンデバイス ASR を狙う小型モデルである。 [^]
  - Footnote: 冒頭で「クラウドレベルの精度を備えた最小規模のプロダクション対応ASRモデルの一つ」とされ、「クラウドは不要」と書かれている。
- 公称では 100M パラメータ、ピークメモリ 200MB 未満が強調されている。 [^]
  - Footnote: 記事には「わずか100Mのパラメータ、ピークメモリ200MB未満」とある。
- 7言語の音声認識に対応している。 [^]
  - Footnote: 対応言語として「Mandarin、English、French、German、Japanese、Korean、Cantonese」が列挙されている。
- 配布は Transformers 形式だけでなく、ONNX Runtime 版と iOS ANE 版も用意されている。 [^]
  - Footnote: モデルカード抜粋に「Audio8-ASR-0.1B-onnx-runtime」と「Audio8-ASR-0.1B-iOS-ANE」が関連リリースとして記載されている。
- 英語 Open ASR Leaderboard の7分割平均は WER 7.03、H200 RTFx 741.15 とされる。 [^]
  - Footnote: 評価結果表に「7分割平均 / 複合スコア EN WER / RTFx 7.03 741.15」とある。
- モデル概要では言語モデル部分が約0.104B、エンドツーエンド固有パラメータが約0.324B とされる。 [^]
  - Footnote: モデル概要に「言語モデルパラメータ数: 103,502,336個（約0.104B）」と「エンドツーエンド固有パラメータ数: 323,990,528個（約0.324B）」がある。
- ONNX 版には 30秒音声切り詰めと 512トークン制限がある。 [^]
  - Footnote: 実行時の制限事項に「30秒を超える音声データは...自動的に切り詰められます」「デコーダーのキャッシュコンテキストは最大512トークン」とある。
- 筆者の長時間音声テストでは安定した文字起こしには至っていない。 [^]
  - Footnote: PyTorch 版の試行後に「安定して文字起こしできる感がない」「今のところ30秒限定して使うのが安定かなぁ」と書いている。
- ライセンスは CC-BY-NC-4.0 に変更された可能性がある点を筆者が注意点として挙げている。 [^]
  - Footnote: まとめに「元々はApache-2.0で公開されたみたいだけど、あとからCC-BY-NC-4.0に変更されてるっぽくて」とある。

### References
- https://zenn.dev/kun432/scraps/f8b16a3139ebb1
- https://huggingface.co/AutoArk-AI/Audio8-ASR-0.1B
- https://github.com/AutoArk/open-audio-opd
- https://arxiv.org/abs/2605.28139
