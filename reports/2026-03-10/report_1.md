# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-03-10T10:56:03.9664590+09:00
- Articles: 3

## 「livekit-wakeword」を試す
- Date: 2026-03-10T03:03:00+09:00

### Executive Summary
- LiveKitのエバンジェリスト投稿にあったウェイクワードのサンプルコードが出発点。
- サンプルはLiveKit接続で特定フレーズ時のみ応答する方式に見える。
- その方式はASRを常時使う必要がありそうという所感が書かれている。
- 関連リポジトリとしてlivekit-wakewordを発見した旨が記載。
- README抜粋で音声認識アプリ向けウェイクワードライブラリと説明。
- openWakeWordをベースにYAML設定で学習フローを一貫化する点が示される。
- Conv-Attention分類器で時間構造を扱い、精度向上と誤検知低減を狙う。

### Key Findings
- LiveKitの投稿でウェイクワードのサンプルコードが公開されていたことが調査のきっかけ。 [^]
  - Footnote: 「以前にLiveKitのエバンジェリストの方のポストで、ウェイクワードのサンプルコードが公開されていた。」
- サンプル方式はASRを常時使う前提に見え、常時利用が必要という懸念が示されている。 [^]
  - Footnote: 「フレーズの検出はASRを使っている。これだとASRをずっと使い続ける必要があるように思う。」
- livekit-wakewordは音声認識アプリ向けのオープンソースウェイクワードライブラリと記載。 [^]
  - Footnote: 「An open-source wake word library for creating voice-enabled applications.」
- openWakeWordをベースに、単一YAMLで合成データ生成から学習・エクスポートまで一貫化する設計。 [^]
  - Footnote: 「openWakeWord をベースに、トレーニングプロセスを効率化。単一の YAML 設定ファイルで、合成データの生成、データ拡張、学習、エクスポートまでを一貫して行えます。」
- Conv-Attention分類器で時間構造を保持し、精度向上と誤検知低減を狙うと説明されている。 [^]
  - Footnote: 「1次元時間畳み込みとマルチヘッド自己注意機構を採用し…精度向上と誤検知の低減を実現しています」
- 依存関係管理はuvで一括管理するためトラブルを減らすと明記されている。 [^]
  - Footnote: 「依存関係のトラブルゼロ — uv があらゆる処理を一括して管理するため」

### References
- https://zenn.dev/kun432/scraps/18547c54e50e73
- https://github.com/livekit/livekit-wakeword

## 「KenLM」を試す
- Date: 2026-03-10T00:34:00+09:00

### Executive Summary
- KenLMは「爆速で軽いn-gram言語モデル用ツールキット」と要約されている。
- 言語モデルの自然さ評価を数値化する考え方を簡潔に説明。
- KenLMの主要機能はモデル作成・絞り込み・スコア計算の3点。
- 大規模でもオンディスク学習とModified Kneser-Ney smoothingを使うと記載。
- バイナリ化による高速ロードやマルチスレッド対応など強みを列挙。
- 機械翻訳などで言語モデル部分として使われる点が示される。
- Ubuntu 24.04でのビルド手順と必要パッケージ、uvでのPython利用手順を記録。

### Key Findings
- KenLMは高速・軽量なn-gram言語モデル用ツールキットとして位置づけられている。 [^]
  - Footnote: 「『爆速で軽い n-gram 言語モデル用ツールキット』って感じ」
- 機能はモデル作成（estimate）、絞り込み（filter）、スコア計算（query）の3つに整理されている。 [^]
  - Footnote: 「言語モデルを『作る（estimate）』『軽くする・絞り込む（filter）』『使ってスコア計算する（query）』」
- 学習はオンディスク（ストリーミング）アルゴリズムで大規模コーパスにも対応する。 [^]
  - Footnote: 「デカいコーパスでもいけるように『オンディスク（ストリーミング）アルゴリズム』で動く」
- 平滑化にModified Kneser-Ney smoothingを用いると書かれている。 [^]
  - Footnote: 「平滑化は『Modified Kneser-Ney smoothing』を使ってて」
- SRILM/IRSTLMより速くメモリ効率が良いなどの特徴が列挙されている。 [^]
  - Footnote: 「SRILM や IRSTLM より速くてメモリも食わない」
- Ubuntu 24.04でのビルド例と依存パッケージが具体的に示されている。 [^]
  - Footnote: 「Linuxでやり直してみた。Ubunt-24.04で。」「sudo apt install build-essential cmake libboost-system-dev ...」

### References
- https://zenn.dev/kun432/scraps/e1db7f82966dcf
- https://kheafield.com/code/kenlm/

## 「VOSK」の文法モードを試す
- Date: 2026-03-09T14:55:00+09:00

### Executive Summary
- Voskの文法モードを知って試した記録で、過去のVoskスクラップ参照から開始。
- VoskはWFSTで認識し、全語彙モードと文法モードの違いを整理。
- 文法モードは語彙を数十語に絞り、誤検知・CPU負荷・速度面で利点があると記載。
- 認識語彙の実行時更新（オンライン更新）に関する注意点が示される。
- Macで環境を作り、Vosk/Silero VADなどを入れて実験した手順が記載。
- VAD経由だと[unk]が混じりやすく、パラメータ調整が必要という所感。
- 簡易ウェイクワード＋固定発話の用途には手軽と結論づけている。

### Key Findings
- VoskはWFSTで認識し、全語彙モードでは辞書の全単語が候補になると説明されている。 [^]
  - Footnote: 「Voskは内部でWeighted Finite-State Transducer（WFST）を使って音声認識を行う。全語彙モードでは、発音辞書に登録されている全単語が認識候補になる。」
- 文法モードは指定語彙だけに制限し、誤検知低下・CPU負荷低下・速度向上が挙げられている。 [^]
  - Footnote: 「認識候補が数万から数十語に絞られるため：誤検知率が大幅に低下する／CPU負荷が下がる／認識速度が向上する」
- Vosk-APIは認識語彙のオンライン更新をサポートするが、静的グラフでは不可という注意がある。 [^]
  - Footnote: 「Vosk-APIでは、認識語彙のオンライン更新をサポートしています。…静的グラフを使用する大規模モデルではこの変更をサポートしていない」
- 語彙追加は単純ではなく、特定キーワードだけ認識させる矯正に近いという理解が示されている。 [^]
  - Footnote: 「新しい語彙の追加はそんな簡単にできるわけではなくて…辞書に登録されている特定のキーワードやフレーズだけを認識、それ以外は認識しない、というのを矯正するような仕組み」
- VAD経由で[unk]が混じるなど認識が不安定になるため、パラメータ調整が必要と述べている。 [^]
  - Footnote: 「VADを経由させると、意図せず [unk] が含まれてしまって…VADのパラメータを調整したりして試行錯誤する必要がありそう。」
- 簡易ウェイクワード＋固定発話の用途なら手軽にできるという結論。 [^]
  - Footnote: 「シンプルなウェイクワード＋あらかじめ決まった発話のインテントだけ取得する、とかなら、お手軽にできそう。」

### References
- https://zenn.dev/kun432/scraps/66d749573dbed8
- https://alphacephei.com/vosk/adaptation
