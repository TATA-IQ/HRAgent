from langchain import hub
from typing import List
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import RunnableSequence
import os
os.environ["OPENAI_API_KEY"]="None"
print("============generation chain========")
# llm=ChatOllama(base_url="http://172.16.0.178:8010",model="llama3.2:1b",temperature=0.1)
llm =ChatOpenAI(base_url="http://10.40.0.18:8000/v1",model="meta-llama/Llama-3.2-3B-Instruct")
class QuestionExtracter(BaseModel):
    Question:List[str]= Field(description="Get the Contexts only")
    # grader: str= Field(description="If LLM generation 1 is better say LLAMA, if LLM generation2 is better say recursive")
structured_llm=llm.with_structured_output(QuestionExtracter)
# template="""You are an HR assistant for helping on HR Policy's. Use the following pieces of retrieved context to answer the question.
# In case if you are getting greet, greet the user.
# Question: {question} 
# Context: {context} 
# Answer:"""#hub.pull("rlm/rag-prompt")
system = """You are a Human Resource (HR) agent. Your task is to answer user questions clearly and understandably based on the provided documents. If the user greets you, respond with a polite and appropriate greeting. Ensure your responses are tailored to address the user's queries comprehensively and professionally."""
human="""
Given Context from the user just Generate synthetically the same context in 5 different way, so that it can help us in retriving the document. Do not put any extra information
Question: {question} 
Context: {question}
Answer:
"""
prompt= ChatPromptTemplate.from_messages(
    [
        ("system",''),
        ("human",human),
    ]
)

# prompt=Chat
enhance_chain: RunnableSequence = prompt|structured_llm#|StrOutputParser()
print(enhance_chain)
print("==========End Generation Chain More query=======s")