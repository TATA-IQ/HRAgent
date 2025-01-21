#!/usr/bin/env python
# coding: utf-8

# In[1]:


from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
import chromadb
import ollama
import os
from tqdm import tqdm
from langchain_chroma import Chroma
from langchain.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from langchain_text_splitters import RecursiveCharacterTextSplitter


# In[2]:


path=r"D:/HRAgent/Policies/ANTI-BRIBERY AND ANTI-CORRUPTION POLICY OF TATA INDUSTRIES.pdf"


# In[3]:


loader=PyPDFLoader(path)


# In[4]:


resultantpdf=[]


# In[5]:


resultantpdf.extend(loader.load())


# In[6]:


url="http://172.16.0.178:8010"


# In[7]:


embedding=OllamaEmbeddings(model="llama3.2:1b",base_url=url)


# In[8]:


text_splitter = RecursiveCharacterTextSplitter(
                                                chunk_size=250,
                                                chunk_overlap=50,
                                                length_function=len,
                                                is_separator_regex=False,
                                            )
print("=======chunk creation=========") 
chunks= text_splitter.create_documents([doc.page_content for doc in tqdm(resultantpdf)])


# In[ ]:


chroma_db = Chroma.from_documents(
    documents=chunks, 
    embedding=embedding, 
    persist_directory="knowledgebase", 
    collection_name="recursive_embed_knolwdgev1"
)


# In[ ]:


chroma_db.as_retriever().get_relevant_documents("finance vice persident of tata insights and quants")


# In[ ]:


prompt_template = """Use the following pieces of context to answer the question at the end. 
If you do not know the answer, please think rationally and answer from your own knowledge base.
Don't put extra information

{context}

Question: {question}
"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)


# In[ ]:


llm=ChatOllama(base_url=url,model="llama3.2:1b",temperature=0.1)


# In[ ]:


query="finance vp of tata iq?"


# In[ ]:


chain_type_kwargs = {"prompt": PROMPT}
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff", 
    retriever=chroma_db.as_retriever(), 
    chain_type_kwargs=chain_type_kwargs)

print(qa_chain.run(query))


# In[ ]:




