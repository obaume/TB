from typing import List
from langchain_core.output_parsers import JsonOutputParser
from evaluation import Evaluation

parser = JsonOutputParser(pydantic_object=List[Evaluation])
