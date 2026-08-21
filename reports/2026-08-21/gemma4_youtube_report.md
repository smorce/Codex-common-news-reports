# YouTube Video Summary Report (Error)

- Generated at: 2026-08-21T00:08:12Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
03: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=Fr7d0Bg34_8
[youtube] Fr7d0Bg34_8: Downloading webpage
[youtube] Fr7d0Bg34_8: Downloading android vr player API JSON
[youtube] Fr7d0Bg34_8: Downloading web safari player API JSON
[info] Fr7d0Bg34_8: Downloading 1 format(s): 18
[INFO] yt-dlp format='b' merge=None
[WARNING] yt-dlp failed (b): ERROR: unable to download video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=Fr7d0Bg34_8
[youtube] Fr7d0Bg34_8: Downloading webpage
[youtube] Fr7d0Bg34_8: Downloading android vr player API JSON
[youtube] Fr7d0Bg34_8: Downloading web safari player API JSON
[youtube] Fr7d0Bg34_8: Downloading player e937390a-tv
[youtube] [jsc:node] Solving JS challenges using node
[info] Fr7d0Bg34_8: Downloading 1 format(s): 18
[INFO] yt-dlp format='best[ext=mp4]/best' merge=None
[WARNING] yt-dlp failed (best[ext=mp4]/best): ERROR: unable to download video data: HTTP Error 403: Forbidden
ERROR: unable to download video data: HTTP Error 403: Forbidden

[youtube] Extracting URL: https://www.youtube.com/watch?v=Fr7d0Bg34_8
[youtube] Fr7d0Bg34_8: Downloading webpage
[youtube] Fr7d0Bg34_8: Downloading android vr player API JSON
[youtube] Fr7d0Bg34_8: Downloading web safari player API JSON
[info] Fr7d0Bg34_8: Downloading 1 format(s): 18
[INFO] Skipping (download): 'メンズのTシャツは減点方式！？体型別ベストTシャツは？【ゆなてぃイベント開催】' — ERROR: unable to download video data: HTTP Error 403: Forbidden
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1801, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1777, in main
    raise RuntimeError(
RuntimeError: Only 1 video(s) summarized from 15 candidates (need 3). Members-only or unavailable videos may dominate the channel feed.

```
