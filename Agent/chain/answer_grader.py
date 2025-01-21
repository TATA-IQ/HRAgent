from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import RunnableSequence

from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from Agent.chain.retrival_grader import system
from langchain_ollama import ChatOllama
import os
os.environ["OPENAI_API_KEY"]="None"

class GradeAnswer(BaseModel):
    binary_score:bool= Field(description="IS answer address the question , 'yes' or 'no'")
    grader: str= Field(description="If LLM generation 1 is better say LLAMA, if LLM generation2 is better say recursive")

llm =ChatOpenAI(base_url="http://10.40.0.18:8000/v1",model="meta-llama/Llama-3.2-3B-Instruct")
# llm=ChatOllama(base_url="http://172.16.0.178:8010",model="llama3.2:1b",temperature=0.1)

structure_llm_grader= llm.with_structured_output(GradeAnswer)
system = """You are a  grader assessing whether an answer addresses / resolve a question \n
Give a binary score 'yes' or 'no'. 'Yes' means that the answer resolves the question.
Also, given two generation,choose which is the best answer if LLM generation1 is better, give LLAMA as value to
grader and if  LLM generation2 is better give recursive as value
"""

answer_prompt= ChatPromptTemplate.from_messages(
    [
        ("system",system),
        ("human","User question: \n\n {question} \n\n LLM generation1: {generation_llama} LLM generation2: {generation_recursive}"),
    ]
)

answer_grader: RunnableSequence = answer_prompt | structure_llm_grader