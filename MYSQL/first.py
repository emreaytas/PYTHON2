import pymysql as sql
# if exists   demek eğer varsa demek.
connection = sql.connect(
         host = "localhost",
         password = "12345",
         user= "root",
      ) # önceden oluşmuş bir  database varsa o zaman database = "ismi"  şeklinde bağlantı sağlayabilirdik.

print(connection) # <pymysql.connections.Connection    burada olduğu gibi bağlantı sağlanmış...

# tablo oluşturma...

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


def showTables():
    cursor.execute("show tables")
    for i in cursor:
        print(i) 

# showTables()           

def addData(name,age):
    # verileri bir tuple içerisinde vermeliyiz.
    veriler = (name,age)
    sorgu = """insert into table1(name,age) values(%s,%s)""" # istersek name age yazmazdık hepsi sırası ile veri alırdı içine. ama eğer boş yer bırakmak istersek falan o zaman sırası ile hangi veriler girilecek belli ederiz.    
    # %s demek gelecek verinin yeri demektir.
    cursor.execute(sorgu,veriler)
    connection.commit() # commit'leme yaparız böylece veriler databaseye gönderilir. göndermezsek cursorda kalır.
    