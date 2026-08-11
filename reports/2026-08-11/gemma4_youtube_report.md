# YouTube Video Summary Report (Error)

- Generated at: 2026-08-11T00:16:25Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
   Window 7/8: frames=8, range=12:56-14:47
[INFO]   Window 8/8: frames=4, range=15:03-15:51

[INFO] (2/3) Downloading… '長い夏も洒落て見せる！大人の旬アイテムでトータルスタイル提案！| B.R. Fashion College Lesson.896 アウール'
[INFO] Downloaded: gemma4_cache\02_XgrZa8_4VBI.mp4 (63.86 MB)
[INFO] (2/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 60 frame(s), sampling=uniform, duration=1544.89s, first=12.87s, last=1532.02s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 60 frame(s), window_size=8, windows=8
[INFO]   Window 1/8: frames=8, range=00:13-03:13
[INFO]   Window 2/8: frames=8, range=03:39-06:39
[INFO]   Window 3/8: frames=8, range=07:05-10:05
[INFO]   Window 4/8: frames=8, range=10:31-13:31
[INFO]   Window 5/8: frames=8, range=13:57-16:57
[INFO]   Window 6/8: frames=8, range=17:23-20:23
[INFO]   Window 7/8: frames=8, range=20:49-23:49
[INFO]   Window 8/8: frames=4, range=24:15-25:32

[INFO] (3/3) Downloading… '清潔感命！女子は短パンのどこを見てる？大人が絶対気をつけたいポイント！'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\03_d1PPWcbyFo8.%(ext)s', 'https://www.youtube.com/watch?v=d1PPWcbyFo8', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
