# YouTube Video Summary Report (Error)

- Generated at: 2026-05-09T00:05:44Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
[WARNING] RSS fetch failed; falling back to yt-dlp: Failed to fetch RSS after 3 attempts: 'https://www.youtube.com/feeds/videos.xml?channel_id=UCUWtuyVjeMQygQiy3adHb1g'
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1549, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1489, in main
    pairs = get_latest_video_urls_from_channel(args.channel_url, n=args.num_videos)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 426, in get_latest_video_urls_from_channel
    return get_latest_video_urls_via_ytdlp(channel_url, n)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 225, in get_latest_video_urls_via_ytdlp
    raise RuntimeError(f"yt-dlp flat-playlist failed (exit {cp.returncode}): {err}")
RuntimeError: yt-dlp flat-playlist failed (exit 1): ERROR: [youtube:tab] UCUWtuyVjeMQygQiy3adHb1g: Unable to download API page: HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 11001] getaddrinfo failed) (caused by TransportError("HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 11001] getaddrinfo failed)"))

```
