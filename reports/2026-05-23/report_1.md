# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-05-23T09:01:31.3052690+09:00
- Articles: 3

## 「BitCPM-CANN」を試す

### Executive Summary
- BitCPM-CANNは、OpenBMBなどによる1.58ビット三値量子化モデルファミリーを試したスクラップである。
- 対象モデルは0.5B、1B、3B、8Bの4サイズで、Ascend NPU上のネイティブ訓練スタックを特徴としている。
- 記事では、未量子化QATチェックポイント、擬似量子化モデル、GGUF版の違いを整理している。
- 実際に試す候補として、llama.cpp向けGGUFのTQ2_0形式が本来の低ビット推論向けと判断されている。
- モデルカードでは、1B以上のモデルがフル精度MiniCPM4比で約95.7%以上の保持率を示すとされている。
- Ubuntu 22.04とRTX4090環境で8B GGUF TQ2_0をllama-cliから実行している。
- 英語出力は成立し、日本語出力も一定程度生成できたが、速度面では速い印象は薄いと評価している。

### Key Findings
- BitCPM-CANNはエッジAI向けに低メモリでの大規模モデル利用を狙う。 [^]
  - Footnote: 本文に「8Bモデルがモバイル、PC、自動車デバイスでスムーズに動作」「BF16比で約6倍低いメモリフットプリント」とある。
- モデルサイズは0.5B、1B、3B、8Bの4種類で提供されている。 [^]
  - Footnote: 本文に「モデルは、0.5B / 1B / 3B / 8B の4つのパラメータサイズがある」とある。
- 推論用途では未量子化QATチェックポイントではなく、擬似量子化版またはGGUF版を選ぶ必要がある。 [^]
  - Footnote: 本文に「このモデルは直接的な推論用途には適していません」「推論にご利用の場合は、擬似量子化版…をご使用ください」とある。
- 筆者は実用的な試用対象としてGGUFのTQ2_0を選んでいる。 [^]
  - Footnote: 本文に「試すとしたら、GGUFのTQ2_0 を使うのだろうと思う」とある。
- 1B、3B、8Bモデルでは性能保持率が95.7%から97.2%とされる。 [^]
  - Footnote: 評価結果に「保持率 95.7%」「97.2%」「97.1%」が示されている。
- 三値QATの訓練スループット低下は小さいと説明されている。 [^]
  - Footnote: 本文に「スループットの低下はわずか5%」「148 TFLOP/s vs. 155 TFLOP/s」とある。
- RTX4090でのllama.cpp実行では、英語・日本語の生成はできたが速度面は課題として見ている。 [^]
  - Footnote: 本文に「Ubuntu-22.04+RTX4090で試す」「Prompt: 47.3 t/s | Generation: 21.6 t/s」「むしろ遅い？」とある。

### References
- https://zenn.dev/kun432/scraps/9f0a86c12d7b94
- https://huggingface.openbmb.com/collections/openbmb/bitcpm4-cann
- https://www.modelscope.cn/collections/OpenBMB/BitCPM4-CANN

## Tencentの翻訳モデル「HY-MT2」を試す

### Executive Summary
- Tencentの多言語翻訳モデルHy-MT2を紹介し、特に新しい30B-A3Bモデルを試している。
- Hy-MT2は1.8B、7B、30B-A3Bの3サイズを持ち、33言語間翻訳に対応するとされる。
- 1.8BモデルはAngelSlim 1.25ビット超量子化により440MBまで小さくできると紹介されている。
- 記事ではREADMEの概要、配布モデル、指示テンプレート、対応言語、学習・量子化ツールを整理している。
- ライセンスはEUでの使用不可や商用利用条件など制約が強く、筆者はオープンソースと言い切る点に疑問を示している。
- Colaboratory A100ハイメモリ環境で30B-A3BをTransformersから読み込み、VRAM消費は約60GBと記録している。
- 英日・日英翻訳の実験では、少なくとも例文レベルで自然な翻訳結果が得られている。

### Key Findings
- Hy-MT2は3つのモデルサイズで提供される翻訳モデルファミリーである。 [^]
  - Footnote: 本文に「1.8B、7B、30B-A3B（MoE）の3つのモデルサイズを提供」とある。
