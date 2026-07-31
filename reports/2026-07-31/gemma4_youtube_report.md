# YouTube Video Summary Report (Error)

- Generated at: 2026-07-31T00:08:28Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
s]
Loading weights:  89%|████████▉ | 1742/1951 [01:30<00:01, 146.28it/s]
Loading weights:  90%|█████████ | 1757/1951 [01:30<00:01, 142.48it/s]
Loading weights:  91%|█████████ | 1772/1951 [01:30<00:01, 138.72it/s]
Loading weights:  92%|█████████▏| 1788/1951 [01:30<00:01, 126.84it/s]
Loading weights:  92%|█████████▏| 1801/1951 [01:31<00:01, 112.62it/s]
Loading weights:  93%|█████████▎| 1819/1951 [01:31<00:01, 119.56it/s]
Loading weights:  94%|█████████▍| 1834/1951 [01:31<00:01, 114.92it/s]
Loading weights:  95%|█████████▌| 1860/1951 [01:31<00:00, 149.32it/s]
Loading weights:  96%|█████████▌| 1876/1951 [01:31<00:00, 148.95it/s]
Loading weights:  97%|█████████▋| 1895/1951 [01:31<00:00, 152.44it/s]
Loading weights:  98%|█████████▊| 1912/1951 [01:31<00:00, 139.94it/s]
Loading weights:  99%|█████████▉| 1927/1951 [01:31<00:00, 131.83it/s]
Loading weights: 100%|█████████▉| 1947/1951 [01:32<00:00, 142.04it/s]
Loading weights: 100%|██████████| 1951/1951 [01:32<00:00, 21.13it/s] 

[INFO] (1/3) Downloading… '清潔感命！女子は短パンのどこを見てる？大人が絶対気をつけたいポイント！'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\01_d1PPWcbyFo8.%(ext)s', 'https://www.youtube.com/watch?v=d1PPWcbyFo8', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
