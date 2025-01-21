from langchain_chroma import Chroma
from Agent.ingestor.embedders import Embedders
class LLAMAIngestor():
    def __init__(self,persist_dir,collection_name):
        self.persist_dir=persist_dir
        self.collection_name=collection_name
        self.embedding=Embedders.LLamaEmbeders()
    def data_ingestor(self):
        retriever=Chroma(
            collection_name=self.collection_name,
            persist_directory=self.persist_dir,
            embedding_function=self.embedding

        ).as_retriever()  
        return retriever  

class MaxbaiIngestor():
    def __init__(self,persist_dir,collection_name):
        
        self.persist_dir=persist_dir
        self.collection_name=collection_name
        self.embedding=Embedders.mxbaiEmbeders()
    def data_ingestor(self):
        retriever=Chroma(
            collection_name=self.collection_name,
            persist_directory=self.persist_dir,
            embedding_function=self.embedding

        ).as_retriever()  
        return retriever  

class RecurssiveIngestor():
    def __init__(self,persist_dir,collection_name):
        
        self.persist_dir=persist_dir
        self.collection_name=collection_name
        self.embedding=Embedders.mxbaiEmbeders()
    def data_ingestor(self):
        retriever=Chroma(
            collection_name=self.collection_name,
            persist_directory=self.persist_dir,
            embedding_function=self.embedding

        ).as_retriever()  
        return retriever  
