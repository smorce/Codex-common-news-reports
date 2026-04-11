#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemma 4 E2B Instruct で動画を要約するサンプル（安全版・全体均等サンプリング・ウィンドウ分割対応）。

既定チャンネル（DEFAULT_CHANNEL_URL）の RSS から最新 N 本（既定3本）を取得し、
yt-dlp でダウンロードして要約し、Markdown レポートに保存する。

この版は、torchcodec が無い環境で Transformers が動画を全フレーム読み込みして
RAM を大量消費しやすい問題を避けるため、次の方針を取る。

- 既定の --video-input-mode=auto:
  - torchcodec がある → ネイティブ動画入力を使う
  - torchcodec がない → ffmpeg で動画全体からフレームを先に間引き、画像列として渡す
- --video-input-mode=native:
  - torchcodec 必須。無い場合は明示的にエラーで止める
- --video-input-mode=frames:
  - 常に ffmpeg でフレーム抽出して画像列として渡す

フレーム抽出は既定で --frame-sampling=uniform。
つまり、動画の先頭だけではなく、開始から終了までをほぼ等間隔で見る。
長尺動画では、max_frames に達したら全体に均等に散らして抽出する。

さらに frames モードでは、抽出したフレーム全部を 1 回の generate に渡さず、
小さなウィンドウに分けて順番に要約し、最後にテキストだけで統合する。
これで、フレーム枚数が多いときの CUDA OOM を起こしにくくする。

依存:
  uv sync / pip install -U torch transformers accelerate feedparser requests pillow
  ネイティブ動画入力を使う場合は torchcodec を推奨:
    pip install -U torchcodec
  システムに yt-dlp（マージ時は ffmpeg / ffprobe）を用意すること。

使い方:
  uv run --link-mode=copy gemma4_e2b_video_summary.py
  uv run --link-mode=copy gemma4_e2b_video_summary.py --video-url "https://www.youtube.com/watch?v=..."
  uv run --link-mode=copy gemma4_e2b_video_summary.py --video-path ./sample.mp4
  uv run --link-mode=copy gemma4_e2b_video_summary.py --video-input-mode=frames --frame-sampling=uniform --frames-per-window 4 --frame-height 256 --max-frames 32
"""

from __future__ import annotations

import argparse
import gc
import json
import math
import re
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from zoneinfo import ZoneInfo

import feedparser
import requests


# ----------------------------------
# 設定値
# ----------------------------------
MODEL_NAME = "google/gemma-4-E2B-it"
DEFAULT_CHANNEL_URL = "https://www.youtube.com/channel/UCUWtuyVjeMQygQiy3adHb1g"
DEFAULT_NUM_VIDEOS = 3
DEFAULT_MAX_NEW_TOKENS = 2048
DEFAULT_FRAME_FPS = 1.0
DEFAULT_MAX_FRAMES = 60
DEFAULT_FRAME_HEIGHT = 360
DEFAULT_FRAME_SAMPLING = "uniform"
DEFAULT_FRAMES_PER_WINDOW = 8
DEFAULT_WINDOW_MAX_NEW_TOKENS = 384

PROMPT_DEFAULT = """日本語で実践的なレポートを生成してください。固有名詞や具体例をできるだけ入れてください。出力はJSON形式にしてください。

### 出力形式
<<<JSON_OUTPUT
{
  "summary": "動画の内容を説明（400〜500字）",
  "key_points": [
    "ポイント1",
    "ポイント2",
    "ポイント3",
    "ポイント4",
    "ポイント5"
  ],
  "conclusion": "動画の核心メッセージを1〜2文で",
  "recommended_action": "視聴者への具体的なアクション1つ"
}
JSON_OUTPUT>>>
"""

RSS_REQUEST_TIMEOUT_SEC = 30
RSS_RETRY_MAX = 3
RSS_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)


@dataclass
class FrameSamplingResult:
    frame_paths: list[Path]
    timestamps_sec: list[float]
    duration_sec: float | None
    sampling_mode: str


class GenerateCudaOutOfMemoryError(RuntimeError):
    """model.generate 実行中の CUDA OOM を識別するための例外。"""


def run(
    cmd: list[str],
    *,
    check: bool = True,
    capture: bool = False,
    text: bool = True,
) -> subprocess.CompletedProcess:
    """subprocess.run の薄いラッパー（Windows では UTF-8 を優先）。"""
    kwargs: dict = {
        "check": check,
        "capture_output": capture,
        "text": text,
    }
    if text and sys.platform == "win32":
        kwargs["encoding"] = "utf-8"
        kwargs["errors"] = "replace"
    return subprocess.run(cmd, **kwargs)


def has_module(module_name: str) -> bool:
    try:
        __import__(module_name)
        return True
    except Exception:
        return False


def is_torchcodec_available() -> bool:
    return has_module("torchcodec")


def fetch_youtube_rss_feed(rss_url: str) -> bytes:
    """
    YouTube チャンネル RSS を HTTP で取得する。
    feedparser.parse(URL) の内部取得では 403 や空ボディになりやすいため、
    ブラウザ相当のヘッダで取る。
    """
    last_exc: BaseException | None = None
    for attempt in range(1, RSS_RETRY_MAX + 1):
        try:
            response = requests.get(
                rss_url,
                timeout=RSS_REQUEST_TIMEOUT_SEC,
                headers={
                    "User-Agent": RSS_USER_AGENT,
                    "Accept": "application/xml, text/xml, application/rss+xml, */*;q=0.9",
                    "Accept-Language": "en-US,en;q=0.9",
                },
            )
            response.raise_for_status()
            if not response.content:
                raise RuntimeError("Empty RSS response body")
            return response.content
        except Exception as exc:
            last_exc = exc
            if attempt < RSS_RETRY_MAX:
                time.sleep(1.0 * attempt)
    raise RuntimeError(
        f"Failed to fetch RSS after {RSS_RETRY_MAX} attempts: {rss_url!r}"
    ) from last_exc


def _channel_videos_page_url(channel_url: str) -> str:
    """チャンネルページ URL に /videos を付けてアップロード一覧用 URL にする。"""
    url = channel_url.strip().rstrip("/")
    if url.endswith("/videos"):
        return url
    return f"{url}/videos"


def get_latest_video_urls_via_ytdlp(channel_url: str, n: int) -> list[tuple[str, str]]:
    """
    RSS が 404 や空になる場合の代替。
    yt-dlp のフラットプレイリストで最新 n 本を取得する。
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    page = _channel_videos_page_url(channel_url)
    cp = run(
        [
            "yt-dlp",
            "--no-warnings",
            "--quiet",
            "--flat-playlist",
            "--print",
            "%(title)s\t%(url)s",
            "--playlist-items",
            f"1:{n}",
            page,
        ],
        check=False,
        capture=True,
        text=True,
    )
    if cp.returncode != 0:
        err = (cp.stderr or "").strip() or (cp.stdout or "").strip() or "(no output)"
        raise RuntimeError(f"yt-dlp flat-playlist failed (exit {cp.returncode}): {err}")

    out: list[tuple[str, str]] = []
    for line in (cp.stdout or "").splitlines():
        line = line.strip()
        if not line or "\t" not in line:
            continue
        title, url = line.split("\t", 1)
        title = title.strip()
        url = url.strip()
        if url.startswith("http"):
            out.append((url, title))

    if len(out) < n:
        raise RuntimeError(f"yt-dlp returned only {len(out)} video(s), need {n}: {page!r}")
    return out[:n]


