from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import List
from langserve import add_routes
from langchain_core.pydantic_v1 import BaseModel
from packages.template import template
from packages.parser import parser
from packages.llms.openai import llm as openai



LANGCHAIN_TRACING_V2 = True
LANGCHAIN_API_KEY = "ls__1fec0371002f4a29a2f8cb8c5c5d2583"
LANGCHAIN_PROJECT = "autograder-poo-api"


class Evaluation_grid_item(BaseModel):
    field_name: str
    max_point: int

class Prompt(BaseModel):
    evalution_grid: List[Evaluation_grid_item]
    code: str


app = FastAPI()

@app.post("/openai")
async def openai(prompt: Prompt):
    return invoke_prompt(prompt, openai)

@app.post("/mistral")
async def mistral(prompt: Prompt):
    return input (prompt, mistral)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

def invoke_prompt(prompt:Prompt, llm):
    return (template | llm | parser).invoke({"evaluation_grid": prompt.evalution_grid, "code": prompt.code})

# Edit this to add the chain you want to add
add_routes(app, NotImplemented)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
