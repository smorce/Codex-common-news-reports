# YouTube Video Summary Report (Error)

- Generated at: 2026-08-25T00:17:58Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
催！'
[INFO] yt-dlp format='bv*+ba/b' merge='mp4'
[INFO] Downloaded: gemma4_cache\01_1.mp4 (2.17 MB)
[INFO] (1/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 31 frame(s), sampling=uniform, duration=30.68s, first=0.49s, last=30.18s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 31 frame(s), window_size=8, windows=4
[INFO]   Window 1/4: frames=8, range=00:00-00:07
[INFO]   Window 2/4: frames=8, range=00:08-00:15
[INFO]   Window 3/4: frames=8, range=00:16-00:23
[INFO]   Window 4/4: frames=7, range=00:24-00:30
[INFO] Skipping (probe): '人気上昇中！半袖シャツの大人モテコーデ♪ コスパも抜群なおすすめスタイル！ Press Room 120 ジーステージ' — [youtube] AjA8NVsIfVc: Downloading initial data API JSON
[INFO] Skipping (probe): '長い夏も洒落て見せる！大人の旬アイテムでトータルスタイル提案！| B.R. Fashion College Lesson.896 アウール' — [youtube] XgrZa8_4VBI: Downloading initial data API JSON
[INFO] Skipping (probe): '清潔感命！女子は短パンのどこを見てる？大人が絶対気をつけたいポイント！' — [youtube] d1PPWcbyFo8: Downloading initial data API JSON
[INFO] Skipping (probe): '良いシャツの見分け方！名門ナポリシャツの魅力とは？マシンとハンドを徹底解剖 | B.R. Fashion College Lesson.895 ナポリシャツ特集' — [youtube] A3T9PhBENhc: Downloading initial data API JSON
[INFO] Skipping (probe): '男の清潔感はどう変える？大人男子の見た目を変えた！宮永えいとが語る"身だしなみ文化"｜B.R.CHANNEL THE INTUITION #19' — [youtube] d0yVN81boHE: Downloading initial data API JSON
[INFO] Skipping (probe): '短パンが苦手な大人におすすめ！夏の最新グレスラを徹底解説！| B.R. Fashion College Lesson.894 グレーパンツ特集' — [youtube] W-OJSuYQjWM: Downloading initial data API JSON
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1801, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1777, in main
    raise RuntimeError(
RuntimeError: Only 1 video(s) summarized from 15 candidates (need 3). Members-only or unavailable videos may dominate the channel feed.

```
