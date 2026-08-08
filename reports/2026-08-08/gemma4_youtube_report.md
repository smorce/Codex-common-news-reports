# YouTube Video Summary Report (Error)

- Generated at: 2026-08-08T00:18:32Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
:  82%|████████▏ | 1599/1951 [02:11<00:04, 78.21it/s]
Loading weights:  83%|████████▎ | 1614/1951 [02:11<00:03, 86.24it/s]
Loading weights:  83%|████████▎ | 1625/1951 [02:11<00:04, 80.77it/s]
Loading weights:  84%|████████▍ | 1635/1951 [02:11<00:04, 74.40it/s]
Loading weights:  85%|████████▌ | 1666/1951 [02:12<00:02, 106.63it/s]
Loading weights:  89%|████████▉ | 1742/1951 [02:12<00:00, 237.58it/s]
Loading weights:  92%|█████████▏| 1794/1951 [02:12<00:00, 288.71it/s]
Loading weights:  94%|█████████▎| 1829/1951 [02:12<00:00, 262.11it/s]
Loading weights:  95%|█████████▌| 1860/1951 [02:12<00:00, 172.05it/s]
Loading weights:  97%|█████████▋| 1884/1951 [02:12<00:00, 164.26it/s]
Loading weights:  98%|█████████▊| 1905/1951 [02:13<00:00, 169.50it/s]
Loading weights:  99%|█████████▊| 1926/1951 [02:13<00:00, 92.34it/s] 
Loading weights: 100%|█████████▉| 1947/1951 [02:13<00:00, 99.44it/s]
Loading weights: 100%|██████████| 1951/1951 [02:13<00:00, 14.57it/s]

[INFO] (1/3) Downloading… '人気上昇中！半袖シャツの大人モテコーデ♪ コスパも抜群なおすすめスタイル！ Press Room 120 ジーステージ'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\01_AjA8NVsIfVc.%(ext)s', 'https://www.youtube.com/watch?v=AjA8NVsIfVc', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
