import os
import json
import time
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import libsql

# .env を読み込み（既存環境変数は保持）
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"), override=False)

TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL", "")
TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN", "")

DDL_DAILY_REPORT = """
CREATE TABLE IF NOT EXISTS daily_ai_news_reports (
  report_id TEXT PRIMARY KEY,
  site TEXT NOT NULL,
  report_date TEXT NOT NULL,
  generated_at TEXT,
  num_articles INTEGER NOT NULL,
  articles_json TEXT NOT NULL,
  markdown_content TEXT,
  created_at REAL NOT NULL,
  updated_at REAL
);
"""

_conn = None


def _get_conn():
    global _conn
    if _conn is None:
        if not TURSO_DATABASE_URL:
            raise RuntimeError("TURSO_DATABASE_URL is not set. Please set it in .env")
        _conn = libsql.connect(TURSO_DATABASE_URL, auth_token=TURSO_AUTH_TOKEN)
    return _conn


def _ensure_schema() -> None:
    conn = _get_conn()
    conn.execute(DDL_DAILY_REPORT)
    conn.commit()


def push_daily_report(report_obj: Dict[str, Any], markdown_content: Optional[str], report_date: str) -> str:
    """reports/{YYYY-MM-DD}/report.json をもとに Turso にUPSERTする。

    JSONのトップレベルKEYを列に対応させて保存:
    - site -> site
    - generated_at -> generated_at
    - num_articles -> num_articles（なければ articles 配列長）
    - articles -> articles_json（文字列化）
    - markdown_content -> markdown_content
    - report_date は呼び出し元引数
    - report_id は ai-news-{report_date}
    """
    _ensure_schema()

    site = report_obj.get("site") or "ai-news.dev"
    generated_at = report_obj.get("generated_at") or ""
    articles = report_obj.get("articles") or []
    num_articles = report_obj.get("num_articles") or (len(articles) if isinstance(articles, list) else 0)
    # タイムスタンプを含めて新レコードとして追加
    timestamp = int(time.time())
    report_id = f"ai-news-{report_date}-{timestamp}"
    articles_text = json.dumps(articles, ensure_ascii=False)
    created_at = time.time()
    updated_at = created_at

    conn = _get_conn()
    conn.execute(
        """
        INSERT INTO daily_ai_news_reports (
          report_id, site, report_date, generated_at, num_articles, articles_json, markdown_content, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(report_id) DO UPDATE SET
          site=excluded.site,
          report_date=excluded.report_date,
          generated_at=excluded.generated_at,
          num_articles=excluded.num_articles,
          articles_json=excluded.articles_json,
          markdown_content=excluded.markdown_content,
          updated_at=excluded.updated_at
        """,
        (
            report_id,
            site,
            report_date,
            generated_at,
            int(num_articles) if isinstance(num_articles, int) else 0,
            articles_text,
            markdown_content or None,
            created_at,
            updated_at,
        ),
    )
    conn.commit()

    return report_id


