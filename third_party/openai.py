from config.env import openai_api_key, openai_default_model
from langchain_openai import ChatOpenAI
from langchain_core.globals import set_verbose, set_debug
import logging

logging.basicConfig(level=logging.INFO)

# Enabled by default
set_verbose(True)
set_debug(True)

llm = ChatOpenAI(
    api_key=openai_api_key,
    model=openai_default_model,
    temperature=1,
    reasoning_effort="minimal",
)
