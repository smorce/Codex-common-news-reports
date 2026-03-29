#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qwen3-VL で動画を要約するサンプル。
既定チャンネル（DEFAULT_CHANNEL_URL）の RSS から最新 N 本（既定3本）を取得し、
yt-dlp でダウンロードして要約、Markdown レポートに保存する。

圧縮・サイズ制限は行わない（yt_top3_gemini_report と同様の取得方針）。

依存:
  uv sync（pyproject.toml に torch / transformers / qwen-vl-utils 等）
  システムに yt-dlp（マージ時は ffmpeg）を用意すること。

メモ:
  Hugging Face のローカルキャッシュを使う。
    from_pretrained("Qwen/Qwen3-VL-4B-Instruct") は Hugging Face のローカルキャッシュを使います。
    初回（キャッシュに無いとき）だけ、モデル・設定などをダウンロードしてキャッシュに保存します。
    2回目以降は、そのキャッシュから読み込むので、通常は再ダウンロードは発生しません。
  
  obsidianのメモ:
    Qwen3-VL の軽量版(4B, 8B)は良さそう。4B Instruct は使ってみたけど激強だったし、DeepSeek-OCR も良かった。決定版。
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from zoneinfo import ZoneInfo

import feedparser

# torch / transformers / qwen_vl_utils は generate_video_summary 内で遅延インポートする。
# --dry-run や RSS のみの確認では未インストールでも動かせる。


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
    if text:
        if sys.platform == "win32":
            kwargs["encoding"] = "utf-8"
            kwargs["errors"] = "replace"
    return subprocess.run(cmd, **kwargs)


