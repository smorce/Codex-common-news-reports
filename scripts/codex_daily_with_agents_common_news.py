#!/usr/bin/env python3
# scripts/codex_daily_with_agents_common_news.py

# 標準出力を UTF-8（かつエラーは置換）に再設定
# 先頭に追加（ファイルの一番上、他の import の前に置くのが確実）
import os
import sys

# Python の UTF-8 モードを有効化（環境変数）
os.environ.setdefault("PYTHONUTF8", "1")

# 標準出力／標準エラーを UTF-8 に設定し、出力不可文字は置換する
try:
    # Python 3.7+ で利用可
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    # 古い環境など reconfigure が無い場合は無視しておく
    pass


import random
import subprocess
import tempfile
import shutil
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel


# =============================================================================
# リトライ設定 (Retry Configuration) - 429 等の一時的エラー用
# =============================================================================
LLM_MAX_RETRIES = int(os.getenv("LLM_MAX_RETRIES", "3"))
LLM_RETRY_BASE_DELAY = float(os.getenv("LLM_RETRY_BASE_DELAY", "10.0"))
LLM_RETRY_MAX_DELAY = float(os.getenv("LLM_RETRY_MAX_DELAY", "120.0"))
LLM_RETRY_STATUS_CODES = [429, 500, 502, 503, 504]


class RetryHandler:
    """
    指数バックオフとジッターを使用したリトライハンドラー。
    Codex 実行時の 429 / 5xx / タイムアウト等に備える。
    """

    def __init__(
        self,
        max_retries: int = LLM_MAX_RETRIES,
        base_delay: float = LLM_RETRY_BASE_DELAY,
        max_delay: float = LLM_RETRY_MAX_DELAY,
        retry_status_codes: list[int] | None = None,
        log_func=None,
    ):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.retry_status_codes = retry_status_codes or LLM_RETRY_STATUS_CODES
        self.log_func = log_func

    def should_retry(self, exception: Exception, attempt: int) -> bool:
        """
        リトライすべきかどうかを判定する。

        Args:
            exception: 発生した例外
            attempt: 現在の試行回数（0始まり）

        Returns:
            リトライすべき場合は True
        """
        if attempt >= self.max_retries:
            return False

        error_str = str(exception)

        # コンテキストウィンドウ超過エラーはリトライしない（回復不可能）
        non_retryable_keywords = [
            "context_length_exceeded",
            "context window",
            "input exceeds",
        ]
        if any(kw in error_str.lower() for kw in non_retryable_keywords):
            msg = f"Non-retryable error detected (context length exceeded): {error_str[:200]}"
            if self.log_func:
                self.log_func(msg)
            return False

        # ステータスコード（429, 5xx 等）が含まれる場合はリトライ
        for code in self.retry_status_codes:
            if str(code) in error_str:
                return True

        # タイムアウトや接続エラーもリトライ
        retry_keywords = ["timeout", "connection", "rate", "limit", "throttl"]
        return any(kw in error_str.lower() for kw in retry_keywords)

    def get_delay(self, attempt: int) -> float:
        """
        リトライ前の待機時間を計算する（指数バックオフ + ジッター）。

        Args:
            attempt: 現在の試行回数（0始まり）

        Returns:
            待機時間（秒）
        """
        delay = min(self.base_delay * (2**attempt), self.max_delay)
        jitter = random.uniform(0, delay * 0.1)
        return delay + jitter


