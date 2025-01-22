from typing import Any, Dict
from Agent.chain.enhance_query import enhance_chain
from Agent.state import GraphState
def generate_query(state: GraphState):
    print("*******************Node : Generate More Query**************")
    print(state)
    question=state['question']
    
    # documents_llama=state['document_llama']
    # documents_maxbai=state['document_mxbai']
    # documents_recursive=state['document_recursive']
    # documents= documents_llama+documents_maxbai+documents_recursive
    generation= enhance_chain.invoke({"question":question})
    print("**********8")
    print(generation.Question)
    print(type(generation.Question))
    return {"question":",".join(generation.Question)}