- 33言語の翻訳に対応し、日本語も対応言語一覧に含まれる。 [^]
  - Footnote: 本文に「33言語間の翻訳をサポート」とあり、対応言語表に「日本語 ja 日语」とある。
- 1.8Bモデルはモバイル用途を意識した軽量化が強調されている。 [^]
  - Footnote: 本文に「1.8B: 440MB、モバイルチップで動作」「AngelSlim 1.25ビット超量子化技術」とある。
- 30B-A3Bが以前のバージョンから増えた主要な差分として扱われている。 [^]
  - Footnote: 本文に「以前のバージョンとの違いとしては、パラメータサイズのバリエーションとして 30B-A3B が増えている」とある。
- 30B-A3Bの通常ロードではA100上で約60GBのVRAMを消費している。 [^]
  - Footnote: 本文に「VRAM消費は60GB程度」とあり、NVIDIA-SMI出力で「60100MiB / 81920MiB」と示されている。
- FP8量子化版もあるが、筆者の試行では動作確認に至っていない。 [^]
  - Footnote: 本文に「30B-A3B には FP8量子化版もある」「自分が試したときはうまく動かなかった」とある。
- ライセンス制約は採用判断上の大きな懸念として扱われている。 [^]
  - Footnote: 本文に「EUでは使用不可・商用利用は一定のMAU以下に限定・他モデルの学習には使用禁止」とある。

### References
- https://zenn.dev/kun432/scraps/527e198418845c
- https://github.com/Tencent-Hunyuan/Hy-MT2

## OpenAI Python SDK を aiohttp で使う

### Executive Summary
- OpenAI Python SDKの非同期HTTPバックエンドを、低リソース環境で比較したスクラップである。
- 発端はRaspberry Piのような環境で、SDK利用時の起動や最初のチャンク受信が遅く感じられる点にある。
- まず標準のAsyncOpenAIとストリーミングで、MacとRaspberry Pi 4Bのstartup、TTFT、チャンク間隔を比較している。
- 次にhttpxのkeep-aliveを無効化した構成を試し、さらにOpenAI SDKのaiohttpバックエンドも試している。
- Macでは起動時間が300ms台、Raspberry Piでは数秒規模となり、起動オーバーヘッドの差が目立つ。
- TTFTはRaspberry Piで7から8秒台の結果が多く、HTTP接続やTLSなどの影響も推測している。
- aiohttp化で一部数値は変わるものの、筆者は劇的な改善とは見ていない。

### Key Findings
- 低リソース環境ではOpenAI Python SDKの起動オーバーヘッドが目立つ。 [^]
  - Footnote: 標準構成でMacのstartupは324.4ms、Raspberry Pi 4Bは3179.7msと記録されている。
- 標準構成ではRaspberry PiのTTFTがMacより大幅に長い。 [^]
  - Footnote: 標準構成でMacのtime to first chunkは793.6ms、Raspberry Pi 4Bは8209.6msとある。
- 最初のチャンク以降の生成間隔は、環境差が比較的小さい。 [^]
  - Footnote: 本文に「最初のチャンク以降の生成はそんなに変わらない」とあり、平均チャンク間隔は13.2msと14.5msで近い。
- httpxのkeep-aliveを無効化しても、筆者は大きな改善とは判断していない。 [^]
  - Footnote: 本文に「そんなに変わらないかな」とあり、Raspberry PiのTTFTは8311.8msと記録されている。
- OpenAI Python SDKはaiohttpバックエンドを使う構成に変更できる。 [^]
  - Footnote: 本文に「aiohttp に変更することができるらしい」「uv add "openai[aiohttp]"」とある。
- aiohttp構成ではRaspberry PiのTTFTが標準構成より短くなった例がある。 [^]
  - Footnote: aiohttp構成でRaspberry Piのtime to first chunkは7449.6msと記録されている。
- ストリーミングを確実に閉じる実装も示されている。 [^]
  - Footnote: コード例に「finally: await stream.close()」および「streamingを途中終了・例外終了した場合でも接続を閉じる」とある。

### References
- https://zenn.dev/kun432/scraps/220122eee7ce36
