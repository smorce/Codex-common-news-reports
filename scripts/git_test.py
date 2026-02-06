#!/usr/bin/env python3
# scripts/git_test.py
# Git操作のテストスクリプト

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

class GitTester:
    def __init__(self):
        """初期化"""
        # スクリプトの場所から相対的にリポジトリパスを決定
        script_dir = Path(__file__).parent
        self.repo_path = script_dir.parent  # scriptsディレクトリの親ディレクトリ
        self.test_file = self.repo_path / "test_file_for_git.txt"
        
        print(f"Repository path: {self.repo_path}")
        print(f"Current working directory: {os.getcwd()}")
        print("-" * 50)

    def run_git_command(self, command_args, description=""):
        """Gitコマンドを実行して結果を表示"""
        print(f"\n=== {description} ===")
        print(f"Command: git {' '.join(command_args)}")
        
        try:
            # リポジトリディレクトリに移動
            original_cwd = os.getcwd()
            os.chdir(self.repo_path)
            
            try:
                result = subprocess.run(
                    ['git'] + command_args,
                    capture_output=True,
                    text=True,
                    check=False  # エラーでも継続
                )
                
                print(f"Return code: {result.returncode}")
                
                if result.stdout.strip():
                    print("STDOUT:")
                    print(result.stdout)
                
                if result.stderr.strip():
                    print("STDERR:")
                    print(result.stderr)
                
                return result
                
            finally:
                # 元のディレクトリに戻る
                os.chdir(original_cwd)
                
        except Exception as e:
            print(f"Error executing git command: {e}")
            return None

    def test_git_status(self):
        """git status の様々なオプションをテスト"""
        print("\n" + "="*60)
        print("GIT STATUS TESTS")
        print("="*60)
        
        # 基本的な git status
        self.run_git_command(['status'], "Basic git status")
        
        # --porcelain オプション（スクリプト向け）
        self.run_git_command(['status', '--porcelain'], "Git status --porcelain")
        
        # --short オプション
        self.run_git_command(['status', '--short'], "Git status --short")
        
        # --branch オプション
        self.run_git_command(['status', '--branch'], "Git status --branch")
        
        # 未追跡ファイルも表示
        self.run_git_command(['status', '--untracked-files=all'], "Git status with untracked files")

    def test_git_info(self):
        """Gitリポジトリの基本情報を取得"""
        print("\n" + "="*60)
        print("GIT REPOSITORY INFO")
        print("="*60)
        
        # 現在のブランチ
        self.run_git_command(['branch', '--show-current'], "Current branch")
        
        # 全ブランチ
        self.run_git_command(['branch', '-a'], "All branches")
        
        # リモートURL
        self.run_git_command(['remote', '-v'], "Remote URLs")
        
        # 最新のコミット
        self.run_git_command(['log', '--oneline', '-5'], "Recent commits (last 5)")
        
        # 変更されたファイル（ステージング済み）
        self.run_git_command(['diff', '--cached', '--name-only'], "Staged files")
        
        # 変更されたファイル（未ステージング）
        self.run_git_command(['diff', '--name-only'], "Modified files (unstaged)")

    def create_test_file(self):
        """テスト用ファイルを作成"""
        print("\n" + "="*60)
        print("CREATING TEST FILE")
        print("="*60)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = f"""# Test File for Git Operations

Created at: {timestamp}

This is a test file created by git_test.py script.
It will be used to test various git operations.

Random content: {hash(timestamp) % 10000}
"""
        
        self.test_file.write_text(content, encoding='utf-8')
        print(f"Created test file: {self.test_file}")
        print(f"File size: {self.test_file.stat().st_size} bytes")

    def test_git_add_and_status(self):
        """ファイル追加とステータス変化をテスト"""
        print("\n" + "="*60)
        print("GIT ADD AND STATUS CHANGES")
        print("="*60)
        
        # ファイル作成前のステータス
        self.run_git_command(['status', '--porcelain'], "Status before creating file")
        
        # テストファイル作成
        self.create_test_file()
        
        # ファイル作成後のステータス
        self.run_git_command(['status', '--porcelain'], "Status after creating file")
        
        # ファイルをステージング
        rel_path = self.test_file.relative_to(self.repo_path)
        self.run_git_command(['add', str(rel_path)], f"Adding file: {rel_path}")
        
        # ステージング後のステータス
        self.run_git_command(['status', '--porcelain'], "Status after staging file")
        
        # ファイルを変更
        content = self.test_file.read_text(encoding='utf-8')
        content += f"\n\nModified at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        self.test_file.write_text(content, encoding='utf-8')
        
        # 変更後のステータス
        self.run_git_command(['status', '--porcelain'], "Status after modifying staged file")

    def test_git_diff(self):
        """git diff の様々なオプションをテスト"""
        print("\n" + "="*60)
        print("GIT DIFF TESTS")
        print("="*60)
        
        # ステージングエリアとの差分
        self.run_git_command(['diff', '--cached'], "Diff cached (staged changes)")
        
        # 作業ディレクトリとの差分
        self.run_git_command(['diff'], "Diff working directory")
        
        # ファイル名のみ
        self.run_git_command(['diff', '--name-only'], "Diff --name-only")
        
        # 統計情報
        self.run_git_command(['diff', '--stat'], "Diff --stat")

    def cleanup_test_file(self):
        """テストファイルをクリーンアップ"""
        print("\n" + "="*60)
        print("CLEANUP")
        print("="*60)
        
        if self.test_file.exists():
            # ファイルを削除
            self.test_file.unlink()
            print(f"Deleted test file: {self.test_file}")
            
            # 削除後のステータス
            self.run_git_command(['status', '--porcelain'], "Status after deleting file")
            
            # ステージングエリアからも削除
            rel_path = self.test_file.relative_to(self.repo_path)
            self.run_git_command(['reset', 'HEAD', str(rel_path)], f"Unstaging file: {rel_path}")
            
            # 最終ステータス
            self.run_git_command(['status', '--porcelain'], "Final status")
        else:
            print("Test file does not exist - nothing to clean up")

    def run_all_tests(self):
        """全てのテストを実行"""
        print("GIT OPERATIONS TEST SCRIPT")
        print("=" * 60)
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        try:
            self.test_git_status()
            self.test_git_info()
            self.test_git_add_and_status()
            self.test_git_diff()
            
        except KeyboardInterrupt:
            print("\n\nTest interrupted by user")
        except Exception as e:
            print(f"\n\nUnexpected error: {e}")
        finally:
            self.cleanup_test_file()
        
        print("\n" + "="*60)
        print(f"Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """メイン関数"""
    tester = GitTester()
    tester.run_all_tests()

if __name__ == "__main__":
    main()
