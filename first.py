import sqlite3 as sql 

conn = sql.connect("ders.db")
cursor = conn.cursor()

cursor.execute("""select * from calisanlar where ad in('ahmet','emre','ford','bmw')""")
listall = cursor.fetchall()

for calisan in listall:
    print(calisan)
    
    
conn.commit()
conn.close()


"""
import sqlite3 ile hazır bir kütüphane olan sqlite3'ü çağırırız. bunu veritabanı kullanmak için kullanacağız.

conn = sqlite3.connect('ders.db') # böylece var olan veritabanına bağlanacak aynı path üzerinde tabiki. eğer yoksa bu veritabanını oluşturacak. varsa bağlanacak.

veritabanına bağlandıktan sonra onun üzerinde işlemler yapabilmek için bir cursor oluşturmak gerekir. 
    cursor1 = conn.cursor() olarak bunu yapabiliriz.

db işlemlerini bağlanmayı vs biz with open ve as ilede yapabiliriz.

conn.commit() # bunun ile yaptığımız işlemleri kaydettirebiliriz.

conn.close() # bunun ile ise bağlantıyı kesebiliriz. 

cursor1.execute() ile ise sql komutları göndereceğiz. bunun için cursora ihtiyaç var.

CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,SURNAME TEXT,AGE INTEGER)   # if not exists demek eğer varsa elleme yoksa oluştur demektir eğer bunu kullanmazsak ve bu tablo varsa hata verir.

..................
eğer var olan tablo silinsin yenisi oluşturulsun istersek drop table students deriz. ve tablo düşürülür.
.............................................................

cursor1.execute("instert into students values('ali','rrrr','20')") # bu şekilde ise veri eklemesi yapabiliriz.

add_command = "instert into students values('ali','rrrr','20')"
cursor1.execute(add_command) # bunun ile ise parçalara ayırarak işlem yapabiliriz. ve f format ile ise istediğimiz verileri ekleme yapabiliriz.
......................................................................................................................................................

name = input("Adinizi giriniz: ")
surname = input("Soyadinizi giriniz: ")
age = int(input("Yasinizi giriniz: "))

format1 = f"('{name}','{surname}','{age}')"
add_command = f"insert into students values{format1}"
cursor1.execute(add_command)

bu yapi ile istenen verileri alabiliriz.




......................................................................................................................................................

...birden fazla veri ekleme...................................................................................................................................................

datas = [('ali','veli','20'),('mercedes','bmw','6'),('ford','focus','7')]

add_command = "insert into students values{}"

for data1 in datas:
    cursor1.execute(add_command.format(data1))

-------------------------------------------------------------------------------------------- diğer yöntem.

datas = [('ali','veli','20'),('mercedes','bmw','6'),('ford','focus','7')]
add_command = "insert into students values(?,?,?)" # sutun sayisi kadar soru işareti koyacağız.

cursor1.executemany(add_command,datas) # böylece tüm verileri tek seferde ekleyebiliriz.
conn.commit()
    
......................................................................................................................................................


"""

'''
def insertData(name,surname,age):
    con = sqlite3.connect("ders.db")
    cursor = con.cursor()
    
    add_command = """insert into students values{}"""
    
    data = (name,surname,age)
    cursor.execute(add_command.format(data))
    con.commit()
    con.close()
    
''' # eleman ekleme fonksiyonu yazdık...

'''

verileri güncelleme.    
    
import sqlite3 as sql 

conn = sql.connect("ders.db")

cursor1 = conn.cursor()

cursor1.execute("""update students set name = 'Emre',age = '21' where name = 'Emre' and surname = 'aytas'""") # zaten istenen dbye bağlıyız. tablo adı ile direkt olarak işelm yapabiliriz. birden fazla db ilede işlem yapabiliriz sqlite içerisinde bulunan ama bunun için ise conn1 gibi farklı bir bağlantı eklemek lazım.
            # böylece güncelleme olacak.

conn.commit()
conn.close()

rowid ilede işlem yapabiliriz yani satır numarası ile. 

cursor1.execute("""update students set name = 'Emre',age = age + 1 where age > 30""") # age = age + 1 kalıbını kullanabiliriz.      
    
'''

