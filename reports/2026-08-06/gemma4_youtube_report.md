# YouTube Video Summary Report (Error)

- Generated at: 2026-08-06T00:15:34Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
█▋   | 1307/1951 [01:41<00:15, 41.70it/s]
Loading weights:  68%|██████▊   | 1331/1951 [01:41<00:08, 69.17it/s]
Loading weights:  69%|██████▊   | 1339/1951 [01:41<00:09, 63.02it/s]
Loading weights:  69%|██████▉   | 1348/1951 [01:42<00:11, 52.78it/s]
Loading weights:  73%|███████▎  | 1430/1951 [01:42<00:02, 186.67it/s]
Loading weights:  78%|███████▊  | 1526/1951 [01:42<00:01, 331.44it/s]
Loading weights:  81%|████████  | 1571/1951 [01:42<00:01, 239.28it/s]
Loading weights:  83%|████████▎ | 1619/1951 [01:42<00:01, 280.27it/s]
Loading weights:  87%|████████▋ | 1707/1951 [01:42<00:00, 396.36it/s]
Loading weights:  90%|█████████ | 1761/1951 [01:43<00:00, 324.13it/s]
Loading weights:  93%|█████████▎| 1805/1951 [01:43<00:00, 272.80it/s]
Loading weights:  94%|█████████▍| 1842/1951 [01:43<00:00, 268.63it/s]
Loading weights:  98%|█████████▊| 1917/1951 [01:43<00:00, 357.89it/s]
Loading weights: 100%|██████████| 1951/1951 [01:43<00:00, 18.79it/s] 

[INFO] (1/3) Downloading… '長い夏も洒落て見せる！大人の旬アイテムでトータルスタイル提案！| B.R. Fashion College Lesson.896 アウール'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\01_XgrZa8_4VBI.%(ext)s', 'https://www.youtube.com/watch?v=XgrZa8_4VBI', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
