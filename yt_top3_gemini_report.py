#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import datetime as dt
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import feedparser
import requests


def run(cmd: list[str], *, check: bool = True, capture: bool = False, text: bool = True, stdin=None, env=None, encoding: str | None = None, errors: str = "strict", timeout: float | None = None) -> subprocess.CompletedProcess:
    """
    Run a command with subprocess.run().
    
    Args:
        cmd: Command to run as a list of strings
        check: If True, raise CalledProcessError on non-zero exit
        capture: If True, capture stdout and stderr
        text: If True, decode output as text
        stdin: Optional file-like object or file descriptor for stdin
        env: Optional environment variables dict (if None, inherits current env)
        encoding: Encoding for text mode (default: UTF-8 on Windows, system default on Unix)
        errors: Error handling for encoding (default: 'strict', use 'replace' for robustness)
    """
    # On Windows, default to UTF-8 encoding to avoid cp932 issues
    if text and encoding is None:
        if sys.platform == "win32":
            encoding = "utf-8"
            errors = "replace"  # Use replace to handle any encoding issues gracefully
    
    kwargs = {
        "check": check,
        "capture_output": capture,
        "text": text,
        "env": env,
    }
    
    # Handle stdin: if it's a string, use input parameter; otherwise use stdin parameter
    if stdin is not None:
        if isinstance(stdin, str):
            kwargs["input"] = stdin
        else:
            kwargs["stdin"] = stdin
    
    # Only add encoding/errors if text mode is enabled
    if text:
        kwargs["encoding"] = encoding
        kwargs["errors"] = errors
    
    # Add timeout if provided
    if timeout is not None:
        kwargs["timeout"] = timeout
    
    return subprocess.run(cmd, **kwargs)


def check_ffmpeg_available() -> bool:
    """Check if ffmpeg is available in PATH."""
    try:
        result = run(["ffmpeg", "-version"], check=False, capture=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def extract_channel_id_from_url(channel_url: str) -> str | None:
    """
    Accepts:
      - https://www.youtube.com/channel/UCxxxx
      - https://www.youtube.com/@handle
      - other channel-like URLs that resolve to a channel page
    Returns:
      - channel_id starting with UC...
    """
    # Fast path: /channel/UC...
    m = re.search(r"/channel/(UC[a-zA-Z0-9_-]{10,})", channel_url)
    if m:
        return m.group(1)

    # Fetch HTML and regex out channelId / externalId
    try:
        resp = requests.get(channel_url, allow_redirects=True, timeout=20, headers={
            "User-Agent": "Mozilla/5.0 (compatible; yt-top3-bot/1.0)"
        })
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        print(f"[ERROR] Failed to fetch channel page: {e}", file=sys.stderr)
        return None

    patterns = [
        r'"channelId"\s*:\s*"(UC[a-zA-Z0-9_-]{10,})"',
        r'"externalId"\s*:\s*"(UC[a-zA-Z0-9_-]{10,})"',
        r'itemprop="channelId"\s+content="(UC[a-zA-Z0-9_-]{10,})"',
    ]
    for pat in patterns:
        m = re.search(pat, html)
        if m:
            return m.group(1)

    return None


def rss_url_for_channel_id(channel_id: str) -> str:
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"


def video_id_from_link(link: str) -> str | None:
    """
    Extract video ID from YouTube URL.
    Supports both regular (/watch?v=) and shorts (/shorts/) formats.
    """
    try:
        # Check for shorts format: /shorts/VIDEOID
        if "/shorts/" in link:
            m = re.search(r"/shorts/([a-zA-Z0-9_-]+)", link)
            if m:
                return m.group(1)
        
        # Regular format: /watch?v=VIDEOID
        q = parse_qs(urlparse(link).query)
        v = q.get("v", [None])[0]
        return v
    except Exception:
        return None


def safe_filename(s: str, max_len: int = 120) -> str:
    s = re.sub(r"[\\/:*?\"<>|]+", "_", s)
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > max_len:
        s = s[:max_len].rstrip()
    return s


def check_moviepy_available() -> tuple[bool, str]:
    """
    Check if moviepy is available and can be imported.
    Returns (is_available, error_message)
    """
    try:
        import moviepy
        print(f"[DEBUG] moviepy module found, version: {getattr(moviepy, '__version__', 'unknown')}", file=sys.stderr)
    except ImportError as e:
        return False, f"moviepy module not found: {e}"
    
    try:
        # moviepy 2.x: editor module removed, import directly from moviepy
        from moviepy import VideoFileClip
        print(f"[DEBUG] VideoFileClip imported successfully", file=sys.stderr)
    except ImportError as e:
        return False, f"VideoFileClip import failed: {e}. Try: pip install imageio-ffmpeg"
    except Exception as e:
        return False, f"moviepy initialization failed: {e}"
    
    return True, ""


def compress_video_with_moviepy(input_path: Path, output_path: Path, target_size_mb: float = 18.0) -> Path:
    """
    Compress video using moviepy (Python library) to meet target size.
    This is a fallback when ffmpeg CLI is not available.
    
    Note: moviepy requires ffmpeg binaries, but can use bundled versions.
    Install: pip install moviepy
    
    Args:
        input_path: Input video file
        output_path: Output compressed video file
        target_size_mb: Target file size in MB (default: 18MB)
    
    Returns:
        Path to compressed video file
    """
    try:
        # moviepy 2.x: editor module removed, import directly from moviepy
        from moviepy import VideoFileClip
    except ImportError as e:
        error_msg = (
            f"moviepy import failed: {e}\n\n"
            f"moviepy may be installed but missing dependencies.\n"
            f"Try installing with: pip install moviepy\n"
            f"Or install imageio-ffmpeg: pip install imageio-ffmpeg\n"
            f"Or use ffmpeg CLI directly for compression."
        )
        raise ImportError(error_msg) from e
    except Exception as e:
        error_msg = (
            f"moviepy initialization failed: {e}\n\n"
            f"moviepy may be installed but not properly configured.\n"
            f"Try reinstalling: pip install --upgrade moviepy imageio-ffmpeg"
        )
        raise RuntimeError(error_msg) from e
    
    print(f"[INFO] Compressing video using moviepy...", file=sys.stderr)
    
    # Verify input file exists before attempting compression
    if not input_path.exists():
        raise FileNotFoundError(f"Input video file not found: {input_path}")
    
    try:
        # Load video
        video = VideoFileClip(str(input_path))
        duration_sec = video.duration
        original_size_mb = input_path.stat().st_size / (1024 * 1024)
        original_fps = video.fps
        original_width = video.w
        original_height = video.h
        
        print(f"[INFO] Original video: {original_width}x{original_height}@{original_fps:.1f}fps, {original_size_mb:.2f}MB, {duration_sec:.1f}s", file=sys.stderr)
        
        # Calculate required total bitrate from target file size
        # target_size_mb * 8 (bits) * 1024 (KB) / duration_sec = total_bitrate_kbps
        audio_bitrate_kbps = 64  # Fixed audio bitrate
        total_bitrate_kbps = (target_size_mb * 8 * 1024) / duration_sec
        target_video_bitrate_kbps = total_bitrate_kbps - audio_bitrate_kbps
        
        print(f"[INFO] Target file size: {target_size_mb:.2f}MB, required total bitrate: {total_bitrate_kbps:.1f}kbps", file=sys.stderr)
        
        # Dynamically adjust resolution, fps, and bitrate to meet target size
        # Start with original settings and reduce if needed
        current_width = original_width
        current_height = original_height
        current_fps = original_fps
        current_bitrate = target_video_bitrate_kbps
        
        # Calculate compression ratio
        compression_ratio = original_size_mb / target_size_mb
        
        # Progressive reduction: adjust resolution, fps, and bitrate based on target size
        # Resolution levels: 1080p -> 720p -> 480p -> 360p -> 320p -> 240p
        resolution_levels = [
            (1920, 1080),  # 1080p
            (1280, 720),   # 720p
            (854, 480),    # 480p
            (640, 360),    # 360p
            (568, 320),    # 320p
            (426, 240),    # 240p
        ]
        
        # FPS levels: 30 -> 24 -> 15 -> 12 -> 10
        fps_levels = [30, 24, 15, 12, 10]
        
        # Find appropriate resolution and fps based on target bitrate
        aspect_ratio = original_width / original_height
        best_resolution = None
        best_fps = None
        
        # Try different combinations to find one that fits within target bitrate
        for res_width, res_height in resolution_levels:
            # Adjust resolution to maintain aspect ratio
            if aspect_ratio > (res_width / res_height):
                adj_width = res_width
                adj_height = int(res_width / aspect_ratio)
            else:
                adj_height = res_height
                adj_width = int(adj_height * aspect_ratio)
            
            # Ensure even dimensions
            adj_width = adj_width - (adj_width % 2)
            adj_height = adj_height - (adj_height % 2)
            
            # Skip if resolution is larger than original
            if adj_width > original_width or adj_height > original_height:
                continue
            
            # Try different FPS levels
            for fps in fps_levels:
                if fps > original_fps:
                    continue
                
                # Estimate if this combination can achieve target bitrate
                # Rough estimation: lower resolution and fps allow lower bitrate
                # This is a heuristic - actual encoding will determine final size
                estimated_bitrate = target_video_bitrate_kbps
                
                # If estimated bitrate is reasonable (not too low), use this combination
                if estimated_bitrate >= 20:  # Minimum reasonable bitrate
                    best_resolution = (adj_width, adj_height)
                    best_fps = fps
                    break
            
            if best_resolution:
                break
        
        # If no combination found, use most aggressive settings
        if not best_resolution:
            # Use smallest resolution and lowest fps
            if aspect_ratio > (426 / 240):
                best_width = 426
                best_height = int(426 / aspect_ratio)
            else:
                best_height = 240
                best_width = int(240 * aspect_ratio)
            best_width = best_width - (best_width % 2)
            best_height = best_height - (best_height % 2)
            best_resolution = (best_width, best_height)
            best_fps = 10
        
        # Apply resolution reduction if needed
        if best_resolution[0] < original_width or best_resolution[1] < original_height:
            try:
                video = video.resized(best_resolution)
            except AttributeError:
                video = video.resize(best_resolution)
            print(f"[INFO] Reduced resolution to {best_resolution[0]}x{best_resolution[1]}", file=sys.stderr)
        
        target_fps = best_fps
        if target_fps < original_fps:
            print(f"[INFO] Will reduce frame rate from {original_fps:.1f}fps to {target_fps}fps", file=sys.stderr)
        
        # Use calculated bitrate, but ensure minimum
        min_bitrate = 20  # Absolute minimum for watchable video
        if current_bitrate < min_bitrate:
            current_bitrate = min_bitrate
            print(f"[WARNING] Target bitrate too low, using minimum {min_bitrate}kbps", file=sys.stderr)
        
        target_bitrate_kbps = int(current_bitrate)
        
        print(f"[INFO] Final settings: {best_resolution[0]}x{best_resolution[1]}@{target_fps}fps, {target_bitrate_kbps}kbps video + {audio_bitrate_kbps}kbps audio", file=sys.stderr)
        
        # Use aggressive preset for better compression when needed
        # Use 'ultrafast' for aggressive compression, 'fast' for moderate
        preset = 'ultrafast' if compression_ratio > 2.0 else 'fast'
        
        # Write compressed video
        write_kwargs = {
            'codec': 'libx264',
            'audio_codec': 'aac',
            'bitrate': f'{target_bitrate_kbps}k',
            'audio_bitrate': f'{audio_bitrate_kbps}k',
            'preset': preset,
            'threads': 4,
            'logger': None  # Suppress progress bar
        }
        
        # Add fps parameter if frame rate was reduced
        if target_fps < original_fps:
            write_kwargs['fps'] = target_fps
        
        video.write_videofile(str(output_path), **write_kwargs)
        
        # Close video to free resources
        video.close()
        
        # Verify output size
        output_size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"[SUCCESS] Compressed video using moviepy: {output_size_mb:.2f} MB", file=sys.stderr)
        
        return output_path
    except Exception as e:
        print(f"[ERROR] Moviepy compression failed: {e}", file=sys.stderr)
        raise


