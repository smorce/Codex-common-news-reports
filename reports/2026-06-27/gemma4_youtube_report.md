# YouTube Video Summary Report (Error)

- Generated at: 2026-06-27T00:17:23Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
/s]
Loading weights: 100%|██████████| 1951/1951 [00:36<00:00, 53.72it/s] 

[INFO] (1/3) Downloading… 'お洒落で今価値の高い腕時計とは？スマートな大人の腕時計選び！ Press Room 117 ジェラルド・チャールズ'
[INFO] Downloaded: gemma4_cache\01_XE1BV_n4Yag.mp4 (62.17 MB)
[INFO] (1/3) Summarizing…
[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.
[INFO] Using frame fallback: 60 frame(s), sampling=uniform, duration=1368.49s, first=11.40s, last=1357.09s, height=360, frames_per_window=8
[INFO] Windowed frame summarization: 60 frame(s), window_size=8, windows=8
[INFO]   Window 1/8: frames=8, range=00:11-02:51
[INFO]   Window 2/8: frames=8, range=03:14-05:54
[INFO]   Window 3/8: frames=8, range=06:16-08:56
[INFO]   Window 4/8: frames=8, range=09:19-11:58
[INFO]   Window 5/8: frames=8, range=12:21-15:01
[INFO]   Window 6/8: frames=8, range=15:24-18:03
[INFO]   Window 7/8: frames=8, range=18:26-21:06
[INFO]   Window 8/8: frames=4, range=21:29-22:37

[INFO] (2/3) Downloading… 'おしゃれの知識が深まる！服の選び方が変わる！最先端素材づくりの裏側 Press Room 116 K-3B＆カジファクトリーパーク'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1690, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 435, in download_mp4_simple
    raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command '['yt-dlp', '--no-update', '--no-warnings', '--extractor-args', 'youtube:lang=ja', '--js-runtimes', 'node', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\02_ZVtyuouT7Os.%(ext)s', 'https://www.youtube.com/watch?v=ZVtyuouT7Os', '--no-part', '--no-continue', '--merge-output-format', 'mp4']' returned non-zero exit status 1.

```
