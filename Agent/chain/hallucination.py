from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
# from langchain_openai.chat_models import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from Agent.chain.retrival_grader import system
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
os.environ["OPENAI_API_KEY"]="None"
load_dotenv()
# llm= ChatOllama(base_url="http://172.16.0.178:8010",model="llama3.2:1b",temperature=0.1)
llm =ChatOpenAI(base_url="http://10.40.0.18:8000/v1",model="meta-llama/Llama-3.2-3B-Instruct")

class GradeHallucination(BaseModel):
    binary_score:bool= Field(description="Score for grading hallucination in yes or no")

structured_llm_grader = llm.with_structured_output(GradeHallucination)
system=""" You are a grader assesing whether an LLM generation is grounded in / supported by the given set of documents.
Give a binary score 'yes' or 'no'. 'Yes' means the answer is grounded / supported by the set of documents 
"""

hallucination_prompt=ChatPromptTemplate.from_messages(
[    ("system", system),
    ("human", "User question: \n\n {documents} \n\n LLM generation: {generation}")
])
hallucination_grader: RunnableSequence = hallucination_prompt | structured_llm_grader