def check_ffmpeg_available() -> bool:
    """PATH に ffmpeg があるか。"""
    try:
        result = run(["ffmpeg", "-version"], check=False, capture=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def check_ffprobe_available() -> bool:
    """PATH に ffprobe があるか。"""
    try:
        result = run(["ffprobe", "-version"], check=False, capture=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def download_mp4_simple(video_url: str, out_path: Path) -> Path:
    """
    yt-dlp で動画を取得し mp4 にまとめる。
    圧縮やファイルサイズによる再試行は行わない。
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    template = str(out_path.with_suffix(".%(ext)s"))
    has_ffmpeg = check_ffmpeg_available()

    if has_ffmpeg:
        format_spec = "bv*+ba/b"
        merge_format = "mp4"
    else:
        print(
            "[WARNING] ffmpeg not found. Using single-format download (may be lower quality).",
            file=sys.stderr,
        )
        format_spec = "best[ext=mp4][vcodec*=avc1]/best[ext=mp4]/best"
        merge_format = None

    mp4 = out_path.with_suffix(".mp4")
    if mp4.exists():
        try:
            mp4.unlink()
        except OSError as exc:
            print(f"[WARNING] Failed to remove existing file: {exc}", file=sys.stderr)

    for part_file in out_path.parent.glob(out_path.stem + "*.part"):
        try:
            part_file.unlink()
        except OSError:
            pass

    cmd = [
        "yt-dlp",
        "-f",
        format_spec,
        "-o",
        template,
        video_url,
    ]
    if merge_format:
        cmd.extend(["--merge-output-format", merge_format])
    cmd.extend(["--js-runtimes", "deno", "--no-part", "--no-continue"])

    run(cmd, check=True, capture=False)

    mp4 = out_path.with_suffix(".mp4")
    if not mp4.exists():
        candidates = list(out_path.parent.glob(out_path.stem + ".*"))
        if candidates:
            candidates.sort(key=lambda p: p.stat().st_size, reverse=True)
            mp4 = candidates[0]
        else:
            raise FileNotFoundError(f"Download finished but output not found: {out_path}")

    print(
        f"[INFO] Downloaded: {mp4} ({mp4.stat().st_size / (1024 * 1024):.2f} MB)",
        file=sys.stderr,
    )
    return mp4


def delete_downloaded_video_permanently(video_path: Path) -> None:
    """
    要約用にダウンロードした動画を完全削除する。
    pathlib.Path.unlink() はゴミ箱を使わずファイルを消す。
    同じ stem の副次ファイルも可能な範囲で削除する。
    """
    video_path = video_path.resolve()
    stem = video_path.stem
    parent = video_path.parent
    candidates = sorted(parent.glob(f"{stem}.*"))

    for attempt in range(3):
        gc.collect()
        try:
            import torch

            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except Exception:
            pass

        failed: list[Path] = []
        for path in candidates:
            if not path.exists():
                continue
            try:
                path.unlink()
            except PermissionError:
                failed.append(path)
            except OSError as exc:
                print(f"[WARNING] Failed to delete file {path}: {exc}", file=sys.stderr)

        if not failed:
            return
        candidates = failed
        if attempt < 2:
            time.sleep(0.5)

    for path in candidates:
        if path.exists():
            print(f"[WARNING] Could not delete (file may be in use): {path}", file=sys.stderr)


def local_path_for_video(local_path: Path) -> str:
    """ローカル動画パスを絶対パス文字列にする。"""
    return str(local_path.resolve())


def channel_id_from_url(channel_url: str) -> str | None:
    """https://www.youtube.com/channel/UC... から channel_id を取り出す。"""
    match = re.search(r"/channel/(UC[a-zA-Z0-9_-]{10,})", channel_url.strip())
    if match:
        return match.group(1)
    return None


def rss_url_for_channel_id(channel_id: str) -> str:
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"


def get_latest_video_urls_from_channel(channel_url: str, n: int = 1) -> list[tuple[str, str]]:
    """
    チャンネル RSS から新しい順に最大 n 件の (動画URL, タイトル) を返す。
    RSS が使えないときは yt-dlp にフォールバックする。
    """
    cid = channel_id_from_url(channel_url)
    if not cid:
        raise ValueError(
            f"Could not extract channel id from URL: {channel_url!r} "
            "(expected .../channel/UC...)"
        )

    rss = rss_url_for_channel_id(cid)
    feed = None
    try:
        raw = fetch_youtube_rss_feed(rss)
        feed = feedparser.parse(raw)
    except RuntimeError as exc:
        print(f"[WARNING] RSS fetch failed; falling back to yt-dlp: {exc}", file=sys.stderr)

    if feed is not None and feed.entries:
        out: list[tuple[str, str]] = []
        for entry in feed.entries[:n]:
            link = (getattr(entry, "link", None) or "").strip()
            title = (getattr(entry, "title", None) or "").strip()
            if link:
                out.append((link, title))
        if len(out) >= n:
            return out[:n]
        print(
            f"[WARNING] RSS had only {len(out)} usable entries (need {n}); "
            "falling back to yt-dlp.",
            file=sys.stderr,
        )
    elif feed is not None:
        bozo_ex = getattr(feed, "bozo_exception", None)
        print(
            f"[WARNING] RSS had no entries (bozo={getattr(feed, 'bozo', None)!r}, "
            f"bozo_exception={bozo_ex!r}); falling back to yt-dlp.",
            file=sys.stderr,
        )

    return get_latest_video_urls_via_ytdlp(channel_url, n)


def video_id_from_watch_url(url: str) -> str | None:
    """YouTube watch URL から動画 ID を取り出す。"""
    try:
        query = parse_qs(urlparse(url).query)
        return query.get("v", [None])[0]
    except Exception:
        return None


def strip_markdown_code_fence(text: str) -> str:
    """先頭の ``` / ```json などのフェンスを外す。"""
    s = text.strip()
    if not s.startswith("```"):
        return s
    lines = s.splitlines()
    if not lines:
        return s
    lines = lines[1:]
    while lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines).strip()


def try_parse_json_summary_object(raw: str) -> dict | None:
    """
    モデル出力から JSON オブジェクトを取り出す。
    前後に説明文や ``` フェンスがあっても、先頭の { から raw_decode する。
    """
    s = strip_markdown_code_fence(raw)
    if not s:
        return None
    if not s.startswith("{"):
        idx = s.find("{")
        if idx == -1:
            return None
        s = s[idx:]
    try:
        obj, _end = json.JSONDecoder().raw_decode(s)
    except json.JSONDecodeError:
        return None
    return obj if isinstance(obj, dict) else None


def format_json_summary_to_markdown(data: dict) -> str:
    """summary / key_points / conclusion / recommended_action を読みやすい Markdown にする。"""
    lines: list[str] = []

    summary = data.get("summary")
    if summary is not None and str(summary).strip():
        lines.extend(["#### 概要", "", str(summary).strip(), ""])

    key_points = data.get("key_points")
    if key_points is not None:
        lines.extend(["#### ポイント", ""])
        if isinstance(key_points, list):
            for point in key_points:
                lines.append(f"- {point}")
        else:
            lines.append(f"- {key_points}")
        lines.append("")

    conclusion = data.get("conclusion")
    if conclusion is not None and str(conclusion).strip():
        lines.extend(["#### 結論", "", str(conclusion).strip(), ""])

    action = data.get("recommended_action")
    if action is not None and str(action).strip():
        lines.extend(["#### おすすめアクション", "", str(action).strip(), ""])

    return "\n".join(lines).rstrip()


def summary_raw_to_report_body(raw: str) -> str:
    """要約テキストが JSON ならパースして整形し、失敗時はそのまま返す。"""
    parsed = try_parse_json_summary_object(raw)
    if parsed is not None:
        body = format_json_summary_to_markdown(parsed)
        if body:
            return body
    return raw.strip()


def sanitize_filename_part(text: str, max_len: int = 80) -> str:
    """保存ファイル名用に簡易サニタイズする。"""
    text = re.sub(r'[\\/:*?"<>|]+', "_", text)
    text = re.sub(r"\s+", "_", text).strip("._")
    if len(text) > max_len:
        text = text[:max_len]
    return text or "video"


def probe_video_duration_seconds(video_path: Path) -> float | None:
    """
    ffprobe で動画長を秒で取得する。
    取れないときは None を返す。
    """
    if not check_ffprobe_available():
        return None

    cp = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(video_path),
        ],
        check=False,
        capture=True,
        text=True,
    )
    if cp.returncode != 0:
        return None

    value = (cp.stdout or "").strip()
    if not value:
        return None
    try:
        duration = float(value)
    except ValueError:
        return None
    if not math.isfinite(duration) or duration <= 0:
        return None
    return duration


