# YouTube Video Summary Report (Error)

- Generated at: 2026-06-26T00:28:31Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
1-21:55
[INFO]   Window 7/8: frames=8, range=22:22-25:36
[INFO]   Window 8/8: frames=4, range=26:04-27:27

[INFO] (2/3) Downloading… '白Tのお悩み解決！夏の黒やネイビーが優秀＆体型カバーにおすすめの選び方！| B.R. Fashion College Lesson.890 ダークトーン特集'
[INFO] Downloaded: gemma4_cache\02_ZsSDJqAXJmg.mp4 (55.80 MB)
[INFO] (2/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 60 frame(s), sampling=uniform, duration=1272.31s, first=10.60s, last=1261.71s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 60 frame(s), window_size=8, windows=8
[INFO]   Window 1/8: frames=8, range=00:11-02:39
[INFO]   Window 2/8: frames=8, range=03:00-05:29
[INFO]   Window 3/8: frames=8, range=05:50-08:18
[INFO]   Window 4/8: frames=8, range=08:40-11:08
[INFO]   Window 5/8: frames=8, range=11:29-13:58
[INFO]   Window 6/8: frames=8, range=14:19-16:47
[INFO]   Window 7/8: frames=8, range=17:08-19:37
[INFO]   Window 8/8: frames=4, range=19:58-21:02

[INFO] (3/3) Downloading… 'プラダやエルメス…衣装だけの専用ルームに潜入！'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\03_3.%(ext)s', 'https://www.youtube.com/shorts/BBl6hKvmo48', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
