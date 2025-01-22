from langchain.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_text_splitters import RecursiveCharacterTextSplitter

import ollama
import os
from tqdm import tqdm
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings

class DBCreation():
    def __init__(self,folder_path,url):
        self.folder_path=folder_path
        self.embedding=SpacyEmbeddings(model_name="en_core_web_sm")#OllamaEmbeddings(model="llama3.2:1b",base_url=url)
        # self.embedding2=OllamaEmbeddings(model="mxbai-embed-large",base_url=url)
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
    def create_sementic_data_spacy(self):
        alldocs=self.load_files()
        
        
        semanticchunker=SemanticChunker(self.embedding, breakpoint_threshold_type="percentile")
        print("=======chunk creation=========")
        chunks=semanticchunker.create_documents([doc.page_content for doc in tqdm(alldocs)])
        print("=="*19)
        # print(chunks.shape)
        print("**"*19)
        modified_chunks=[]
        for ch in chunks:
            try:
                if ch.page_content=="":
                    pass
                else:
                    modified_chunks.append(ch.page_content)
            except:
                print(ex)
        return modified_chunks
    
    def create_knowledge_semantic_spacy(self,db_name="knowledgespacy"):
        # collection=self.db.create_client()
        # chunks=self.create_sementic_data()
        chunks=self.create_sementic_data_spacy()
        print("========embedding creationon llama==============")
        # print(chunks)
        # for  i,d in tqdm(chunks):
        #     response = self.embedding.embeddings(model="mxbai-embed-large", prompt=d)
        #     embedding = response["embedding"]
        # print(self.db_name)
        print(len(chunks))
        chroma_db = Chroma.from_texts(
                        texts=chunks[:99],
                        embedding=self.embedding, 
                        persist_directory=db_name, 
                        collection_name="demospacy"
                    )
        print("=====Spacy data created=======")
        retriver_test=chroma_db.as_retriever().get_relevant_documents("finance vice persident of tata insights and quants")
        print("==============Test======")
        print(retriver_test)
    

    







