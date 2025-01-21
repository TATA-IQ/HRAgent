from typing import Any, Dict
from Agent.chain.generation import generate_chain
from Agent.state import GraphState
def generate_llama(state: GraphState):
    print("*******************Node : Generate**************")
    print(state)
    question=state['question']
    documents=state['documents']
    # documents_llama=state['document_llama']
    # documents_maxbai=state['document_mxbai']
    # documents_recursive=state['document_recursive']
    # documents= documents_llama+documents_maxbai+documents_recursive
    generation= generate_chain.invoke({"context":documents,"question":question})
    print("**********8")
    print(generation)
    return {"documents":documents, "question":question, "generation_llama":generation}
def generate_recursive(state: GraphState):
    print("*******************Node : Generate**************")
    question=state['question']
    documents=state['document']
    # documents_llama=state['document_llama']
    # documents_maxbai=state['document_mxbai']
    # documents_recursive=state['document_recursive']
    # documents= documents_llama+documents_maxbai+documents_recursive
    generation= generate_chain.invoke({"context":documents,"question":question})
    return {"documents":documents, "question":question, "generation_recursive":generation}