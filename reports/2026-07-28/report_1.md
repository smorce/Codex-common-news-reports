# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-07-28T09:01:31.6027844+09:00
- Articles: 3

## 「Qwen-Audio-3.0-TTS」を試す
- Date: 2026-07-27T21:36:00+09:00

### Executive Summary
- Alibaba の Qwen-Audio-3.0-TTS を試すスクラップである。
- モデルは Flash と Plus の2系統で、リアルタイム性と高品質生成を分けている。
- 16言語対応、自然言語によるスタイル制御、非言語タグ、堅牢なボイスクローニングが主な特徴として整理されている。
- Artificial Analysis の Speech Arena では Plus が Provider Voices の首位級として紹介されている。
- 低フレームレートの音声トークナイザーにより、推論ステップ削減と音声品質の両立を狙う構成が説明されている。
- DashScope SDK と WebSocket エンドポイントを使った Python 実装例が掲載されている。
- プロンプトで発話トーン、速度、感情、声色を指定できる点が試されている。
- 感情タグやリッチ言語タグは Qwen-Audio-3.0-TTS 系モデル固有の制御機能として扱われている。

### Key Findings
- Qwen-Audio-3.0-TTS は Flash と Plus の2種類で提供される。 [^]
  - Footnote: 記事中に「Flash: リアルタイム対話」「Plus: 高品質生成」と記載されている。
- モデルは多言語、スタイル制御、非言語タグ、ボイスクローニングを主要機能としている。 [^]
  - Footnote: 「16言語に対応した多言語カバレッジ」「自然言語によるスタイル制御」「非言語的な詳細のための細分化されたタグ」「不完全なオーディオからのより堅牢なボイスクローニング」と列挙されている。
- Artificial Analysis の評価では Plus が高い音声品質スコアを示している。 [^]
  - Footnote: 「Eloスコアは1,236（+17/-17）で、1,305回のarena出場に基づき」と記載されている。
- 速度面では競合上位モデルより遅い可能性がある。 [^]
  - Footnote: 「秒間16文字を生成し、Simba 3.2（30.2）、Gemini 3.1 Flash TTS（27）、Sonic 3.5（120）よりも低い」と記載されている。
- 価格は Sonic 3.5 より安い一方、Gemini 3.1 Flash TTS や Simba 3.2 より高い。 [^]
  - Footnote: 「1M文字あたり$27.59」「Sonic 3.5（$39.00/1M）より安く、Gemini 3.1 Flash TTS（$18.31/1M）やSimba 3.2（$10.00/1M）より高い」と比較されている。
- 音声処理の効率化には 12.5 Hz の低フレームレート音声トークナイザーが関係する。 [^]
  - Footnote: 「12.5 Hz の低フレームレートの音声トークナイザー」「1秒間あたりの処理ステップをかなり減らしてる」と説明されている。
- プロンプトによる声質制御は、具体的かつ多面的な記述が推奨される。 [^]
  - Footnote: 記事中のプラクティスで「曖昧さを避け具体的に」「一面的ではなく多面的に」「主観的ではなく客観的に」と説明されている。
- 感情タグとリッチ言語タグは Plus と Flash のみで利用できる。 [^]
  - Footnote: 「対応モデル：qwen-audio-3.0-tts-plus および qwen-audio-3.0-tts-flash のみサポートされています」と記載されている。

### References
- https://zenn.dev/kun432/scraps/04ff5d177b1cc4
- https://github.com/QwenAudio/FunAudioLLM.github.io/tree/master/qwen-audio-3.0-tts/index.html

## 「Inflect-Micro-v2 / Inflect-Nano-v2」を試す
- Date: 2026-07-27T16:07:00+09:00

### Executive Summary
- ローカル向け TTS ベンチマーク tts-bench と Inflect-Micro-v2 / Inflect-Nano-v2 を扱うスクラップである。
- tts-bench は処理速度、音声確認、評価スコアを横断して比較できるツールとして紹介されている。
- デモサイトではモデル別・プロンプト別の試聴、速度比較、客観スコア確認ができる。
- 2026年6月時点の速度面では、CPU で Piper、CUDA で Kokoro、Apple M4 で Piper が高速例として挙げられている。
- Inflect-Micro v2 は936万パラメータ、Inflect-Nano v2 は396万パラメータの小型英語 TTS モデルとして紹介されている。
- Colaboratory T4 上で Nano と Micro をダウンロードし、requirements と推論コードを使って試している。
- Nano-v2 は CPU でも比較的高速で、GPU ではさらに大幅に短時間で推論できたと記録されている。
- 日本語には未対応だが、学習用コードがあり、日本語向け拡張の可能性にも触れている。

### Key Findings
- tts-bench はハードウェアを問わず TTS の速度や品質確認を支援する。 [^]
  - Footnote: 「使用するハードウェアを問わず測定できます」として、処理速度、音声確認、評価スコアが説明されている。
- 速度評価には TTFA、RTFx、メモリ使用量が含まれる。 [^]
  - Footnote: 「TTFA」「RTFx」「メモリ使用量、CPU/CUDA/Apple Silicon環境でのパフォーマンス」と記載されている。
