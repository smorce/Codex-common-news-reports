# YouTube Video Summary Report (Error)

- Generated at: 2026-07-14T00:19:11Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
924/1951 [00:15<00:00, 734.68it/s]
Loading weights: 100%|██████████| 1951/1951 [00:15<00:00, 123.88it/s]

[INFO] (1/3) Downloading… '女子も憧れるイケオジな着こなし提案！Z世代男子に着て欲しい大人の渋コーデ♪'
[INFO] Downloaded: gemma4_cache\01_Evobrnz3yJM.mp4 (77.26 MB)
[INFO] (1/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 60 frame(s), sampling=uniform, duration=1286.46s, first=10.72s, last=1275.73s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 60 frame(s), window_size=8, windows=8
[INFO]   Window 1/8: frames=8, range=00:11-02:41
[INFO]   Window 2/8: frames=8, range=03:02-05:32
[INFO]   Window 3/8: frames=8, range=05:54-08:24
[INFO]   Window 4/8: frames=8, range=08:45-11:15
[INFO]   Window 5/8: frames=8, range=11:37-14:07
[INFO]   Window 6/8: frames=8, range=14:28-16:58
[INFO]   Window 7/8: frames=8, range=17:20-19:50
[INFO]   Window 8/8: frames=4, range=20:11-21:16

[INFO] (2/3) Downloading… 'この夏モテる♪大人スポーティカジュアルな上品スタイル、イチ押しはこれ！Press Room 118 K-3B'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\02_gpspKJ4dV2E.%(ext)s', 'https://www.youtube.com/watch?v=gpspKJ4dV2E', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
