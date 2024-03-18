from typing import List
from langchain_core.output_parsers import JsonOutputParser
from packages.evaluation import EvaluationGrid

parser = JsonOutputParser(pydantic_object=EvaluationGrid)
