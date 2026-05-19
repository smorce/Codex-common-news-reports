# YouTube Video Summary Report (Error)

- Generated at: 2026-05-19T00:48:33Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
 older than 90 days!
         It is strongly recommended to always use the latest version.
         You installed yt-dlp with pip or using the wheel from PyPi; Use that to update.
         To suppress this warning, add --no-update to your command/config.
WARNING: [youtube] No supported JavaScript runtime could be found. Only deno is enabled by default; to use another runtime add  --js-runtimes RUNTIME[:PATH]  to your command/config. YouTube extraction without a JS runtime has been deprecated, and some formats may be missing. See  https://github.com/yt-dlp/yt-dlp/wiki/EJS  for details on installing one
ERROR: [youtube] tT-J9TyoFw8: Join this channel to get access to members-only content like this video, and other exclusive perks.
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
subprocess.CalledProcessError: Command '['yt-dlp', '-f', 'bv*+ba/b', '-o', 'gemma4_cache\\02_tT-J9TyoFw8.%(ext)s', 'https://www.youtube.com/watch?v=tT-J9TyoFw8', '--merge-output-format', 'mp4', '--js-runtimes', 'deno', '--no-part', '--no-continue']' returned non-zero exit status 1.

```
