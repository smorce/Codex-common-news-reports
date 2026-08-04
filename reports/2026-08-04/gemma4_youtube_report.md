# YouTube Video Summary Report (Error)

- Generated at: 2026-08-04T00:19:34Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
71.38it/s]
Loading weights: 100%|██████████| 1951/1951 [00:30<00:00, 64.34it/s] 

[INFO] (1/3) Downloading… '清潔感命！女子は短パンのどこを見てる？大人が絶対気をつけたいポイント！'
[INFO] Downloaded: gemma4_cache\01_d1PPWcbyFo8.mp4 (67.26 MB)
[INFO] (1/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 60 frame(s), sampling=uniform, duration=1307.14s, first=10.89s, last=1296.25s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 60 frame(s), window_size=8, windows=8
[INFO]   Window 1/8: frames=8, range=00:11-02:43
[INFO]   Window 2/8: frames=8, range=03:05-05:38
[INFO]   Window 3/8: frames=8, range=05:59-08:32
[INFO]   Window 4/8: frames=8, range=08:54-11:26
[INFO]   Window 5/8: frames=8, range=11:48-14:21
[INFO]   Window 6/8: frames=8, range=14:42-17:15
[INFO]   Window 7/8: frames=8, range=17:37-20:09
[INFO]   Window 8/8: frames=4, range=20:31-21:36

[INFO] (2/3) Downloading… '良いシャツの見分け方！名門ナポリシャツの魅力とは？マシンとハンドを徹底解剖 | B.R. Fashion College Lesson.895 ナポリシャツ特集'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\02_A3T9PhBENhc.%(ext)s', 'https://www.youtube.com/watch?v=A3T9PhBENhc', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
