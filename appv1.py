
from Agent.graph import  app
# ingest=Ingestion()
# ingest.load_data()
if __name__=='__main__':
    print("===RagFlow===")
    print(app.invoke(
        input={"question": "who is the vp of tata insights and quants ?"}
    ))