def format_ffmpeg_timestamp(seconds: float) -> str:
    """ffmpeg 用に秒を小数表記へ整形する。"""
    return f"{max(0.0, seconds):.6f}"


def compute_uniform_sample_timestamps(duration_sec: float, sample_count: int) -> list[float]:
    """
    動画全体を sample_count 区間に分け、その中央を時刻として返す。
    これで開始から終了までをほぼ均等に見る。
    """
    if sample_count < 1:
        raise ValueError("sample_count must be >= 1")
    if duration_sec <= 0 or not math.isfinite(duration_sec):
        return [0.0]

    eps = min(0.001, max(duration_sec / 1000.0, 1e-6))
    if sample_count == 1:
        return [max(0.0, min(duration_sec - eps, duration_sec / 2.0))]

    step = duration_sec / sample_count
    timestamps: list[float] = []
    for idx in range(sample_count):
        ts = (idx + 0.5) * step
        ts = max(0.0, min(duration_sec - eps, ts))
        timestamps.append(ts)
    return timestamps


def extract_frame_at_timestamp_with_ffmpeg(
    video_path: Path,
    out_path: Path,
    *,
    timestamp_sec: float,
    height: int,
) -> None:
    """
    指定時刻の 1 フレームを ffmpeg で抽出する。
    -ss を入力側に置き、高速化しつつ正確な位置へ寄せる。
    """
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-ss",
        format_ffmpeg_timestamp(timestamp_sec),
        "-i",
        str(video_path),
        "-frames:v",
        "1",
        "-q:v",
        "2",
        "-vf",
        f"scale=-2:{height}",
        str(out_path),
    ]
    run(cmd, check=True, capture=False)


