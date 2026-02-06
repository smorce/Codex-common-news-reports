#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
動画ダウンロードと圧縮機能のテストスクリプト
"""

import sys
from pathlib import Path

# メインスクリプトの関数をインポート
from yt_top3_gemini_report import download_mp4, compress_video, check_ffmpeg_available, check_moviepy_available

def test_video_download():
    """短い動画をダウンロードして圧縮をテスト"""
    
    # テスト用の動画
    # 短い動画で基本動作をテスト
    # test_video_url = "https://www.youtube.com/shorts/waaAZ_f_S2I"
    
    # 長い動画で圧縮機能をテスト（27分の動画）
    test_video_url = "https://www.youtube.com/watch?v=57aDPcM9UxA"
    output_dir = Path("test_output")
    output_dir.mkdir(exist_ok=True)
    
    output_path = output_dir / "test_video.mp4"
    
    print("=" * 60)
    print("動画ダウンロードと圧縮機能のテスト")
    print("=" * 60)
    print(f"\nテスト動画URL: {test_video_url}")
    print(f"出力先: {output_path}")
    print()
    
    # 環境チェック
    print("環境チェック:")
    ffmpeg_available = check_ffmpeg_available()
    moviepy_available, moviepy_error = check_moviepy_available()
    
    print(f"  - FFmpeg CLI: {'利用可能' if ffmpeg_available else '利用不可'}")
    print(f"  - MoviePy: {'利用可能' if moviepy_available else f'利用不可 ({moviepy_error})'}")
    print()
    
    try:
        # 既存ファイルを削除
        if output_path.exists():
            output_path.unlink()
            print(f"[INFO] 既存ファイルを削除しました: {output_path}")
        
        # 動画をダウンロード（20MB制限）
        print("\n[1/3] 動画をダウンロード中...")
        print("-" * 60)
        downloaded_file = download_mp4(test_video_url, output_path, max_size_mb=20.0)
        
        file_size_mb = downloaded_file.stat().st_size / (1024 * 1024)
        print(f"\n[SUCCESS] ダウンロード完了!")
        print(f"  ファイル: {downloaded_file}")
        print(f"  サイズ: {file_size_mb:.2f} MB")
        
        # 20MBを超えている場合は圧縮をテスト
        if file_size_mb > 20.0:
            print(f"\n[2/3] ファイルサイズが20MBを超えています。圧縮を試行します...")
            print("-" * 60)
            
            compressed_path = output_dir / "test_video_compressed.mp4"
            if compressed_path.exists():
                compressed_path.unlink()
            
            compressed_file = compress_video(downloaded_file, compressed_path, target_size_mb=18.0)
            
            compressed_size_mb = compressed_file.stat().st_size / (1024 * 1024)
            print(f"\n[SUCCESS] 圧縮完了!")
            print(f"  ファイル: {compressed_file}")
            print(f"  サイズ: {compressed_size_mb:.2f} MB")
            print(f"  圧縮率: {(1 - compressed_size_mb / file_size_mb) * 100:.1f}%")
            
            if compressed_size_mb <= 20.0:
                print(f"\n✓ 圧縮成功: {compressed_size_mb:.2f} MB <= 20.0 MB")
            else:
                print(f"\n⚠ 圧縮後も20MBを超えています: {compressed_size_mb:.2f} MB > 20.0 MB")
                print(f"   より積極的な圧縮設定が必要です。")
                print(f"   現在の設定: 解像度640px以下、24fps、100kbps最小ビットレート")
        else:
            print(f"\n[2/3] 圧縮不要: ファイルサイズが20MB以下です ({file_size_mb:.2f} MB)")
        
        print("\n" + "=" * 60)
        print("[3/3] テスト完了!")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n[ERROR] テスト失敗: {type(e).__name__}: {e}")
        import traceback
        print("\n詳細:")
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_video_download()
    sys.exit(0 if success else 1)
