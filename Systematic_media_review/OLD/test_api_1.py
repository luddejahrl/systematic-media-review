from duckduckgo_search import ddg_news

def ddg_news(
    keywords,
    region="wt-wt",
    safesearch="moderate",
    time=None,
    max_results=None,
    page=1,
    output=None,
):
    """DuckDuckGo news search. Query params: https://duckduckgo.com/params

    Args:
        keywords (str): keywords for query.
        region (str): wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch (str): on, moderate, off. Defaults to "moderate".
        time (Optional[str], optional): d, w, m. Defaults to None.
        max_results (Optional[int], optional): maximum number of results, max=240. Defaults to None.
            if max_results is set, then the parameter page is not taken into account.
        page (int, optional): page for pagination. Defaults to 1.
        output (Optional[str], optional): csv, json. Defaults to None.

    Returns:
        Optional[List[dict]]: DuckDuckGo news search results.
    """
    
from duckduckgo_search import ddg_news


keywords = "russia invasion ukraine"
r = ddg_news(keywords, region='wt-wt', safesearch='Off', time='y', max_results=1)

print(r)

r = ddg_news(keywords, region='wt-wt', safesearch='Off', time='d', max_results=1)

print(r)