def check_ffmpeg_available() -> bool:
    """PATH に ffmpeg があるか。"""
    try:
        result = run(["ffmpeg", "-version"], check=False, capture=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def download_mp4_simple(video_url: str, out_path: Path) -> Path:
    """
    yt-dlp で動画を取得し mp4 にまとめる（yt_top3_gemini_report.download_mp4 の簡略版）。
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
        except OSError as e:
            print(f"[WARNING] Failed to remove existing file: {e}", file=sys.stderr)

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

    print(f"[INFO] Downloaded: {mp4} ({mp4.stat().st_size / (1024 * 1024):.2f} MB)", file=sys.stderr)
    return mp4


def local_path_for_qwen_video(local_path: Path) -> str:
    """
    ローカル動画を Qwen / qwen_vl_utils 向けの文字列にする。
    Windows では decord が file:// URI を開けないことがあるため、絶対パスを使う。
    """
    return str(local_path.resolve())


def channel_id_from_url(channel_url: str) -> str | None:
    """https://www.youtube.com/channel/UC... から channel_id を取り出す。"""
    m = re.search(r"/channel/(UC[a-zA-Z0-9_-]{10,})", channel_url.strip())
    if m:
        return m.group(1)
    return None


def rss_url_for_channel_id(channel_id: str) -> str:
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"


def get_latest_video_urls_from_channel(channel_url: str, n: int = 1) -> list[tuple[str, str]]:
    """
    チャンネル RSS から新しい順に最大 n 件の (動画URL, タイトル) を返す。
    """
    cid = channel_id_from_url(channel_url)
    if not cid:
        raise ValueError(
            f"Could not extract channel id from URL: {channel_url!r} "
            "(expected .../channel/UC...)"
        )
    rss = rss_url_for_channel_id(cid)
    feed = feedparser.parse(rss)
    if getattr(feed, "bozo", False) and not feed.entries:
        raise RuntimeError(f"RSS parse failed or empty: {rss}")
    out: list[tuple[str, str]] = []
    for e in feed.entries[:n]:
        link = (getattr(e, "link", None) or "").strip()
        title = (getattr(e, "title", None) or "").strip()
        if link:
            out.append((link, title))
    if len(out) < n:
        raise RuntimeError(
            f"Not enough videos in RSS (wanted {n}, got {len(out)}): {rss}"
        )
    return out


def video_id_from_watch_url(url: str) -> str | None:
    """YouTube watch URL から動画 ID を取り出す。"""
    try:
        q = parse_qs(urlparse(url).query)
        v = q.get("v", [None])[0]
        return v
    except Exception:
        return None


def sanitize_filename_part(s: str, max_len: int = 80) -> str:
    """保存ファイル名用に簡易サニタイズ。"""
    s = re.sub(r'[\\/:*?"<>|]+', "_", s)
    s = re.sub(r"\s+", "_", s).strip("._")
    if len(s) > max_len:
        s = s[:max_len]
    return s or "video"


MODEL_NAME = "Qwen/Qwen3-VL-4B-Instruct"

DEFAULT_CHANNEL_URL = "https://www.youtube.com/channel/UCUWtuyVjeMQygQiy3adHb1g"

# RSS から取得して要約する本数の既定値（チャンネルモード）
DEFAULT_NUM_VIDEOS = 3

# 要約が途中で切れないよう、新規生成トークン上限を十分に取る（旧 256 では日本語長文が不足しがち）
DEFAULT_MAX_NEW_TOKENS = 2048

PROMPT_DEFAULT = (
    "日本語で実践的なレポートを生成してください。出力はJSON形式で提示してください。",
    "",
    "### 出力形式",
    "",
    "<<<JSON_OUTPUT",
    "{",
    '  "summary": "動画の内容を説明（400〜500字）",',
    '  "key_points": [',
    '    "ポイント1",',
    '    "ポイント2",',
    '    "ポイント3",',
    '    "ポイント4",',
    '    "ポイント5",',
    '  ],',
    '  "conclusion": "動画の核心メッセージを1〜2文で",',
    '  "recommended_action": "視聴者への具体的なアクション1つ"',
    "}",
    "JSON_OUTPUT>>>",
)

# Qwen3-VL README では total_pixels は 24576 * 32 * 32 未満を推奨
QWEN3_VL_TOTAL_PIXELS_RECOMMENDED_MAX = 24576 * 32 * 32
PIXEL_BASE = 32 * 32

# 24GB 級 VRAM で長尺動画時に OOM しにくいよう、qwen_vl_utils の警告に合わせて上限制御
# （「max_pixels exceeds limit」のログを避けるため、おおよそ 22 * (32*32) 相当に抑える）
VRAM_24G_MAX_PIXELS_PER_FRAME = 22 * PIXEL_BASE
VRAM_24G_TOTAL_PIXELS_CAP = 3000 * PIXEL_BASE
VRAM_24G_FPS_CAP = 0.25


@dataclass
class VideoBudget:
    fps: float
    min_pixels: int
    max_pixels: int
    total_pixels: int
    profile: str
    free_gb: float
    total_gb: float
    free_ratio: float


def round_to_multiple(value: int, base: int) -> int:
    """value を base の倍数に丸める。"""
    return max(base, int(round(value / base)) * base)


def get_cuda_mem_info(device, torch_mod) -> tuple[int, int]:
    """
    現在の GPU の空きメモリと総メモリを返す。
    PyTorch docs: torch.cuda.memory.mem_get_info()
    """
    if not torch_mod.cuda.is_available():
        raise RuntimeError("CUDA is not available. This script assumes a CUDA GPU (e.g. RTX 4090).")

    if device is None:
        device = torch_mod.cuda.current_device()

    torch_mod.cuda.empty_cache()
    free_bytes, total_bytes = torch_mod.cuda.memory.mem_get_info(device=device)
    return free_bytes, total_bytes


def choose_video_budget_for_rtx4090(
    torch_mod,
    reserve_gb: float = 6.0,
    device=None,
) -> VideoBudget:
    """
    RTX 4090 を想定した実用ヒューリスティック。
    - 空きメモリから reserve_gb を引いた「実効空きメモリ」で判断する
    - fps / max_pixels / total_pixels を安全側に自動調整する
    """
    free_bytes, total_bytes = get_cuda_mem_info(device, torch_mod)
    free_gb = free_bytes / (1024**3)
    total_gb = total_bytes / (1024**3)

    effective_free_gb = max(0.0, free_gb - reserve_gb)
    free_ratio = effective_free_gb / max(total_gb, 1e-6)

    if effective_free_gb >= 14:
        profile = "high"
        fps = 2.0
        min_pixels = 16 * PIXEL_BASE
        max_pixels = 512 * PIXEL_BASE
        total_pixels = 22000 * PIXEL_BASE
    elif effective_free_gb >= 10:
        profile = "balanced"
        fps = 1.5
        min_pixels = 8 * PIXEL_BASE
        max_pixels = 384 * PIXEL_BASE
        total_pixels = 18000 * PIXEL_BASE
    elif effective_free_gb >= 7:
        profile = "safe"
        fps = 1.0
        min_pixels = 4 * PIXEL_BASE
        max_pixels = 256 * PIXEL_BASE
        total_pixels = 14000 * PIXEL_BASE
    else:
        profile = "very_safe"
        fps = 0.5
        min_pixels = 4 * PIXEL_BASE
        max_pixels = 128 * PIXEL_BASE
        total_pixels = 8000 * PIXEL_BASE

    total_pixels = min(total_pixels, QWEN3_VL_TOTAL_PIXELS_RECOMMENDED_MAX - PIXEL_BASE)

    min_pixels = round_to_multiple(min_pixels, PIXEL_BASE)
    max_pixels = round_to_multiple(max_pixels, PIXEL_BASE)
    total_pixels = round_to_multiple(total_pixels, PIXEL_BASE)

    if min_pixels > max_pixels:
        min_pixels = max_pixels

    return VideoBudget(
        fps=fps,
        min_pixels=min_pixels,
        max_pixels=max_pixels,
        total_pixels=total_pixels,
        profile=profile,
        free_gb=free_gb,
        total_gb=total_gb,
        free_ratio=free_ratio,
    )


def clamp_budget_for_single_gpu_24gb(budget: VideoBudget) -> VideoBudget:
    """
    単一 GPU 約 24GB で動画が長い場合の OOM を避けるため、バジェットをさらに絞る。
    """
    fps = min(budget.fps, VRAM_24G_FPS_CAP)
    max_pixels = min(budget.max_pixels, VRAM_24G_MAX_PIXELS_PER_FRAME)
    total_pixels = min(budget.total_pixels, VRAM_24G_TOTAL_PIXELS_CAP)
    min_pixels = min(budget.min_pixels, max_pixels)
    min_pixels = round_to_multiple(min_pixels, PIXEL_BASE)
    max_pixels = round_to_multiple(max_pixels, PIXEL_BASE)
    total_pixels = round_to_multiple(total_pixels, PIXEL_BASE)
    if min_pixels > max_pixels:
        min_pixels = max_pixels
    return VideoBudget(
        fps=fps,
        min_pixels=min_pixels,
        max_pixels=max_pixels,
        total_pixels=total_pixels,
        profile=f"{budget.profile}+24g_clamp",
        free_gb=budget.free_gb,
        total_gb=budget.total_gb,
        free_ratio=budget.free_ratio,
    )


def build_messages(video_uri: str, user_prompt: str, budget: VideoBudget):
    return [
        {
            "role": "user",
            "content": [
                {
                    "type": "video",
                    "video": video_uri,
                    "fps": budget.fps,
                    "min_pixels": budget.min_pixels,
                    "max_pixels": budget.max_pixels,
                    "total_pixels": budget.total_pixels,
                },
                {
                    "type": "text",
                    "text": user_prompt,
                },
            ],
        }
    ]


def load_qwen_model(model_name: str):
    """モデルとプロセッサを1回だけ読み込む（複数本連続推論用）。"""
    from transformers import AutoModelForImageTextToText, AutoProcessor

    model = AutoModelForImageTextToText.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto",
    )
    processor = AutoProcessor.from_pretrained(model_name)
    return model, processor