def compress_video_with_ffmpeg(input_path: Path, output_path: Path, target_size_mb: float = 18.0) -> Path:
    """
    Compress video using ffmpeg CLI to meet target size.
    Uses two-pass encoding for better quality at lower bitrates.
    
    Args:
        input_path: Input video file
        output_path: Output compressed video file
        target_size_mb: Target file size in MB (default: 18MB, leaving margin for 20MB limit)
    
    Returns:
        Path to compressed video file
    """
    # Calculate target bitrate based on video duration
    # Get video duration using ffprobe
    try:
        duration_cmd = [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(input_path)
        ]
        result = run(duration_cmd, capture=True, text=True, check=True)
        duration_sec = float(result.stdout.strip())
    except Exception as e:
        print(f"[WARNING] Failed to get video duration: {e}. Using default compression.", file=sys.stderr)
        duration_sec = 60  # Default assumption
    
    # Calculate target bitrate (kbps)
    # target_size_mb * 8 (bits) * 1024 (KB) / duration_sec - audio_bitrate
    # Reserve 128kbps for audio
    audio_bitrate_kbps = 128
    target_bitrate_kbps = int((target_size_mb * 8 * 1024) / duration_sec) - audio_bitrate_kbps
    
    # Ensure minimum bitrate
    if target_bitrate_kbps < 200:
        target_bitrate_kbps = 200
        print(f"[WARNING] Target bitrate too low, using minimum 200kbps", file=sys.stderr)
    
    print(f"[INFO] Compressing video: duration={duration_sec:.1f}s, target_bitrate={target_bitrate_kbps}kbps", file=sys.stderr)
    
    # Use single-pass encoding for speed
    cmd = [
        "ffmpeg",
        "-i", str(input_path),
        "-c:v", "libx264",           # H.264 codec
        "-b:v", f"{target_bitrate_kbps}k",  # Video bitrate
        "-maxrate", f"{target_bitrate_kbps}k",
        "-bufsize", f"{target_bitrate_kbps * 2}k",
        "-c:a", "aac",               # Audio codec
        "-b:a", f"{audio_bitrate_kbps}k",  # Audio bitrate
        "-ac", "2",                  # Stereo audio
        "-preset", "fast",           # Encoding speed
        "-movflags", "+faststart",   # Enable streaming
        "-y",                        # Overwrite output
        str(output_path)
    ]
    
    try:
        run(cmd, check=True, capture=False)
        
        # Verify output size
        output_size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"[SUCCESS] Compressed video: {output_size_mb:.2f} MB", file=sys.stderr)
        
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] FFmpeg compression failed: {e}", file=sys.stderr)
        raise


def compress_video(input_path: Path, output_path: Path, target_size_mb: float = 18.0) -> Path:
    """
    Compress video to target size using available tools.
    Tries in order: ffmpeg CLI -> moviepy (Python library)
    
    Args:
        input_path: Input video file
        output_path: Output compressed video file
        target_size_mb: Target file size in MB
    
    Returns:
        Path to compressed video file
    """
    # Try ffmpeg CLI first (fastest and most reliable)
    if check_ffmpeg_available():
        try:
            print(f"[INFO] Using ffmpeg CLI for compression...", file=sys.stderr)
            return compress_video_with_ffmpeg(input_path, output_path, target_size_mb)
        except Exception as e:
            print(f"[WARNING] FFmpeg CLI compression failed: {e}", file=sys.stderr)
            print(f"[INFO] Falling back to moviepy...", file=sys.stderr)
    
    # Fallback to moviepy
    print(f"[INFO] Checking moviepy availability...", file=sys.stderr)
    moviepy_available, moviepy_error = check_moviepy_available()
    if not moviepy_available:
        raise ImportError(
            f"No compression tools available.\n\n"
            f"moviepy check failed: {moviepy_error}\n\n"
            f"Please install one of the following:\n"
            f"  1. ffmpeg CLI: https://ffmpeg.org/download.html\n"
            f"  2. moviepy with dependencies:\n"
            f"     pip install moviepy imageio-ffmpeg\n"
            f"     (or: uv add moviepy imageio-ffmpeg)\n\n"
            f"If moviepy is installed but not working, try:\n"
            f"  pip install --upgrade moviepy imageio-ffmpeg"
        )
    
    print(f"[INFO] Using moviepy for compression...", file=sys.stderr)
    try:
        return compress_video_with_moviepy(input_path, output_path, target_size_mb)
    except ImportError as e:
        raise ImportError(
            f"moviepy import failed: {e}\n\n"
            f"Please install moviepy: pip install moviepy\n"
            f"Or install ffmpeg CLI: https://ffmpeg.org/download.html"
        ) from e
    except Exception as e:
        moviepy_available, moviepy_error = check_moviepy_available()
        raise RuntimeError(
            f"All compression methods failed.\n"
            f"FFmpeg CLI: {'available' if check_ffmpeg_available() else 'not available'}\n"
            f"Moviepy: {'available' if moviepy_available else f'not available ({moviepy_error})'}\n"
            f"Last error: {e}"
        ) from e


