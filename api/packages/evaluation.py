from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List


class Evaluation(BaseModel):
    field_name: str = Field(description="Name of the field in the evaluation grid")
    points: int = Field(description="Number of points earned for this field in the evaluation grid")
    max_points: int = Field(description="Maximum points for this field in the evaluation grid")
    explanation: str = Field(description="Explanation for the points earned for this field in the evaluation grid")


class EvaluationGrid(BaseModel):
    rows: List[Evaluation] = Field(description="List of evaluation")
