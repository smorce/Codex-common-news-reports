#!/usr/bin/env python3
# scripts/get_reddit.py

import json
import time
from datetime import datetime, timezone
from urllib import request, error


def collect_reddit_raw_data(
    tech_subs=None,
    news_subs=None,
    num_articles=2,
    retry_max=3,
    timeout=30,
    user_agent="CodexAgent/1.0 (contact: example@example.com)"
):
    """
    Reddit JSON API から生データを収集
    
    Args:
        tech_subs: tech カテゴリのサブレディットリスト（デフォルト: ["artificial", "compsci", "coding"]）
        news_subs: news カテゴリのサブレディットリスト（デフォルト: ["technology", "Futurology"]）
        num_articles: 各グループから取得する記事数
        retry_max: 最大リトライ回数
        timeout: タイムアウト秒数
        user_agent: User-Agent 文字列
        
    Returns:
        dict: {"tech": [...], "news": [...], "fetched_at": "..."}
    """
    if tech_subs is None:
        tech_subs = ["artificial", "compsci", "coding"]
    if news_subs is None:
        news_subs = ["technology", "Futurology"]
    
    def fetch_group(subs):
        combined = "+".join(subs)
        url = f"https://www.reddit.com/r/{combined}/top.json?t=day&limit={num_articles}"
        last_exc = None
        
        for attempt in range(1, retry_max + 1):
            try:
                req = request.Request(url, headers={"User-Agent": user_agent})
                with request.urlopen(req, timeout=timeout) as resp:
                    if resp.status != 200:
                        raise RuntimeError(f"HTTP {resp.status}")
                    payload = resp.read()
                return json.loads(payload)
            except (error.URLError, error.HTTPError, RuntimeError, json.JSONDecodeError) as exc:
                last_exc = exc
                if attempt == retry_max:
                    raise
                time.sleep(1)
        raise last_exc
    
    def normalize(items):
        normalized = []
        for child in items.get("data", {}).get("children", []):
            data = child.get("data", {})
            normalized.append({
                "title": data.get("title"),
                "permalink": data.get("permalink"),
                "url": data.get("url"),
                "created_utc": data.get("created_utc"),
                "subreddit": data.get("subreddit"),
                "author": data.get("author"),
                "score": data.get("score"),
                "num_comments": data.get("num_comments"),
            })
        return normalized
    
    def to_iso(ts):
        if ts is None:
            return None
        return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()
    
    # データ取得
    tech_raw = fetch_group(tech_subs)
    news_raw = fetch_group(news_subs)
    
    tech_items = normalize(tech_raw)
    news_items = normalize(news_raw)
    
    result = {
        "tech": [
            {**item, "created_iso": to_iso(item.get("created_utc"))}
            for item in tech_items
        ],
        "news": [
            {**item, "created_iso": to_iso(item.get("created_utc"))}
            for item in news_items
        ],
        "fetched_at": datetime.now(tz=timezone.utc).isoformat(),
    }
    
    return result


def main():
    """スタンドアロン実行用（テスト）"""
    result = collect_reddit_raw_data()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

