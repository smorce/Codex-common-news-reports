# YouTube Video Summary Report (Error)

- Generated at: 2026-08-15T00:02:06Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
oading weights:  63%|██████▎   | 1238/1951 [00:15<00:10, 70.43it/s]
Loading weights:  64%|██████▍   | 1251/1951 [00:15<00:09, 77.05it/s]
Loading weights:  65%|██████▍   | 1259/1951 [00:15<00:09, 74.51it/s]
Loading weights:  65%|██████▍   | 1267/1951 [00:15<00:12, 55.70it/s]
Loading weights:  66%|██████▌   | 1280/1951 [00:15<00:10, 61.85it/s]
Loading weights:  66%|██████▌   | 1292/1951 [00:15<00:09, 68.54it/s]
Loading weights:  71%|███████   | 1379/1951 [00:15<00:02, 236.61it/s]
Loading weights:  75%|███████▍  | 1458/1951 [00:16<00:01, 363.43it/s]
Loading weights:  80%|███████▉  | 1552/1951 [00:16<00:00, 498.68it/s]
Loading weights:  85%|████████▌ | 1660/1951 [00:16<00:00, 644.31it/s]
Loading weights:  89%|████████▉ | 1742/1951 [00:16<00:00, 689.58it/s]
Loading weights:  94%|█████████▍| 1840/1951 [00:16<00:00, 751.18it/s]
Loading weights:  99%|█████████▉| 1930/1951 [00:16<00:00, 790.38it/s]
Loading weights: 100%|██████████| 1951/1951 [00:16<00:00, 117.56it/s]

[INFO] (1/3) Downloading… 'Tシャツも大人っぽく着こなす♪ 女子モテコーデの正解はコレ！ Press Room 121'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\01_dyOtUTgwhPc.%(ext)s', 'https://www.youtube.com/watch?v=dyOtUTgwhPc', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
