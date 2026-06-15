from tavily import TavilyClient
from config.env import tavily_api_key

tavily = TavilyClient(api_key=tavily_api_key)