def infer_one_video(
    model,
    processor,
    video_uri: str,
    user_prompt: str,
    *,
    print_budget: bool = True,
    max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
) -> tuple[str, VideoBudget]:
    """既にロード済みの model / processor で1本推論する。"""
    import torch
    from qwen_vl_utils import process_vision_info

    budget = choose_video_budget_for_rtx4090(torch)
    budget = clamp_budget_for_single_gpu_24gb(budget)

    if print_budget:
        print("=== Dynamic video budget ===")
        print(f"profile      : {budget.profile}")
        print(f"free / total : {budget.free_gb:.2f} GB / {budget.total_gb:.2f} GB")
        print(f"fps          : {budget.fps}")
        print(f"min_pixels   : {budget.min_pixels}")
        print(f"max_pixels   : {budget.max_pixels}")
        print(f"total_pixels : {budget.total_pixels}")

    messages = build_messages(video_uri, user_prompt, budget)

    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    images, videos, video_kwargs = process_vision_info(
        messages,
        image_patch_size=16,
        return_video_kwargs=True,
        return_video_metadata=True,
    )

    if videos is not None:
        videos, video_metadatas = zip(*videos)
        videos = list(videos)
        video_metadatas = list(video_metadatas)
    else:
        video_metadatas = None

    inputs = processor(
        text=[text],
        images=images,
        videos=videos,
        padding=True,
        return_tensors="pt",
        **video_kwargs,
    )
    inputs = inputs.to(model.device)

    generated_ids = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
    )

    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]

    output_text = processor.batch_decode(
        generated_ids_trimmed,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False,
    )

    return output_text[0], budget