def extract_head_sampled_frames_with_ffmpeg(
    video_path: Path,
    out_dir: Path,
    *,
    fps: float,
    max_frames: int,
    height: int,
) -> FrameSamplingResult:
    """
    先頭から一定 FPS でフレームを抽出する旧方式。
    長尺動画では後半が落ちるので、互換用に残す。
    """
    if fps <= 0:
        raise ValueError("fps must be > 0")
    if max_frames < 1:
        raise ValueError("max_frames must be >= 1")
    if height < 64:
        raise ValueError("height must be >= 64")
    if not check_ffmpeg_available():
        raise RuntimeError(
            "ffmpeg が見つかりません。--video-input-mode=frames を使うには ffmpeg が必要です。"
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    pattern = out_dir / "frame_%05d.jpg"

    vf_parts = [f"fps={fps}", f"scale=-2:{height}"]
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        str(video_path),
        "-vf",
        ",".join(vf_parts),
        "-frames:v",
        str(max_frames),
        str(pattern),
    ]
    run(cmd, check=True, capture=False)

    frame_paths = sorted(out_dir.glob("frame_*.jpg"))
    if not frame_paths:
        raise RuntimeError(f"フレーム抽出に失敗しました: {video_path}")

    timestamps_sec = [idx / fps for idx in range(len(frame_paths))]
    duration_sec = probe_video_duration_seconds(video_path)
    return FrameSamplingResult(
        frame_paths=frame_paths,
        timestamps_sec=timestamps_sec,
        duration_sec=duration_sec,
        sampling_mode="head",
    )


def extract_uniform_frames_with_ffmpeg(
    video_path: Path,
    out_dir: Path,
    *,
    fps: float,
    max_frames: int,
    height: int,
) -> FrameSamplingResult:
    """
    動画全体から等間隔でフレームを抽出する。
    短い動画では duration * fps を目安に枚数を決め、長い動画では max_frames を上限にする。
    """
    if fps <= 0:
        raise ValueError("fps must be > 0")
    if max_frames < 1:
        raise ValueError("max_frames must be >= 1")
    if height < 64:
        raise ValueError("height must be >= 64")
    if not check_ffmpeg_available():
        raise RuntimeError(
            "ffmpeg が見つかりません。--video-input-mode=frames を使うには ffmpeg が必要です。"
        )

    duration_sec = probe_video_duration_seconds(video_path)
    if duration_sec is None:
        print(
            "[WARNING] ffprobe で動画長を取得できませんでした。先頭サンプリングへフォールバックします。",
            file=sys.stderr,
        )
        return extract_head_sampled_frames_with_ffmpeg(
            video_path,
            out_dir,
            fps=fps,
            max_frames=max_frames,
            height=height,
        )

    estimated_count = max(1, int(math.ceil(duration_sec * fps)))
    sample_count = min(max_frames, estimated_count)
    timestamps_sec = compute_uniform_sample_timestamps(duration_sec, sample_count)

    out_dir.mkdir(parents=True, exist_ok=True)
    frame_paths: list[Path] = []
    for idx, ts in enumerate(timestamps_sec, start=1):
        out_path = out_dir / f"frame_{idx:05d}.jpg"
        extract_frame_at_timestamp_with_ffmpeg(
            video_path,
            out_path,
            timestamp_sec=ts,
            height=height,
        )
        if out_path.exists() and out_path.stat().st_size > 0:
            frame_paths.append(out_path)

    if not frame_paths:
        raise RuntimeError(f"均等フレーム抽出に失敗しました: {video_path}")

    return FrameSamplingResult(
        frame_paths=frame_paths,
        timestamps_sec=timestamps_sec[: len(frame_paths)],
        duration_sec=duration_sec,
        sampling_mode="uniform",
    )


def extract_sampled_frames_with_ffmpeg(
    video_path: Path,
    out_dir: Path,
    *,
    fps: float,
    max_frames: int,
    height: int,
    frame_sampling: str,
) -> FrameSamplingResult:
    """フレーム抽出方式を選んで実行する。"""
    if frame_sampling == "uniform":
        return extract_uniform_frames_with_ffmpeg(
            video_path,
            out_dir,
            fps=fps,
            max_frames=max_frames,
            height=height,
        )
    if frame_sampling == "head":
        return extract_head_sampled_frames_with_ffmpeg(
            video_path,
            out_dir,
            fps=fps,
            max_frames=max_frames,
            height=height,
        )
    raise ValueError(f"Unknown frame_sampling: {frame_sampling}")


