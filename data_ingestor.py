from store.dbstore import DBCreation
import multiprocessing as mp

if __name__ == "__main__":
    db=DBCreation(r"D:/HRAgent/Policies/","http://172.16.0.178:8010")
    db.create_knowledge_semantic_spacy()
    