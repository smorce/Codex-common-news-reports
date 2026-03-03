# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-03T09:01:57+09:00
- Articles: 3

## 「Qwen3.5 Smallモデル」を試す
- Date: 2026-03-03T01:40:00+09:00

### Executive Summary
- Qwen3.5 Smallの小型モデルシリーズの紹介メモ。
- 0.8B、2B、4B、9Bの4サイズが並ぶ。
- 同じQwen3.5基盤でネイティブマルチモーダルや改良アーキテクチャを強調。
- エッジデバイス向けの高速モデルから軽量エージェント向けまで幅を持たせている。
- Baseモデルも同時リリースと明記されている。
- Hugging FaceやModelScopeのコレクションリンクが提示されている。
- Unsloth側のGGUF提供やガイドへのリンクも添えられている。

### Key Findings
- Qwen3.5 Smallは0.8B/2B/4B/9Bの4モデルで構成される。 [^]
  - Footnote: Qwen3.5-0.8B · Qwen3.5-2B · Qwen3.5-4B · Qwen3.5-9B
- 同一のQwen3.5基盤で、ネイティブマルチモーダルや改良アーキテクチャ、強化学習のスケールを強調している。 [^]
  - Footnote: 同じQwen3.5基盤…ネイティブマルチモーダル、改良されたアーキテクチャ、スケーラブルなRL
- 0.8B/2Bは小型・高速でエッジ向け、4Bは軽量エージェント向け、9Bは大規模モデルとの差を縮めると説明されている。 [^]
  - Footnote: 0.8B / 2B → 小型で高速、エッジデバイスに最適 / 4B → 軽量エージェント向け… / 9B → 大規模モデルとのギャップを…
- Baseモデルも同時にリリースすると記載されている。 [^]
  - Footnote: Baseモデルも同時にリリースします。
- UnslothからGGUFがすでに出ているとのコメントがある。 [^]
  - Footnote: UnslothからもGGUFがもう出ている。
- 9Bは6GB RAMで動作可能、視覚的推論では4倍サイズのモデルより良い性能とされる。 [^]
  - Footnote: 9Bモデルは6GBのRAM環境で実行できます／視覚的推論タスク…4倍のサイズを持つモデルよりも優れた性能

### References
- https://zenn.dev/kun432/scraps/bd7e1b67833834
- https://huggingface.co/collections/Qwen/qwen35
- https://huggingface.co/collections/unsloth/qwen35
- https://unsloth.ai/docs/models/qwen3.5

## 「FireRed-OCR」を試す
- Date: 2026-03-02T02:50:00+09:00

### Executive Summary
- FireRed-OCRの発見と試用メモ。
- Hugging Face上の新しいOCRモデルとして紹介されている。
- 学習時にFormat-Constrained GRPOを使い、出力の構文妥当性を強制すると記載。
- OmniDocBench v1.5でSOTA主張や2.1Bパラメータなどの仕様が言及されている。
- uv-scripts/ocrデータセットに追加された旨が示されている。
- Highland Newsページでの試験結果では、終盤で出力が切れるが強力に見えると評価。
- 表構造の再現は過去の試行より良い一方、画像は無視される様子と述べられている。

### Key Findings
- FireRed-OCRはHugging Face上の新しいOCRモデルとして紹介されている。 [^]
  - Footnote: FireRed-OCR、@huggingface での新しい OCR モデル。
- 学習時にFormat-Constrained GRPOを使い、出力の厳密な構文妥当性を強制すると記述されている。 [^]
  - Footnote: Format-Constrained GRPO を使用して、出力の厳密な構文的妥当性を強制
- エンドツーエンドモデルの中でOmniDocBench v1.5でSOTA（92.94%）を主張している。 [^]
  - Footnote: OmniDocBench v1.5 (92.94%) で SOTA を主張
- モデルは2.1Bパラメータで、ライセンスはApache 2.0とされている。 [^]
  - Footnote: 2.1B パラメータ、Apache 2.0。
- uv-scripts/ocrのデータセットに追加されたと明記されている。 [^]
  - Footnote: uv-scripts/ocr リポジトリに追加されました
- Highland Newsのページで試験した結果、フルページの終わりで切れるが強力に見えると評価されている。 [^]
  - Footnote: 出力はフルページの終わり近くで切れてしまいますが、かなり強力に見えます。
- 表構造の再現度は過去試した中で最も高い可能性があるが、画像は無視される様子と述べられている。 [^]
  - Footnote: 表構造の再現度は過去試した中でも一番高いかもしれない／ただし画像については無視される様子

### References
- https://zenn.dev/kun432/scraps/b5b6f75bbb1b16
- https://huggingface.co/datasets/uv-scripts/ocr
- http://huggingface.co/datasets/davanstrien/nls-highland-news-firered-ocr

## 「OpenClaw」を試す
- Date: 2026-03-01T21:41:00+09:00

### Executive Summary
- OpenClawの安全性評判が気になりつつ公式に触れて理解する記録。
- OpenClawは端末上で動作するパーソナルAIアシスタントとして説明される。
- 多数のコミュニケーションチャネルに対応し、モバイルで音声入出力が可能。
- ローカル優先のゲートウェイが制御プレーンで、価値はアシスタント機能にあるとされる。
- オンボーディングは`openclaw onboard`のウィザードが推奨されている。
- MITライセンスで、ドキュメントが充実している印象と記載。
- 規模の大きさや管理の難しさへの懸念が述べられている。

### Key Findings
- セキュリティ面の評判が気になり、代替を調べたうえで公式を触る流れが示されている。 [^]
  - Footnote: セキュリティ周りの評判もあって試せずにいた／代替を調べてみたり
- OpenClawはユーザーのデバイス上で動作するパーソナルAIアシスタントと説明されている。 [^]
  - Footnote: ユーザーが自身のデバイス上で直接運用できる パーソナルAIアシスタント
- WhatsAppやTelegramなど多数のチャネルに対応し、macOS/iOS/Androidで音声入出力が可能とされている。 [^]
  - Footnote: WhatsApp、Telegram、Slack…iMessage…macOS / iOS / Android環境で音声入力・出力が可能
- ゲートウェイは制御プレーンで、価値はアシスタント機能にあると説明されている。 [^]
  - Footnote: ゲートウェイは単なる制御プレーンに過ぎず、真の価値はアシスタント機能そのもの
- 推奨セットアップは`openclaw onboard`のウィザードで、macOS/Linux/Windows（WSL2推奨）に対応とされている。 [^]
  - Footnote: openclaw onboard…macOS、Linux、およびWindows環境（WSL2を強く推奨）
- 要件としてNode 22以上と記載され、インストールスクリプト主体のローカル導入が説明されている。 [^]
  - Footnote: Node-22以上…インストールスクリプト…ローカルに直接インストール
- ライセンスはMITで、公式ドキュメントは情報量が多いと記載されている。 [^]
  - Footnote: ライセンスはMITライセンス。／公式ドキュメントは、かなり情報量が多く…
- 規模面ではコミット数やPR数、追加行数が大きく、管理面の懸念が示されている。 [^]
  - Footnote: main へのコミット数: 1695／マージされたPR: 492／追加195940行…安全に管理できるのかなぁ…

### References
- https://zenn.dev/kun432/scraps/337ea21710c496
- https://github.com/openclaw/openclaw
- https://docs.openclaw.ai/
