def article_serializer(article) -> dict:
    return {
        "id": str(article["_id"]),
        "title": article["Title"],
        "summary": article["Summary"],
        "picture": article["Picture"]
    }

def articles_serializer(articles) -> list:
    return [article_serializer(article) for article in articles]