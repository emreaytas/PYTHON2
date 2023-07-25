import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017") # yerel sunucumuza bağlanmak istiyoruz.   copy connection string ile işlem yaparız aslında direkt olarak.

mydb = myclient["node_app"] # client ile databaseye
mycollection = mydb["collection1"] # database ile collectiona bağlanırız.
result1 = mycollection.find_one() # ilk veriyi bize getirir.
print(result1) # ilk kaydı bize getirdi.
result2 = mycollection.find() # bir filtre sorgusu yollamazsak tüüm verileri getirir. select * from gibi.
print(result2) # tüm verileri getirdi. filtreleme yapmazsak. 


for i in result2: # tüm kayıtları getirir böylece.
    print(i)
for i in mycollection.find({},{"_id":0,'name':1,"price":1}): # 0 olan fieldsler getirilmez 1 olanlar getirilir. True False mantığı aslında.  "_id" field'si gelmeyecek böylece.   ilk {} tüm kayıtları ara demek ikinci {} içindekiler ile ise kolon seçimi yaparız. 
    print(i)
 






