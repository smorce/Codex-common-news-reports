# AI Common Report (https://ai-news.dev/)

- Generated at: 2026-04-01T09:52:41.8378344+09:00
- Articles: 3

## メルカリグループ AI活用基本ポリシー | 株式会社メルカリ

### Executive Summary
- AIの可能性を最大限に引き出し、リスク管理とイノベーションの両立を目的とする基本方針を示している。
- ミッション達成のためにAIを活用し、社会やステークホルダーへの影響リスクに向き合う姿勢を明記している。
- 人間中心のAI社会原則を参照し、多様な人々の可能性を広げる活用を掲げる。
- 包摂性と公平性の確保を重視し、利用者への影響に配慮する方針を示す。
- 他者の権利侵害を防ぐための対策や、生成物の確認体制など適法・倫理的利用を求める。
- AIシステムの機能・利用データ・出力精度やリスクを説明し、透明性と説明責任を高める。
- 技術進展や法規の変化を踏まえ、ポリシーとAIガバナンスを定期的に見直す。

### Key Findings
- AI活用の目的は、可能性の最大化とリスク管理の両立である。 [^]
  - Footnote: 「AIの可能性を最大限に引き出し、AI活用に伴うリスク管理とイノベーションを両立」
- AIはミッション達成を加速させる重要な役割として位置付けられている。 [^]
  - Footnote: 「ミッション達成を加速させる上で、ますます重要な役割を担う」
- 人間中心のAI社会原則に基づいた活用を掲げている。 [^]
  - Footnote: 「人間中心のAI社会原則」
- 他者の権利侵害を避けるための対策と、生成物の確認体制を求めている。 [^]
  - Footnote: 「他者の権利を侵害しないよう必要な対策」および「社内の確認体制を整備し、適法かつ倫理的な利用を徹底」
- AIシステムの機能や利用データ、出力精度や潜在的リスクを説明する方針を示す。 [^]
  - Footnote: 「AIシステムの機能、利用データ、その出力結果の精度や潜在的リスクについて...適切に説明」
- AI技術や法規の変化を踏まえ、ポリシーとガバナンスを定期的に見直す。 [^]
  - Footnote: 「AI技術の急速な進展、関連法規や社会規範の変化...定期的に見直し」

### References
- https://about.mercari.com/ai-policy/

## ローカルAIを活用したら、大量のサブスクが解約できたぞ！
- Date: 2026-03-31

### Executive Summary
- ローカルLLMの活用で、検索や要約などのサブスク依存を減らせると紹介している。
- ファイルへのアクセス権付与は難しそうだが、実際はシンプルだと述べる。
- RAGを用いてファイルを小さな塊に分割し、ベクトル埋め込みとして保存する。
- 質問時は関連部分だけを検索し、ファイルはPC外に出さずに回答できる。
- GPT4AllのLocalDocsでフォルダ指定の自動インデックス作成が可能とする。
- AnythingLLMはPDFやWordなどを処理でき、プロジェクト別ワークスペースを作れる。
- OllamaでLLaMA 3の3B量子化モデルを動かし、必要に応じて8B/13Bも検討できる。

### Key Findings
- ローカルLLMがあれば、作業を簡単かつ効率的にできると示している。 [^]
  - Footnote: 「ローカルLLMさえあれば、より簡単に、より効率的に作業することができる」
- RAGを使い、ファイルを小さな塊に分割してベクトル埋め込みに変換する。 [^]
  - Footnote: 「RAG...ファイルを小さな塊に分割して...『ベクトル埋め込み』に変換」
- 質問時は関連部分のみ検索し、ファイルはPC外に出ない。 [^]
  - Footnote: 「もっとも関連性の高い部分だけを検索」「ファイルが自身のPCの外に出ることなく」
- GPT4AllのLocalDocsはフォルダ指定で自動インデックス作成を行う。 [^]
  - Footnote: 「GPT4Allの『LocalDocs』...フォルダを指定するだけで自動的にファイルのインデックス作成」
- AnythingLLMはPDFやWord、TXT、CSVを処理し、ワークスペースを構築できる。 [^]
  - Footnote: 「PDF、Word、TXT、CSVファイルを処理でき、プロジェクトごとに別々のワークスペースを構築」
- 完全オフラインで動作し、必要条件は十分な処理能力である。 [^]
  - Footnote: 「どちらのツールも完全にオフラインで動作し、唯一の条件は...十分な処理能力」
- OllamaでLLaMA 3の3B量子化モデルを動かし、必要なら8B/13Bも検討できる。 [^]
  - Footnote: 「Ollamaを使ってLLaMA 3の3B量子化モデル」「8Bや13Bのモデルに挑戦」

### References
- https://www.lifehacker.jp/article/2603-gave-local-llm-access-to-files-replaced-three-apps/

## Release: llm-all-models-async 0.1
- Date: 2026-03-31T20:52:00

### Executive Summary
- LLMプラグインは同期モデルと非同期モデルの両方を定義できると説明している。
- 非同期版はAPIバックエンドで一般的で、同期版はプラグイン内で直接実行する傾向がある。
- 著者のllm-mrchatterboxは同期のみで、Datasetteの機能では非同期が必要だった。
- 同期モデルをスレッドプールで非同期化するプラグインを作成した。
- そのためにLLM本体に追加のプラグインフック機構が必要になった。
- 新フックはLLM 0.30で公開されたと記している。
- リリースはllm-all-models-async 0.1として公開されている。

### Key Findings
- LLMプラグインは同期と非同期のモデルを定義できる。 [^]
  - Footnote: 「LLM plugins can define new models in both sync and async varieties」
- 非同期はAPIモデルで一般的、同期はプラグイン内で直接実行される。 [^]
  - Footnote: 「async variants are most common for API-backed models」「sync variants tend to be things that run the model directly within the plugin」
- Datasetteは非同期モデルのみ利用できるため、同期専用プラグインでは不都合がある。 [^]
  - Footnote: 「Datasette can only use async models」
- 同期モデルをスレッドプールで非同期化するプラグインを作成した。 [^]
  - Footnote: 「turns sync models into async models using a thread pool」
- この対応にはLLM本体の新しいプラグインフックが必要だった。 [^]
  - Footnote: 「ended up needing an extra plugin hook mechanism in LLM itself」
- 新フックはLLM 0.30で提供された。 [^]
  - Footnote: 「shipped just now in LLM 0.30」

### References
- https://simonwillison.net/2026/Mar/31/llm-all-models-async/
