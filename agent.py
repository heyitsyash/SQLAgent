from langchain.agents import create_agent
from db import db,tools
from prompts import system_prompt
from model import gemini_model

prompt = system_prompt.format(dialect = db.dialect,top_k = 5)

agent = create_agent(
    gemini_model,
    tools,
    system_prompt=prompt,
)

question = "Which genre on average has the longest tracks?"

for step in agent.stream(
    {"messages": [{"role": "user", "content": question}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()
