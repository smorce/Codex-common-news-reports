# YouTube Video Summary Report (Error)

- Generated at: 2026-07-25T00:13:57Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
   | 1251/1951 [00:17<00:10, 67.56it/s]
Loading weights:  65%|██████▍   | 1265/1951 [00:17<00:08, 77.43it/s]
Loading weights:  65%|██████▌   | 1273/1951 [00:17<00:08, 76.35it/s]
Loading weights:  66%|██████▌   | 1281/1951 [00:17<00:10, 65.74it/s]
Loading weights:  67%|██████▋   | 1307/1951 [00:17<00:05, 107.54it/s]
Loading weights:  72%|███████▏  | 1403/1951 [00:17<00:01, 310.18it/s]
Loading weights:  75%|███████▍  | 1461/1951 [00:17<00:01, 374.75it/s]
Loading weights:  79%|███████▉  | 1537/1951 [00:17<00:00, 475.77it/s]
Loading weights:  83%|████████▎ | 1625/1951 [00:17<00:00, 580.77it/s]
Loading weights:  88%|████████▊ | 1712/1951 [00:18<00:00, 654.78it/s]
Loading weights:  92%|█████████▏| 1789/1951 [00:18<00:00, 680.92it/s]
Loading weights:  96%|█████████▌| 1871/1951 [00:18<00:00, 707.58it/s]
Loading weights: 100%|██████████| 1951/1951 [00:18<00:00, 672.93it/s]
Loading weights: 100%|██████████| 1951/1951 [00:18<00:00, 105.91it/s]

[INFO] (1/3) Downloading… '短パンが苦手な大人におすすめ！夏の最新グレスラを徹底解説！| B.R. Fashion College Lesson.894 グレーパンツ特集'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\01_W-OJSuYQjWM.%(ext)s', 'https://www.youtube.com/watch?v=W-OJSuYQjWM', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
