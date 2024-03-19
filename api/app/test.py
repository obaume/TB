from packages.llms.openai import llm
from langchain_core.prompts import ChatPromptTemplate
chain = ChatPromptTemplate.from_template("Tell me a joke about {topic}") | llm
print(chain.invoke({"topic": "ice hockey"}))

