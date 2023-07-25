import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017") # yerel sunucumuza bağlanmak istiyoruz.   copy connection string ile işlem yaparız aslında direkt olarak.


mydb = myclient["node_app"]
mycollection = mydb["collection1"] 

# delete_one() tek bir kayıt siler ilk gelen kayıtı. silmede direkt olarak satır silme gibi document silinir.  delete_many() ile ise çoklu veri silinir.
# içerisine bir koşul vericez ve silme işlemi yapacak.

mycollection.delete_one({"name":"ford"}) # ismi ford olan silinecek. ilk gelen document silinecek tek bir silme yapacak.
result = mycollection.delete_many({"name":"ford","price":5000}) # tüm ismi ford olan ve price 5000 olanlar silinecek
# direkt olarak mycollection.deletemany(...) yapabiliriz ama bir obje dönecek ve o obje ile kaç tanesi silindi vs görebileceğiz. 
print(result.deleted_count) # kaç kayıt silindi gösterir.


