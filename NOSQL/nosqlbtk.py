
url = "mongodb+srv://emreaytas:"+"34ffm72"+"@cluster0.mq5dsce.mongodb.net/?retryWrites=true&w=majority"

from pymongo.mongo_client import MongoClient
myclient = MongoClient(url)
try:
    myclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


mydb = myclient["node_app"] # önceden var olan bir db olmalı.
mycollection = mydb["collection1"] # önceden var edilmiş bir collection olmalı.

data = {"name":"emre","surname":"aytas"}
x = mycollection.insert_one(data)
print(x)
