from app.db.repositories.parsers import string_or_null

def select_all_news_query() -> str:
    return \
        f"SELECT (news.select_all_master_news()).*"

def select_all_news_images_query() -> str:
    return \
        f"SELECT (news.select_all_slave_news()).*"

def select_news_preview_query(start: int, count: int) -> str:
    return \
        f"SELECT * FROM news.news ORDER BY id DESC LIMIT {count} OFFSET {start}"

def select_news_query(id: int) -> str:
    return \
        f"SELECT * FROM news.news WHERE id={id}"

def select_images_for_news_query(fk: int) -> str:
    return \
        f"SELECT (news.select_slave_news({fk})).*"

def get_news_count_query() -> str:
    return \
        f"SELECT news.get_news_count() AS count"
