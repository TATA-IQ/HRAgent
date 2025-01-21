from typing import  Any, Dict

from typer.cli import state

from Agent.state import GraphState
from Agent.ingestor.load_ingestor import LLAMAIngestor, MaxbaiIngestor, RecurssiveIngestor

class StateRetrieveLLAMA():
    def __init__(self,persist_dir,collection_name):
        self.ingestor=LLAMAIngestor(persist_dir,collection_name)
        self.ingestor_retieve=self.ingestor.data_ingestor()
    def retrieve(self,state: GraphState):
        print("*******************Node : Retrieve**************")
        print("----Retrieve----")
        print(state)
        question = state['question']
        documents=self.ingestor_retieve.invoke(question)
        # print(documents)
        return  {"documents":documents, "question":question} 
class StateRetrieveMaxbai():
    def __init__(self,persist_dir,collection_name):
        self.ingestor=MaxbaiIngestor(persist_dir,collection_name)
        self.ingestor_retieve=self.ingestor.data_ingestor()
    def retrieve(self,state: GraphState):
        print("*******************Node : Retrieve**************")
        print("----Retrieve----")
        print(state)
        question = state['question']
        documents=self.ingestor_retieve.invoke(question)
        return  {"document":documents, "question":question} 

class StateRetrieveRecursive():
    def __init__(self,persist_dir,collection_name):
        self.ingestor=RecurssiveIngestor(persist_dir,collection_name)
        self.ingestor_retieve=self.ingestor.data_ingestor()
    def retrieve(self,state: GraphState):
        print("*******************Node : Retrieve**************")
        print("----Retrieve----")
        print(state)
        question = state['question']
        documents=self.ingestor_retieve.invoke(question)
        return  {"document":documents, "question":question} 