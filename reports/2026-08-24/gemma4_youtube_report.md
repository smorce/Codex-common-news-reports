# YouTube Video Summary Report (Error)

- Generated at: 2026-08-24T00:20:22Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
ing URL: https://www.youtube.com/watch?v=W-OJSuYQjWM
[youtube] W-OJSuYQjWM: Downloading webpage
[youtube] W-OJSuYQjWM: Downloading android vr player API JSON
[youtube] W-OJSuYQjWM: Downloading web safari player API JSON
[info] W-OJSuYQjWM: Downloading 1 format(s): 18
[INFO] yt-dlp format='b' merge=None
[WARNING] yt-dlp failed (b): ERROR: unable to download video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=W-OJSuYQjWM
[youtube] W-OJSuYQjWM: Downloading webpage
[youtube] W-OJSuYQjWM: Downloading android vr player API JSON
[youtube] W-OJSuYQjWM: Downloading web safari player API JSON
[youtube] W-OJSuYQjWM: Downloading player 2574220e-tv
[youtube] [jsc:node] Solving JS challenges using node
[info] W-OJSuYQjWM: Downloading 1 format(s): 18
[INFO] yt-dlp format='best[ext=mp4]/best' merge=None
[WARNING] yt-dlp failed (best[ext=mp4]/best): ERROR: unable to download video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=W-OJSuYQjWM
[youtube] W-OJSuYQjWM: Downloading webpage
[youtube] W-OJSuYQjWM: Downloading android vr player API JSON
[youtube] W-OJSuYQjWM: Downloading web safari player API JSON
[info] W-OJSuYQjWM: Downloading 1 format(s): 18
[INFO] Skipping (download): '短パンが苦手な大人におすすめ！夏の最新グレスラを徹底解説！| B.R. Fashion College Lesson.894 グレーパンツ特集' — ERROR: unable to download video data: HTTP Error 403: Forbidden
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1801, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1777, in main
    raise RuntimeError(
RuntimeError: Only 1 video(s) summarized from 15 candidates (need 3). Members-only or unavailable videos may dominate the channel feed.

```
