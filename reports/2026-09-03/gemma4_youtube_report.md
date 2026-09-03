# YouTube Video Summary Report (Error)

- Generated at: 2026-09-03T00:20:01Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=XgrZa8_4VBI
[youtube] XgrZa8_4VBI: Downloading webpage
[youtube] XgrZa8_4VBI: Downloading android vr player API JSON
[youtube] XgrZa8_4VBI: Downloading web safari player API JSON
[info] XgrZa8_4VBI: Downloading 1 format(s): 18
[INFO] yt-dlp format='b' merge=None
[WARNING] yt-dlp failed (b): ERROR: unable to download video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=XgrZa8_4VBI
[youtube] XgrZa8_4VBI: Downloading webpage
[youtube] XgrZa8_4VBI: Downloading android vr player API JSON
[youtube] XgrZa8_4VBI: Downloading web safari player API JSON
[info] XgrZa8_4VBI: Downloading 1 format(s): 18
[INFO] yt-dlp format='best[ext=mp4]/best' merge=None
[WARNING] yt-dlp failed (best[ext=mp4]/best): ERROR: unable to download video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=XgrZa8_4VBI
[youtube] XgrZa8_4VBI: Downloading webpage
[youtube] XgrZa8_4VBI: Downloading android vr player API JSON
[youtube] XgrZa8_4VBI: Downloading web safari player API JSON
[info] XgrZa8_4VBI: Downloading 1 format(s): 18
[INFO] Skipping (download): '長い夏も洒落て見せる！大人の旬アイテムでトータルスタイル提案！| B.R. Fashion College Lesson.896 アウール' — ERROR: unable to download video data: HTTP Error 403: Forbidden
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1801, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1777, in main
    raise RuntimeError(
RuntimeError: Only 1 video(s) summarized from 15 candidates (need 3). Members-only or unavailable videos may dominate the channel feed.

```
