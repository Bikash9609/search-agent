import logging
from langchain.tools import tool
from third_party.tavily import tavily


@tool
def web_search_tool(query: str, limit: int = 3):
    """
    Search web with a given query and get results.
    Args:
        query: short concise search term
        limit: number of results to return
    Returns:
        List of web search results for that query
    """

    if limit > 3:
        limit = 3

    logging.info(f"Calling web search for: {query} with limit: {limit}")

    res = tavily.search(query, max_results=limit)
    if not res["results"]:
        return []

    required_fields = ["title", "url", "content"]
    return [
        {k: result[k] for k in required_fields if k in result}
        for result in res["results"]
    ]
