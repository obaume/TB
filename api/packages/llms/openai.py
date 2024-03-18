from langchain_openai import OpenAI
import os

llm = OpenAI(openai_api_key=os.environ['OPENAI_API_KEY'])
