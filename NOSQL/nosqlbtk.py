from pymongo import MongoClient
url = "mongodb://localhost:27017/"


from pymongo.mongo_client import MongoClient
myclient = MongoClient(url)
try:
    mydb = myclient["node_app"] # önceden var olan bir db olmalı.
    mycollection = mydb["collection1"] # önceden var edilmiş bir collection olmalı.,
    myquery = {"name":"emre"}
    data = {"name":"mercedes","surname":"amg"}
    
     
    veriler = mycollection.find(myquery,{"_id":0})
    for i in veriler:
        print(i)
        
        

except Exception as e:
    print(e)