def resolve_video_input_mode(requested_mode: str) -> str:
    """
    実際に使う入力モードを決める。
    auto では torchcodec があれば native、無ければ frames に落とす。
    """
    if requested_mode not in {"auto", "native", "frames"}:
        raise ValueError(f"Unknown video input mode: {requested_mode}")

    if requested_mode == "native":
        if not is_torchcodec_available():
            raise RuntimeError(
                "torchcodec が見つかりません。ネイティブ動画入力は torchcodec を前提にしてください。\n"
                "この環境でそのまま進めると、Transformers / torchvision 側で動画を全フレーム読み込んでから\n"
                "間引く経路に入り、RAM を大量に使うことがあります。\n"
                "対処方法:\n"
                "  1) pip install -U torchcodec\n"
                "  2) もしくは --video-input-mode=frames を使う"
            )
        return "native"

    if requested_mode == "frames":
        return "frames"

    if is_torchcodec_available():
        return "native"

    print(
        "[INFO] torchcodec not found. Falling back to ffmpeg frame extraction to avoid full-frame decode.",
        file=sys.stderr,
    )
    return "frames"


def load_gemma_model(model_name: str):
    """Gemma 4 モデルとプロセッサを 1 回だけ読み込む。"""
    try:
        from transformers import AutoModelForMultimodalLM, AutoProcessor
    except ImportError as exc:
        raise RuntimeError(
            "transformers が古い可能性があります。Gemma 4 では "
            "AutoModelForMultimodalLM が必要です。最新版へ更新してください。"
        ) from exc

    model = AutoModelForMultimodalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto",
    )
    processor = AutoProcessor.from_pretrained(model_name)
    return model, processor


def build_video_messages(video_uri: str, user_prompt: str) -> list[dict]:
    return [
        {
            "role": "user",
            "content": [
                {"type": "video", "video": video_uri},
                {"type": "text", "text": user_prompt},
            ],
        }
    ]


def build_frame_messages(frame_paths: list[Path], user_prompt: str) -> list[dict]:
    content: list[dict] = []
    for path in frame_paths:
        content.append({"type": "image", "image": str(path.resolve())})
    content.append(
        {
            "type": "text",
            "text": (
                "以下は同一動画から時系列順に、動画全体をカバーするよう抽出したフレームです。"
                "動画全体の流れとして理解して要約してください。\n\n"
                f"{user_prompt}"
            ),
        }
    )
    return [{"role": "user", "content": content}]


def build_text_messages(text_prompt: str) -> list[dict]:
    return [{"role": "user", "content": [{"type": "text", "text": text_prompt}]}]


def iter_frame_windows(items: list[Path], window_size: int):
    if window_size < 1:
        raise ValueError("window_size must be >= 1")
    for start in range(0, len(items), window_size):
        end = min(start + window_size, len(items))
        yield start, end, items[start:end]


def format_seconds_label(seconds: float | None) -> str:
    if seconds is None or not math.isfinite(seconds):
        return "不明"
    total = max(0, int(round(seconds)))
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def build_window_messages(
    frame_paths: list[Path],
    *,
    window_index: int,
    num_windows: int,
    start_sec: float | None,
    end_sec: float | None,
) -> list[dict]:
    content: list[dict] = []
    for path in frame_paths:
        content.append({"type": "image", "image": str(path.resolve())})
    prompt = f"""以下は同一動画を時系列順に分割したうちの 1 区間です。

区間番号: {window_index}/{num_windows}
推定時刻範囲: {format_seconds_label(start_sec)} から {format_seconds_label(end_sec)}

この区間だけを見て、場面の流れ、話題、見た目の変化、重要な出来事を簡潔に整理してください。
出力は JSON だけにしてください。

<<<JSON_OUTPUT
{{
  "window_summary": "この区間で何が起きているかを 120〜220 字で",
  "important_points": [
    "重要点1",
    "重要点2",
    "重要点3"
  ],
  "visual_changes": [
    "画面や場面の変化1",
    "画面や場面の変化2"
  ]
}}
JSON_OUTPUT>>>
"""
    content.append({"type": "text", "text": prompt})
    return [{"role": "user", "content": content}]


def build_final_aggregation_prompt(
    window_outputs: list[tuple[int, float | None, float | None, str]],
    *,
    user_prompt: str,
    duration_sec: float | None,
) -> str:
    lines = [
        "以下は、1 本の動画を時系列順に分けて解析した結果です。",
        "各区間は動画全体から均等サンプリングしたフレームを小分けにして見たものです。",
    ]
    if duration_sec is not None and math.isfinite(duration_sec):
        lines.append(f"動画全体の長さの目安: {format_seconds_label(duration_sec)}")
    lines.extend(["", "### 区間ごとのメモ", ""])
    for index, start_sec, end_sec, text in window_outputs:
        lines.append(
            f"#### 区間 {index} ({format_seconds_label(start_sec)} から {format_seconds_label(end_sec)})"
        )
        lines.append(text.strip())
        lines.append("")
    lines.extend(
        [
            "上の区間メモを統合して、重複や矛盾を整理し、動画全体として一貫した最終要約を作ってください。",
            "出力形式は次の指示に厳密に従ってください。",
            "",
            user_prompt,
        ]
    )
    return "\n".join(lines).strip()


def release_cuda_memory() -> None:
    gc.collect()
    try:
        import torch

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    except Exception:
        pass


def is_cuda_oom_error(exc: BaseException) -> bool:
    text = str(exc).lower()
    return (
        "cuda out of memory" in text
        or "cuda error: out of memory" in text
        or "cublas_status_alloc_failed" in text
    )


