from langchain.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_text_splitters import RecursiveCharacterTextSplitter

import ollama
import os
from tqdm import tqdm
class DB():
    def __init__(self,dbname):
        self.db_name=dbname
    def create_client(self):
        client = chromadb.Client()
        collection = client.create_collection(name=self.db_name)
        return collection

class DBCreation():
    def __init__(self,folder_path,url):
        self.folder_path=folder_path
        self.embedding=OllamaEmbeddings(model="llama3.2:1b",base_url=url)
        self.embedding2=OllamaEmbeddings(model="mxbai-embed-large",base_url=url)
        # self.db_name=dbname
        # self.db=DB(dbname)
    def load_files(self):
        files=os.listdir(self.folder_path)
        resultantpdf=[]
        print("====Loading files====")
        for fil in tqdm(files):
            if ".pdf" in fil:
                path=os.path.join(self.folder_path,fil)
                loader=PyPDFLoader(path)
                resultantpdf.extend(loader.load())
                
        return resultantpdf
    def create_sementic_data_llama(self):
        alldocs=self.load_files()
        
        
        semanticchunker=SemanticChunker(self.embedding, breakpoint_threshold_type="percentile")
        print("=======chunk creation=========")
        chunks=semanticchunker.create_documents([doc.page_content for doc in tqdm(alldocs)])
        print("=="*19)
        # print(chunks.shape)
        print("**"*19)
        return chunks
    def create_sementic_data_mxbai(self):
        alldocs=self.load_files()
        
        
        semanticchunker=SemanticChunker(self.embedding2, breakpoint_threshold_type="percentile")
        print("=======chunk creation=========")
        chunks=semanticchunker.create_documents([doc.page_content for doc in tqdm(alldocs)])
        print("=="*19)
        # print(chunks.shape)
        print("**"*19)
        return chunks
    def create_normal_data(self):
        alldocs=self.load_files()
        
        
        text_splitter = RecursiveCharacterTextSplitter(
                                                chunk_size=300,
                                                chunk_overlap=100,
                                                length_function=len,
                                                is_separator_regex=False,
                                            )
        print("=======chunk creation=========") 
        chunks= text_splitter.create_documents([doc.page_content for doc in tqdm(alldocs)])
        # chunks=semanticchunker.create_documents([doc.page_content for doc in tqdm(alldocs)])
        print("=="*19)
        # print(chunks.shape)
        print("**"*19)
        return chunks    
    def create_knowledge_semantic_llama(self,db_name="hrpolicyllama"):
        # collection=self.db.create_client()
        # chunks=self.create_sementic_data()
        chunks=self.create_sementic_data_llama()
        print("========embedding creationon llama==============")
        # print(chunks)
        # for  i,d in tqdm(chunks):
        #     response = self.embedding.embeddings(model="mxbai-embed-large", prompt=d)
        #     embedding = response["embedding"]
        # print(self.db_name)
        chroma_db = Chroma.from_documents(
                        documents=chunks,
                        embedding=self.embedding, 
                        persist_directory=db_name, 
                        collection_name="tataiq_hrpolicy_demollama"
                    )
        print("=====LLAMa data created=======")
    def create_knowledge_semantic_mxbai(self,db_name="hrpolicymxbai"):
        # collection=self.db.create_client()
        # chunks=self.create_sementic_data()
        chunks=self.create_sementic_data_mxbai()
        print("========embedding creationon mxbai==============")
        # print(chunks)
        # for  i,d in tqdm(chunks):
        #     response = self.embedding.embeddings(model="mxbai-embed-large", prompt=d)
        #     embedding = response["embedding"]
        # print(self.db_name)
        chroma_db = Chroma.from_documents(
                        documents=chunks,
                        embedding=self.embedding2, 
                        persist_directory=db_name, 
                        collection_name="tataiq_hrpolicy_demomxbai"
                    )
        
        print("=====Mxbai data created=======")
    def create_knowledge_recursive(self,db_name="hrpolicyrecursive"):
        # collection=self.db.create_client()
        # chunks=self.create_sementic_data()
        chunks=self.create_normal_data()
        print("========embedding creationon recursive==============")
        # print(chunks)
        # for  i,d in tqdm(chunks):
        #     response = self.embedding.embeddings(model="mxbai-embed-large", prompt=d)
        #     embedding = response["embedding"]
        # print(self.db_name)
        chroma_db = Chroma.from_documents(
                        documents=chunks,
                        embedding=self.embedding2, 
                        persist_directory=db_name, 
                        collection_name="tataiq_hrpolicy_demorecursive"
                    )
        print("=====Recursive data created=======")



    







