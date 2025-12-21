from ddgs import DDGS

def fetch_news(query, region, max_results=25):
    results = []

    with DDGS() as ddgs:
        news = ddgs.news(
            query,
            region=region,
            timelimit="d",
            max_results=max_results
        )
        for item in news:
            results.append(item["title"])

    return results
