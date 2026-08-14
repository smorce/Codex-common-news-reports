# YouTube Video Summary Report (Error)

- Generated at: 2026-08-14T00:09:25Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
4it/s]
Loading weights:  99%|█████████▉| 1931/1951 [00:41<00:00, 611.02it/s]
Loading weights: 100%|██████████| 1951/1951 [00:41<00:00, 47.03it/s] 

[INFO] (1/3) Downloading… '街中にイケオジはどれだけいるのか？仕事は？趣味は？イケオジ突撃インタビュー！'
[INFO] Downloaded: gemma4_cache\01_L-v8vduouuc.mp4 (81.28 MB)
[INFO] (1/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 60 frame(s), sampling=uniform, duration=1379.13s, first=11.49s, last=1367.63s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 60 frame(s), window_size=8, windows=8
[INFO]   Window 1/8: frames=8, range=00:11-02:52
[INFO]   Window 2/8: frames=8, range=03:15-05:56
[INFO]   Window 3/8: frames=8, range=06:19-09:00
[INFO]   Window 4/8: frames=8, range=09:23-12:04
[INFO]   Window 5/8: frames=8, range=12:27-15:08
[INFO]   Window 6/8: frames=8, range=15:31-18:12
[INFO]   Window 7/8: frames=8, range=18:35-21:16
[INFO]   Window 8/8: frames=4, range=21:39-22:48

[INFO] (2/3) Downloading… '広瀬さんがブランド立ち上げ！試着会もやるよ♪'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\02_2.%(ext)s', 'https://www.youtube.com/shorts/2AhE3YDcDH0', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