def download_mp4(video_url: str, out_path: Path, max_size_mb: float = 20.0) -> Path:
    """
    Downloads and merges best video+audio into mp4 using yt-dlp.
    If ffmpeg is not available, falls back to single format selection.
    If downloaded file exceeds max_size_mb, tries lower quality formats.
    If all quality levels exceed limit and ffmpeg is available, compresses the video.
    out_path: exact mp4 path you want (we'll use a template to land there).
    max_size_mb: Maximum file size in MB (default: 20MB for Gemini API limit).
    Returns: final mp4 path
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # yt-dlp output template: must contain %(ext)s
    template = str(out_path.with_suffix(".%(ext)s"))

    # Check if ffmpeg is available
    has_ffmpeg = check_ffmpeg_available()
    
    # Try different quality levels to stay under size limit
    # Format priority: best -> medium -> low (to stay under 20MB)
    # Ensure audio is always included (use formats with audio or merge video+audio)
    if has_ffmpeg:
        quality_levels = [
            ("best", "bv*+ba/b", "Best quality (video+audio)"),
            ("medium", "bestvideo[height<=720]+bestaudio/best[height<=720]/bestvideo[height<=480]+bestaudio/best[height<=480]", "Medium quality (720p/480p with audio)"),
            ("low", "worstvideo[height<=480]+worstaudio/worst[height<=480]/worst", "Low quality (480p or lower with audio)"),
        ]
    else:
        # Without ffmpeg, must use formats that include both video and audio
        quality_levels = [
            ("best", "best[ext=mp4][vcodec*=avc1]/best[ext=mp4]/best", "Best quality (single format with audio)"),
            ("medium", "best[height<=720][ext=mp4][vcodec*=avc1]/best[height<=720][ext=mp4]/best[height<=720]/best[height<=480]", "Medium quality (720p/480p with audio)"),
            ("low", "worst[height<=480][ext=mp4]/worst[height<=480]/worst", "Low quality (480p or lower with audio)"),
        ]
    
    for quality_name, format_spec, quality_desc in quality_levels:
        print(f"[INFO] Trying {quality_desc}...", file=sys.stderr)
        
        # Clean up any existing files before attempting download
        # This ensures yt-dlp will actually download instead of skipping
        mp4 = out_path.with_suffix(".mp4")
        if mp4.exists():
            try:
                mp4.unlink()
                print(f"[INFO] Removed existing file before downloading {quality_desc}", file=sys.stderr)
            except Exception as e:
                print(f"[WARNING] Failed to remove existing file: {e}", file=sys.stderr)
        
        # Also clean up any partial download files (.part files)
        part_files = list(out_path.parent.glob(out_path.stem + "*.part"))
        for part_file in part_files:
            try:
                part_file.unlink()
                print(f"[INFO] Removed partial download file: {part_file.name}", file=sys.stderr)
            except Exception:
                pass
        
        if has_ffmpeg:
            merge_format = "mp4"
        else:
            # Fallback: select single best format that includes both video and audio
            if quality_name == "best":
                print("[WARNING] ffmpeg not found. Using single format with audio (may have lower quality).", file=sys.stderr)
                print("[INFO] To enable merging, install ffmpeg and add it to PATH.", file=sys.stderr)
            merge_format = None

        cmd = [
            "yt-dlp",
            "-f", format_spec,
            "-o", template,
            video_url,
        ]
        
        # Only add merge option if ffmpeg is available
        if merge_format:
            cmd.extend(["--merge-output-format", merge_format])
        
        # Suppress JavaScript runtime warning by explicitly enabling Deno
        # If Deno is not available, yt-dlp will fall back to extraction without JS runtime
        # (Warning is non-fatal and download will still proceed)
        cmd.extend(["--js-runtimes", "deno"])
        
        # Force re-download: don't skip existing files, don't create partial files
        cmd.extend(["--no-part", "--no-continue"])

        try:
            run(cmd, check=True, capture=False)
        except subprocess.CalledProcessError as e:
            print(f"[WARNING] Download failed with {quality_desc}: {e}", file=sys.stderr)
            if quality_name == "low":
                # Last attempt failed, re-raise
                raise
            continue  # Try next quality level

        # After download, file should be .mp4 (or whatever format was selected)
        mp4 = out_path.with_suffix(".mp4")
        if not mp4.exists():
            # Fallback: search for any produced file matching prefix
            candidates = list(out_path.parent.glob(out_path.stem + ".*"))
            if candidates:
                # pick the largest
                candidates.sort(key=lambda p: p.stat().st_size, reverse=True)
                downloaded_file = candidates[0]
                # If downloaded file is not .mp4, try to rename it (if same format)
                if downloaded_file.suffix.lower() != ".mp4":
                    print(f"[INFO] Downloaded file is {downloaded_file.suffix}, not .mp4", file=sys.stderr)
                    mp4 = downloaded_file
                else:
                    mp4 = downloaded_file
            else:
                if quality_name == "low":
                    raise FileNotFoundError(f"Download finished but output not found: {mp4}")
                continue  # Try next quality level
        
        # Check file size
        file_size_mb = mp4.stat().st_size / (1024 * 1024)
        print(f"[INFO] Downloaded file size: {file_size_mb:.2f} MB (limit: {max_size_mb} MB)", file=sys.stderr)
        
        if file_size_mb <= max_size_mb:
            print(f"[SUCCESS] File size is within limit ({file_size_mb:.2f} MB <= {max_size_mb} MB)", file=sys.stderr)
            return mp4
        else:
            print(f"[WARNING] File size exceeds limit ({file_size_mb:.2f} MB > {max_size_mb} MB)", file=sys.stderr)
            
            if quality_name == "low":
                # Last attempt, but file is still too large
                # Try compression before deleting the file
                # Try compression if ffmpeg is available
                if has_ffmpeg:
                    print(f"[INFO] Even lowest quality exceeds {max_size_mb}MB limit ({file_size_mb:.2f} MB).", file=sys.stderr)
                    print(f"[INFO] Attempting compression with ffmpeg...", file=sys.stderr)
                    
                    try:
                        # Compress to 18MB (leave 2MB margin for 20MB limit)
                        compressed_path = out_path.parent / f"{out_path.stem}_compressed.mp4"
                        compressed_file = compress_video(mp4, compressed_path, target_size_mb=18.0)
                        
                        # Check compressed file size
                        compressed_size_mb = compressed_file.stat().st_size / (1024 * 1024)
                        if compressed_size_mb <= max_size_mb:
                            # Replace original with compressed version
                            try:
                                mp4.unlink()
                            except Exception:
                                pass
                            compressed_file.rename(mp4)
                            print(f"[SUCCESS] Compressed to {compressed_size_mb:.2f} MB (within {max_size_mb} MB limit)", file=sys.stderr)
                            return mp4
                        else:
                            print(f"[WARNING] Compressed file still exceeds limit: {compressed_size_mb:.2f} MB", file=sys.stderr)
                            # Try more aggressive compression
                            try:
                                compressed_file.unlink()
                            except Exception:
                                pass
                            
                            # Try 15MB target (more aggressive)
                            compressed_file = compress_video(mp4, compressed_path, target_size_mb=15.0)
                            compressed_size_mb = compressed_file.stat().st_size / (1024 * 1024)
                            
                            if compressed_size_mb <= max_size_mb:
                                try:
                                    mp4.unlink()
                                except Exception:
                                    pass
                                compressed_file.rename(mp4)
                                print(f"[SUCCESS] Aggressively compressed to {compressed_size_mb:.2f} MB", file=sys.stderr)
                                return mp4
                            else:
                                print(f"[ERROR] Even aggressive compression exceeds limit: {compressed_size_mb:.2f} MB", file=sys.stderr)
                                raise RuntimeError(
                                    f"Downloaded file exceeds size limit even after compression: {compressed_size_mb:.2f} MB > {max_size_mb} MB. "
                                    f"Video may be too long or complex for 20MB limit."
                                )
                    except Exception as e:
                        print(f"[ERROR] Compression failed: {e}", file=sys.stderr)
                        raise RuntimeError(
                            f"Downloaded file exceeds size limit: {file_size_mb:.2f} MB > {max_size_mb} MB. "
                            f"Compression attempt failed: {e}"
                        )
                else:
                    # No ffmpeg CLI, try Python-based compression
                    print(f"[ERROR] Even lowest quality exceeds {max_size_mb}MB limit. File: {file_size_mb:.2f} MB", file=sys.stderr)
                    print(f"[INFO] ffmpeg CLI is not available. Trying Python-based compression...", file=sys.stderr)
                    
                    try:
                        compressed_path = out_path.parent / f"{out_path.stem}_compressed.mp4"
                        compressed_file = compress_video(mp4, compressed_path, target_size_mb=18.0)
                        
                        compressed_size_mb = compressed_file.stat().st_size / (1024 * 1024)
                        if compressed_size_mb <= max_size_mb:
                            try:
                                mp4.unlink()
                            except Exception:
                                pass
                            compressed_file.rename(mp4)
                            print(f"[SUCCESS] Compressed to {compressed_size_mb:.2f} MB using Python library", file=sys.stderr)
                            return mp4
                        else:
                            raise RuntimeError(
                                f"Downloaded file exceeds size limit even after compression: {compressed_size_mb:.2f} MB > {max_size_mb} MB."
                            )
                    except Exception as e:
                        raise RuntimeError(
                            f"Downloaded file exceeds size limit: {file_size_mb:.2f} MB > {max_size_mb} MB. "
                            f"Compression failed: {e}\n\n"
                            f"Please install one of the following:\n"
                            f"  1. ffmpeg CLI: https://ffmpeg.org/download.html\n"
                            f"  2. moviepy: pip install moviepy"
                        )
            else:
                # Not the last quality level, delete oversized file and try lower quality
                try:
                    mp4.unlink()
                except Exception:
                    pass
            # Try next quality level
            continue
    
    # Should not reach here, but just in case
    raise RuntimeError("Failed to download file within size limit")


def get_system_memory_gb() -> float:
    """
    Get total system memory in GB.
    Returns memory size in GB, or 8.0 as default if detection fails.
    """
    try:
        if platform.system() == "Windows":
            # Use WMI to get total physical memory
            result = subprocess.run(
                ["powershell", "-Command", "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB"],
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode == 0:
                return float(result.stdout.strip())
        else:
            # Linux/Mac: read from /proc/meminfo or sysctl
            if os.path.exists("/proc/meminfo"):
                with open("/proc/meminfo", "r") as f:
                    for line in f:
                        if line.startswith("MemTotal:"):
                            kb = int(line.split()[1])
                            return kb / (1024 * 1024)  # Convert KB to GB
            elif platform.system() == "Darwin":  # macOS
                result = subprocess.run(
                    ["sysctl", "-n", "hw.memsize"],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if result.returncode == 0:
                    bytes_val = int(result.stdout.strip())
                    return bytes_val / (1024**3)  # Convert bytes to GB
    except Exception:
        pass
    
    # Default to 8GB if detection fails
    return 8.0


def calculate_node_heap_size_mb(total_memory_gb: float) -> int:
    """
    Calculate appropriate Node.js heap size based on total system memory.
    
    Strategy:
    - For systems with < 8GB: Use 2GB (2560MB)
    - For systems with 8-16GB: Use 25% of memory
    - For systems with 16-32GB: Use 20% of memory
    - For systems with 32-64GB: Use 15% of memory
    - For systems with > 64GB: Use 12GB (12288MB) as reasonable upper limit
    
    Returns heap size in MB.
    """
    if total_memory_gb < 8:
        return 2560  # 2.5GB
    elif total_memory_gb < 16:
        return int(total_memory_gb * 1024 * 0.25)  # 25%
    elif total_memory_gb < 32:
        return int(total_memory_gb * 1024 * 0.20)  # 20%
    elif total_memory_gb < 64:
        return int(total_memory_gb * 1024 * 0.15)  # 15%
    else:
        # For very large systems, cap at 12GB to avoid excessive memory usage
        return 12288  # 12GB


def find_gemini_command() -> str | None:
    """
    Finds the gemini CLI command path.
    Returns the full path if found, None otherwise.
    """
    # First try PATH
    gemini_path = shutil.which("gemini")
    if gemini_path:
        return gemini_path
    
    # Try common Windows installation paths
    if sys.platform == "win32":
        username = os.environ.get("USERNAME", "")
        common_paths = [
            f"C:\\Users\\{username}\\AppData\\Local\\Programs\\gemini\\gemini.exe",
            f"C:\\Users\\{username}\\AppData\\Roaming\\npm\\gemini.cmd",
            "C:\\Program Files\\gemini\\gemini.exe",
        ]
        for path in common_paths:
            if os.path.exists(path):
                return path
    
    return None


def validate_summary_quality(summary: str) -> tuple[bool, str]:
    """
    Validate the quality of Gemini's summary output.
    Returns (is_valid, error_message)
    """
    if not summary or len(summary.strip()) < 50:
        return False, "要約が短すぎるか空です"
    
    # Check for Gemini CLI error messages indicating video parsing failure
    error_indicators = [
        "動画を解析できませんでした",
        "動画を視聴していない",
        "動画ファイルの内容のみに基づいて",
        "解析できませんでした",
        "could not parse",
        "failed to parse",
        "unable to process video",
    ]
    summary_lower = summary.lower()
    for indicator in error_indicators:
        if indicator in summary or indicator.lower() in summary_lower:
            return False, f"Gemini CLIが動画を解析できませんでした。動画ファイルの形式やサイズに問題がある可能性があります。"
    
    # Check for required sections
    required_sections = ["## 要約", "## 要点", "## 主張", "## 推奨"]
    missing_sections = [s for s in required_sections if s not in summary]
    if missing_sections:
        return False, f"必須セクションが不足: {', '.join(missing_sections)}"
    
    # Check for excessive English text (more than 30% of content)
    # This helps detect cases where Gemini returns English instead of Japanese
    lines = summary.split("\n")
    content_lines = [l for l in lines if l.strip() and not l.strip().startswith("#")]
    if content_lines:
        english_heavy_lines = sum(1 for line in content_lines 
                                  if len(re.findall(r'[a-zA-Z]', line)) > len(line) * 0.5)
        if english_heavy_lines > len(content_lines) * 0.3:
            return False, "英語テキストが多すぎます（日本語出力が期待されます）"
    
    return True, ""


def clean_gemini_output(result: str) -> str:
    """
    Clean up Gemini output to ensure Japanese-only content.
    Removes common English preambles and non-summary content.
    """
    lines = result.split("\n")
    output_lines = []
    found_first_section = False
    
    for line in lines:
        # Start collecting from the first section header
        if line.strip().startswith("## "):
            found_first_section = True
        
        if found_first_section:
            output_lines.append(line)
    
    return "\n".join(output_lines).strip()


def gemini_summarize_video(video_file: Path, extra_prompt: str, model: str = "gemini-2.5-pro", retry_count: int = 2) -> str:
    """
    Calls Gemini CLI with video file reference using @file syntax.
    Captures stdout as summary.
    
    Note: Standard input has 8MB limit, so we use @file syntax to reference
    the video file path directly instead of piping through stdin.
    Format: gemini "@{file_path} プロンプト"
    
    Args:
        video_file: Path to video file
        extra_prompt: Additional instructions
        model: Gemini model to use (default: gemini-2.5-pro)
        retry_count: Number of retries on quality validation failure
    """
    # Verify video file exists
    if not video_file.exists():
        raise FileNotFoundError(f"Video file not found: {video_file}")
    
    # Find gemini command
    gemini_cmd = find_gemini_command()
    if not gemini_cmd:
        raise FileNotFoundError(
            "gemini command not found in PATH. "
            "Please install Gemini CLI or add it to your PATH."
        )
    
    # Convert Path to absolute path string for Windows compatibility
    # Use forward slashes for better compatibility
    video_file_abs = str(video_file.resolve()).replace("\\", "/")
    
    # Check file path length (Windows has 260 character limit for some operations)
    # If path is too long, create a temporary copy with a shorter path
    temp_file = None
    if len(video_file_abs) > 200:  # Use shorter threshold to be safe
        print(f"[WARNING] File path is very long ({len(video_file_abs)} chars). Creating temporary copy with shorter path.", file=sys.stderr)
        try:
            # Create temp directory with short path
            temp_dir = Path(tempfile.gettempdir()) / "gemini_video_temp"
            temp_dir.mkdir(exist_ok=True)
            
            # Use short filename: just video_id + extension
            video_id_short = video_file.stem[:20] if len(video_file.stem) > 20 else video_file.stem
            temp_file = temp_dir / f"{video_id_short}{video_file.suffix}"
            
            # Copy file to temp location
            print(f"[INFO] Copying to temporary location: {temp_file}", file=sys.stderr)
            shutil.copy2(video_file, temp_file)
            video_file_abs = str(temp_file.resolve()).replace("\\", "/")
            print(f"[INFO] Using temporary file with shorter path ({len(video_file_abs)} chars)", file=sys.stderr)
        except Exception as e:
            print(f"[WARNING] Failed to create temporary copy: {e}. Using original path.", file=sys.stderr)
            temp_file = None
    
    # Debug: Log video file information
    video_size_mb = video_file.stat().st_size / (1024 * 1024)
    video_size_gb = video_size_mb / 1024
    
    print(f"[DEBUG] Video file: {video_file_abs}", file=sys.stderr)
    print(f"[DEBUG] Video file exists: {video_file.exists()}", file=sys.stderr)
    print(f"[DEBUG] Video file size: {video_size_mb:.2f} MB ({video_size_gb:.2f} GB)", file=sys.stderr)
    print(f"[DEBUG] Video file path length: {len(video_file_abs)} characters", file=sys.stderr)
    
    # Check file size limits (Gemini API may have limits)
    if video_size_mb > 500:
        print(f"[WARNING] Video file is very large ({video_size_mb:.2f} MB). This may exceed Gemini API limits.", file=sys.stderr)
    
    # Check file extension
    file_ext = video_file.suffix.lower()
    supported_formats = ['.mp4', '.mov', '.avi', '.mkv', '.webm']
    if file_ext not in supported_formats:
        print(f"[WARNING] Video file format '{file_ext}' may not be supported by Gemini CLI.", file=sys.stderr)
        print(f"[INFO] Supported formats: {', '.join(supported_formats)}", file=sys.stderr)
    
    # Build prompt with @file reference for stdin
    # Use strong context reset and explicit task declaration
    prompt_parts = [
        f"@{video_file_abs}",
        "",
        "### タスク",
        "",
        "1.上記の動画ファイルを視聴する 2.その内容を日本語で要約する 3.要約のみ出力し、要約以外の関係ないコメントや説明は一切含めないでください。",
        "出力は3番のみください。",
        "",
        "### 出力形式",
        "",
        "## 要約（100〜180字）",
        "動画の内容を簡潔に説明",
        "",
        "## 要点（3〜5個）",
        "- ポイント1",
        "- ポイント2",
        "- ポイント3",
        "",
        "## 主張・結論",
        "動画の核心メッセージを1〜2文で",
        "",
        "## 推奨アクション",
        "視聴者への具体的なアクション1つ",
    ]
    if extra_prompt:
        prompt_parts.append("")
        prompt_parts.append("## 追加指示")
        prompt_parts.append(extra_prompt.strip())
    
    prompt = "\n".join(prompt_parts)
    
    # Debug: Log the prompt being sent (first 500 chars)
    print(f"[DEBUG] Prompt preview (first 500 chars):\n{prompt[:500]}...", file=sys.stderr)
    
    # Execute gemini CLI command with stdin input
    # Method: Use stdin to pass prompt with @file syntax
    # Format: echo "prompt" | gemini  or  gemini < input.txt
    # Set NODE_OPTIONS to increase heap size for Node.js (Gemini CLI is Node.js-based)
    # Automatically calculate heap size based on system memory
    env = os.environ.copy()
    node_options = env.get("NODE_OPTIONS", "")
    # Add max-old-space-size if not already set
    if "--max-old-space-size" not in node_options:
        # Calculate appropriate heap size based on system memory
        total_memory_gb = get_system_memory_gb()
        heap_size_mb = calculate_node_heap_size_mb(total_memory_gb)
        print(f"[INFO] System memory: {total_memory_gb:.1f}GB, Setting Node.js heap size to {heap_size_mb}MB", file=sys.stderr)
        if node_options:
            env["NODE_OPTIONS"] = f"{node_options} --max-old-space-size={heap_size_mb}"
        else:
            env["NODE_OPTIONS"] = f"--max-old-space-size={heap_size_mb}"
    
    # Timeout for Gemini CLI execution (8 minutes = 500 seconds)
    # Reduced from 5 minutes to fail faster if there's an issue
    GEMINI_TIMEOUT_SEC = 500
    
    last_error = None
    for attempt in range(retry_count + 1):
        if attempt > 0:
            print(f"[INFO] Retry attempt {attempt}/{retry_count}", file=sys.stderr)
            # If previous error was rate limit, wait longer
            if last_error and ("429" in str(last_error) or "rate limit" in str(last_error).lower() or "quota" in str(last_error).lower() or "MODEL_CAPACITY_EXHAUSTED" in str(last_error)):
                wait_time = 60 * attempt  # Exponential backoff: 60s, 120s, 180s... (longer for capacity issues)
                print(f"[INFO] Rate limit or capacity issue detected, waiting {wait_time} seconds before retry...", file=sys.stderr)
                time.sleep(wait_time)
            else:
                time.sleep(5)  # Brief pause before retry (increased from 2s to 5s)
        
        try:
            # Use stdin to pass prompt (tested and working)
            print(f"[DEBUG] Executing: {gemini_cmd} -m {model} [stdin input with @file reference]", file=sys.stderr)
            print(f"[INFO] Waiting for Gemini response (timeout: {GEMINI_TIMEOUT_SEC}s)...", file=sys.stderr)
            
            # Use subprocess.run() with stdin input
            # This method was confirmed to work in test_gemini_cli.py
            cp = run(
                [gemini_cmd, "-m", model],
                check=True,
                capture=True,
                text=True,
                stdin=prompt,
                env=env,
                timeout=GEMINI_TIMEOUT_SEC,
            )
            result = (cp.stdout or "").strip()
            
            # Debug: Log result preview
            print(f"[DEBUG] Raw result length: {len(result)} chars", file=sys.stderr)
            print(f"[DEBUG] Result preview:\n{result}", file=sys.stderr)
            
            # Log stderr if present (for debugging)
            if cp.stderr:
                print(f"[DEBUG] stderr output:\n{cp.stderr[:500]}...", file=sys.stderr)
            
            # Check if result is empty
            if not result or len(result.strip()) < 10:
                stderr_info = f"\nstderr: {cp.stderr[:500]}" if cp.stderr else ""
                raise RuntimeError(
                    f"Gemini CLI returned empty or very short result (length: {len(result)})"
                    f"{stderr_info}"
                )
            
            # Check for HTTP errors (429 rate limit, etc.) in stderr
            stderr_text = (cp.stderr or "").strip()
            if stderr_text:
                # Check for common HTTP error codes and capacity issues
                is_rate_limit = (
                    "429" in stderr_text or 
                    "rate limit" in stderr_text.lower() or 
                    "quota" in stderr_text.lower() or
                    "MODEL_CAPACITY_EXHAUSTED" in stderr_text or
                    "No capacity available" in stderr_text or
                    "RESOURCE_EXHAUSTED" in stderr_text
                )
                if is_rate_limit:
                    error_detail = (
                        f"⚠️ Gemini APIのレート制限または容量不足に達しました（429エラー）。\n\n"
                        f"エラー詳細:\n"
                        f"- ステータス: 429 (Too Many Requests)\n"
                        f"- 理由: MODEL_CAPACITY_EXHAUSTED または rateLimitExceeded\n"
                        f"- モデル: {model}\n\n"
                        f"stderr出力（最初の1000文字）:\n{stderr_text[:1000]}\n\n"
                        f"stdout出力（最初の500文字）:\n{result[:500]}\n\n"
                        f"解決方法:\n"
                        f"- しばらく待ってから再試行してください（60秒以上推奨）\n"
                        f"- Gemini APIのクォータを確認してください\n"
                        f"- リクエスト間隔を長くしてください\n"
                        f"- 複数の動画を連続処理する場合は、処理間に待機時間を設けてください\n"
                    )
                    raise RuntimeError(error_detail)
            
            # Check for file size limit errors in stderr first
            if stderr_text and "File size exceeds the 20MB limit" in stderr_text:
                error_detail = (
                    f"⚠️ Gemini APIの20MBファイルサイズ制限を超えています。\n\n"
                    f"エラー詳細:\n{stderr_text}\n\n"
                    f"ファイル情報:\n"
                    f"- パス: {video_file_abs}\n"
                    f"- サイズ: {video_size_mb:.2f} MB\n"
                    f"- 拡張子: {video_file.suffix}\n\n"
                    f"解決方法:\n"
                    f"- 動画を低品質で再ダウンロードしてください（自動的に試行されます）\n"
                    f"- または、yt-dlpで品質を指定してダウンロードしてください\n"
                    f"  例: yt-dlp -f 'best[height<=480]' <URL>\n"
                )
                raise RuntimeError(error_detail)
            
            # Check for video parsing failure messages BEFORE cleaning
            if "動画を解析できませんでした" in result or "解析できませんでした" in result:
                # Log the actual Gemini CLI output for debugging
                print(f"[ERROR] Gemini CLI returned video parsing failure message", file=sys.stderr)
                print(f"[DEBUG] Full stdout output:\n{result}", file=sys.stderr)
                if stderr_text:
                    print(f"[DEBUG] Full stderr output:\n{stderr_text}", file=sys.stderr)
                
                # Check if there are clues in stderr about the actual error
                error_clues = []
                if stderr_text:
                    if "429" in stderr_text or "rate limit" in stderr_text.lower():
                        error_clues.append("レート制限（429エラー）の可能性")
                    if "quota" in stderr_text.lower():
                        error_clues.append("クォータ制限の可能性")
                    if "timeout" in stderr_text.lower():
                        error_clues.append("タイムアウトの可能性")
                    if "file" in stderr_text.lower() and "not found" in stderr_text.lower():
                        error_clues.append("ファイルが見つからない可能性")
                    if "too large" in stderr_text.lower() or "size" in stderr_text.lower():
                        error_clues.append("ファイルサイズが大きすぎる可能性")
                
                error_detail = (
                    f"Gemini CLIが動画を解析できませんでした。\n"
                    f"考えられる原因:\n"
                    f"- 動画ファイルの形式がサポートされていない\n"
                    f"- 動画ファイルが破損している\n"
                    f"- 動画ファイルが大きすぎる（{video_size_mb:.2f} MB）\n"
                    f"- ファイルパスが長すぎる（{len(video_file_abs)} 文字）\n"
                    f"- Gemini APIの制限に達している\n"
                )
                
                if error_clues:
                    error_detail += f"\nstderrから検出された可能性:\n"
                    for clue in error_clues:
                        error_detail += f"- {clue}\n"
                
                error_detail += (
                    f"\nファイル情報:\n"
                    f"- パス: {video_file_abs}\n"
                    f"- サイズ: {video_size_mb:.2f} MB\n"
                    f"- 拡張子: {video_file.suffix}\n\n"
                    f"Gemini CLIの実際の出力:\n"
                    f"stdout: {result[:1000]}{'... (truncated)' if len(result) > 1000 else ''}\n"
                )
                
                if stderr_text:
                    error_detail += f"\nstderr: {stderr_text[:1000]}{'... (truncated)' if len(stderr_text) > 1000 else ''}\n"
                
                raise RuntimeError(error_detail)
            
            # Clean up the output
            cleaned_result = clean_gemini_output(result)
            
            # Check if cleaning removed too much
            if not cleaned_result or len(cleaned_result.strip()) < 10:
                print(f"[WARNING] Cleaned result is too short. Using original result.", file=sys.stderr)
                cleaned_result = result
            
            result = cleaned_result
            
            # Validate output quality
            is_valid, error_msg = validate_summary_quality(result)
            if not is_valid:
                print(f"[WARNING] Quality validation failed: {error_msg}", file=sys.stderr)
                last_error = error_msg
                if attempt < retry_count:
                    continue  # Retry
                else:
                    # Last attempt failed validation - raise exception with error message
                    print(f"[ERROR] All retry attempts exhausted. Last error: {error_msg}", file=sys.stderr)
                    raise RuntimeError(f"Quality validation failed: {error_msg}\n\nResult preview: {result[:500]}")
            
            # Success - return validated result
            # Clean up temporary file if created
            if temp_file and temp_file.exists():
                try:
                    temp_file.unlink()
                    print(f"[INFO] Cleaned up temporary file: {temp_file}", file=sys.stderr)
                except Exception as e:
                    print(f"[WARNING] Failed to clean up temporary file: {e}", file=sys.stderr)
            return result
            
        except subprocess.CalledProcessError as e:
            # Provide more detailed error information
            stderr_text = (e.stderr or "").strip()
            stdout_text = (e.stdout or "").strip()
            
            # Check for rate limiting errors
            is_rate_limit = False
            if stderr_text:
                if "429" in stderr_text or "rate limit" in stderr_text.lower() or "quota" in stderr_text.lower():
                    is_rate_limit = True
            
            error_msg = (
                f"Gemini CLI execution failed.\n"
                f"Command: {gemini_cmd} -m {model} \"@{video_file_abs} ...\"\n"
                f"Return code: {e.returncode}\n"
                f"Video file: {video_file_abs}\n"
            )
            
            if is_rate_limit:
                error_msg += (
                    f"\n⚠️ レート制限またはクォータ制限の可能性があります（429エラー）\n"
                    f"解決方法: しばらく待ってから再試行してください\n\n"
                )
            
            if stderr_text:
                error_msg += f"Error output (stderr):\n{stderr_text}\n"
            if stdout_text:
                error_msg += f"Standard output (stdout):\n{stdout_text}\n"
            
            last_error = error_msg
            
            if attempt < retry_count:
                print(f"[WARNING] Execution failed, retrying... ({attempt + 1}/{retry_count})", file=sys.stderr)
                continue
            else:
                raise RuntimeError(error_msg) from e
        except subprocess.TimeoutExpired as e:
            error_msg = f"Gemini CLI timed out after {GEMINI_TIMEOUT_SEC} seconds"
            last_error = error_msg
            
            if attempt < retry_count:
                print(f"[WARNING] Timeout, retrying... ({attempt + 1}/{retry_count})", file=sys.stderr)
                continue
            else:
                raise RuntimeError(error_msg) from e
    
    # Clean up temporary file if created (in case of failure)
    if temp_file and temp_file.exists():
        try:
            temp_file.unlink()
            print(f"[INFO] Cleaned up temporary file after failure: {temp_file}", file=sys.stderr)
        except Exception as e:
            print(f"[WARNING] Failed to clean up temporary file: {e}", file=sys.stderr)
    
    # If we exhausted all retries
    raise RuntimeError(f"Failed after {retry_count + 1} attempts. Last error: {last_error}")


def to_iso_jst_now() -> str:
    # JST fixed offset +09:00
    jst = dt.timezone(dt.timedelta(hours=9))
    return dt.datetime.now(tz=jst).strftime("%Y-%m-%d %H:%M:%S JST")


def generate_individual_report(
    video_data: dict,
    channel_url: str,
    channel_id: str,
    rss: str,
    output_dir: Path,
) -> Path:
    """
    Generate an individual report for a single video.
    
    Args:
        video_data: Dictionary containing video information (rank, title, link, published, video_id, summary, file)
        channel_url: YouTube channel URL
        channel_id: Channel ID
        rss: RSS feed URL
        output_dir: Output directory for reports
    
    Returns:
        Path to the generated individual report file
    """
    individual_reports_dir = output_dir / "individual_reports"
    individual_reports_dir.mkdir(parents=True, exist_ok=True)
    
    now = to_iso_jst_now()
    report_lines = []
    report_lines.append(f"# 動画要約レポート #{video_data['rank']}")
    report_lines.append("")
    report_lines.append(f"- 生成日時: {now}")
    report_lines.append(f"- チャンネルURL: {channel_url}")
    report_lines.append(f"- チャンネルID: {channel_id}")
    report_lines.append(f"- RSS: {rss}")
    report_lines.append("")
    report_lines.append(f"## 動画情報")
    report_lines.append("")
    report_lines.append(f"- 順位: #{video_data['rank']}")
    report_lines.append(f"- タイトル: {video_data['title']}")
    report_lines.append(f"- 公開日時: {video_data['published']}")
    report_lines.append(f"- URL: {video_data['link']}")
    if video_data.get("file"):
        report_lines.append(f"- 解析に使ったファイル: `{video_data['file']}`")
    report_lines.append("")
    report_lines.append("## 要約")
    report_lines.append("")
    if video_data.get("summary"):
        report_lines.append(video_data["summary"])
    else:
        report_lines.append("（要約なし）")
        if video_data.get("file"):
            report_lines.append("")
            report_lines.append(f"**注意**: 動画ファイルはダウンロードされましたが、要約の生成に失敗しました。")
    report_lines.append("")
    
    # Save individual report
    safe_title = safe_filename(video_data["title"] or video_data["video_id"])
    report_filename = f'{video_data["rank"]:02d}_{video_data["video_id"]}_{safe_title}.md'
    report_path = individual_reports_dir / report_filename
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    
    return report_path


def merge_individual_reports(
    results: list[dict],
    channel_url: str,
    channel_id: str,
    rss: str,
    num_videos: int,
    output_dir: Path,
) -> Path:
    """
    Merge all individual reports into a single combined report.
    
    Args:
        results: List of video data dictionaries
        channel_url: YouTube channel URL
        channel_id: Channel ID
        rss: RSS feed URL
        num_videos: Number of videos processed
        output_dir: Output directory for reports
    
    Returns:
        Path to the merged report file
    """
    now = to_iso_jst_now()
    report_lines = []
    report_lines.append(f"# YouTube 最新Top{num_videos} 要約レポート")
    report_lines.append("")
    report_lines.append(f"- 生成日時: {now}")
    report_lines.append(f"- チャンネルURL: {channel_url}")
    report_lines.append(f"- チャンネルID: {channel_id}")
    report_lines.append(f"- RSS: {rss}")
    report_lines.append("")
    report_lines.append("## 一覧")
    report_lines.append("")
    report_lines.append("|順位|公開日時|タイトル|URL|")
    report_lines.append("|---:|---|---|---|")
    for r in results:
        title = r["title"].replace("|", " ")
        pub = r["published"].replace("|", " ")
        link = r["link"]
        report_lines.append(f'|{r["rank"]}|{pub}|{title}|{link}|')

    report_lines.append("")
    report_lines.append("## 各動画の要約")
    report_lines.append("")
    for r in results:
        report_lines.append(f'### #{r["rank"]} {r["title"]}')
        report_lines.append("")
        report_lines.append(f'- 公開日時: {r["published"]}')
        report_lines.append(f'- URL: {r["link"]}')
        if r.get("file"):
            report_lines.append(f'- 解析に使ったファイル: `{r["file"]}`')
        report_lines.append("")
        if r.get("summary"):
            report_lines.append(r["summary"])
        else:
            report_lines.append("（要約なし）")
            if r.get("file"):
                report_lines.append("")
                report_lines.append(f"**注意**: 動画ファイルはダウンロードされましたが、要約の生成に失敗しました。")
        report_lines.append("")

    report_path = output_dir / "report.md"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    
    return report_path


def main():
    ap = argparse.ArgumentParser(
        description="Summarize Top N latest YouTube videos via RSS -> MP4 -> Gemini CLI -> Markdown report",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://www.youtube.com/@channel
  %(prog)s https://www.youtube.com/@channel -n 5
  %(prog)s https://www.youtube.com/@channel -n 3 --keep-mp4
        """
    )
    ap.add_argument("channel_url", help="YouTube channel URL (e.g., https://www.youtube.com/@handle or /channel/UC...)")
    ap.add_argument("-o", "--outdir", default="yt_top3_report", help="Output directory (default: yt_top3_report)")
    ap.add_argument("-n", "--num-videos", type=int, default=3, help="Number of videos to retrieve and summarize (default: 3)")
    ap.add_argument("-m", "--model", default="gemini-2.5-pro", help="使用するGeminiモデル（デフォルト: gemini-2.5-pro）")
    ap.add_argument("--keep-mp4", action="store_true", help="Keep downloaded MP4 files after processing (default: delete)")
    ap.add_argument("--no-download", action="store_true", help="Skip downloading and summarization (debug RSS only)")
    ap.add_argument("--extra-prompt", default="", help="Extra instructions appended to Gemini prompt (optional)")
    args = ap.parse_args()
    
    # Validate num_videos
    if args.num_videos < 1:
        print("[ERROR] Number of videos must be at least 1.", file=sys.stderr)
        sys.exit(1)
    if args.num_videos > 20:
        print("[WARNING] Number of videos exceeds 20. This may take a very long time.", file=sys.stderr)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    channel_id = extract_channel_id_from_url(args.channel_url)
    if not channel_id:
        print("[ERROR] Could not extract channel_id (UC...). Provide a /channel/UC... URL or a valid channel page.", file=sys.stderr)
        sys.exit(2)

    rss = rss_url_for_channel_id(channel_id)
    feed = feedparser.parse(rss)
    if feed.bozo:
        print(f"[ERROR] RSS parse error: {feed.bozo_exception}", file=sys.stderr)
        sys.exit(3)

    # Number of videos to retrieve (from command line argument)
    NUM_VIDEOS = args.num_videos
    # Fetch more entries to account for duplicates (check up to NUM_VIDEOS * 3.5 entries)
    MAX_ENTRIES_TO_CHECK = max(NUM_VIDEOS * 4, 10)
    
    if len(feed.entries) == 0:
        print("[ERROR] No entries found in RSS.", file=sys.stderr)
        sys.exit(4)

    # Deduplicate by video_id and title (same video may appear in different formats)
    seen_video_ids = set()
    seen_titles = set()
    results = []
    rank = 1
    duplicates_skipped = 0
    
    # Process entries until we have NUM_VIDEOS unique videos or run out of entries
    for e in feed.entries[:MAX_ENTRIES_TO_CHECK]:
        if len(results) >= NUM_VIDEOS:
            break
        
        title = getattr(e, "title", "").strip()
        link = getattr(e, "link", "").strip()
        published = getattr(e, "published", "").strip()
        vid = getattr(e, "yt_videoid", None) or video_id_from_link(link)
        
        if not vid:
            vid = f"unknown_{rank}"
        
        # Normalize title for comparison (remove extra spaces, lowercase)
        normalized_title = " ".join(title.lower().split())
        
        # Skip if we've already seen this video_id
        if vid in seen_video_ids:
            print(f"[INFO] Skipping duplicate video_id: {vid} ({title})", file=sys.stderr)
            duplicates_skipped += 1
            continue
        
        # Skip if we've already seen this title (same video, different format/upload)
        if normalized_title and normalized_title in seen_titles:
            print(f"[INFO] Skipping duplicate title: {title} (video_id: {vid})", file=sys.stderr)
            duplicates_skipped += 1
            continue
        
        seen_video_ids.add(vid)
        if normalized_title:
            seen_titles.add(normalized_title)
        
        results.append({
            "rank": rank,
            "title": title,
            "link": link,
            "published": published,
            "video_id": vid,
            "summary": "",
            "file": "",
        })
        rank += 1
    
    # Check if we got enough unique videos
    if len(results) < NUM_VIDEOS:
        print(f"[WARNING] Only found {len(results)} unique videos out of {NUM_VIDEOS} requested.", file=sys.stderr)
        print(f"[WARNING] Skipped {duplicates_skipped} duplicate(s).", file=sys.stderr)
        if len(feed.entries) < MAX_ENTRIES_TO_CHECK:
            print(f"[INFO] RSS feed only contains {len(feed.entries)} entries total.", file=sys.stderr)
        else:
            print(f"[INFO] Checked {MAX_ENTRIES_TO_CHECK} entries, but found too many duplicates.", file=sys.stderr)
    
    if len(results) == 0:
        print("[ERROR] No unique videos found after deduplication.", file=sys.stderr)
        sys.exit(5)

    if args.no_download:
        # Just emit report skeleton
        pass
    else:
        # Process each video independently and generate individual reports
        for r in results:
            safe_title = safe_filename(r["title"] or r["video_id"])
            mp4_path = outdir / "mp4" / f'{r["rank"]:02d}_{r["video_id"]}_{safe_title}.mp4'
            
            # Initialize summary to empty string to ensure it's always set
            r["summary"] = ""
            r["file"] = ""
            
            try:
                print(f"[INFO] Processing #{r['rank']}/{len(results)} independently: {r['link']}", file=sys.stderr)
                
                # Check if existing file exceeds 20MB limit and delete it if so
                GEMINI_MAX_SIZE_MB = 20.0
                if mp4_path.exists():
                    existing_size_mb = mp4_path.stat().st_size / (1024 * 1024)
                    if existing_size_mb > GEMINI_MAX_SIZE_MB:
                        print(f"[INFO] Existing file exceeds {GEMINI_MAX_SIZE_MB}MB limit ({existing_size_mb:.2f} MB). Deleting and re-downloading with lower quality...", file=sys.stderr)
                        try:
                            mp4_path.unlink()
                        except Exception as e:
                            print(f"[WARNING] Failed to delete existing file: {e}", file=sys.stderr)
                
                print(f"[INFO] Downloading #{r['rank']} {r['link']}")
                mp4 = download_mp4(r["link"], mp4_path, max_size_mb=GEMINI_MAX_SIZE_MB)
                r["file"] = str(mp4)
                
                # Check if file was actually downloaded
                if not mp4.exists():
                    raise FileNotFoundError(f"Downloaded file does not exist: {mp4}")
                
                print(f"[INFO] Summarizing via Gemini CLI: {mp4.name} (size: {mp4.stat().st_size / (1024*1024):.2f} MB)", file=sys.stderr)
                r["summary"] = gemini_summarize_video(mp4, args.extra_prompt, model=args.model)
                
                # Verify summary was actually generated
                if not r["summary"] or len(r["summary"].strip()) < 10:
                    raise RuntimeError("Summary is empty or too short after processing")
                
                print(f"[SUCCESS] Summary generated for #{r['rank']} (length: {len(r['summary'])} chars)", file=sys.stderr)
                
                # Generate individual report immediately after processing this video
                individual_report_path = generate_individual_report(
                    r, args.channel_url, channel_id, rss, outdir
                )
                print(f"[INFO] Individual report generated: {individual_report_path}", file=sys.stderr)
                
                # Clean up MP4 file immediately after processing (if not keeping)
                if not args.keep_mp4 and r["file"]:
                    try:
                        Path(r["file"]).unlink(missing_ok=True)
                        print(f"[INFO] Cleaned up MP4 file for #{r['rank']}", file=sys.stderr)
                    except Exception as e:
                        print(f"[WARNING] Failed to clean up MP4 file: {e}", file=sys.stderr)
                
                # Add delay between videos to avoid rate limiting (except for last video)
                if r['rank'] < len(results):
                    wait_seconds = 70  # Wait 70 seconds between videos
                    print(f"[INFO] Waiting {wait_seconds} seconds before processing next video to avoid rate limiting...", file=sys.stderr)
                    time.sleep(wait_seconds)
                
            except FileNotFoundError as e:
                error_msg = f"要約に失敗しました（ファイル/コマンドが見つかりません）。\n\nエラー: {type(e).__name__}: {e}\n\n解決方法: Gemini CLIがインストールされているか、PATHに追加されているか確認してください。"
                r["summary"] = error_msg
                print(f"[ERROR] #{r['rank']}: {error_msg}", file=sys.stderr)
                # Generate individual report even on error
                try:
                    individual_report_path = generate_individual_report(
                        r, args.channel_url, channel_id, rss, outdir
                    )
                    print(f"[INFO] Individual report (with error) generated: {individual_report_path}", file=sys.stderr)
                except Exception as report_error:
                    print(f"[WARNING] Failed to generate individual report: {report_error}", file=sys.stderr)
            except subprocess.CalledProcessError as e:
                error_msg = f"要約に失敗しました（コマンド実行エラー）。\n\nエラー: {type(e).__name__}: {e}\n実行コマンド: {e.cmd}\nリターンコード: {e.returncode}"
                if e.stderr:
                    error_msg += f"\nエラー出力: {e.stderr[:500]}"
                if e.stdout:
                    error_msg += f"\n標準出力: {e.stdout[:500]}"
                r["summary"] = error_msg
                print(f"[ERROR] #{r['rank']}: {error_msg}", file=sys.stderr)
                # Generate individual report even on error
                try:
                    individual_report_path = generate_individual_report(
                        r, args.channel_url, channel_id, rss, outdir
                    )
                    print(f"[INFO] Individual report (with error) generated: {individual_report_path}", file=sys.stderr)
                except Exception as report_error:
                    print(f"[WARNING] Failed to generate individual report: {report_error}", file=sys.stderr)
            except subprocess.TimeoutExpired as e:
                error_msg = f"要約に失敗しました（タイムアウト）。\n\n動画の処理に時間がかかりすぎました（{e.timeout}秒超過）。\n動画ファイルが大きすぎるか、Gemini CLIの応答が遅い可能性があります。"
                r["summary"] = error_msg
                print(f"[ERROR] #{r['rank']}: {error_msg}", file=sys.stderr)
                # Generate individual report even on error
                try:
                    individual_report_path = generate_individual_report(
                        r, args.channel_url, channel_id, rss, outdir
                    )
                    print(f"[INFO] Individual report (with error) generated: {individual_report_path}", file=sys.stderr)
                except Exception as report_error:
                    print(f"[WARNING] Failed to generate individual report: {report_error}", file=sys.stderr)
            except RuntimeError as e:
                error_msg = f"要約に失敗しました（実行時エラー）。\n\nエラー: {type(e).__name__}: {e}\n\n詳細: {str(e)}"
                r["summary"] = error_msg
                print(f"[ERROR] #{r['rank']}: {error_msg}", file=sys.stderr)
                # Generate individual report even on error
                try:
                    individual_report_path = generate_individual_report(
                        r, args.channel_url, channel_id, rss, outdir
                    )
                    print(f"[INFO] Individual report (with error) generated: {individual_report_path}", file=sys.stderr)
                except Exception as report_error:
                    print(f"[WARNING] Failed to generate individual report: {report_error}", file=sys.stderr)
            except Exception as e:
                error_msg = f"要約に失敗しました（予期しない例外）。\n\nエラー: {type(e).__name__}: {e}\n\n詳細: {str(e)}\n\nスタックトレース: {type(e).__name__}"
                r["summary"] = error_msg
                print(f"[ERROR] #{r['rank']}: {error_msg}", file=sys.stderr)
                import traceback
                print(f"[ERROR] Traceback:\n{traceback.format_exc()}", file=sys.stderr)
                # Generate individual report even on error
                try:
                    individual_report_path = generate_individual_report(
                        r, args.channel_url, channel_id, rss, outdir
                    )
                    print(f"[INFO] Individual report (with error) generated: {individual_report_path}", file=sys.stderr)
                except Exception as report_error:
                    print(f"[WARNING] Failed to generate individual report: {report_error}", file=sys.stderr)

        # Clean up remaining MP4 files if not keeping (in case some weren't cleaned up individually)
        if not args.keep_mp4:
            for r in results:
                if r.get("file"):
                    try:
                        Path(r["file"]).unlink(missing_ok=True)
                    except Exception:
                        pass

    # Merge all individual reports into a single combined report
    print(f"[INFO] Merging {len(results)} individual reports into final report...", file=sys.stderr)
    report_path = merge_individual_reports(
        results, args.channel_url, channel_id, rss, NUM_VIDEOS, outdir
    )

    print(f"[DONE] Final merged report written: {report_path}")
    print(f"[INFO] Individual reports are available in: {outdir / 'individual_reports'}", file=sys.stderr)


if __name__ == "__main__":
    main()