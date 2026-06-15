from third_party.openai import llm
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from tools import tools


agent = create_agent(model=llm, tools=tools)


prompt = HumanMessage(str(input("Enter your prompt here: ")))
response = agent.invoke({"messages": [prompt]})
print(response)
