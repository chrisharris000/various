import feedparser

URLS = ["https://www.dailytelegraph.com.au/news/breaking-news/rss",
        "https://www.dailytelegraph.com.au/newslocal/parramatta/rss",
        "https://www.dailytelegraph.com.au/news/nsw/rss",
        "https://www.dailytelegraph.com.au/news/national/rss",
        "https://www.dailytelegraph.com.au/news/world/rss",
        "https://www.news.com.au/content-feeds/latest-news-technology/"]

CATEGORIES = ["Breaking News", "Local", "State", "National", "World", "Technology"]

def extract_data(url):
    news_summary = []
    data = feedparser.parse(url)
    entries = data['entries']
    for e in entries:
        title = e["title"]
        article_summary = e["summary"]
        link = e["links"][0]["href"]
        news_summary.append({'title':title,
                             'article_summary':article_summary,
                             'link':link})
    return news_summary

def information(urls = URLS, categories = CATEGORIES):
    info = {}
    for url, category in zip(urls,categories):
        news_summary = extract_data(url)
        info[category] = news_summary
    return info
