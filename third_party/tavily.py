from langchain_tavily import TavilySearch
from config.env import tavily_api_key

web_search_tool = TavilySearch(api_key=tavily_api_key, max_results=5)
