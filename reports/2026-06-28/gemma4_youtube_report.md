# YouTube Video Summary Report (Error)

- Generated at: 2026-06-28T00:23:06Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
:06
[INFO]   Window 8/8: frames=4, range=21:29-22:37

[INFO] (2/3) Downloading… 'おしゃれの知識が深まる！服の選び方が変わる！最先端素材づくりの裏側 Press Room 116 K-3B＆カジファクトリーパーク'
[INFO] Downloaded: gemma4_cache\02_ZVtyuouT7Os.mp4 (90.21 MB)
[INFO] (2/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 60 frame(s), sampling=uniform, duration=1660.60s, first=13.84s, last=1646.76s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 60 frame(s), window_size=8, windows=8
[INFO]   Window 1/8: frames=8, range=00:14-03:28
[INFO]   Window 2/8: frames=8, range=03:55-07:09
[INFO]   Window 3/8: frames=8, range=07:37-10:50
[INFO]   Window 4/8: frames=8, range=11:18-14:32
[INFO]   Window 5/8: frames=8, range=14:59-18:13
[INFO]   Window 6/8: frames=8, range=18:41-21:55
[INFO]   Window 7/8: frames=8, range=22:22-25:36
[INFO]   Window 8/8: frames=4, range=26:04-27:27

[INFO] (3/3) Downloading… '白Tのお悩み解決！夏の黒やネイビーが優秀＆体型カバーにおすすめの選び方！| B.R. Fashion College Lesson.890 ダークトーン特集'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\03_ZsSDJqAXJmg.%(ext)s', 'https://www.youtube.com/watch?v=ZsSDJqAXJmg', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
