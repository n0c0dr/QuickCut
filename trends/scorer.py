from collections import Counter

STOPWORDS = {
    "today", "live", "news", "update", "latest", "india"
}

def score_trends(phrases, top_n=10):
    counter = Counter(
        p for p in phrases
        if not p.lower() in STOPWORDS
    )

    return [
        trend for trend, _ in counter.most_common(top_n)
    ]
