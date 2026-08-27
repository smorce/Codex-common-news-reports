# YouTube Video Summary Report (Error)

- Generated at: 2026-08-27T00:23:36Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
ng URL: https://www.youtube.com/watch?v=d0yVN81boHE
[youtube] d0yVN81boHE: Downloading webpage
[youtube] d0yVN81boHE: Downloading android vr player API JSON
[youtube] d0yVN81boHE: Downloading web safari player API JSON
[youtube] d0yVN81boHE: Downloading player 6a0e84d6-tv
[youtube] [jsc:node] Solving JS challenges using node
[info] d0yVN81boHE: Downloading 1 format(s): 18
[INFO] yt-dlp format='b' merge=None
[WARNING] yt-dlp failed (b): ERROR: unable to download video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=d0yVN81boHE
[youtube] d0yVN81boHE: Downloading webpage
[youtube] d0yVN81boHE: Downloading android vr player API JSON
[youtube] d0yVN81boHE: Downloading web safari player API JSON
[info] d0yVN81boHE: Downloading 1 format(s): 18
[INFO] yt-dlp format='best[ext=mp4]/best' merge=None
[WARNING] yt-dlp failed (best[ext=mp4]/best): ERROR: unable to download video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=d0yVN81boHE
[youtube] d0yVN81boHE: Downloading webpage
[youtube] d0yVN81boHE: Downloading android vr player API JSON
[youtube] d0yVN81boHE: Downloading web safari player API JSON
[info] d0yVN81boHE: Downloading 1 format(s): 18
[INFO] Skipping (download): '男の清潔感はどう変える？大人男子の見た目を変えた！宮永えいとが語る"身だしなみ文化"｜B.R.CHANNEL THE INTUITION #19' — ERROR: unable to download video data: HTTP Error 403: Forbidden
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1801, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1777, in main
    raise RuntimeError(
RuntimeError: Only 1 video(s) summarized from 15 candidates (need 3). Members-only or unavailable videos may dominate the channel feed.

```