def infer_frame_windows(
    model,
    processor,
    sampling_result: FrameSamplingResult,
    user_prompt: str,
    *,
    frames_per_window: int,
    max_new_tokens: int,
) -> str:
    if frames_per_window < 1:
        raise ValueError("frames_per_window must be >= 1")

    frame_paths = sampling_result.frame_paths
    timestamps_sec = sampling_result.timestamps_sec
    if not frame_paths:
        raise RuntimeError("No sampled frames to summarize.")

    current_window_size = min(frames_per_window, len(frame_paths))
    last_exc: BaseException | None = None

    while current_window_size >= 1:
        try:
            window_outputs: list[tuple[int, float | None, float | None, str]] = []
            windows = list(iter_frame_windows(frame_paths, current_window_size))
            total_windows = len(windows)
            print(
                f"[INFO] Windowed frame summarization: {len(frame_paths)} frame(s), "
                f"window_size={current_window_size}, windows={total_windows}",
                file=sys.stderr,
            )

            for window_number, (start, end, sub_frames) in enumerate(windows, start=1):
                sub_timestamps = timestamps_sec[start:end]
                start_sec = sub_timestamps[0] if sub_timestamps else None
                end_sec = sub_timestamps[-1] if sub_timestamps else None
                print(
                    f"[INFO]   Window {window_number}/{total_windows}: "
                    f"frames={len(sub_frames)}, "
                    f"range={format_seconds_label(start_sec)}-{format_seconds_label(end_sec)}",
                    file=sys.stderr,
                )
                messages = build_window_messages(
                    sub_frames,
                    window_index=window_number,
                    num_windows=total_windows,
                    start_sec=start_sec,
                    end_sec=end_sec,
                )
                window_text = infer_one_messages(
                    model,
                    processor,
                    messages,
                    max_new_tokens=min(DEFAULT_WINDOW_MAX_NEW_TOKENS, max_new_tokens),
                )
                window_outputs.append((window_number, start_sec, end_sec, window_text))

            final_prompt = build_final_aggregation_prompt(
                window_outputs,
                user_prompt=user_prompt,
                duration_sec=sampling_result.duration_sec,
            )
            return infer_one_messages(
                model,
                processor,
                build_text_messages(final_prompt),
                max_new_tokens=max_new_tokens,
            )
        except GenerateCudaOutOfMemoryError as exc:
            last_exc = exc
            if current_window_size == 1:
                break
            next_window_size = max(1, current_window_size // 2)
            if next_window_size == current_window_size:
                next_window_size = current_window_size - 1
            print(
                "[WARNING] CUDA OOM during frame-window summarization. "
                f"Retrying with smaller window_size={next_window_size}.",
                file=sys.stderr,
            )
            release_cuda_memory()
            current_window_size = next_window_size

    raise RuntimeError(
        "frames モードで CUDA メモリが不足しました。"
        " --frames-per-window をさらに小さくするか、--frame-height や --max-frames を下げてください。"
    ) from last_exc


def infer_one_messages(
    model,
    processor,
    messages: list[dict],
    *,
    max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
    do_sample: bool = True,
    temperature: float = 1.0,
    top_p: float = 0.95,
    top_k: int = 64,
    repetition_penalty: float = 1.05,
) -> str:
    """既にロード済みの model / processor で 1 件推論する。"""
    inputs = None
    outputs = None
    generated = None
    try:
        inputs = processor.apply_chat_template(
            messages,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
            add_generation_prompt=True,
        )
        inputs = inputs.to(model.device)

        input_len = inputs["input_ids"].shape[-1]
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=do_sample,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
        )
        generated = outputs[0][input_len:]
        text = processor.decode(generated, skip_special_tokens=True)
        return text.strip()
    except RuntimeError as exc:
        if is_cuda_oom_error(exc):
            release_cuda_memory()
            raise GenerateCudaOutOfMemoryError(str(exc)) from exc
        raise
    finally:
        del inputs, outputs, generated
        release_cuda_memory()


def infer_one_video(
    model,
    processor,
    video_path: Path,
    user_prompt: str,
    *,
    video_input_mode: str,
    frame_fps: float,
    max_frames: int,
    frame_height: int,
    frame_sampling: str,
    frames_per_window: int,
    max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
) -> str:
    """
    1 本の動画を要約する。
    video_input_mode に応じてネイティブ動画入力か画像列入力を使い分ける。
    frames モードでは、小さなウィンドウに分けて段階的に要約する。
    """
    effective_mode = resolve_video_input_mode(video_input_mode)

    if effective_mode == "native":
        messages = build_video_messages(local_path_for_video(video_path), user_prompt)
        return infer_one_messages(
            model,
            processor,
            messages,
            max_new_tokens=max_new_tokens,
        )

    with tempfile.TemporaryDirectory(prefix="gemma4_frames_") as tmpdir:
        sampling_result = extract_sampled_frames_with_ffmpeg(
            video_path,
            Path(tmpdir),
            fps=frame_fps,
            max_frames=max_frames,
            height=frame_height,
            frame_sampling=frame_sampling,
        )
        if sampling_result.duration_sec is not None and sampling_result.timestamps_sec:
            print(
                "[INFO] Using frame fallback: "
                f"{len(sampling_result.frame_paths)} frame(s), "
                f"sampling={sampling_result.sampling_mode}, "
                f"duration={sampling_result.duration_sec:.2f}s, "
                f"first={sampling_result.timestamps_sec[0]:.2f}s, "
                f"last={sampling_result.timestamps_sec[-1]:.2f}s, "
                f"height={frame_height}, "
                f"frames_per_window={frames_per_window}",
                file=sys.stderr,
            )
        else:
            print(
                "[INFO] Using frame fallback: "
                f"{len(sampling_result.frame_paths)} frame(s), "
                f"sampling={sampling_result.sampling_mode}, "
                f"height={frame_height}, "
                f"frames_per_window={frames_per_window}",
                file=sys.stderr,
            )
        return infer_frame_windows(
            model,
            processor,
            sampling_result,
            user_prompt,
            frames_per_window=frames_per_window,
            max_new_tokens=max_new_tokens,
        )


