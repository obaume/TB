from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import List
from langchain_core.pydantic_v1 import BaseModel
from packages.template import template
from packages.parser import parser
from packages.llms.openai import llm as llm_openai
from packages.llms.mistral import llm as llm_mistral
from packages.llms.llama2 import llm as llm_llama2
from langsmith import Client

class EvaluationGridItem(BaseModel):
    field_name: str
    max_point: int


class Prompt(BaseModel):
    evaluation_grid: List[EvaluationGridItem]
    code: str


app = FastAPI()
all_llm = {"openai": llm_openai, "mistral": llm_mistral, "llama2": llm_llama2}


@app.post("/all")
async def all(i: Prompt):
    out = {}
    for name, lmm in all_llm.items():
        out += {name: chain_invoke(i, lmm)}
    return out


@app.post("/openai")
async def openai(i: Prompt):
    return chain_invoke(i, llm_openai)


@app.post("/mistral")
async def mistral(i: Prompt):
    return chain_invoke(i, llm_mistral)


@app.post("/llama2")
async def llama2(i: Prompt):
    return chain_invoke(i, llm_llama2)


def chain_invoke(i: Prompt, llm):
    chain = template | llm | parser
    return chain.invoke({"code": i.dict().get("code"), "evaluation_grid": i.dict().get("evaluation_grid")})


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
