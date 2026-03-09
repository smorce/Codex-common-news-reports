# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-09T09:02:29+09:00
- Articles: 3

## Python でシーケンス比較
- Date: 2026-03-08T23:59:00+09:00

### Executive Summary
- Pythonのシーケンス比較について、difflib / CyDifflib / RapidFuzzを触って検証するメモ。
- 環境はColaboratoryでPython 3.12.12を使用。
- difflibはPython標準モジュールで、SequenceMatcherが中核。
- SequenceMatcherで文字列の類似度をratio()で算出できる。
- ratio()は0.0〜1.0で、1.0に近いほど類似。
- 差分の位置や変更箇所はget_opcodes()で取得する。
- cydifflibが速い傾向は見えるが、実運用のケースで再確認が必要。

### Key Findings
- 比較対象として `difflib` を挙げている。 [^]
  - Footnote: difflib
- 検証環境はColaboratoryだとしている。 [^]
  - Footnote: 環境はColaboratoryで。
- SequenceMatcherはdifflibの中核で、2つのシーケンスを柔軟に比較できると述べている。 [^]
  - Footnote: 2つのシーケンスを柔軟に比較できる、difflibの中核となるクラス。
- ratio()は0.0〜1.0の値を返し、1.0に近いほど似ているという説明。 [^]
  - Footnote: ratio() は 0.0〜1.0の値を返し、1.0 に近いほど似ているということになる。
- 差分の同一箇所や変更箇所の出力にはget_opcodes()を使う。 [^]
  - Footnote: get_opcodes()を使う。これが difflib の全てのベースとなっているらしい。
- 計測では確かに速くなっていると実感している。 [^]
  - Footnote: ふむ、確かに速くなっている。

### References
- https://zenn.dev/kun432/scraps/f55188b54b49a0

## Vending-Bench 2
- Date: 2026-03-08T14:38:00+09:00

### Executive Summary
- Redditのコメント経由でVending-Bench 2を知った経緯から始まるメモ。
- Vending-Bench 2は、AIに一年間ビジネス運営をさせて収益で評価するベンチマーク。
- 自販機ビジネスを一年任せ、最後の銀行残高で成績を付ける設定。
- 一問一答ではなく長期のビジネス運営シミュレーションと説明されている。
- 実務エージェントとしてのスキル（長期的一貫性など）を測る意図がある。
- ツール活用（Web検索やメール交渉）も評価対象のスキルとして挙げられる。
- 評価指標は一年後の銀行口座残高で、未確定利益は含めない。

### Key Findings
- RedditのスレコメントでVending-Bench 2の存在を知った。 [^]
  - Footnote: Redditのスレのコメントで、Vending-Bench 2 ってのがあるのを知った。
- AIに一年間ビジネス運営をさせ、収益を見るベンチマークという説明。 [^]
  - Footnote: Vending-Bench 2って、「AIで一年間ビジネス運営させて、どれだけお金増やせるか見るテスト」って感じのベンチマークだよ。
- 自販機ビジネスを一年任せ、最後の銀行残高で評価するというコンセプト。 [^]
  - Footnote: 「AIエージェントに、自動販売機ビジネスを一年間まかせて、最後の銀行残高で成績をつけるテスト」だよ。
- 一問一答ではなく長期間のビジネス運営シミュレーションだとしている。 [^]
  - Footnote: 一問一答クイズじゃなくて、「長期間のビジネス運営シミュレーション」。
- 長期的な一貫性を測るスキルとして挙げている。 [^]
  - Footnote: 長期的な一貫性（途中で方針ブレないか、ダレないか）
- ツールの使い方（Web検索やメール交渉）も評価対象のスキルとして挙げている。 [^]
  - Footnote: ツールの使い方（仕入れのためのWeb検索やメール交渉）

### References
- https://zenn.dev/kun432/scraps/0fc739b307d48b

## 「sherpa-onnx」を試す
- Date: 2026-03-07T23:34:00+09:00

### Executive Summary
- ウェイクワード/キーワード検出を試す目的でsherpa-onnxを調査した記録。
- sherpa-onnxは軽量で良さそうだという前提から探索が始まる。
- Kaldi後継のk2-fsa内のプロジェクトという位置づけに触れている。
- k2-fsaは音声認識向けのFSA/FSTを扱うOSS群という説明を引用。
- sherpa-onnxはONNX Runtimeでオフライン動作も可能とされる。
- 日本語の事前学習モデルがなく、実用にはモデル作成が必要と示唆。
- RPiのような非力環境では厳しく、GPUがあれば改善余地という見立て。

### Key Findings
- ウェイクワード/キーワード検出を試したくてsherpa-onnxを調べた。 [^]
  - Footnote: ウェイクワード / キーワード検出を試したくて、いろいろ調べてみたら、sherpa-onnxが軽量で良いらしく、
- sherpa-onnxはKaldi後継のk2-fsa内のプロジェクトと捉えている。 [^]
  - Footnote: どうやらKaldiの後継である k2-fsa の中の1つのプロジェクトらしい？
- k2-fsaは音声認識向けのFSA/FSTを扱うOSS群だという説明を引用している。 [^]
  - Footnote: k2-fsa は、音声認識を中心とした音声処理で使う、有限状態オートマトンと有限状態変換器を扱うためのオープンソース群です。
- sherpa-onnxはONNX Runtimeでオフライン動作を含む多様な音声機能を案内している。 [^]
  - Footnote: とくに sherpa-onnx は、ONNX Runtime を使い、インターネット接続なしでも音声認識、音声合成、話者分離、音声区間検出などをさまざまな環境で動かせると案内されています。
- 日本語の事前学習モデルが存在しないと述べている。 [^]
  - Footnote: キーワード抽出・ウェイクワードを試してみたかったのだけど、日本語の事前学習モデルは存在しない。
- RPiのような環境ではASRモデルが厳しく、実用にはモデル作成が必要と見ている。 [^]
  - Footnote: モデルを作成するか、上のASRモデルを流用することになると思うのだけど、RPiのような環境だとASRモデルは厳しい感があるので、実用に耐えうるものとなるとやはりモデルを作るしかなさそう。

### References
- https://zenn.dev/kun432/scraps/1fdc08e096e8b7
