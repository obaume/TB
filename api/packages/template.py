from langchain.prompts import PromptTemplate
from parser import parser

template = PromptTemplate(
    template="""
    You are a computer science professor giving a course on object-oriented programming who will grade a exercise from a 
    student. 
    Here is the evaluation grid for the exercise in a json format:
    {evaluation_grid}
    Here is the student's code :
    {code}
    Your task is foreach topics in the evaluation grid above to give a score between 0 and the max point provided in 
    the grid. Then you will comment on why you gave this amount of point providing what was correctly or incorrectly 
    done in the student's code.
    {format_instructions}
    """,
    input_variables=["evaluation_grid", "code"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)