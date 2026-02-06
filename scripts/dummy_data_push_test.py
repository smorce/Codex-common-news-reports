#!/usr/bin/env python3
# scripts/dummy_data_push_test.py
# ダミーデータを生成してGit操作（add, commit, push）をテストするスクリプト

import os
import sys
import subprocess
import random
from pathlib import Path
from datetime import datetime, timezone
from dotenv import load_dotenv

class DummyDataPushTester:
    def __init__(self):
        """初期化"""
        # スクリプトの場所から相対的にリポジトリパスを決定
        script_dir = Path(__file__).parent
        self.repo_path = script_dir.parent  # scriptsディレクトリの親ディレクトリ
        self.reports_dir = self.repo_path / "reports"
        
        # .envファイルを読み込む
        env_file = self.repo_path / ".env"
        if env_file.exists():
            load_dotenv(env_file)
            print(f"[OK] Loaded .env from: {env_file}")
        else:
            print(f"[WARNING] .env file not found at: {env_file}")
        
        # 出力フォルダ作成
        self.reports_dir.mkdir(exist_ok=True)
        
        print(f"Repository path: {self.repo_path}")
        print(f"Reports directory: {self.reports_dir}")
        print("-" * 60)

    def log(self, message):
        """ログメッセージを表示"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")

    def generate_dummy_ai_news_report(self):
        """ダミーのAIニュースレポートを生成"""
        date = datetime.now().strftime("%Y%m%d")
        utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # ダミーニュース記事のデータ
        dummy_articles = [
            {
                "title": "新しいLLMモデル「GPT-5」がリリース予定",
                "date": "2025-09-28",
                "summary": "OpenAIが次世代の大規模言語モデル「GPT-5」の開発を発表。従来モデルより10倍高速で、より正確な推論能力を持つとされている。",
                "url": "https://ai-news.dev/gpt-5-announcement"
            },
            {
                "title": "自動運転技術の新ブレイクスルー",
                "date": "2025-09-27",
                "summary": "Tesla社が完全自動運転レベル5の技術を実現したと発表。都市部での複雑な交通状況でも安全に運転できる技術が確立された。",
                "url": "https://ai-news.dev/tesla-level5-breakthrough"
            },
            {
                "title": "AIによる医療診断の精度が95%に向上",
                "date": "2025-09-26",
                "summary": "Google DeepMindが開発した医療診断AIが、放射線科医と同等の精度を達成。早期がん検出の成功率が大幅に向上している。",
                "url": "https://ai-news.dev/medical-ai-95-accuracy"
            },
            {
                "title": "量子コンピューティングとAIの融合",
                "date": "2025-09-25",
                "summary": "IBM社が量子コンピューターとAIを組み合わせた新しいアーキテクチャを発表。従来の計算では不可能だった複雑な問題の解決が期待される。",
                "url": "https://ai-news.dev/quantum-ai-fusion"
            },
            {
                "title": "AIアシスタントの感情認識機能が進化",
                "date": "2025-09-24",
                "summary": "Microsoft社のAIアシスタントが人間の感情を99%の精度で認識できるようになった。より自然で共感的な対話が可能になる。",
                "url": "https://ai-news.dev/emotion-recognition-ai"
            },
            {
                "title": "ロボティクスの新時代：汎用ヒューマノイドロボット",
                "date": "2025-09-23",
                "summary": "Boston Dynamics社が家庭用ヒューマノイドロボット「Atlas Home」を発表。日常的な家事や介護業務を自動化できる技術を搭載。",
                "url": "https://ai-news.dev/atlas-home-robot"
            },
            {
                "title": "AIによる気候変動予測モデルの精度向上",
                "date": "2025-09-22",
                "summary": "Google AI研究チームが開発した気候変動予測モデルが、従来より30%高い精度を達成。より正確な災害予測と対策立案が可能になる。",
                "url": "https://ai-news.dev/climate-prediction-ai"
            },
            {
                "title": "次世代チップ「NPU-X」がAI処理速度を革新",
                "date": "2025-09-21",
                "summary": "NVIDIA社が発表した新しいNeural Processing Unit「NPU-X」が、従来のGPUより100倍高速なAI処理を実現。",
                "url": "https://ai-news.dev/npu-x-chip-revolution"
            },
            {
                "title": "AI教育プラットフォームが個別学習を最適化",
                "date": "2025-09-20",
                "summary": "Khan Academy社が開発したAI教育システムが、各生徒の学習パターンを分析して最適な学習プランを自動生成する機能を実装。",
                "url": "https://ai-news.dev/personalized-ai-education"
            },
            {
                "title": "音声合成技術が人間レベルの自然さを達成",
                "date": "2025-09-19",
                "summary": "ElevenLabs社の最新音声合成技術が、人間の声と区別がつかないレベルの自然さを実現。多言語対応と感情表現も可能になった。",
                "url": "https://ai-news.dev/human-level-voice-synthesis"
            }
        ]
        
        # ランダムに記事を選択（5-8記事）
        num_articles = random.randint(5, 8)
        selected_articles = random.sample(dummy_articles, num_articles)
        
        # Markdownレポート生成
        report_content = f"""# AI News Summary - {date}

Generated: {utc_now}

This report was generated automatically using AGENTS.md instructions.

---

"""
        
        for i, article in enumerate(selected_articles, 1):
            report_content += f"""## {i}. {article['title']}

**Publication Date:** {article['date']}

**Summary:** {article['summary']}

**URL:** {article['url']}

---

"""
        
        report_content += f"""
## Summary

本日は{len(selected_articles)}件のAI関連ニュースをまとめました。特に注目すべきは、新しい技術の実用化が進んでいることと、AIの精度向上が様々な分野で報告されていることです。

