from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import List
from langserve import add_routes
from langchain_core.pydantic_v1 import BaseModel
from packages.template import template
from packages.parser import parser
from packages.llms.openai import llm as openai
from packages.llms.mistral import llm as mistral
import os


class EvaluationGridItem(BaseModel):
    field_name: str
    max_point: int


class Prompt(BaseModel):
    evaluation_grid: List[EvaluationGridItem]
    code: str


app = FastAPI()


@app.post("/openai")
async def openai(i: Prompt):
    return await invoke_prompt(i, openai)


@app.post("/mistral")
async def mistral(i: Prompt):
    return await invoke_prompt(i, mistral)


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


async def invoke_prompt(i: Prompt, llm):
    chain = template | llm | parser
    print(i.dict().get("evaluation_grid"))
    print(i.dict().get("code"))
    response = await chain.ainvoke({"evaluation_grid": i.dict().get("evaluation_grid"), "code": i.dict().get("code")})
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