class CodexDailyRunner:
    def __init__(self):
        # --- 設定（環境に合わせて修正してください） ---
        # スクリプトの場所から相対的にリポジトリパスを決定
        script_dir = Path(__file__).parent
        self.repo_path = script_dir.parent  # scriptsディレクトリの親ディレクトリ
        self.console = Console()
        
        # .envファイルを読み込む
        env_file = self.repo_path / ".env"
        if env_file.exists():
            load_dotenv(env_file)
            print(f"Loaded .env from: {env_file}")
        else:
            print(f"Warning: .env file not found at: {env_file}")
        
        # Codex のアイドルタイムアウト（秒）を .env から読み込む（デフォルト60秒）
        try:
            self.codex_idle_timeout = int(os.getenv('CODEX_IDLE_TIMEOUT_SEC', '60'))
        except (ValueError, TypeError):
            self.codex_idle_timeout = 60
        
        self.branch = "main"
        self.report_dir = self.repo_path / "reports"
        self.logs_dir = self.repo_path / "logs"
        self.log_file = self.logs_dir / "codex_daily_with_agents.log"
        # self.agents_file = self.repo_path / "AGENTS.md"
        self.agents_1_file = self.repo_path / "AGENTS_1.md"
        self.agents_2_file = self.repo_path / "AGENTS_2.md"
        self.agents_3_file = self.repo_path / "AGENTS_3.md"
        
        # ディレクトリ作成
        self.report_dir.mkdir(exist_ok=True)
        self.logs_dir.mkdir(exist_ok=True)

        # 429 / 5xx 等用のリトライハンドラー（log は後から参照するため lambda で遅延）
        self.retry_handler = RetryHandler(log_func=lambda msg: self.log(msg))
        # ---------------------------------------

    def log(self, message):
        """ログメッセージを記録"""
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        log_entry = f"{timestamp}\t{message}\n"
        
        # ログファイルに追記
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        
        # コンソールにも出力
        print(f"[{timestamp}] {message}")
    
    def cleanup_temp_files(self):
        """一時ファイルを検索して削除する"""
        self.log("Checking for temporary files to clean up...")
        deleted_count = 0
        temp_patterns = [
            'temp_tasklist.md',                 # Codexタスクリスト
            'report.json',                      # Codex生成の一時JSON
            'report_1.json',                    # AGENTS_1成果物
            'report_2.json',                    # AGENTS_2成果物
            'report_3.json',                    # AGENTS_3成果物
            'codex_raw_output_*.txt',           # Codexエラーログ
            'codex_prompt_*.md',                # 一時プロンプトファイル
        ]
        
        try:
            for pattern in temp_patterns:
                for f in self.repo_path.rglob(pattern):
                    try:
                        if f.is_file():
                            f.unlink()
                            self.log(f"Deleted temporary file: {f}")
                            deleted_count += 1
                    except Exception as e:
                        self.log(f"Warning: Could not delete temporary file {f}: {e}")
            
            if deleted_count > 0:
                self.log(f"Cleaned up {deleted_count} temporary file(s).")
            else:
                self.log("No temporary files found to clean up.")
        except Exception as e:
            self.log(f"Warning: An error occurred during temp file cleanup: {e}")

    def kill_headless_chrome(self):
        """
        chrome-devtools MCP が起動したヘッドレス Chrome を終了する。
        コマンドラインに --headless を含む chrome.exe のみ対象（通常の Chrome は触らない）。
        """
        if os.name != "nt":
            # Windows 以外では未対応（必要なら psutil 等で拡張可）
            return
        try:
            # 1. ヘッドレス Chrome のプロセスを特定して終了
            # Get-CimInstance や Get-WmiObject が権限で失敗する場合があるため、
            # wmic process get を使用して CommandLine を取得し、フィルタリングする。
            self.log("Attempting to kill headless Chrome processes...")
            
            # wmic を使ってプロセスIDとコマンドラインを取得
            wmic_cmd = ["wmic", "process", "where", "name='chrome.exe'", "get", "CommandLine,ProcessId", "/format:list"]
            result = subprocess.run(wmic_cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
            
            if result.returncode == 0:
                # 出力をパースして --headless を含むプロセスIDを特定
                pids_to_kill = []
                current_cmd = ""
                for line in result.stdout.splitlines():
                    line = line.strip()
                    if line.startswith("CommandLine="):
                        current_cmd = line[len("CommandLine="):]
                    elif line.startswith("ProcessId="):
                        pid = line[len("ProcessId="):]
                        if "--headless" in current_cmd:
                            pids_to_kill.append(pid)
                        current_cmd = ""
                
                if pids_to_kill:
                    self.log(f"Found headless Chrome PIDs: {', '.join(pids_to_kill)}")
                    for pid in pids_to_kill:
                        subprocess.run(["taskkill", "/F", "/PID", pid], capture_output=True)
                else:
                    self.log("No headless Chrome processes found via wmic.")

            # 2. chrome-devtools-mcp のプロセス自体も残っている可能性があるので終了
            # こちらも wmic で検索
            wmic_mcp_cmd = ["wmic", "process", "get", "CommandLine,ProcessId", "/format:list"]
            result_mcp = subprocess.run(wmic_mcp_cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
            
            if result_mcp.returncode == 0:
                mcp_pids = []
                current_cmd = ""
                for line in result_mcp.stdout.splitlines():
                    line = line.strip()
                    if line.startswith("CommandLine="):
                        current_cmd = line[len("CommandLine="):]
                    elif line.startswith("ProcessId="):
                        pid = line[len("ProcessId="):]
                        if "chrome-devtools-mcp" in current_cmd:
                            mcp_pids.append(pid)
                        current_cmd = ""
                
                if mcp_pids:
                    self.log(f"Found MCP PIDs: {', '.join(mcp_pids)}")
                    for pid in mcp_pids:
                        subprocess.run(["taskkill", "/F", "/PID", pid], capture_output=True)
            
            self.log("Cleanup of headless Chrome and MCP processes completed.")
        except Exception as e:
            self.log(f"Warning: kill_headless_chrome failed: {e}")

    def run(self):
        """メイン実行処理"""
        try:
            self.log("=== Start ===")

            # 起動前に前回残ったヘッドレス Chrome を終了
            self.kill_headless_chrome()

            # 一時ファイルのクリーンアップ
            self.cleanup_temp_files()

            # パスの存在確認
            if not self.repo_path.exists():
                raise FileNotFoundError(f"Repo not found: {self.repo_path}")
            if not self.agents_1_file.exists():
                raise FileNotFoundError(f"AGENTS_1.md not found: {self.agents_1_file}")
            if not self.agents_2_file.exists():
                raise FileNotFoundError(f"AGENTS_2.md not found: {self.agents_2_file}")
            if not self.agents_3_file.exists():
                raise FileNotFoundError(f"AGENTS_3.md not found: {self.agents_3_file}")

            # 日付と出力ディレクトリ
            date_dir = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            output_dir = self.report_dir / date_dir
            output_dir.mkdir(parents=True, exist_ok=True)

            # 1) AGENTS_1.md を使って要約とレポート生成（LLM/Codex CLI）
            self.log("Processing AGENTS_1.md → report_1.json / report_1.md ...")
            self.process_agents(
                agents_path=self.agents_1_file,
                json_output_name="report_1.json",
                md_output_name="report_1.md",
            )

            # 2) AGENTS_2.md を使って要約とレポート生成（LLM/Codex CLI）
            self.log("Processing AGENTS_2.md → report_2.json / report_2.md ...")
            self.process_agents(
                agents_path=self.agents_2_file,
                json_output_name="report_2.json",
                md_output_name="report_2.md",
            )

            # 3) AGENTS_3.md を使って要約とレポート生成（LLM/Codex CLI）
            self.log("Processing AGENTS_3.md → report_3.json / report_3.md ...")
            self.process_agents(
                agents_path=self.agents_3_file,
                json_output_name="report_3.json",
                md_output_name="report_3.md",
            )

            # 4) GeminiCLI（YouTube要約）を実行し、report.md を YYYY-MM-DD にコピー
            self.log("Running GeminiCLI (yt_top3_gemini_report) → gemini_youtube_report.md ...")
            self.run_gemini_youtube_report(output_dir, date_dir)

            # Git操作（出力物と新規/更新された scripts もコミット）
            self.git_operations(output_dir, date_dir)
            try:
                self.git_operations(self.repo_path / "scripts", date_dir)
            except Exception as e:
                self.log(f"WARNING: git add for scripts failed: {e}")

            self.log("=== Finished ===")

        except Exception as e:
            self.log(f"ERROR: {e}")
            raise

    def process_agents(self, agents_path: Path, json_output_name: str, md_output_name: str):
        """指定の AGENTS ファイルを使って Codex を実行し、所定のファイル名で保存して返す。"""
        # 出力基準パス
        date_dir = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        output_dir = self.report_dir / date_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        # Codex が生成する一時ファイル（固定名）
        temp_json = output_dir / "report.json"

        # タイムスタンプの埋め込み
        utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        agents_content = agents_path.read_text(encoding='utf-8')
        agents_content = agents_content.replace('{utc_timestamp}', utc_now)

        # 直前実行の残骸を削除
        if temp_json.exists():
            try:
                temp_json.unlink()
            except Exception:
                pass

        # 一時プロンプトファイル（デバッグや履歴のために残す）
        safe_name = agents_path.stem
        temp_prompt_file = Path(tempfile.gettempdir()) / f"codex_prompt_{safe_name}_{date_dir}.md"
        temp_prompt_file.write_text(agents_content, encoding='utf-8')
        self.log(f"{agents_path.name} content written to {temp_prompt_file} (length {temp_prompt_file.stat().st_size} bytes)")

        # 前回のヘッドレス Chrome が残っていれば終了（次の run で「ブラウザが既に起動」を防ぐ）
        self.kill_headless_chrome()
        time.sleep(2)  # OSによるプロセス解放待ち

        # Codex 実行（429 / 5xx 等は指数バックオフでリトライ）
        self.log("Invoking codex exec...")
        attempt = 0
        while True:
            try:
                _ = self.run_codex(agents_content, expected_report_path=temp_json)
                break
            except Exception as e:
                # 非ゼロ終了でも temp_json が存在すれば続行
                if temp_json.exists() and temp_json.stat().st_size > 0:
                    break
                if not self.retry_handler.should_retry(e, attempt):
                    raise
                delay = self.retry_handler.get_delay(attempt)
                self.log(
                    f"Retrying after error (attempt {attempt + 1}/{self.retry_handler.max_retries}): {e}. "
                    f"Waiting {delay:.1f}s..."
                )
                time.sleep(delay)
                attempt += 1
            finally:
                # 今回起動したヘッドレス Chrome を終了（次の AGENTS_* 実行で衝突しないように）
                self.kill_headless_chrome()
                time.sleep(1)

        # 生成された JSON を読み込み
        if (not temp_json.exists()) or (temp_json.stat().st_size == 0):
            raise FileNotFoundError(f"report.json not found or empty: {temp_json}")
        with open(temp_json, 'r', encoding='utf-8') as f:
            report_obj = json.load(f)
        self.log(f"JSON report detected at {temp_json}")

        # 所定のファイル名に保存（JSON）
        final_json_path = output_dir / json_output_name
        with open(final_json_path, 'w', encoding='utf-8') as f:
            json.dump(report_obj, f, ensure_ascii=False, indent=2)
        self.log(f"Saved JSON to {final_json_path}")

        # JSON -> Markdown 変換と保存（所定名）
        md_content = self._convert_report_json_to_markdown(report_obj)
        final_md_path = output_dir / md_output_name
        final_md_path.write_text(md_content, encoding='utf-8')
        self.log(f"Markdown report saved to {final_md_path}")

        # 一時の report.json は混乱の元なので削除
        try:
            if temp_json.exists():
                temp_json.unlink()
        except Exception:
            pass

        return report_obj, md_content
    
    
    def find_codex_command(self):
        """Codex CLIのパスを検索"""
        # まずPATHから検索
        codex_path = shutil.which("codex")
        if codex_path:
            return codex_path
        
        # 一般的なインストール場所を検索
        common_paths = [
            "C:\\Program Files\\codex\\codex.exe",
            f"C:\\Users\\{os.environ.get('USERNAME', '')}\\AppData\\Local\\Programs\\codex\\codex.exe",
            f"C:\\Users\\{os.environ.get('USERNAME', '')}\\AppData\\Roaming\\npm\\codex.cmd",
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                return path
        
        return None

    def run_codex(self, agents_content, expected_report_path: Path | None = None):
        """Codex CLIを実行"""
        # 期待する report.json の場所（呼び出し元から明示的に受け取り、日付ずれを防止）
        if expected_report_path is not None:
            report_file = Path(expected_report_path)
        else:
            date_dir = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            output_dir = self.report_dir / date_dir
            report_file = output_dir / "report.json"
        
        # Codex コマンドのパスを検索
        codex_cmd = self.find_codex_command()
        
        if not codex_cmd:
            error_msg = ("Codex CLI が見つかりません。以下を確認してください:\n"
                        "1. Codex CLI がインストールされているか\n"
                        "2. PATH に Codex が設定されているか")
            self.log(f"ERROR: {error_msg}")
            raise FileNotFoundError(error_msg)
        
        self.log(f"Using Codex CLI: {codex_cmd}")
        self.log(f"DEBUG: USERPROFILE={os.environ.get('USERPROFILE')}, HOME={os.environ.get('HOME')}")
        
        # プロジェクトローカル設定（.codex/config.toml = ヘッドレス chrome-devtools）。trusted 時のみ読み込まれる。
        config_path = Path.home() / ".codex" / "config.toml"
        local_config_path = self.repo_path / ".codex" / "config.toml"
        # #region agent log
        try:
            import json
            debug_log_path = Path(__file__).parent.parent / ".cursor" / "debug.log"
            if config_path.exists():
                config_content = config_path.read_text(encoding='utf-8')
                log_entry = json.dumps({
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "A",
                    "location": f"{__file__}:393",
                    "message": "config.toml exists and content read",
                    "data": {"config_path": str(config_path), "config_content": config_content},
                    "timestamp": int(time.time() * 1000)
                }, ensure_ascii=False)
                debug_log_path.parent.mkdir(parents=True, exist_ok=True)
                with open(debug_log_path, "a", encoding="utf-8") as f:
                    f.write(log_entry + "\n")
            else:
                log_entry = json.dumps({
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "A",
                    "location": f"{__file__}:393",
                    "message": "config.toml does not exist",
                    "data": {"config_path": str(config_path)},
                    "timestamp": int(time.time() * 1000)
                }, ensure_ascii=False)
                debug_log_path.parent.mkdir(parents=True, exist_ok=True)
                with open(debug_log_path, "a", encoding="utf-8") as f:
                    f.write(log_entry + "\n")
        except Exception as e:
            pass
        # #endregion
        try:
            self.console.print(Panel.fit(f"Codex CLI: [bold]{codex_cmd}[/]\nProject config: [yellow]{local_config_path}[/] (headless MCP)\nMode: [cyan]exec --yolo -c model_reasoning_effort=\"medium\"[/]", title="Codex Runner", border_style="blue"))
        except Exception:
            pass
        
        try:
            # codex exec --yolo コマンドを実行（ストリーミング表示）
            # Windows では codex コマンドを shell=True で実行
            # CODEX_HOME を明示的に設定してホームディレクトリの検出を助ける
            # モデルは明示的に最新の gpt-5.2-codex を使用
            # config.toml に [text] verbosity = "medium" を設定済みのため、それを利用
            cmd_list = [
                "codex", "exec", "--yolo", 
                "-m", "gpt-5.2-codex", 
                "-c", "model_reasoning_effort=medium",
                "-c", 'text.verbosity="medium"'
            ]
            # #region agent log
            try:
                import json
                debug_log_path = Path(__file__).parent.parent / ".cursor" / "debug.log"
                log_entry = json.dumps({
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "B",
                    "location": f"{__file__}:411",
                    "message": "Command list before execution",
                    "data": {"cmd_list": cmd_list},
                    "timestamp": int(time.time() * 1000)
                }, ensure_ascii=False)
                debug_log_path.parent.mkdir(parents=True, exist_ok=True)
                with open(debug_log_path, "a", encoding="utf-8") as f:
                    f.write(log_entry + "\n")
            except Exception as e:
                pass
            # #endregion
            self.log(f"Executing: {' '.join(cmd_list)}")
            
            env = os.environ.copy()
            user_home = str(Path.home())
            if 'USERPROFILE' not in env:
                env['USERPROFILE'] = user_home
            if 'HOME' not in env:
                env['HOME'] = user_home
            env['CODEX_HOME'] = str(Path.home() / ".codex")
            
            # リポジトリルートを cwd にすることで .codex/config.toml（ローカル・ヘッドレス MCP）が読み込まれる（trusted 時）
            process = subprocess.Popen(
                cmd_list,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                shell=True,
                env=env,
                cwd=str(self.repo_path)
            )

            # エージェントへのプロンプトを投入
            assert process.stdin is not None
            process.stdin.write(agents_content)
            process.stdin.close()

            stdout_lines: list[str] = []
            stderr_lines: list[str] = []
            last_output_time = time.time()
            output_lock = threading.Lock()

            def reader(stream, collector, tag, style):
                nonlocal last_output_time
                for line in iter(stream.readline, ''):
                    line = line.rstrip('\n')
                    collector.append(line)
                    with output_lock:
                        last_output_time = time.time()
                    try:
                        self.console.print(f"[{style}]{tag}[/]: {line}")
                    except Exception:
                        print(f"{tag}: {line}")

            assert process.stdout is not None and process.stderr is not None
            t_out = threading.Thread(target=reader, args=(process.stdout, stdout_lines, 'stdout', 'cyan'), daemon=True)
            t_err = threading.Thread(target=reader, args=(process.stderr, stderr_lines, 'stderr', 'red'), daemon=True)

            with self.console.status("[bold green]Codex 実行中...[/]", spinner="dots"):
                t_out.start()
                t_err.start()
                
                # タイムアウト監視（最大10分、出力停止後60秒で終了）
                M = 10 * 60
                IDLE_TIMEOUT = self.codex_idle_timeout
                idle_termination_detected = False
                
                try:
                    while process.poll() is None:
                        current_time = time.time()
                        with output_lock:
                            time_since_output = current_time - last_output_time
                        
                        # 全体のタイムアウトチェック
                        if current_time - last_output_time > M:
                            process.kill()
                            raise subprocess.TimeoutExpired('codex exec --yolo', timeout=M)
                        
                        # 出力が停止してから一定時間経過したら終了
                        if time_since_output > IDLE_TIMEOUT and stdout_lines:
                            self.log(f"No output for {IDLE_TIMEOUT}s, assuming completion")
                            process.terminate()
                            time.sleep(2)  # 終了処理を待つ
                            if process.poll() is None:
                                process.kill()
                            idle_termination_detected = True
                            break
                        
                        time.sleep(1)
                        
                except subprocess.TimeoutExpired:
                    process.kill()
                    # 念のためスレッドの終了を待つ
                    t_out.join(timeout=5)
                    t_err.join(timeout=5)
                    raise subprocess.TimeoutExpired('codex exec --yolo', timeout=M)

                # プロセス終了後、リーダーースレッドが完了するのを待つ
                t_out.join(timeout=5)
                t_err.join(timeout=5)

            rc = process.returncode if process.returncode is not None else -1
            
            # 実行結果の表示（成功・失敗問わず）
            stdout_content = "\n".join(stdout_lines)
            stderr_content = "\n".join(stderr_lines)

            # アイドルタイムアウトで強制終了したが report.json が生成済みなら成功扱い
            if idle_termination_detected:
                # ファイルフラッシュ待ちの短いリトライ
                for _ in range(4):
                    if report_file.exists() and report_file.stat().st_size > 0:
                        break
                    time.sleep(0.5)
                if report_file.exists() and report_file.stat().st_size > 0:
                    self.log(f"Idle timeout reached; report found at {report_file}. Treating as success.")
                    return stdout_content
            
            self.log(f"Codex execution completed with return code: {rc}")
            
            # stdout の内容をログに出力
            if stdout_content.strip():
                self.log("=== Codex stdout output ===")
                for line in stdout_lines:
                    self.log(f"STDOUT: {line}")
                self.log("=== End of stdout output ===")
            else:
                self.log("Codex stdout is empty")
            
            # stderr がある場合も表示
            if stderr_content.strip():
                self.log("=== Codex stderr output ===")
                for line in stderr_lines:
                    self.log(f"STDERR: {line}")
                self.log("=== End of stderr output ===")

                # #region agent log
                try:
                    import json
                    import re
                    debug_log_path = Path(__file__).parent.parent / ".cursor" / "debug.log"
                    
                    # エラーメッセージから実際に送信された設定値を抽出
                    verbosity_error_match = re.search(r"Unsupported value: '(\w+)' is not supported", stderr_content)
                    verbosity_param_match = re.search(r'"param":\s*"([^"]+)"', stderr_content)
                    actual_verbosity_value = verbosity_error_match.group(1) if verbosity_error_match else None
                    verbosity_param = verbosity_param_match.group(1) if verbosity_param_match else None
                    
                    # config.tomlの内容を再確認
                    config_path = Path.home() / ".codex" / "config.toml"
                    config_verbosity_value = None
                    if config_path.exists():
                        config_content = config_path.read_text(encoding='utf-8')
                        verbosity_match = re.search(r'verbosity\s*=\s*"(\w+)"', config_content)
                        if verbosity_match:
                            config_verbosity_value = verbosity_match.group(1)
                    
                    log_entry = json.dumps({
                        "sessionId": "debug-session",
                        "runId": "run1",
                        "hypothesisId": "D",
                        "location": f"{__file__}:590",
                        "message": "Actual sent configuration values extracted from error",
                        "data": {
                            "return_code": rc,
                            "actual_sent_verbosity": actual_verbosity_value,
                            "verbosity_param_name": verbosity_param,
                            "config_file_verbosity": config_verbosity_value,
                            "config_file_path": str(config_path),
                            "error_message": verbosity_error_match.group(0) if verbosity_error_match else None
                        },
                        "timestamp": int(time.time() * 1000)
                    }, ensure_ascii=False)
                    debug_log_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(debug_log_path, "a", encoding="utf-8") as f:
                        f.write(log_entry + "\n")
                except Exception as e:
                    pass
                # #endregion

                # 特定の認証エラーを検知して日本語でログに残す
                if "refresh token was already used" in stderr_content:
                    self.log("【要対応】認証トークンが失効しています。ターミナルで 'codex login' を実行して再ログインしてください。")
            
            if rc != 0:
                # エラーの場合、生の出力を保存
                date_tag = datetime.now(timezone.utc).strftime("%Y%m%d")
                err_file = self.report_dir / f"codex_raw_output_{date_tag}.txt"
                error_content = (
                    "STDOUT:\n" + stdout_content +
                    "\n\nSTDERR:\n" + stderr_content +
                    f"\n\nReturn code: {rc}"
                )
                err_file.write_text(error_content, encoding='utf-8')
                self.log(f"Codex exited with code {rc}. Saving raw output for diagnosis.")
                
                # 少し待って report.json が現れるか再確認（遅延フラッシュ対策）
                for _ in range(6):
                    if report_file.exists() and report_file.stat().st_size > 0:
                        break
                    time.sleep(0.5)

                # report.json が存在する場合は成功扱いで終了
                if (report_file.exists() and report_file.stat().st_size > 0):
                    self.log(f"report.json found despite non-zero exit. Treating as success: {report_file}")
                    return stdout_content
                
                # report.json がない場合のみ例外を投げる（メッセージに stderr の一部を含め 429 等をリトライ判定に利用）
                err_snippet = (stderr_content or "")[-2000:] if stderr_content else ""
                raise subprocess.CalledProcessError(
                    rc,
                    [
                        codex_cmd, 'exec', '--yolo',
                        '-m', 'gpt-5.2-codex',
                        '-c', 'model_reasoning_effort=medium',
                        '-c', 'text.verbosity="medium"'
                    ],
                    f"Codex failed. See {err_file}. stderr excerpt: {err_snippet}"
                )

            return stdout_content
            
        except subprocess.TimeoutExpired:
            # タイムアウトでも report.json が存在すれば成功扱い
            for _ in range(6):
                if report_file.exists() and report_file.stat().st_size > 0:
                    break
                time.sleep(0.5)
            if report_file.exists() and report_file.stat().st_size > 0:
                self.log(f"Timeout occurred but report found at {report_file}. Treating as success.")
                return ""
            error_msg = "Codex コマンドがタイムアウトしました（10分）"
            self.log(f"ERROR: {error_msg}")
            raise RuntimeError(error_msg)
        except subprocess.CalledProcessError:
            raise
        except Exception as e:
            # その他の例外でも report.json が存在すれば成功扱い
            for _ in range(6):
                try:
                    if report_file.exists() and report_file.stat().st_size > 0:
                        break
                except Exception:
                    pass
                time.sleep(0.5)
            try:
                if report_file.exists() and report_file.stat().st_size > 0:
                    self.log(f"Exception occurred but report found at {report_file}. Treating as success.")
                    return ""
            except Exception:
                pass
            error_msg = f"Codex コマンドの実行に失敗しました: {e}"
            self.log(f"ERROR: {error_msg}")
            raise RuntimeError(error_msg)
    
    def git_operations(self, target_path, date):
        """Git操作（add, commit, push）。target_path はファイルまたはディレクトリ"""
        try:
            # リポジトリディレクトリに移動
            original_cwd = os.getcwd()
            os.chdir(self.repo_path)
            
            try:
                # git add（相対パスで追加）
                rel_path = target_path.relative_to(self.repo_path)
                subprocess.run(['git', 'add', str(rel_path)], check=True)
                
                # 直近の add によりステージされた変更のみを確認（対象パスに限定）
                staged_result = subprocess.run(
                    ['git', 'diff', '--name-only', '--cached', '--', str(rel_path)],
                    capture_output=True,
                    text=True,
                    check=True
                )
                
                if staged_result.stdout.strip():
                    # ステージ済みの変更がある場合はコミットとプッシュ
                    commit_msg = f"Auto: AI News report {date} (JSON)"
                    subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
                    subprocess.run(['git', 'push', 'origin', self.branch], check=True)
                    self.log(f"Committed and pushed to {self.branch}")
                else:
                    # ステージ済みの変更がない（通常想定のケースもある）
                    self.log(f"No staged changes to commit for {rel_path}. Skipping commit/push.")
                    
            finally:
                # 元のディレクトリに戻る
                os.chdir(original_cwd)
                
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Git operation failed: {e}")
        except Exception as e:
            raise RuntimeError(f"Git operation error: {e}")

    # GeminiCLI（YouTube要約）の出力フォルダ名・コピー先ファイル名
    GEMINI_YOUTUBE_OUTPUT_DIR = "Gemini_YouTube_Summary_Report"
    GEMINI_YOUTUBE_REPORT_COPY_NAME = "gemini_youtube_report.md"

    def _write_gemini_error_report(
        self, output_dir: Path, error_message: str, error_detail: str = ""
    ) -> None:
        """失敗時に reports/YYYY-MM-DD/gemini_youtube_report.md にエラー内容を書き出す（Git push に含まれる）。"""
        dest = output_dir / self.GEMINI_YOUTUBE_REPORT_COPY_NAME
        utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        lines = [
            "# Gemini YouTube Report (Error)",
            "",
            f"- Generated at: {utc_now}",
            "- Status: Failed",
            "",
            "## Error",
            "",
            error_message,
        ]
        if error_detail:
            lines.extend(["", "## Details", "", "```", error_detail, "```", ""])
        dest.write_text("\n".join(lines), encoding="utf-8")
        self.log(f"Wrote error report to {dest}")

    def run_gemini_youtube_report(self, output_dir: Path, date_dir: str) -> None:
        """
        yt_top3_gemini_report.py を実行し、成功時に report.md を YYYY-MM-DD フォルダにコピーする。
        一時的な失敗は RetryHandler でリトライ。最終的に失敗した場合はエラー内容を同パスに書き出し、Git push に含める。
        """
        gemini_cmd = [
            "uv", "run", "--link-mode=copy", "yt_top3_gemini_report.py",
            "https://www.youtube.com/channel/UCUWtuyVjeMQygQiy3adHb1g",
            "-o", self.GEMINI_YOUTUBE_OUTPUT_DIR,
            "-n", "5",
        ]
        self.log(f"Running GeminiCLI: {' '.join(gemini_cmd)}")
        attempt = 0
        last_error_message = ""
        last_error_detail = ""
        while True:
            try:
                result = subprocess.run(
                    gemini_cmd,
                    cwd=str(self.repo_path),
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=600,
                )
                if result.returncode != 0:
                    err_snippet = (result.stderr or result.stdout or "")[-2000:]
                    last_error_message = f"GeminiCLI exited with code {result.returncode}."
                    last_error_detail = err_snippet
                    raise RuntimeError(f"{last_error_message} {err_snippet}")

                src_report = self.repo_path / self.GEMINI_YOUTUBE_OUTPUT_DIR / "report.md"
                if not src_report.exists():
                    last_error_message = f"Gemini report not found: {src_report}"
                    raise FileNotFoundError(last_error_message)

                dest_report = output_dir / self.GEMINI_YOUTUBE_REPORT_COPY_NAME
                shutil.copy2(src_report, dest_report)
                self.log(f"Copied Gemini report to {dest_report}")
                return

            except subprocess.TimeoutExpired as e:
                last_error_message = "GeminiCLI timed out."
                last_error_detail = str(e)
                if not self.retry_handler.should_retry(e, attempt):
                    self.log("GeminiCLI timed out. Writing error report and continuing.")
                    self._write_gemini_error_report(
                        output_dir, last_error_message, last_error_detail
                    )
                    return
                delay = self.retry_handler.get_delay(attempt)
                self.log(
                    f"GeminiCLI timed out. Retrying (attempt {attempt + 1}/{self.retry_handler.max_retries}). "
                    f"Waiting {delay:.1f}s..."
                )
                time.sleep(delay)
                attempt += 1
            except (RuntimeError, FileNotFoundError) as e:
                if not last_error_message:
                    last_error_message = str(e)
                self.log(f"GeminiCLI error: {e}")
                if not self.retry_handler.should_retry(e, attempt):
                    self.log(
                        "Skipping copy (non-retryable or max retries). Writing error report and continuing."
                    )
                    self._write_gemini_error_report(
                        output_dir, last_error_message, last_error_detail
                    )
                    return
                delay = self.retry_handler.get_delay(attempt)
                self.log(
                    f"Retrying GeminiCLI (attempt {attempt + 1}/{self.retry_handler.max_retries}). "
                    f"Waiting {delay:.1f}s..."
                )
                time.sleep(delay)
                attempt += 1
            except Exception as e:
                self.log(f"GeminiCLI unexpected error (continuing): {e}")
                cause = getattr(e, "__cause__", None)
                self._write_gemini_error_report(
                    output_dir, str(e), str(cause) if cause else ""
                )
                return

    def _normalize_report(self, data):
        """（未使用）将来的な入力ゆらぎ対応のために残置。現状は Codex 生成JSONをそのまま使用。"""
        return data

    def _validate_articles_schema(self, report_obj):
        """（簡易）スキーマ検証。Codex 生成JSONを前提に最低限でチェック。"""
        if not isinstance(report_obj, dict):
            raise ValueError("Report root must be an object")
        if not isinstance(report_obj.get("articles"), list):
            raise ValueError("'articles' must be an array")

    def _convert_report_json_to_markdown(self, report_obj):
        """report.json 相当のオブジェクトを Markdown に整形して返す。"""
        def esc(text):
            if text is None:
                return ""
            return str(text).strip()

        lines = []
        # ヘッダー
        lines.append(f"# AI News Report ({esc(report_obj.get('site'))})")
        lines.append("")
        lines.append(f"- Generated at: {esc(report_obj.get('generated_at'))}")
        lines.append(f"- Articles: {report_obj.get('num_articles', len(report_obj.get('articles', [])))}")
        lines.append("")

        # 各記事
        for idx, art in enumerate(report_obj.get('articles', []), start=1):
            title = esc(art.get('title')) or f"Article {idx}"
            date_val = esc(art.get('date'))
            lines.append(f"## {title}")
            if date_val:
                lines.append(f"- Date: {date_val}")
            lines.append("")

            # Executive Summary
            es = art.get('executive_summary', []) or []
            if es:
                lines.append("### Executive Summary")
                for s in es:
                    if isinstance(s, str) and s.strip():
                        lines.append(f"- {s.strip()}")
                lines.append("")

            # Key Findings
            kfs = art.get('key_findings', []) or []
            if kfs:
                lines.append("### Key Findings")
                for kf in kfs:
                    if isinstance(kf, dict):
                        point = esc(kf.get('point'))
                        foot = esc(kf.get('footnote'))
                        if foot:
                            lines.append(f"- {point} [^]")
                            lines.append(f"  - Footnote: {foot}")
                        else:
                            lines.append(f"- {point}")
                    elif isinstance(kf, str) and kf.strip():
                        lines.append(f"- {kf.strip()}")
                lines.append("")

            # References
            refs = art.get('references', []) or []
            if refs:
                lines.append("### References")
                for r in refs:
                    if isinstance(r, str) and r.strip():
                        lines.append(f"- {r.strip()}")
                lines.append("")

        return "\n".join(lines).rstrip() + "\n"

def main():
    """メイン関数"""
    runner = CodexDailyRunner()
    runner.run()

if __name__ == "__main__":
    main()