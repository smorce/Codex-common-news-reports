# ============================================
# Google Colab用 RSS記事取得サンプルコード
# result = collect_rss_sources(
#     feed_config=FEED_CONFIG,
#     days=7,           # ← 7日間に変更
#     limit_per_feed=10 # ← 各フィードから10件に変更
# )
# ============================================

# 1. 必要なライブラリのインストール
!pip install feedparser requests beautifulsoup4 -q

# 2. コードの実装
import re
import json
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Optional

import feedparser
import requests
from bs4 import BeautifulSoup


def _parse_entry_datetime(entry) -> Optional[datetime]:
    """RSSエントリから日付を抽出"""
    try:
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            return datetime(*entry.published_parsed[:6])
        if hasattr(entry, "updated_parsed") and entry.updated_parsed:
            return datetime(*entry.updated_parsed[:6])
    except Exception:
        pass
    return None


def _extract_article_text(entry, url: str, session: requests.Session) -> str:
    """記事本文のテキストを抽出"""
    # 1) エントリのsummaryから取得
    if hasattr(entry, "summary") and entry.summary:
        return BeautifulSoup(entry.summary, "html.parser").get_text(" ", strip=True)

    # 2) 本文ページから抽出
    try:
        resp = session.get(url, timeout=15)
        if resp.status_code != 200:
            return ""
        soup = BeautifulSoup(resp.text, "html.parser")

        # meta descriptionを優先
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc and meta_desc.get("content"):
            return str(meta_desc.get("content")).strip()

        # なければ最初の6段落を取得
        paragraphs = soup.find_all("p")
        if paragraphs:
            texts = [p.get_text(" ", strip=True) for p in paragraphs[:6]]
            return "\n".join([t for t in texts if t])
    except Exception as e:
        print(f"⚠️ 記事取得エラー ({url}): {e}")
        return ""

    return ""


def collect_rss_sources(
    feed_config: Dict[str, List[str]],
    days: int = 1,
    limit_per_feed: int = 3,
) -> Dict[str, object]:
    """RSSソースを機械的に収集して生データJSONを返す"""
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        }
    )

    cutoff = datetime.now() - timedelta(days=days)
    sources: List[Dict[str, object]] = []

    print(f"📡 RSS収集開始: {len(feed_config)}カテゴリ、過去{days}日間、各フィード最大{limit_per_feed}件\n")

    for category, feed_urls in feed_config.items():
        print(f"📂 カテゴリ: {category} ({len(feed_urls)}フィード)")
        
        for feed_url in feed_urls:
            try:
                print(f"  ⏳ 取得中: {feed_url}")
                parsed = feedparser.parse(feed_url)
                feed_name = (
                    parsed.feed.title if hasattr(parsed, "feed") and hasattr(parsed.feed, "title") else feed_url
                )
                entries = list(getattr(parsed, "entries", []))

                # 日付フィルタ → 新しい順にしてlimit
                filtered: List = []
                for e in entries:
                    dt = _parse_entry_datetime(e)
                    if dt is None or dt >= cutoff:
                        filtered.append((dt or datetime.now(), e))
                filtered.sort(key=lambda x: x[0], reverse=True)
                filtered = [e for _dt, e in filtered[:limit_per_feed]]

                for e in filtered:
                    url = getattr(e, "link", None)
                    if not url:
                        continue
                    title = getattr(e, "title", "無題")
                    published_at = _parse_entry_datetime(e)
                    text = _extract_article_text(e, url, session)

                    sources.append(
                        {
                            "feed_name": feed_name,
                            "category": category,
                            "title": title,
                            "url": url,
                            "date": published_at.strftime("%Y-%m-%dT%H:%M:%S") if published_at else None,
                            "text": text[:500] + "..." if len(text) > 500 else text,  # 表示用に500文字制限
                        }
                    )
                
                print(f"    ✅ {len(filtered)}件取得: {feed_name}")
                
            except Exception as e:
                print(f"    ❌ エラー: {e}")
                continue
        
        print()

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "generated_at": now_utc,
        "site": "tech-blogs/rss-sources",
        "num_articles": len(sources),
        "sources": sources,
    }


# 3. フィード設定（feed.tomlの内容）
FEED_CONFIG = {
    "tech_blogs": [
        "https://engineering.atspotify.com/feed/",
        "https://netflixtechblog.com/feed",
        "https://blog.cloudflare.com/rss/",
        "https://blog.google/technology/developers/rss/",
        "https://aws.amazon.com/blogs/aws/feed/",
        "https://devblogs.microsoft.com/python/feed/",
        "https://blog.twitter.com/engineering/en_us/blog.rss",
        "https://medium.com/feed/airbnb-engineering",
    ],
    "ai_ml": [
        "https://ai.googleblog.com/feeds/posts/default",
        "https://openai.com/blog/rss/",
        "https://huggingface.co/blog/feed.xml",
        "https://ai-news.dev/feeds/",
        "https://rss.beehiiv.com/feeds/GcFiF2T4I5.xml",
        "https://thinkingmachines.ai/index.xml",
    ],
    "zenn": [
        "https://zenn.dev/topics/cursor/feed",
        "https://zenn.dev/topics/langchain/feed",
        "https://zenn.dev/topics/mcp/feed",
        "https://zenn.dev/topics/ai駆動開発/feed",
    ],
    "qiita": [
        "http://qiita.com/tags/AI/feed.atom",
        "http://qiita.com/tags/Cursor/feed.atom",
        "http://qiita.com/tags/LangChain/feed.atom",
        "http://qiita.com/tags/LLM/feed.atom",
        "http://qiita.com/tags/mcp/feed.atom",
        "http://qiita.com/tags/AI駆動開発/feed.atom",
    ],
}

# 4. 実行
print("="*60)
print("🚀 RSS記事収集テスト開始")
print("="*60 + "\n")

# パラメータを調整可能
result = collect_rss_sources(
    feed_config=FEED_CONFIG,
    days=1,           # 過去1日間の記事
    limit_per_feed=3  # 各フィードから最大3件
)

# 5. 結果表示
print("="*60)
print("📊 収集結果")
print("="*60)
print(f"生成日時: {result['generated_at']}")
print(f"総記事数: {result['num_articles']}件\n")

# カテゴリ別の集計
category_counts = {}
for source in result['sources']:
    cat = source['category']
    category_counts[cat] = category_counts.get(cat, 0) + 1

print("📈 カテゴリ別集計:")
for cat, count in category_counts.items():
    print(f"  • {cat}: {count}件")

print("\n📝 取得記事一覧（最初の5件）:")
for i, source in enumerate(result['sources'][:5], 1):
    print(f"\n{i}. [{source['category']}] {source['title']}")
    print(f"   🔗 {source['url']}")
    print(f"   📅 {source['date'] or '日付不明'}")
    print(f"   📰 {source['feed_name']}")
    if source['text']:
        preview = source['text'][:100].replace('\n', ' ')
        print(f"   💬 {preview}...")

# 6. JSON出力（ファイル保存も可能）
print("\n" + "="*60)
print("💾 JSON出力")
print("="*60)

json_output = json.dumps(result, ensure_ascii=False, indent=2)
print(json_output[:1000] + "\n... (省略)")

# ファイルに保存する場合（Colabの場合は左側のファイルアイコンからダウンロード可能）
with open('rss_sources.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print("\n✅ rss_sources.json に保存しました")