*このレポートは自動生成されました。*
"""
        
        return report_content, date

    def run_git_command(self, command_args, description=""):
        """Gitコマンドを実行して結果を表示"""
        self.log(f"[EXEC] {description}")
        self.log(f"Command: git {' '.join(command_args)}")
        
        try:
            # リポジトリディレクトリに移動
            original_cwd = os.getcwd()
            os.chdir(self.repo_path)
            
            try:
                result = subprocess.run(
                    ['git'] + command_args,
                    capture_output=True,
                    text=True,
                    check=True,  # エラーで例外を発生
                    encoding='utf-8',
                    errors='replace'  # Unicode エラーを回避
                )
                
                if result.stdout.strip():
                    self.log(f"[SUCCESS] STDOUT:\n{result.stdout}")
                
                if result.stderr.strip():
                    self.log(f"[WARNING] STDERR:\n{result.stderr}")
                
                return result
                
            finally:
                # 元のディレクトリに戻る
                os.chdir(original_cwd)
                
        except subprocess.CalledProcessError as e:
            self.log(f"[ERROR] Git command failed with return code {e.returncode}")
            if e.stdout:
                self.log(f"STDOUT: {e.stdout}")
            if e.stderr:
                self.log(f"STDERR: {e.stderr}")
            raise
        except Exception as e:
            self.log(f"[ERROR] Error executing git command: {e}")
            raise

    def check_git_status(self):
        """現在のGitステータスを確認"""
        self.log("[STATUS] Checking current Git status...")
        result = self.run_git_command(['status', '--porcelain'], "Get porcelain status")
        
        if result.stdout.strip():
            self.log(f"[CHANGES] Current changes:\n{result.stdout}")
            return True
        else:
            self.log("[CLEAN] Working directory is clean")
            return False

    def create_and_push_dummy_report(self):
        """ダミーレポートを作成してGitにプッシュ"""
        try:
            self.log("[START] Starting dummy data push test...")
            
            # 1. 初期状態のチェック
            self.check_git_status()
            
            # 2. ダミーレポート生成
            self.log("[GENERATE] Generating dummy AI news report...")
            report_content, date = self.generate_dummy_ai_news_report()
            
            report_file = self.reports_dir / f"ai-news-summary-{date}-test.md"
            report_file.write_text(report_content, encoding='utf-8')
            
            self.log(f"[CREATED] Created dummy report: {report_file}")
            self.log(f"[INFO] File size: {report_file.stat().st_size} bytes")
            
            # 3. ファイル作成後のステータス確認
            self.log("[STATUS] Status after creating file:")
            self.check_git_status()
            
            # 4. Git add
            rel_path = report_file.relative_to(self.repo_path)
            self.run_git_command(['add', str(rel_path)], f"Adding file: {rel_path}")
            
            # 5. ステージング後のステータス確認
            self.log("[STATUS] Status after staging:")
            self.check_git_status()
            
            # 6. Git commit
            commit_msg = f"Test: AI News summary {date} (dummy data)"
            self.run_git_command(['commit', '-m', commit_msg], f"Committing with message: {commit_msg}")
            
            # 7. Git push
            self.log("[PUSH] Pushing to remote repository...")
            branch = "main"  # または現在のブランチを取得
            self.run_git_command(['push', 'origin', branch], f"Pushing to origin/{branch}")
            
            # 8. 最終ステータス確認
            self.log("[STATUS] Final status:")
            self.check_git_status()
            
            self.log("[SUCCESS] Dummy data push test completed successfully!")
            self.log(f"[FILE] Report file: {report_file}")
            
            return report_file
            
        except Exception as e:
            self.log(f"[ERROR] Test failed: {e}")
            raise

    def cleanup_test_file(self, report_file):
        """テストファイルをクリーンアップ（オプション）"""
        try:
            self.log("[CLEANUP] Cleaning up test file...")
            
            if report_file.exists():
                # ファイルを削除
                report_file.unlink()
                self.log(f"[DELETED] Deleted test file: {report_file}")
                
                # Git から削除
                rel_path = report_file.relative_to(self.repo_path)
                self.run_git_command(['add', str(rel_path)], f"Staging deletion: {rel_path}")
                
                # コミット
                commit_msg = f"Cleanup: Remove test file {rel_path.name}"
                self.run_git_command(['commit', '-m', commit_msg], f"Committing cleanup")
                
                # プッシュ
                self.run_git_command(['push', 'origin', 'main'], "Pushing cleanup")
                
                self.log("[SUCCESS] Cleanup completed")
            else:
                self.log("[INFO] Test file not found - nothing to clean up")
                
        except Exception as e:
            self.log(f"[WARNING] Cleanup failed (not critical): {e}")

    def run_full_test(self, cleanup=False):
        """完全なテストを実行"""
        self.log("=" * 60)
        self.log("[TEST] DUMMY DATA PUSH TEST")
        self.log("=" * 60)
        self.log(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        report_file = None
        
        try:
            report_file = self.create_and_push_dummy_report()
            
            if cleanup:
                # クリーンアップを実行（オプション）
                user_input = input("\nCleanup test file? (y/N): ").strip().lower()
                if user_input == 'y':
                    self.cleanup_test_file(report_file)
            
        except KeyboardInterrupt:
            self.log("\n[ERROR] Test interrupted by user")
        except Exception as e:
            self.log(f"\n[ERROR] Unexpected error: {e}")
            raise
        finally:
            self.log("=" * 60)
            self.log(f"Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """メイン関数"""
    tester = DummyDataPushTester()
    tester.run_full_test(cleanup=False)  # cleanup=True にするとテストファイルを自動削除

if __name__ == "__main__":
    main()
