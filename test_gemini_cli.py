#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini CLI動作確認用テストスクリプト
"""

import subprocess
import sys
import shutil
import os
from pathlib import Path


def find_gemini_command():
    """Gemini CLIコマンドのパスを探す"""
    gemini_path = shutil.which("gemini")
    if gemini_path:
        return gemini_path
    
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


def test_gemini_with_file():
    """@file構文でテスト（テキストファイルを使用）"""
    gemini_cmd = find_gemini_command()
    if not gemini_cmd:
        return False
    
    # テスト用のテキストファイルを作成
    test_file = Path("test_input.txt")
    test_content = """
人工知能（AI）は、コンピュータが人間のような知能を模倣する技術です。
機械学習、深層学習、自然言語処理などの分野が含まれます。
AIは医療、交通、教育など様々な分野で活用されています。
"""
    test_file.write_text(test_content, encoding="utf-8")
    
    try:
        test_file_abs = str(test_file.resolve()).replace("\\", "/")
        prompt = f"@{test_file_abs}\n\nこのファイルの内容を日本語で要約してください（50字程度）。"
        
        print(f"[INFO] @file構文でテストします...")
        print(f"[DEBUG] ファイル: {test_file_abs}")
        print(f"[DEBUG] プロンプト長: {len(prompt)} chars")
        
        try:
            result = subprocess.run(
                [gemini_cmd, prompt],
                capture_output=True,
                text=True,
                encoding="utf-8" if sys.platform == "win32" else None,
                errors="replace" if sys.platform == "win32" else "strict",
                timeout=30,
            )
        except subprocess.TimeoutExpired:
            print("[WARNING] @file構文でタイムアウトしました（30秒）- これは既知の問題です")
            return False
        
        print(f"[INFO] リターンコード: {result.returncode}")
        
        if result.stdout:
            print(f"\n[SUCCESS] 標準出力:")
            print("-" * 60)
            print(result.stdout)
            print("-" * 60)
        
        if result.stderr:
            print(f"\n[INFO] 標準エラー出力:")
            print("-" * 60)
            print(result.stderr)
            print("-" * 60)
        
        if result.returncode == 0:
            print("\n[SUCCESS] @file構文でGemini CLIは正常に動作しています！")
            return True
        else:
            print(f"\n[ERROR] @file構文でエラー（コード: {result.returncode}）")
            return False
    finally:
        # クリーンアップ
        if test_file.exists():
            test_file.unlink()


def test_gemini_simple():
    """シンプルなテキスト要約でテスト"""
    gemini_cmd = find_gemini_command()
    if not gemini_cmd:
        print("[ERROR] Gemini CLIが見つかりません", file=sys.stderr)
        print("[INFO] インストール方法: npm install -g @google/gemini-cli", file=sys.stderr)
        return False
    
    print(f"[INFO] Gemini CLI found: {gemini_cmd}")
    
    # ダミーテキスト
    dummy_text = """
    人工知能（AI）は、コンピュータが人間のような知能を模倣する技術です。
    機械学習、深層学習、自然言語処理などの分野が含まれます。
    AIは医療、交通、教育など様々な分野で活用されています。
    """
    
    prompt = f"以下のテキストを日本語で要約してください（50字程度）：{dummy_text}"
    
    print(f"[INFO] プロンプトを送信します...")
    print(f"[DEBUG] Prompt length: {len(prompt)} chars")
    print(f"[DEBUG] Prompt preview: {prompt[:100]}...")
    
    # 複数の方法を試す
    test_methods = [
        ("位置引数", [gemini_cmd, prompt]),
        ("--promptオプション", [gemini_cmd, "--prompt", prompt]),
        ("-pオプション", [gemini_cmd, "-p", prompt]),
    ]
    
    for method_name, cmd in test_methods:
        print(f"\n[TEST] 方法: {method_name}")
        print(f"[DEBUG] コマンド: {' '.join(cmd[:2])} ...")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding="utf-8" if sys.platform == "win32" else None,
                errors="replace" if sys.platform == "win32" else "strict",
                timeout=30,  # 30秒タイムアウト
            )
        
            print(f"[INFO] リターンコード: {result.returncode}")
            
            if result.stdout:
                print(f"\n[SUCCESS] 標準出力:")
                print("-" * 60)
                print(result.stdout)
                print("-" * 60)
            
            if result.stderr:
                print(f"\n[INFO] 標準エラー出力:")
                print("-" * 60)
                print(result.stderr)
                print("-" * 60)
            
            if result.returncode == 0:
                print(f"\n[SUCCESS] {method_name}でGemini CLIは正常に動作しています！")
                return True
            else:
                print(f"\n[FAILED] {method_name}でエラー（コード: {result.returncode}）")
                # 次の方法を試す
                continue
            
        except subprocess.TimeoutExpired:
            print(f"[ERROR] {method_name}でタイムアウトしました（30秒）")
            continue
        except FileNotFoundError:
            print(f"[ERROR] {method_name}でコマンドが見つかりません")
            continue
        except Exception as e:
            print(f"[ERROR] {method_name}で予期しないエラー: {type(e).__name__}: {e}")
            continue
    
    # すべての方法が失敗
    print("\n[ERROR] すべての方法でGemini CLIの実行に失敗しました")
    return False


def test_gemini_stdin():
    """標準入力（stdin）でプロンプトを渡すテスト"""
    gemini_cmd = find_gemini_command()
    if not gemini_cmd:
        return False
    
    print(f"[INFO] 標準入力でテストします...")
    
    # ダミーテキスト
    dummy_text = """