- 品質判断は最終的に人間の試聴を重視する構成である。 [^]
  - Footnote: 「品質評価は主観的な要素を含むため、最終的な判断基準となるのはあなたの耳です」と説明されている。
- Inflect-Micro v2 と Inflect-Nano v2 はどちらも Apache 2.0 で、英語向けの小型モデルである。 [^]
  - Footnote: 表で Inflect-Micro v2 は「936万」、Inflect-Nano v2 は「396万」、どちらも「—（英語）」「Apache 2.0」と示されている。
- Nano-v2 の CPU 推論は 607 ms 程度で実行された。 [^]
  - Footnote: Nano-v2 の計測結果として「607 ms ± 24.5 ms per loop」と記載されている。
- Nano-v2 の GPU 推論は CPU より大幅に速い。 [^]
  - Footnote: GPU に切り替えた後の計測結果として「61.2 ms ± 16.6 ms per loop」と記載されている。
- Micro-v2 は Nano-v2 より大きく、CPU 推論ではより時間がかかった。 [^]
  - Footnote: Micro-v2 の CPU 計測結果として「1.32 s ± 282 ms per loop」と記載されている。
- Micro-v2 の GPU 推論は 82.3 ms 程度で動作した。 [^]
  - Footnote: Micro-v2 の GPU 計測結果として「82.3 ms ± 19 ms per loop」と記載されている。
- Nano-v2 は v1 よりロボット的な印象が少なく、CPU でも速そうだと評価されている。 [^]
  - Footnote: まとめで「nano-v2 だと v1のようなロボットっぽさはそんなに感じないし、CPUでも速そう」と述べられている。

### References
- https://zenn.dev/kun432/scraps/688cef5359c0f8
- https://github.com/5uck1ess/tts-bench
- https://huggingface.co/owensong/Inflect-Nano-v2
- https://huggingface.co/owensong/Inflect-Micro-v2

## 「MOSS-SoundEffect-v2.0」を試す
- Date: 2026-07-26T23:32:00+09:00

### Executive Summary
- MOSS-SoundEffect-v2.0 を Colaboratory L4 環境で試したスクラップである。
- モデルは自然言語プロンプトから環境音、都市音、生物音、人間の動作音などを生成する。
- v2.0 では DiT と Flow Matching を使う設計に変わり、旧来の自己回帰型構成から更新されている。
- 最大30秒、48 kHz までの音声生成を制御できると紹介されている。
- インストール時にはクリーンな Python 3.12 環境が推奨され、Colaboratory では依存関係で詰まりやすい点が記録されている。
- protobuf のバージョン衝突により diffusers 関連の import error が発生し、protobuf を更新して回避している。
- モデルロード時点で VRAM は約10GB、複数回推論後は約15GB 消費したと記録されている。
- 効果音生成のオープンモデルとして貴重だが、リソース消費の大きさとプロンプト制御の難しさが課題としてまとめられている。

### Key Findings
- MOSS-SoundEffect v2.0 は非音声音響生成に特化したモデルである。 [^]
  - Footnote: 「テキストから非音声音響を生成する専用モデル」と説明されている。
- 基盤アーキテクチャは DiT + Flow Matching である。 [^]
  - Footnote: 「Flow Matchingという目的関数を用いて学習されたDiffusion Transformer（DiT）」と記載されている。
- 生成対象は環境音、都市音、生物音、人間の動作音など幅広い。 [^]
  - Footnote: 「高忠実度の環境音、都市音、生物音、人間の動作音を生成します」と記載されている。
- 出力は最長30秒、48 kHz まで制御可能である。 [^]
  - Footnote: 「生成される音声の持続時間は最長30秒、サンプリングレートは48 kHzまで制御可能」と説明されている。
- 推奨ハイパーパラメータは num_inference_steps 100、cfg_scale 4.0、sigma_shift 5.0、seconds 10.0 である。 [^]
  - Footnote: 表に「num_inference_steps 100」「cfg_scale 4.0」「sigma_shift 5.0」「seconds 10.0」と記載されている。
- Colaboratory では依存関係の都合で protobuf 関連エラーが発生した。 [^]
  - Footnote: エラーとして「cannot import name 'runtime_version' from 'google.protobuf'」が記録されている。
- protobuf を 5.28 以上 6 未満へ更新することで実行を進めている。 [^]
  - Footnote: 回避策として「pip install -U "protobuf>=5.28,<6"」が示されている。
- モデルロード直後の VRAM 消費は約10GBである。 [^]
  - Footnote: NVIDIA-SMI の出力として「10658MiB / 23034MiB」と記録されている。
- 数回推論後の VRAM 消費は約15GBまで増えている。 [^]
  - Footnote: 数回推論後の出力として「15186MiB / 23034MiB」と記載されている。
- プロンプトによる効果音制御は試行錯誤が必要と評価されている。 [^]
  - Footnote: 「プロンプトでの制御はなかなか難しいな、色々試行錯誤は必要そう」と述べられている。

### References
- https://zenn.dev/kun432/scraps/c15a8af84f93b2
- https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect-v2.0
- https://github.com/OpenMOSS/MOSS-TTS