def generate_video_summary(
    model_name: str,
    video_path: Path,
    user_prompt: str,
    *,
    video_input_mode: str,
    frame_fps: float,
    max_frames: int,
    frame_height: int,
    frame_sampling: str,
    frames_per_window: int,
    max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
) -> str:
    """単体実行用: モデルを読み込んで 1 本要約する。"""
    model, processor = load_gemma_model(model_name)
    return infer_one_video(
        model,
        processor,
        video_path,
        user_prompt,
        video_input_mode=video_input_mode,
        frame_fps=frame_fps,
        max_frames=max_frames,
        frame_height=frame_height,
        frame_sampling=frame_sampling,
        frames_per_window=frames_per_window,
        max_new_tokens=max_new_tokens,
    )


def default_report_path() -> Path:
    """Asia/Tokyo の日付でレポートパスを決める。"""
    now = datetime.now(ZoneInfo("Asia/Tokyo"))
    return Path("gemma4_reports") / f"{now.strftime('%Y-%m-%d')}_gemma4_summary.md"


def write_markdown_report(
    out_path: Path,
    *,
    channel_url: str,
    model_name: str,
    entries: list[tuple[str, str, str]],
    generated_at_iso: str,
) -> None:
    """
    entries: (url, title, summary) のリスト。
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        "# Gemma 4 動画要約レポート",
        "",
        f"- 生成日時: {generated_at_iso}",
        f"- チャンネル: {channel_url}",
        f"- モデル: `{model_name}`",
        f"- 本数: {len(entries)}",
        "",
    ]
    for i, (url, title, summary) in enumerate(entries, start=1):
        safe_title = title.replace("\n", " ").strip() or "(無題)"
        body = summary_raw_to_report_body(summary)
        lines.extend(
            [
                f"## {i}. {safe_title}",
                "",
                f"- **URL**: {url}",
                "",
                "### 要約",
                "",
                body,
                "",
                "---",
                "",
            ]
        )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gemma 4 E2B Instruct で動画要約。既定チャンネルの最新動画は RSS で選び yt-dlp で取得する。"
    )
    parser.add_argument(
        "--video-path",
        type=Path,
        default=None,
        help="ローカル動画ファイル（指定時はダウンロードをスキップ）",
    )
    parser.add_argument(
        "--channel-url",
        default=DEFAULT_CHANNEL_URL,
        help=f"チャンネル URL（既定: {DEFAULT_CHANNEL_URL}）。--video-url 指定時は未使用。",
    )
    parser.add_argument(
        "--video-url",
        default=None,
        help="ダウンロード元を直接指定（未指定時は --channel-url の RSS から取得）",
    )
    parser.add_argument(
        "-n",
        "--num-videos",
        type=int,
        default=DEFAULT_NUM_VIDEOS,
        metavar="N",
        help=f"RSS から新しい順に取得して要約する本数（既定: {DEFAULT_NUM_VIDEOS}）。--video-path / --video-url 指定時は無視。",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="要約レポートの Markdown 出力パス（未指定時: gemma4_reports/YYYY-MM-DD_gemma4_summary.md）。複数本モードで使用。",
    )
    parser.add_argument(
        "--download-dir",
        type=Path,
        default=Path("gemma4_cache"),
        help="yt-dlp の保存先ディレクトリ",
    )
    parser.add_argument(
        "--download-filename",
        default="sample",
        help="単体モード（1本のみ）時の保存ベース名（拡張子なし）。複数本時は動画IDベースで保存。",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="RSS 解決とダウンロードまで行い、モデル推論は行わない",
    )
    parser.add_argument(
        "--model",
        default=MODEL_NAME,
        help="Hugging Face モデル名",
    )
    parser.add_argument(
        "--prompt",
        default=PROMPT_DEFAULT,
        help="ユーザー指示プロンプト",
    )
    parser.add_argument(
        "--max-new-tokens",
        type=int,
        default=DEFAULT_MAX_NEW_TOKENS,
        metavar="T",
        help=f"生成の最大新規トークン数（既定: {DEFAULT_MAX_NEW_TOKENS}）。要約が途中で切れる場合は増やす。",
    )
    parser.add_argument(
        "--video-input-mode",
        choices=["auto", "native", "frames"],
        default="auto",
        help=(
            "動画入力の扱い。auto=torchcodec があればネイティブ動画、無ければ ffmpeg フレーム抽出。"
            "native=torchcodec 必須。frames=常にフレーム抽出。"
        ),
    )
    parser.add_argument(
        "--frame-fps",
        type=float,
        default=DEFAULT_FRAME_FPS,
        help=f"フレーム抽出時の基準 FPS（既定: {DEFAULT_FRAME_FPS}）。uniform では動画長から目安枚数を決めるために使う。",
    )
    parser.add_argument(
        "--max-frames",
        type=int,
        default=DEFAULT_MAX_FRAMES,
        help=f"フレーム抽出時の最大枚数（既定: {DEFAULT_MAX_FRAMES}）。",
    )
    parser.add_argument(
        "--frame-height",
        type=int,
        default=DEFAULT_FRAME_HEIGHT,
        help=f"フレーム抽出時の高さ（既定: {DEFAULT_FRAME_HEIGHT}）。",
    )
    parser.add_argument(
        "--frame-sampling",
        choices=["uniform", "head"],
        default=DEFAULT_FRAME_SAMPLING,
        help=(
            "frames モード時の抽出方法。uniform=動画全体から等間隔に抽出。"
            "head=先頭から一定 FPS で抽出。既定は uniform。"
        ),
    )
    parser.add_argument(
        "--frames-per-window",
        type=int,
        default=DEFAULT_FRAMES_PER_WINDOW,
        help=(
            f"frames モードで 1 回の generate に渡す最大フレーム枚数（既定: {DEFAULT_FRAMES_PER_WINDOW}）。"
            "大きいほど速い一方、CUDA メモリを多く使います。"
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.max_new_tokens < 64:
        raise ValueError("--max-new-tokens must be >= 64")
    if args.num_videos < 1:
        raise ValueError("--num-videos must be >= 1")
    if args.frame_fps <= 0:
        raise ValueError("--frame-fps must be > 0")
    if args.max_frames < 1:
        raise ValueError("--max-frames must be >= 1")
    if args.frame_height < 64:
        raise ValueError("--frame-height must be >= 64")
    if args.frames_per_window < 1:
        raise ValueError("--frames-per-window must be >= 1")

    generated_at = datetime.now(ZoneInfo("Asia/Tokyo")).isoformat()

    # --- 単体: ローカルファイル ---
    if args.video_path is not None:
        if not args.video_path.is_file():
            raise FileNotFoundError(f"Video file not found: {args.video_path}")

        video_path = args.video_path.resolve()
        print(f"[INFO] Using local file: {video_path}", file=sys.stderr)

        if args.dry_run:
            print("\n=== dry-run: skip model inference ===")
            print(f"video_path: {video_path}")
            print(f"video_input_mode: {resolve_video_input_mode(args.video_input_mode)}")
            print(f"frame_sampling: {args.frame_sampling}")
            print(f"frames_per_window: {args.frames_per_window}")
            return

        summary = generate_video_summary(
            model_name=args.model,
            video_path=video_path,
            user_prompt=args.prompt,
            video_input_mode=args.video_input_mode,
            frame_fps=args.frame_fps,
            max_frames=args.max_frames,
            frame_height=args.frame_height,
            frame_sampling=args.frame_sampling,
            frames_per_window=args.frames_per_window,
            max_new_tokens=args.max_new_tokens,
        )
        print("\n=== Summary ===")
        print(summary)

        out = args.output or default_report_path()
        write_markdown_report(
            out,
            channel_url="(local file)",
            model_name=args.model,
            entries=[(str(video_path), video_path.name, summary)],
            generated_at_iso=generated_at,
        )
        print(f"\n[INFO] Report written: {out}", file=sys.stderr)
        return

    # --- 単体: 明示 URL ---
    if args.video_url:
        video_url = args.video_url.strip()
        print(f"[INFO] Using explicit video URL: {video_url}", file=sys.stderr)
        out_base = args.download_dir / args.download_filename
        mp4_path = download_mp4_simple(video_url, out_base)

        try:
            if args.dry_run:
                print("\n=== dry-run: skip model inference ===")
                print(f"video_path: {mp4_path.resolve()}")
                print(f"video_input_mode: {resolve_video_input_mode(args.video_input_mode)}")
                print(f"frame_sampling: {args.frame_sampling}")
                print(f"frames_per_window: {args.frames_per_window}")
                return

            summary = generate_video_summary(
                model_name=args.model,
                video_path=mp4_path.resolve(),
                user_prompt=args.prompt,
                video_input_mode=args.video_input_mode,
                frame_fps=args.frame_fps,
                max_frames=args.max_frames,
                frame_height=args.frame_height,
                frame_sampling=args.frame_sampling,
                frames_per_window=args.frames_per_window,
                max_new_tokens=args.max_new_tokens,
            )
            print("\n=== Summary ===")
            print(summary)

            vid = video_id_from_watch_url(video_url) or "video"
            out = args.output or default_report_path()
            write_markdown_report(
                out,
                channel_url="(single URL)",
                model_name=args.model,
                entries=[(video_url, vid, summary)],
                generated_at_iso=generated_at,
            )
            print(f"\n[INFO] Report written: {out}", file=sys.stderr)
        finally:
            delete_downloaded_video_permanently(mp4_path)
        return

    # --- チャンネル RSS: 複数本 ---
    pairs = get_latest_video_urls_from_channel(args.channel_url, n=args.num_videos)
    for i, (url, title) in enumerate(pairs, start=1):
        print(f"[INFO] RSS #{i}: {title!r}\n       {url}", file=sys.stderr)

    if args.dry_run:
        print("\n=== dry-run: skip download & model inference ===")
        print(f"video_input_mode: {resolve_video_input_mode(args.video_input_mode)}")
        print(f"frame_sampling: {args.frame_sampling}")
        return

    model, processor = load_gemma_model(args.model)
    report_entries: list[tuple[str, str, str]] = []

    for i, (video_url, title) in enumerate(pairs, start=1):
        vid = video_id_from_watch_url(video_url) or f"{i}"
        stem = f"{i:02d}_{sanitize_filename_part(vid)}"
        out_base = args.download_dir / stem
        print(f"\n[INFO] ({i}/{len(pairs)}) Downloading…", file=sys.stderr)
        mp4_path = download_mp4_simple(video_url, out_base)

        try:
            print(f"[INFO] ({i}/{len(pairs)}) Summarizing…", file=sys.stderr)
            summary = infer_one_video(
                model,
                processor,
                mp4_path.resolve(),
                args.prompt,
                video_input_mode=args.video_input_mode,
                frame_fps=args.frame_fps,
                max_frames=args.max_frames,
                frame_height=args.frame_height,
                frame_sampling=args.frame_sampling,
                frames_per_window=args.frames_per_window,
                max_new_tokens=args.max_new_tokens,
            )
            report_entries.append((video_url, title, summary))

            print(f"\n=== Summary {i}/{len(pairs)} ===")
            print(summary)
        finally:
            delete_downloaded_video_permanently(mp4_path)

    out = args.output or default_report_path()
    write_markdown_report(
        out,
        channel_url=args.channel_url,
        model_name=args.model,
        entries=report_entries,
        generated_at_iso=generated_at,
    )
    print(f"\n[INFO] Report written: {out}", file=sys.stderr)


if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass
    main()