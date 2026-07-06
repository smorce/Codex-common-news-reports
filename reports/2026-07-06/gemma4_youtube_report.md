# YouTube Video Summary Report (Error)

- Generated at: 2026-07-06T00:37:20Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
100%|██████████| 1951/1951 [00:20<00:00, 95.92it/s] 

[INFO] (1/3) Downloading… '学生起業家から成功！M&A、採用メディアを展開する若き経営者の戦略！｜B.R.CHANNEL THE INTUITION #18'
[INFO] Downloaded: gemma4_cache\01_DicymH4PzZk.mp4 (90.26 MB)
[INFO] (1/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 60 frame(s), sampling=uniform, duration=1862.33s, first=15.52s, last=1846.81s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 60 frame(s), window_size=8, windows=8
[INFO]   Window 1/8: frames=8, range=00:16-03:53
[INFO]   Window 2/8: frames=8, range=04:24-08:01
[INFO]   Window 3/8: frames=8, range=08:32-12:09
[INFO]   Window 4/8: frames=8, range=12:40-16:18
[INFO]   Window 5/8: frames=8, range=16:49-20:26
[INFO]   Window 6/8: frames=8, range=20:57-24:34
[INFO]   Window 7/8: frames=8, range=25:05-28:43
[INFO]   Window 8/8: frames=4, range=29:14-30:47

[INFO] (2/3) Downloading… '今、理想のパンツ丈は？太さや形別で徹底検証！知っておきたい正解シルエット | B.R. Fashion College Lesson.891 パンツの丈を検証'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\02_3Y1FBFkaqxc.%(ext)s', 'https://www.youtube.com/watch?v=3Y1FBFkaqxc', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
