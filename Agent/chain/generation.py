from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
os.environ["OPENAI_API_KEY"]="None"
print("============generation chain========")
# llm=ChatOllama(base_url="http://172.16.0.178:8010",model="llama3.2:1b",temperature=0.1)
llm =ChatOpenAI(base_url="http://10.40.0.18:8000/v1",model="meta-llama/Llama-3.2-3B-Instruct")
# template="""You are an HR assistant for helping on HR Policy's. Use the following pieces of retrieved context to answer the question.
# In case if you are getting greet, greet the user.
# Question: {question} 
# Context: {context} 
# Answer:"""#hub.pull("rlm/rag-prompt")
system = """You are a Human Resource (HR) agent. Your task is to answer user questions clearly and understandably based on the provided documents. If the user greets you, respond with a polite and appropriate greeting. Ensure your responses are tailored to address the user's queries comprehensively and professionally."""
human="""
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""
prompt= ChatPromptTemplate.from_messages(
    [
        ("system",system),
        ("human",human),
    ]
)

# prompt=Chat
generate_chain = prompt|llm|StrOutputParser()
print(generate_chain)
print("==========End Generation Chain=======s")