from store.dbstore import DBCreation
import multiprocessing as mp
def fun_execute(fn):
    fn()
if __name__ == "__main__":
    db=DBCreation(r"D:/HRAgent/Policies/","http://172.16.0.178:8010")
    with mp.Pool(processes=3) as pool:
            # Use map to apply the function to each element of the list
        results = pool.map(fun_execute, [db.create_knowledge_semantic_llama()])

