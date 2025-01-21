from store.dbstore import DBCreation
db=DBCreation(r"D:/HRAgent/Policies/","http://172.16.0.178:8010")
data=db.create_knowledge()
print(data)