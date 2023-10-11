import pymysql as sql
# if exists   demek eğer varsa demek.
connection = sql.connect(
         host = "localhost",
         password = "12345",
         user= "root",
      ) # önceden oluşmuş bir  database varsa o zaman database = "ismi"  şeklinde bağlantı sağlayabilirdik.

print(connection) # <pymysql.connections.Connection    burada olduğu gibi bağlantı sağlanmış...

cursor = connection.cursor() # bir cursor oluştururuz. komutları yollamak için.
cursor.execute("""CREATE DATABASE if not exists EMRE""") # if not exists demek eğer yoksa oluştur demek.
cursor.execute("USE EMRE") # şu an o database'yi kullanıyoruz. sistemde.

def showDatabases():
    cursor.execute("show databases") # bilgiler cursora yüklenir bizde yazdırırsak eğer bu bilgileri çekmiş oluruz.
    for i in cursor:
        print(i)

# showDatabases()

def createTable():
    sorgu = """create table if not exists table1 (name varchar(100),age integer(10))"""
    cursor.execute(sorgu)
    
createTable()

def updateData(name):
    sorgu = """update table1 set name = '%s' where name = '%s'""" # önce update edilecek tablo sonra set ile değişim olunca neler değişecek belirt. sonra 
    cursor.execute(sorgu,("emre",name))
    connection.commit()

    

# showData()
whereName("emre")


    