人工知能（AI）は、コンピュータが人間のような知能を模倣する技術です。
機械学習、深層学習、自然言語処理などの分野が含まれます。
AIは医療、交通、教育など様々な分野で活用されています。
"""
    
    prompt = f"以下のテキストを日本語で要約してください（50字程度）：{dummy_text}"
    
    print(f"[DEBUG] プロンプト長: {len(prompt)} chars")
    print(f"[DEBUG] プロンプトプレビュー: {prompt[:100]}...")
    
    try:
        # stdinからプロンプトを渡す
        result = subprocess.run(
            [gemini_cmd],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8" if sys.platform == "win32" else None,
            errors="replace" if sys.platform == "win32" else "strict",
            timeout=30,
        )
        
        print(f"[INFO] リターンコード: {result.returncode}")
        
        if result.stdout:
            print(f"\n[SUCCESS] 標準出力:")
            print("-" * 60)
            print(result.stdout)
            print("-" * 60)
        
        if result.stderr:
            print(f"\n[INFO] 標準エラー出力:")
            print("-" * 60)
            print(result.stderr)
            print("-" * 60)
        
        if result.returncode == 0:
            print("\n[SUCCESS] 標準入力でGemini CLIは正常に動作しています！")
            return True
        else:
            print(f"\n[ERROR] 標準入力でエラー（コード: {result.returncode}）")
            return False
    except subprocess.TimeoutExpired:
        print("[ERROR] 標準入力でタイムアウトしました（30秒）")
        return False
    except Exception as e:
        print(f"[ERROR] 標準入力で予期しないエラー: {type(e).__name__}: {e}")
        return False


def test_gemini_with_url():
    """URLを直接渡すテスト（YouTubeの短い動画など）"""
    gemini_cmd = find_gemini_command()
    if not gemini_cmd:
        return False
    
    print(f"[INFO] URL直接指定でテストします...")
    
    # テスト用のURL（短いYouTube動画や公開されているWebページ）
    test_urls = [
        ("YouTube Shorts", "https://www.youtube.com/shorts/waaAZ_f_S2I"),
        ("公開Webページ", "https://www.example.com"),
    ]
    
    for url_name, url in test_urls:
        print(f"\n[TEST] URLタイプ: {url_name}")
        print(f"[DEBUG] URL: {url}")
        
        # 方法1: URLを位置引数として渡す
        prompt1 = f"{url}\n\nこのURLの内容を日本語で要約してください。"
        
        # 方法2: --promptオプションでURLを渡す
        prompt2 = f"以下のURLの内容を要約してください: {url}"
        
        test_methods = [
            ("位置引数（URL直接）", [gemini_cmd, prompt1]),
            ("--promptオプション（URL）", [gemini_cmd, "--prompt", prompt2]),
        ]
        
        for method_name, cmd in test_methods:
            print(f"\n[TEST] 方法: {method_name}")
            print(f"[DEBUG] コマンド: {' '.join(cmd[:2])} ...")
            
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    encoding="utf-8" if sys.platform == "win32" else None,
                    errors="replace" if sys.platform == "win32" else "strict",
                    timeout=60,  # URL処理は時間がかかる可能性があるので60秒
                )
                
                print(f"[INFO] リターンコード: {result.returncode}")
                
                if result.stdout:
                    print(f"\n[SUCCESS] 標準出力:")
                    print("-" * 60)
                    print(result.stdout[:500])  # 最初の500文字のみ表示
                    if len(result.stdout) > 500:
                        print("... (truncated)")
                    print("-" * 60)
                
                if result.stderr:
                    print(f"\n[INFO] 標準エラー出力:")
                    print("-" * 60)
                    print(result.stderr[:500])  # 最初の500文字のみ表示
                    if len(result.stderr) > 500:
                        print("... (truncated)")
                    print("-" * 60)
                
                if result.returncode == 0:
                    print(f"\n[SUCCESS] {method_name}でURL処理が成功しました！")
                    return True
                else:
                    print(f"\n[FAILED] {method_name}でエラー（コード: {result.returncode}）")
                    # 次の方法を試す
                    continue
                    
            except subprocess.TimeoutExpired:
                print(f"[ERROR] {method_name}でタイムアウトしました（60秒）")
                continue
            except Exception as e:
                print(f"[ERROR] {method_name}で予期しないエラー: {type(e).__name__}: {e}")
                continue
        
        # このURLタイプでは成功しなかったが、次のURLを試す
        print(f"[INFO] {url_name}では成功しませんでした。次のURLを試します...")
    
    print("\n[ERROR] すべてのURLテストが失敗しました")
    return False


def test_gemini_version():
    """Gemini CLIのバージョン確認"""
    gemini_cmd = find_gemini_command()
    if not gemini_cmd:
        return False
    
    print(f"[INFO] Gemini CLIのバージョンを確認します...")
    
    try:
        result = subprocess.run(
            [gemini_cmd, "--version"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        
        if result.returncode == 0:
            print(f"[SUCCESS] バージョン情報:")
            print(result.stdout or result.stderr)
            return True
        else:
            print(f"[WARNING] バージョンコマンドが失敗しました（コード: {result.returncode}）")
            if result.stderr:
                print(result.stderr)
            return False
    except Exception as e:
        print(f"[ERROR] バージョン確認エラー: {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("Gemini CLI 動作確認テスト")
    print("=" * 60)
    print()
    
    # バージョン確認
    print("[TEST 1] バージョン確認")
    print("-" * 60)
    success0 = test_gemini_version()
    print()
    
    # シンプルな要約テスト
    print("[TEST 2] シンプルなテキスト要約テスト")
    print("-" * 60)
    success1 = test_gemini_simple()
    print()
    
    # @file構文テスト
    print("[TEST 3] @file構文テスト")
    print("-" * 60)
    success2 = test_gemini_with_file()
    print()
    
    # 標準入力テスト
    print("[TEST 4] 標準入力（stdin）テスト")
    print("-" * 60)
    success3 = test_gemini_stdin()
    print()
    
    # URL直接指定テスト
    print("[TEST 5] URL直接指定テスト")
    print("-" * 60)
    success4 = test_gemini_with_url()
    print()
    
    # 結果サマリー
    print("=" * 60)
    print("[RESULT] テスト結果サマリー")
    print("=" * 60)
    print(f"  TEST 1 (バージョン確認): {'OK' if success0 else 'NG'}")
    print(f"  TEST 2 (位置引数): {'OK' if success1 else 'NG'}")
    print(f"  TEST 3 (@file構文): {'OK' if success2 else 'NG (タイムアウト)'}")
    print(f"  TEST 4 (標準入力): {'OK' if success3 else 'NG'}")
    print(f"  TEST 5 (URL直接指定): {'OK' if success4 else 'NG'}")
    print("=" * 60)
    
    # 少なくとも1つ成功していればOK
    if success1 or success3 or success4:
        print("[RESULT] 一部のテストが成功しました！動作可能な方法が見つかりました。")
        sys.exit(0)
    else:
        print("[RESULT] すべてのテストが失敗しました。上記のエラーを確認してください。")
        sys.exit(1)
