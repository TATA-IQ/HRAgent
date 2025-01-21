from typing import List, TypedDict

class GraphState(TypedDict):
    """
    Represents the state of Graph
    """
    question: str
    generation: str
    documents: List[str]
    generation_llama: str
    generation_recursive: str
    # document_mxbai: List[str]
    # document_recursive: List[str]