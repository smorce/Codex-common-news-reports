"""gemma4_e2b_video_summary の yt-dlp スキップ・候補プールの単体テスト。"""

from __future__ import annotations

import gemma4_e2b_video_summary as g4


def test_video_candidate_pool_size() -> None:
    assert g4.video_candidate_pool_size(3) == 15
    assert g4.video_candidate_pool_size(1) == 11


def test_is_skippable_ytdlp_error_members_only() -> None:
    err = (
        "ERROR: [youtube] tT-J9TyoFw8: Join this channel to get access to "
        "members-only content like this video"
    )
    assert g4.is_skippable_ytdlp_error(err)


def test_is_skippable_ytdlp_error_other() -> None:
    assert not g4.is_skippable_ytdlp_error("ERROR: network timeout")


def test_is_retryable_ytdlp_error_403() -> None:
    err = "ERROR: unable to download video data: HTTP Error 403: Forbidden"
    assert g4.is_retryable_ytdlp_error(err)
    assert g4._ytdlp_error_summary(err) == err


def test_ytdlp_base_args_include_player_client() -> None:
    args = g4._ytdlp_base_args()
    joined = " ".join(args)
    assert "youtube:lang=ja;player_client=default,-android_sdkless" in joined
    assert "--no-update" in args


def test_ytdlp_base_args_include_ejs_when_js_runtime_present() -> None:
    args = g4._ytdlp_base_args()
    if any(name in args for name in ("node", "deno")):
        assert "--remote-components" in args
        idx = args.index("--remote-components")
        assert args[idx + 1] == "ejs:github"


if __name__ == "__main__":
    test_video_candidate_pool_size()
    test_is_skippable_ytdlp_error_members_only()
    test_is_skippable_ytdlp_error_other()
    test_is_retryable_ytdlp_error_403()
    test_ytdlp_base_args_include_player_client()
    test_ytdlp_base_args_include_ejs_when_js_runtime_present()
    print("all tests passed")
