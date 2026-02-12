# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-02-12T09:01:56+09:00
- Articles: 3

## 「MioTTS」を試す

### Executive Summary
- 軽量TTSモデルMioTTSの公開情報と試行内容を整理した。
- 0.1B〜2.6Bまで複数サイズがあり、小型でも音声合成可能とされる。
- 推論コード、デモ、コーデックが同時に提供されている。
- 既定プリセット音声として日本語/英語の男女が同梱されている。
- プリセット音声は特定モデル由来で商用利用不可の注意がある。
- 音声クローンではデバイス不一致が原因のエラーが出たが修正で改善。
- Flash Attention未導入時はSDPAへフォールバックする旨が記録されている。

### Key Findings
- MioTTSは0.1B〜2.6Bまで複数サイズのモデルが公開された。 [^]
  - Footnote: 「0.1B～2.6Bまで様々なサイズのモデルを公開しています！」
- デモ、推論コード、コーデックが同時に提供されている。 [^]
  - Footnote: 「デモや推論コード、コーデックなども同時に公開しています。」
- デフォルトプリセットは日本語/英語の男女音声が同梱されている。 [^]
  - Footnote: 「以下のプリセットが同梱されています: jp_female / jp_male / en_female / en_male」
- プリセット由来音声は商用利用不可と明記されている。 [^]
  - Footnote: 「これを用いて合成した音声は商用利用出来ません。」
- 音声クローンの失敗は参照波形のデバイス不一致が原因で、デバイス移動で解消した。 [^]
  - Footnote: 「reference_waveform = reference_waveform.to(_codec_device(self.codec))」
- Flash Attention未導入時はPyTorch SDPAにフォールバックする警告が出る。 [^]
  - Footnote: 「FlashAttention is not installed. Falling back to PyTorch SDPA implementation.」
- MIOTTS_DEVICEをcpuにするとクローンが問題なく動作したと記録されている。 [^]
  - Footnote: 「MIOTTS_DEVICE を cpu にすると問題なくクローンができる。」

### References
- https://zenn.dev/kun432/scraps/d7b1baada3c03a

## vLLMの「入力ストリーミングとリアルタイムAPI」 を試す（Voxtral Mini 4B Realtime 2602）

### Executive Summary
- vLLMの入力ストリーミングとリアルタイムAPIをVoxtralで検証した。
- 公式ポストとブログで入力ストリーミング対応が紹介されている。
- 入力ストリーミングは音声アシスタント等でTTFT短縮に重要と説明される。
- チャンク分割では文脈断裂や同時処理の弱さが問題として挙げられる。
- 真のストリーミングには因果的注意と段階的学習が要件と記載される。
- vLLM nightlyとmistral-commonを導入し、Voxtralで約13GB VRAMを使用した。
- WebSocket/Gradioのサンプルで音声ファイルとマイクのリアルタイム文字起こしを行った。

### Key Findings
- 入力ストリーミングとリアルタイムWebSocket APIの提供が公式に告知されている。 [^]
  - Footnote: 「Streaming input + Realtime WebSocket API」
- 入力ストリーミングはセッションベースの更新設計としてPRで議論されている。 [^]
  - Footnote: 「[Feature] add session based streaming input support to v1」
- 真のストリーミング推論には注意機構パターンと段階的学習の要件がある。 [^]
  - Footnote: 「以下の2つの重要な要件を満たす必要があります：適切な注意機構パターンと、段階的な処理に対応した学習です。」
- VoxtralでのvLLMサーバ起動時、VRAM消費は約13GBと記載されている。 [^]
  - Footnote: 「VRAM消費は13GB程度。」
- 導入したvLLMはnightly系で、mistral-common 1.9.0が入ったと記録されている。 [^]
  - Footnote: 「+ mistral-common==1.9.0」「+ vllm==0.16.0rc2.dev94+g786806dd4」
- クライアントのサンプルはWebSocketの音声ファイル文字起こしとGradioマイクの2種。 [^]
  - Footnote: 「クライアントのサンプルコードは2つ用意されている。」
- Gradio GUIからマイク音声でリアルタイム文字起こしを行った。 [^]
  - Footnote: 「Gradio GUIからWebSocketで接続してマイク音声をリアルタイム文字起こし。」

### References
- https://zenn.dev/kun432/scraps/905a0f48fac106

## Wikipedia: AI生成記事の特徴 ⑦その他

### Executive Summary
- WikipediaのAI生成記事検出指標「その他」セクションを整理した。
- 文体が途中で急変し不自然に完璧な文法になる点が指標とされる。
- 英語の地域的用法が突然変化する場合も疑いポイントとされる。
- AI生成の編集要約は長文・形式的・略語なし等の傾向が列挙されている。
- AfC下書きで査読者向けの提出声明が含まれることがあると指摘される。
- AfCや保護テンプレートの不適切挿入が検知材料になると説明される。
- LLM文体が一般化すると文体検出が難しくなる可能性に言及している。

### Key Findings
- 文体が突然変わり不自然に完璧な文法になる場合はAI利用の可能性がある。 [^]
  - Footnote: 「記事の途中で文体が突然変わり、普段よりも不自然に完璧な文法になっている場合」
- 英語の地域的用法が突然完全に変化した場合は疑うべきとされる。 [^]
  - Footnote: 「英語の用法が突然＋完全に変化している場合にのみ、その可能性を疑うべき」
- AI生成の編集要約は長文、形式的な一人称、略語なし等の傾向がある。 [^]
  - Footnote: 「一般的な記述よりも遥かに長文」「形式的な一人称の段落形式」「略語を使用しない」
- AfC下書きに査読者向け提出声明が含まれるとAI生成と判断されやすい。 [^]
  - Footnote: 「査読者はこれを見た場合、AI生成と即時に判断して却下・削除できる。」
- AfC submissionテンプレートの却下済み文言を含む生成はプロセス上あり得ない。 [^]
  - Footnote: 「プロセス上起こり得ないため、査読者は理由なしで即時却下することになる」
- pp/pp-move等の保護テンプレートは管理者のみ設定可能でAfCでは使われない。 [^]
  - Footnote: 「保護されたページで使用されるテンプレートで…AFCでこういったテンプレートが使用されることはあり得ない。」
- AI生成の注意書きが冒頭に追記される例があると述べられている。 [^]
  - Footnote: 「冒頭にAI生成による旨が注意書きとして追記されている様子。」

### References
- https://zenn.dev/kun432/scraps/56ade16ea8b426