'''

veri silme...

import sqlite3 as sql 

conn = sql.connect("ders.db")

cursor1 = conn.cursor()

cursor1.execute("""delete from students where = surname = 'aytas' or surname = 'AYTAS' """) # delete'de sağlanan koşulda satırı komple siler veriler satır satır tutulur ve direkt satırı silme işlemi uygulanır.
print("Silme islemi basarilidir.")
conn.commit()
conn.close()


'''

'''
import sqlite3 as sql 

def deleteAge(age):
    conn1 = sql.connect("ders.db")
    cursor = conn1.cursor()
    
    deleteCommand = """delete from students where age = {}""" 
    cursor.execute(deleteCommand.format(age))
    conn1.commit()
    conn1.close()

''' # yaşa göre veri silen bir fonksiyon...


'''

tablodaki verileri yazdırma...

import sqlite3 as sql 

conn1 = sql.connect("ders.db")
cursor1 = conn1.cursor()

cursor1.execute("""select * from students""")
tumdegerler = cursor1.fetchall() # fetchall() ile imlecin getirdiği değerleri atarız. bir liste içerisinde getirir bize. imlecin seçtiği elemanları almak için kullanırız.
                      #.fetchone olarak kullanırsak eğer ilk elemanı alır bir daha kullanırsak ikinci satırı alır tıpkı dosyalardaki imleç gibi çalışır.
                         
                      # mesela iki kere cursor1.fecthone() kullandıktan sonra cursor1.fetchall() kullanırsak eğer ilk iki değer hariç tüm hepsini alır değer derken satır yani çünkü verileri satır satır tutar sql... 
                      
                      
                         
print(type(tumdegerler)) # <class 'list'> 

conn1.commit()
conn1.close()

select * from students where not age >= 40 # böylece yaşı 40tan küçük olanları alırız not ile koşulu tersine çeviririz.

....................................................................................

# fetchamny = cursor1.fetchmany(3) # ilk üç satırı bize getirir ilk üç veriyi verir bize. ama eğer içeri sıfır verirsek tüm değerleri getirir. eğer 100 yazarsak ve elde o kadar veri yoksa ne kadar varsa hepsini getirir hata çıkarmadan.

# cursor.execute("""select rowid,* from students""") # rowid dahil hepsini getirir. ama burada dikkat etmemiz gereken bir şey var rowid ve * ile gleen değerler tek bit tuplle içerisinde gelecek. yani her veriyi elde edileni bir tupple içerisinde bize geri sunacak.


'''

'''
def printAll():
    conn1 = sql.connect("ders.db")
    cursor1 = conn1.cursor()

    cursor1.execute("""select * from students""")
    tumdegerler = cursor1.fetchall()
    for satir in tumdegerler:
        print(satir)

    conn1.commit()
    conn1.close()
''' # tüm verileri yazdıran bir fonksiyon.


'''

cursor.execute("""select * from calisanlar where ad in('ahmet','emre','ford','bmw')""") # bu yapı ile birden fazla and koymaya gerek kalmaz bir tuple içerisindeki verilerden getirir. in bu işe yarar içeride olanlara göre verileri getirir. where ad not in('emre','bmw','ford') böyle olursa eğer o zaman bu içeride olmayanları getirecek.

cursor.execute("""select * from calisanlar where maas between 1500 and 3000""") # böylece maasları 1500 ile 3000 olanları bize getirir koşul ifadesi yazmaya gerek kalmaz 1500 ve 3000i dahil etti..

cursor.execute("""select * from calisanlar where ad like 'ah%'""") # ismin baş kısmı ah olanları getirir... '%ah'  olursa sonu ah ile bitenleri arar...  ortada olanları ise '%ah%' ortasında bir yerde ah olanları getirir.
                                                                   # büyük küçük harf ayrımı yapmaz. 
                                                                    
cursor.execute("""select * from calisanlar where ad like 'm___e_' """) # ilk harfi m 4. harfi e olan isme göre değerleri bize getirir.

'''

