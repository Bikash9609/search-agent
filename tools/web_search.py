from langchain.tools import tool
import logging


@tool
def web_search_tool(query: str, limit: int = 10):
    """
    Search web with a given query and get results.
    Args:
        query: short concise search term
        limit: number of results to return
    Returns:
        Web search results for that query

    """
    logging.info(f"Calling web search for: {query} with limit: {limit}")
    return
