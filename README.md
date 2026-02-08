https://github.com/smorce/Codex-common-news-reports


uv add -r requirements.txt --link-mode=copy


~/.codex/config.toml を作って chrome-devtools-mcp をヘッドレスで動かすようにした。
グローバルの config.toml は使わないようにした。




# BRチャンネルの動画をダウンロードして最新 TOP N の動画をGeminiCLIで要約してレポートする。mp4は削除。
uv run --link-mode=copy yt_top3_gemini_report.py "https://www.youtube.com/channel/UCUWtuyVjeMQygQiy3adHb1g" -o out_report -n 5


uv run --link-mode=copy yt_top3_gemini_report.py "https://www.youtube.com/channel/UCUWtuyVjeMQygQiy3adHb1g" -o out_report -n 5 --model gemini-3-flash-preview
→3.0 はレートリミットエラーが出やすいので微妙。
- 生成物: out_report/report.md と out_report/mp4/ 以下のMP4





# コモンニュースを取得したい場合は以下を実行するだけ。AGENTS.md の指示が動き出す。勝手にブラウザが開く。
codex -m gpt-5.1-codex-mini --yolo -c model_reasoning_effort="high" --search "$@"
→あとは、マークダウンにまとめてGitHubにPUSHすれば携帯からも見られるようになる。
みたいサイトはドンドン追加すれば良い。政治・芸能・科学・アメリカ など。


.\run_codex_spinner.ps1




# Chrome DevTools MCP
以下はうまくいったプロンプト:
---
https://ai-news.dev/ を開いて安定するまで待って。
そこから最新の記事3件のURLを開いて各ページの要約を提示してください。                      
---
これで特定のURLを指定してスクレイピングできる。
"--headless=true" にするとMCPが使われないので注意。


========================================


# Web検索ありで起動
codex -m gpt-5.1-codex-mini --yolo -c model_reasoning_effort="high" --search "$@"