def generate_video_summary(
    model_name: str,
    video_uri: str,
    user_prompt: str,
    *,
    max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
):
    """単体実行用: モデルを読み込んで1本要約する。"""
    model, processor = load_qwen_model(model_name)
    return infer_one_video(
        model,
        processor,
        video_uri,
        user_prompt,
        max_new_tokens=max_new_tokens,
    )


def default_report_path() -> Path:
    """Asia/Tokyo の日付でレポートパスを決める。"""
    now = datetime.now(ZoneInfo("Asia/Tokyo"))
    return Path("qwen3_vl_reports") / f"{now.strftime('%Y-%m-%d')}_qwen3_vl_summary.md"


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
        "# Qwen3-VL 動画要約レポート",
        "",
        f"- 生成日時: {generated_at_iso}",
        f"- チャンネル: {channel_url}",
        f"- モデル: `{model_name}`",
        f"- 本数: {len(entries)}",
        "",
    ]
    for i, (url, title, summary) in enumerate(entries, start=1):
        safe_title = title.replace("\n", " ").strip() or "(無題)"
        lines.extend(
            [
                f"## {i}. {safe_title}",
                "",
                f"- **URL**: {url}",
                "",
                "### 要約",
                "",
                summary.strip(),
                "",
                "---",
                "",
            ]
        )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Qwen3-VL で動画要約。既定チャンネルの最新動画は RSS で選び yt-dlp で取得する。"
    )
    p.add_argument(
        "--video-path",
        type=Path,
        default=None,
        help="ローカル動画ファイル（指定時はダウンロードをスキップ）",
    )
    p.add_argument(
        "--channel-url",
        default=DEFAULT_CHANNEL_URL,
        help=f"チャンネル URL（既定: {DEFAULT_CHANNEL_URL}）。--video-url 指定時は未使用。",
    )
    p.add_argument(
        "--video-url",
        default=None,
        help="ダウンロード元を直接指定（未指定時は --channel-url の RSS から取得）",
    )
    p.add_argument(
        "-n",
        "--num-videos",
        type=int,
        default=DEFAULT_NUM_VIDEOS,
        metavar="N",
        help=f"RSS から新しい順に取得して要約する本数（既定: {DEFAULT_NUM_VIDEOS}）。--video-path / --video-url 指定時は無視。",
    )
    p.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="要約レポートの Markdown 出力パス（未指定時: qwen3_vl_reports/YYYY-MM-DD_qwen3_vl_summary.md）。複数本モードで使用。",
    )
    p.add_argument(
        "--download-dir",
        type=Path,
        default=Path("qwen3_vl_cache"),
        help="yt-dlp の保存先ディレクトリ",
    )
    p.add_argument(
        "--download-filename",
        default="sample",
        help="単体モード（1本のみ）時の保存ベース名（拡張子なし）。複数本時は動画IDベースで上書き保存。",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="RSS 解決とダウンロードまで行い、モデル推論は行わない",
    )
    p.add_argument(
        "--model",
        default=MODEL_NAME,
        help="Hugging Face モデル名",
    )
    p.add_argument(
        "--prompt",
        default=PROMPT_DEFAULT,
        help="ユーザー指示プロンプト",
    )
    p.add_argument(
        "--max-new-tokens",
        type=int,
        default=DEFAULT_MAX_NEW_TOKENS,
        metavar="T",
        help=f"生成の最大新規トークン数（既定: {DEFAULT_MAX_NEW_TOKENS}）。要約が途中で切れる場合は増やす。",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    if args.max_new_tokens < 64:
        raise ValueError("--max-new-tokens must be >= 64")
    generated_at = datetime.now(ZoneInfo("Asia/Tokyo")).isoformat()

    # --- 単体: ローカルファイル ---
    if args.video_path is not None:
        if not args.video_path.is_file():
            raise FileNotFoundError(f"Video file not found: {args.video_path}")
        video_uri = local_path_for_qwen_video(args.video_path)
        print(f"[INFO] Using local file: {video_uri}", file=sys.stderr)

        if args.dry_run:
            print("\n=== dry-run: skip model inference ===")
            print(f"video_uri: {video_uri}")
            return

        summary, _budget = generate_video_summary(
            model_name=args.model,
            video_uri=video_uri,
            user_prompt=args.prompt,
            max_new_tokens=args.max_new_tokens,
        )
        print("\n=== Summary ===")
        print(summary)
        out = args.output or default_report_path()
        write_markdown_report(
            out,
            channel_url="(local file)",
            model_name=args.model,
            entries=[
                (
                    str(args.video_path.resolve()),
                    args.video_path.name,
                    summary,
                )
            ],
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
        video_uri = local_path_for_qwen_video(mp4_path)

        if args.dry_run:
            print("\n=== dry-run: skip model inference ===")
            print(f"video_uri: {video_uri}")
            return

        summary, _budget = generate_video_summary(
            model_name=args.model,
            video_uri=video_uri,
            user_prompt=args.prompt,
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
        return

    # --- チャンネル RSS: 複数本 ---
    if args.num_videos < 1:
        raise ValueError("--num-videos must be >= 1")

    pairs = get_latest_video_urls_from_channel(args.channel_url, n=args.num_videos)
    for i, (url, title) in enumerate(pairs):
        print(f"[INFO] RSS #{i + 1}: {title!r}\n       {url}", file=sys.stderr)

    if args.dry_run:
        print("\n=== dry-run: skip download & model inference ===")
        return

    import torch

    model, processor = load_qwen_model(args.model)
    report_entries: list[tuple[str, str, str]] = []

    for i, (video_url, title) in enumerate(pairs):
        vid = video_id_from_watch_url(video_url) or f"{i + 1}"
        stem = f"{i + 1:02d}_{sanitize_filename_part(vid)}"
        out_base = args.download_dir / stem
        print(f"\n[INFO] ({i + 1}/{len(pairs)}) Downloading…", file=sys.stderr)
        mp4_path = download_mp4_simple(video_url, out_base)
        video_uri = local_path_for_qwen_video(mp4_path)

        print(f"[INFO] ({i + 1}/{len(pairs)}) Summarizing…", file=sys.stderr)
        summary, _budget = infer_one_video(
            model,
            processor,
            video_uri,
            args.prompt,
            print_budget=(i == 0),
            max_new_tokens=args.max_new_tokens,
        )
        report_entries.append((video_url, title, summary))
        torch.cuda.empty_cache()

        print(f"\n=== Summary {i + 1}/{len(pairs)} ===")
        print(summary)

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
