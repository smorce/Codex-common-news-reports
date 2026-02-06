import subprocess
import shutil
import sys
import os

def find_codex_command():
    """Codex CLIのパスを検索"""
    # まずPATHから検索
    codex_path = shutil.which("codex")
    if codex_path:
        return codex_path
    
    # 一般的なインストール場所を検索
    common_paths = [
        "C:\\Program Files\\codex\\codex.exe",
        "C:\\Users\\{}\\AppData\\Local\\Programs\\codex\\codex.exe".format(os.environ.get("USERNAME", "")),
        "C:\\Users\\{}\\AppData\\Roaming\\npm\\codex.cmd".format(os.environ.get("USERNAME", "")),
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            return path
    
    return None

def run_codex_command(command_args):
    """Codex コマンドを実行"""
    codex_cmd = find_codex_command()
    
    if not codex_cmd:
        print("エラー: Codex CLI が見つかりません。", file=sys.stderr)
        print("以下を確認してください:", file=sys.stderr)
        print("1. Codex CLI がインストールされているか", file=sys.stderr)
        print("2. PATH に Codex が設定されているか", file=sys.stderr)
        print("3. uv run 環境でも PATH が利用可能か", file=sys.stderr)
        return None
    
    print(f"Codex CLI を実行します: {codex_cmd}")
    
    try:
        # Codex コマンドを実行
        result = subprocess.run(
            [codex_cmd] + command_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30  # タイムアウトを設定
        )
        return result
    except subprocess.TimeoutExpired:
        print("エラー: Codex コマンドがタイムアウトしました。", file=sys.stderr)
        return None
    except Exception as e:
        print(f"エラー: Codex コマンドの実行に失敗しました: {e}", file=sys.stderr)
        return None

# 例: 認証済み & CLIが利用可能な状態でコマンドを実行
result = run_codex_command([
    "exec", 
    "--full-auto",
    "--skip-git-repo-check", 
    "print hello world by Python"
])

# 結果の表示
if result is not None:
    print("=== 標準出力 ===")
    print(result.stdout)
    print("\n=== エラー出力 ===")
    print(result.stderr)
    print(f"\n=== 終了コード: {result.returncode} ===")
else:
    print("Codex コマンドの実行に失敗しました。")