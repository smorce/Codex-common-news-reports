# YouTube Video Summary Report (Error)

- Generated at: 2026-07-23T00:20:29Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
00:00, 528.30it/s]
Loading weights: 100%|██████████| 1951/1951 [01:18<00:00, 24.86it/s] 

[INFO] (1/3) Downloading… '短パンが苦手な大人におすすめ！夏の最新グレスラを徹底解説！| B.R. Fashion College Lesson.894 グレーパンツ特集'
[INFO] Downloaded: gemma4_cache\01_W-OJSuYQjWM.mp4 (44.91 MB)
[INFO] (1/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 60 frame(s), sampling=uniform, duration=932.10s, first=7.77s, last=924.33s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 60 frame(s), window_size=8, windows=8
[INFO]   Window 1/8: frames=8, range=00:08-01:57
[INFO]   Window 2/8: frames=8, range=02:12-04:01
[INFO]   Window 3/8: frames=8, range=04:16-06:05
[INFO]   Window 4/8: frames=8, range=06:21-08:09
[INFO]   Window 5/8: frames=8, range=08:25-10:14
[INFO]   Window 6/8: frames=8, range=10:29-12:18
[INFO]   Window 7/8: frames=8, range=12:33-14:22
[INFO]   Window 8/8: frames=4, range=14:38-15:24

[INFO] (2/3) Downloading… 'メンズのTシャツは減点方式！？体型別ベストTシャツは？【ゆなてぃイベント開催】'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\02_Fr7d0Bg34_8.%(ext)s', 'https://www.youtube.com/watch?v=Fr7d0Bg34_8', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
