from .config import CATEGORIES, REGIONS
from .fetcher import fetch_news
from .nlp import extract_trends
from .scorer import score_trends

def get_category_trends(category, region="india", state=None):
    queries = CATEGORIES.get(category, [])
    region_code = REGIONS.get(region, "in-en")

    all_titles = []

    for q in queries:
        query = q
        if state:
            query = f"{state} {q}"

        all_titles.extend(fetch_news(query, region_code))

    phrases = extract_trends(all_titles)
    return score_trends(phrases)
