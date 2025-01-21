from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field

from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"]="None"
class RouteQuery(BaseModel):
    datasource: Literal["vectorstore"]= Field(
        description="Given a user question choose to route it to web search or a vectorscore"
    )

# llm=ChatOllama(base_url="http://172.16.0.178:8010",model="llama3.2:1b",temperature=0.1)
llm =ChatOpenAI(base_url="http://10.40.0.18:8000/v1",model="meta-llama/Llama-3.2-3B-Instruct")
structure_llm_router=llm.with_structured_output(RouteQuery)

system="""
You are an expert at routing user question to a vectorstore or web search.
The vectorstore contain the document related to agents, prompt engineering and adversarial attacks
Use vectorstore for question on these topics. For all else, use web search
"""

route_prompt=ChatPromptTemplate.from_messages([
    ("system",system),
    ("human","{question}")
])

question_router=route_prompt|structure_llm_router