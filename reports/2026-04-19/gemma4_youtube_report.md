# YouTube Video Summary Report (Error)

- Generated at: 2026-04-19T00:08:18Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
/8: frames=8, range=08:30-10:56
[INFO]   Window 5/8: frames=8, range=11:17-13:43
[INFO]   Window 6/8: frames=8, range=14:04-16:30
[INFO]   Window 7/8: frames=8, range=16:51-19:16
[INFO]   Window 8/8: frames=4, range=19:37-20:40

[INFO] (2/3) Downloading…
WARNING: [youtube] No supported JavaScript runtime could be found. Only deno is enabled by default; to use another runtime add  --js-runtimes RUNTIME[:PATH]  to your command/config. YouTube extraction without a JS runtime has been deprecated, and some formats may be missing. See  https://github.com/yt-dlp/yt-dlp/wiki/EJS  for details on installing one
ERROR: [youtube] 5-AV2OeU-2c: Join this channel to get access to members-only content like this video, and other exclusive perks.
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1549, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1507, in main
    mp4_path = download_mp4_simple(video_url, out_base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 306, in download_mp4_simple
    run(cmd, check=True, capture=False)
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 144, in run
    return subprocess.run(cmd, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\AppData\Roaming\uv\python\cpython-3.12.11-windows-x86_64-none\Lib\subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['yt-dlp', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\02_5-AV2OeU-2c.%(ext)s', 'https://www.youtube.com/watch?v=5-AV2OeU-2c', '--merge-output-format', 'mp4', '--js-runtimes', 'deno', '--no-part', '--no-continue']' returned non-zero exit status 1.

```
