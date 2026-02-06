#!/usr/bin/env python3
# scripts/get_github_trending.py

import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup


@dataclass
class Repository:
    name: str
    description: Optional[str]
    link: str
    stars: int
    stars_today: int  # 今日獲得したスター数
    stars_period: str  # "today" or "this week"
    readme_content: Optional[str]


def _read_languages_config(languages_file: Path) -> Dict[str, List[str]]:
    """languages.toml を読み込む。

    Python 3.11+ の tomllib を使う（追加依存を増やさない）。
    """
    import tomllib

    with open(languages_file, "rb") as f:
        data = tomllib.load(f)
    general = data.get("general", []) or []
    specific = data.get("specific", []) or []
    # 型をだいたい保証
    general = [str(x) for x in general]
    specific = [str(x) for x in specific]
    return {"general": general, "specific": specific}


def _retrieve_repositories(language: str, limit: int) -> List[Repository]:
    """GitHub Trending から指定言語のリポジトリを取得。"""
    base_url = "https://github.com/trending"
    url = base_url + (f"/{language}" if language else "")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    }

    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error retrieving repositories for language {language}: {e}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    repositories: List[Repository] = []

    for article in soup.select("article.Box-row")[: limit if limit and limit > 0 else None]:
        # Name
        name_el = article.select_one("h2 a")
        if not name_el:
            continue
        raw_name = name_el.text.strip().replace("\n", " ")
        # Normalize spaces around '/'
        name = "/".join(part.strip() for part in raw_name.split("/") if part.strip())
        link = f"https://github.com{name_el.get('href', '').strip()}"

        # Description
        desc_el = article.select_one("p")
        description = desc_el.text.strip() if desc_el and desc_el.text else None

        # Stars (累積スター数)
        stars = 0
        star_link = article.select_one("a[href$='/stargazers']")
        if star_link and star_link.text:
            digits = star_link.text.strip().replace(",", "").replace(".", "")
            if digits.isdigit():
                stars = int(digits)
        else:
            # Fallback: try to find any number near star svg
            possible = article.select("a")
            for a in possible:
                txt = (a.text or "").strip().replace(",", "").replace(".", "")
                if txt.isdigit():
                    stars = int(txt)
                    break

        # Stars today/this week (トレンドスター数) - これが重要！
        stars_today = 0
        stars_period = "today"
        
        # 複数のセレクタを試す（GitHubのHTML構造は変わることがある）
        trend_selectors = [
            "span.d-inline-block.float-sm-right",
            "span.float-sm-right",
            "span[class*='float']",
            "div.f6.color-fg-muted.mt-2 span:last-child",
        ]
        
        trend_text = ""
        for selector in trend_selectors:
            trend_el = article.select_one(selector)
            if trend_el:
                trend_text = trend_el.get_text(" ", strip=True)
                if "star" in trend_text.lower():
                    break
        
        # "123 stars today" or "1,234 stars this week" のパターンをマッチ
        if trend_text:
            # 数字とカンマを含むパターン: "1,234 stars today"
            match = re.search(r'([\d,]+)\s+stars?\s+(today|this\s+week)', trend_text, re.IGNORECASE)
            if match:
                stars_today = int(match.group(1).replace(",", ""))
                stars_period = "today" if "today" in match.group(2).lower() else "this week"

        # README全文を取得
        readme_content = None
        try:
            repo_resp = requests.get(link, headers=headers, timeout=15)
            repo_resp.raise_for_status()
            repo_soup = BeautifulSoup(repo_resp.text, "html.parser")

            # README のセレクタを複数試す（GitHubのHTML構造変更に対応）
            readme_el = None
            selectors = [
                "div[data-testid='readme-blob']",  # 新しい test-id
                "#readme article",                 # 従来のセレクタ
                "article.markdown-body",           # Markdown 本文
            ]
            for s in selectors:
                readme_el = repo_soup.select_one(s)
                if readme_el:
                    break
            
            if readme_el:
                readme_content = readme_el.get_text("\n", strip=True)
        except Exception as e:
            # READMEが取得できなくても処理は続ける
            print(f"Could not retrieve README for {name}: {e}", file=sys.stderr)

        repositories.append(
            Repository(
                name=name,
                description=description,
                link=link,
                stars=stars,
                stars_today=stars_today,
                stars_period=stars_period,
                readme_content=readme_content,
            )
        )

    return repositories


def _dedupe_repositories(repos_by_lang: List[Tuple[str, List[Repository]]]) -> List[Repository]:
    """言語横断で重複（同一リンク）を排除。"""
    seen: Dict[str, Repository] = {}
    for _lang, repos in repos_by_lang:
        for r in repos:
            if r.link not in seen:
                seen[r.link] = r
            else:
                # Prefer higher stars_today (今日のスター数) if duplicate appears
                if r.stars_today > seen[r.link].stars_today:
                    seen[r.link] = r
                elif r.stars_today == seen[r.link].stars_today and r.stars > seen[r.link].stars:
                    # 同じ今日のスター数なら、累積スター数が多い方を優先
                    seen[r.link] = r
    return list(seen.values())


def collect_github_trending_report(
    languages_file: Path,
    general_limit: int = 10,
    specific_limit: int = 5,
    min_stars_today: int = 0,  # フィルタ条件
) -> Dict[str, object]:
    """GitHub Trending をクロールし、プロジェクト用レポートJSONを返す。"""
    config = _read_languages_config(languages_file)

    repos_by_language: List[Tuple[str, List[Repository]]] = []

    for language in config.get("general", []):
        repos_by_language.append((language or "all", _retrieve_repositories(language, general_limit)))

    for language in config.get("specific", []):
        repos_by_language.append((language, _retrieve_repositories(language, specific_limit)))

    deduped = _dedupe_repositories(repos_by_language)

    # Filter by minimum stars today (今日のスター数でフィルタ)
    if min_stars_today > 0:
        deduped = [r for r in deduped if r.stars_today >= min_stars_today]

    # Sort by stars_today desc (今日のスター数でソート - これが重要！)
    # 次に累積スター数でソート
    deduped.sort(key=lambda r: (r.stars_today, r.stars), reverse=True)

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    now_local = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    articles: List[Dict[str, object]] = []
    for r in deduped:
        executive_summary: List[str] = []
        if r.description:
            executive_summary.append(r.description)

        if r.readme_content:
            executive_summary.append("---")
            executive_summary.append(r.readme_content)

        # 今日の獲得スター数＋累計スター数
        executive_summary.append(f"今日の獲得スター数: {r.stars_today:,}")
        executive_summary.append(f"累積スター数: {r.stars:,}")

        # key_findings は NULL を指定
        key_findings = None  # type: ignore[assignment]

        articles.append(
            {
                "url": r.link,
                "title": r.name,
                "date": None,
                "executive_summary": executive_summary,
                "key_findings": key_findings,
                "references": [r.link],
                "retrieved_at": now_utc,
            }
        )

    report_obj: Dict[str, object] = {
        "generated_at": now_utc,
        "site": "github-trending",
        "num_articles": len(articles),
        "articles": articles,
    }

    return report_obj

