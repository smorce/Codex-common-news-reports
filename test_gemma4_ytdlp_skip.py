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


if __name__ == "__main__":
    test_video_candidate_pool_size()
    test_is_skippable_ytdlp_error_members_only()
    test_is_skippable_ytdlp_error_other()
    print("all tests passed")
