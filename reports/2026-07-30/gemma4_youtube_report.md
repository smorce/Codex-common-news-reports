# YouTube Video Summary Report (Error)

- Generated at: 2026-07-30T00:19:02Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
:23
[INFO]   Window 8/8: frames=4, range=18:43-19:43

[INFO] (2/3) Downloading… '男の清潔感はどう変える？大人男子の見た目を変えた！宮永えいとが語る"身だしなみ文化"｜B.R.CHANNEL THE INTUITION #19'
[INFO] Downloaded: gemma4_cache\02_d0yVN81boHE.mp4 (81.58 MB)
[INFO] (2/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 60 frame(s), sampling=uniform, duration=1723.73s, first=14.36s, last=1709.37s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 60 frame(s), window_size=8, windows=8
[INFO]   Window 1/8: frames=8, range=00:14-03:35
[INFO]   Window 2/8: frames=8, range=04:04-07:25
[INFO]   Window 3/8: frames=8, range=07:54-11:15
[INFO]   Window 4/8: frames=8, range=11:44-15:05
[INFO]   Window 5/8: frames=8, range=15:34-18:55
[INFO]   Window 6/8: frames=8, range=19:24-22:45
[INFO]   Window 7/8: frames=8, range=23:13-26:34
[INFO]   Window 8/8: frames=4, range=27:03-28:29

[INFO] (3/3) Downloading… '短パンが苦手な大人におすすめ！夏の最新グレスラを徹底解説！| B.R. Fashion College Lesson.894 グレーパンツ特集'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\03_W-OJSuYQjWM.%(ext)s', 'https://www.youtube.com/watch?v=W-OJSuYQjWM', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
