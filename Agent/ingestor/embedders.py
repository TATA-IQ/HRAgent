from langchain_ollama import OllamaEmbeddings
import spacy
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
class Embedders():
    def LLamaEmbeders(model_name="llama3.2:1b",base_url="http://172.16.0.178:8010"):
        llamaembeders=SpacyEmbeddings(model_name="en_core_web_sm")#OllamaEmbeddings(model=model_name,base_url=base_url)
        return llamaembeders
    def mxbaiEmbeders(model_name="mxbai-embed-large",base_url="http://172.16.0.178:8010"):
        maxbaiembeders=OllamaEmbeddings(model=model_name,base_url=base_url) 
        return maxbaiembeders   