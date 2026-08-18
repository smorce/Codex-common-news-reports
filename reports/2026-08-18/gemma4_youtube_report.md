# YouTube Video Summary Report (Error)

- Generated at: 2026-08-18T00:18:45Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
nload video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=-mNgZHTLpmw
[youtube] -mNgZHTLpmw: Downloading webpage
[youtube] -mNgZHTLpmw: Downloading android vr player API JSON
[youtube] -mNgZHTLpmw: Downloading web safari player API JSON
[info] -mNgZHTLpmw: Downloading 1 format(s): 18
[INFO] yt-dlp format='b' merge=None
[WARNING] yt-dlp failed (b): ERROR: unable to download video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=-mNgZHTLpmw
[youtube] -mNgZHTLpmw: Downloading webpage
[youtube] -mNgZHTLpmw: Downloading android vr player API JSON
[youtube] -mNgZHTLpmw: Downloading web safari player API JSON
[info] -mNgZHTLpmw: Downloading 1 format(s): 18
[INFO] yt-dlp format='best[ext=mp4]/best' merge=None
[WARNING] yt-dlp failed (best[ext=mp4]/best): ERROR: unable to download video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=-mNgZHTLpmw
[youtube] -mNgZHTLpmw: Downloading webpage
[youtube] -mNgZHTLpmw: Downloading android vr player API JSON
[youtube] -mNgZHTLpmw: Downloading web safari player API JSON
[info] -mNgZHTLpmw: Downloading 1 format(s): 18
[INFO] Skipping (download): '女子が本当に好きなショートパンツスタイルって？上品×抜け感で作るコーデ3選♪ Press Room 119' — ERROR: unable to download video data: HTTP Error 403: Forbidden
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1801, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1777, in main
    raise RuntimeError(
RuntimeError: Only 1 video(s) summarized from 15 candidates (need 3). Members-only or unavailable videos may dominate the channel feed.

```
