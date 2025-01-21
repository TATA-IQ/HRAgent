from pydantic import BaseModel
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"]="None"
# from dotenv import load_dotenv
# load_dotenv()
llm =ChatOpenAI(base_url="http://10.40.0.18:8000/v1",model="meta-llama/Llama-3.2-3B-Instruct")
# llm=ChatOllama(base_url="http://172.16.0.178:8010",model="llama3.2:1b",temperature=0)
print("============Retrieval Grader========")
class GradeDocument(BaseModel):
    binary_score: str= Field("Give a binary score 'yes' or 'no' score to indicate whether the document is relevant or not")

structure_llm_grader= llm.with_structured_output(GradeDocument)

system=""" You are a grader assessing relevance of a retrieved document to a user question.\n
If the document contains keyword(s) or semantic meaning related to the question, grade it as a relevent.
Give a binary score 'yes' or 'no' score to indicate whether the document is relevant or not

"""
print("=========Grader of Retrival========")
grade_prompt= ChatPromptTemplate.from_messages([
    ("system",system),
    ("human",'Retrieved documents: \n\n {documents} \n\n user_question: {question}')
])
# print(grade_prompt)
retrieval_grader=grade_prompt|structure_llm_grader
print("===========Retrival grader call done=======")
print(retrieval_grader)
print("====================Retrieval Grader Ender==============")