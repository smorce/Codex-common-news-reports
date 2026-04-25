# AI Common Report (https://zenn.dev/kun432?tab=scraps)

- Generated at: 2026-04-25T11:17:31.7147124+09:00
- Articles: 3

## Terraformのコードから最小のIAM権限をリストアップしてくれる「Pike」を試す

### Executive Summary
- Terraform/OpenTofu のコードから必要最小限の IAM 権限を洗い出す Pike を試している。
- LLM に IAM ポリシーを作らせる方法は、足りなかったり多すぎたりして判断が難しいと述べている。
- Pike は古い記事で紹介されていたが、現在も更新されている様子だと確認している。
- 対応対象は OpenTofu/Terraform と AWS/GCP/Azure で、最近は機能追加も入っている。
- 記事では JSON モジュール、GCP 比較、バックエンド検出の追加が挙げられている。
- Ubuntu 24.04 では Go 環境を用意してソースから入れる手順を採っている。
- 実行時に make が失敗したため、terraform init / plan / apply へ切り替える流れになっている。

### Key Findings
- Pike の狙いは Terraform/OpenTofu の実行に必要な最小権限を抽出すること。 [^]
  - Footnote: 記事本文で、インフラコードに必要な最小限の IAM 権限を判定するツールだと説明されている。
- LLM による権限推定は不完全になりやすく、手作業確認が必要になりがち。 [^]
  - Footnote: 冒頭で、LLM にやらせても不足や過剰が起きやすいという懸念が述べられている。
- Pike は古い紹介記事のツールだが、現行でも更新が続いている。 [^]
  - Footnote: 本文で 2022 年の記事由来でありつつ、更新が入っていることを確認している。
- 最近の機能追加として JSON モジュール対応と GCP 比較機能がある。 [^]
  - Footnote: 本文に JSON モジュールのサポート追加と、GCP のデプロイ済みロール比較が挙がっている。
- バックエンド検出も追加され、S3 と GCP に対応している。 [^]
  - Footnote: 記事中で backend detection 機能の追加が明記されている。
- 実運用では make 実行時に policyDocument の ASCII 制約で失敗している。 [^]
  - Footnote: エラーログに policyDocument が printable ASCII でないため無効という IAM エラーが出ている。
- 回避策として、生成済みの .pike 配下に対して terraform init / plan / apply を直接実行している。 [^]
  - Footnote: 記事の後半で、再度 make せずに cd .pike から terraform を実行する手順が示されている。

### References
- https://zenn.dev/kun432/scraps/36b36da97dd228
- https://github.com/JamesWoolfenden/pike
- https://dev.classmethod.jp/articles/pike-terraform-generate-iam-policy/

## 「LiteParse」を試す

### Executive Summary
- LiteParse は複雑な PDF レイアウトを空間グリッドに整理する OSS のドキュメントパーサー。
- VLM や ML モデルに依存せず、ヒューリスティクスだけで動く点を強調している。
- Y 座標で行を揃え、アンカーを抽出し、テキストをグリッド列へ投影する流れが中核になっている。
- 複数カラムや表を含む PDF でも構造を保った抽出がしやすい。
- CLI として使えるが、記事ではブラウザ版を試作している。
- 公式ブログの deep dive と GitHub リポジトリが案内されている。
- 総じて、文書抽出の高速・軽量な選択肢として紹介されている。

### Key Findings
- LiteParse は複雑な PDF レイアウト、テキスト、表をクリーンな空間グリッドに解析する。 [^]
  - Footnote: 記事冒頭で、複雑な PDF を空間グリッドへ解析するのが得意だと説明されている。
- 推論系モデルを使わず、ヒューリスティクスベースで高速に動作する。 [^]
  - Footnote: 本文で VLM や ML モデルを使わず、完全にヒューリスティクスベースだと述べている。
- 処理の要点は、Y 座標で行を並べ、左・右・中央アンカーを使って分類すること。 [^]
  - Footnote: 番号付きで、行ソート、アンカー抽出、分類、グリッド投影の流れが示されている。
- 投影後は後処理で余白や不要なスペースを削る。 [^]
  - Footnote: 手順の最後に、余分なスペースとマージンを取り除くと説明されている。
- CLI だけでなく、コーディングエージェント統合も想定されている。 [^]
  - Footnote: 記事で、CLI 経由またはコーディングエージェントへの統合で使えると書かれている。
- 著者は Node.js CLI しかないため、ブラウザで動く版を作ったと述べている。 [^]
  - Footnote: 本文に、Node.js CLI のみだったのでブラウザ版を作ったという説明がある。

### References
- https://zenn.dev/kun432/scraps/7a6de84125d54c
- https://llamaindex.ai/blog/how-liteparse-turns-pdfs-into-text-a-deep-dive-into-the-grid-projection-algorithm
- https://github.com/run-llama/liteparse

## 「GPT画像生成モデル プロンプトガイド」を試す

### Executive Summary
- OpenAI の gpt-image モデルのプロンプトガイドを翻訳しながら試している。
- gpt-image-2 は本番用途の既定候補として位置づけられている。
- 品質と遅延のトレードオフを調整でき、low / medium / high の使い分けがある。
- gpt-image-2 のサイズは柔軟だが、辺の長さや総ピクセル数に制約がある。
- インフォグラフィック、翻訳、フォトリアル、ロゴ、広告、UI、科学図解、スライドなど多様な用途が整理されている。
- テキスト入り画像や編集系では、レイアウトやラベルの明示が重要とされる。
- 結論として、実務では gpt-image-2 を中心に設計するのが基本になっている。

### Key Findings
- gpt-image-2 はクリエイティブワークフロー向けで、高品質と制御性が重視される。 [^]
  - Footnote: 記事冒頭で、制作向けの高い制御性と品質を持つモデルだとまとめられている。
- 新規利用では gpt-image-2 がデフォルト推奨で、gpt-image-1 系は移行対象として扱われる。 [^]
  - Footnote: モデル比較表で、新規では gpt-image-2 を推奨し、旧モデルは互換用途とされている。
- 品質設定は low / medium / high のトレードオフで、速度重視なら low が推奨される。 [^]
  - Footnote: 本文に、低遅延重視なら low、品質重視なら high という整理がある。
- サイズ指定には最大辺 3840px 未満、16 の倍数、3:1 未満、総ピクセル数制約がある。 [^]
  - Footnote: gpt-image-2 のサイズ制約として、辺長・比率・総ピクセルの条件が列挙されている。
- 実務でよく使うサイズとして 1024x1024、1024x1536、1536x1024、2560x1440、3840x2160 が整理されている。 [^]
  - Footnote: よく使われるサイズ一覧に、用途別の代表解像度が並んでいる。
- 用途別には、インフォグラフィック、UI モックアップ、科学図解、スライド作成などのガイドがある。 [^]
  - Footnote: 目次と本文で、複数の代表ユースケースが細かく章立てされている。
- テキスト入りの図やスライドでは、ラベル・数値・余白・可読性を明示することが重要。 [^]
  - Footnote: スライド/図解の節で、テキストや数値を直接書き込み、装飾を抑えるよう勧めている。

### References
- https://zenn.dev/kun432/scraps/b554956579241c
- https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
- https://github.com/openai/openai-cookbook/tree/main/examples/multimodal/image-gen-models-prompting-guide.ipynb
