
url = "mongodb://localhost:27017/"

from pymongo.mongo_client import MongoClient
myclient = MongoClient(url)
try:
    mydb = myclient["node_app"] # önceden var olan bir db olmalı.
    mycollection = mydb["collection1"] # önceden var edilmiş bir collection olmalı.
    print(myclient.list_database_names())
    
except Exception as e:
    print(e)

