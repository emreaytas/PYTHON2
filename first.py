import sqlite3 as sql
import time

def create_table():
    conn = sql.connect("ders.db")
    cursor = conn.cursor()
    cursor.execute('create table if not exists users (id int primary key,name text,lastname text,username text,password text)')

    conn.commit()
    conn.close()

def insert(name,lastname,username,password):
    conn = sql.connect("ders.db")
    cursor = conn.cursor()
    
    addcommand = """insert into users(name,lastname,username,password) values{}"""
    data = (name,lastname,username,password)
    cursor.execute(addcommand.format(data)) 
    
    conn.commit()
    conn.close()

def printall():
    conn = sql.connect("ders.db")
    cursor = conn.cursor()
    
    cursor.execute("select * from users")
    listall = cursor.fetchall()
    for a in listall:
        print(a)
    
    conn.close() 
    
def updatepassword(username,newpassword):
    conn = sql.connect("ders.db")
    cursor = conn.cursor()
    
    updatecommand = """"update users set password = '{}' where username = '{}' """ # eğer gelecek değer str ise o zaman parantezler tırnak içerisine alınmalıdır. ama int değer ise o zaman olmaz. gerek yok denebilir hatta.
    cursor.execute(updatecommand.format(newpassword,username))
          
    conn.commit()
    conn.close()

def loginmenu(user):
    print(f"""
          {user[1]} {user[2]} {user[3]}
          
          1 - Bir kullanici ara
          2 - tum kullanicilari yazdir
          3 - hesabimi sil
          4 - cikis yap 
        
          """)



def deleteaccount(username): 
    conn = sql.connect("ders.db")
    cursor = conn.cursor()
    
    dltcommand = """delete from users where username = '{}' """ # sadece sayılar için tırnaksız olarak süslü parantez koyarız.
    cursor.execute(dltcommand.format(username))
     
    conn.commit()
    conn.close()

def deletetable():
    conn = sql.connect("ders.db")
    cursor = conn.cursor()
    
    cursor.execute("""drop table users""") 
     
    conn.commit()
    conn.close()


def searchuser(username):
    conn = sql.connect("ders.db")
    cursor = conn.cursor()
    
    srcommand = """select * from users where username = '{}' """
    cursor.execute(srcommand.format(username))
    user = cursor.fetchone()
    
    #commite gerek yok...
           
    conn.close()
    
    return user

create_table()

def printmenu():
    
    print("""
         1 - Giris yap
         2 - Kaydol
         3 - Kapat   
         """)

while True:
    
    printmenu()
    
    secim = input("\nYapacaginiz islemi giriniz: ")
    
    if secim == "1":
        username = input("Kullanci adi giriniz: ")
        password = input("Sifrenizi giriniz: ")
        search = searchuser(username)
        if search == None: # eğer bu eleman yoksa None dönecek...
            print("Böyle bir kullanici yok...")
            continue
        if password == search[4]:
            print("giris basarili...")
            while True:
                loginmenu(search)
                islem = input("Yapmak istediginiz islemi giriniz: ")
                if islem == "1":
                    u = input("Kullanici adini giriniz: ")
                    birisi = searchuser(u)
                    
                    if birisi == None:
                        print("Boyle bir kullanici yok")   
                        continue
                    
                    print(f"{birisi[1]} {birisi[2]} {birisi[3]}")
                    
                elif islem == "2":
                    printall()
                
                elif islem == "3":
                    
                    deleteaccount(username)
                    time.sleep(1)
                
                elif islem == "4":
                    print("Cikis yapiliyor.")
                    time.sleep(1)
                    break
                else:
                    print("Hatali islem...")
                    time.sleep(1)
            
    elif secim == "2":
        name = input("İsminizi giriniz: ")
        lastname = input("Soyisminizi giriniz: ")
        username = input("Kullanici adinizi giriniz: ")
        user = searchuser(username)
        if user != None:
            print("Böyle bir kullanici zaten var...")
            continue
        password = input("Sifrenizi giriniz: ")
        
        insert(name,lastname,username,password)
        print("\nKayit basarili...\n")         
        
        
        
    elif secim == "3":
        break
    else:
        print("Hatali islem...")
        time.sleep(1)

print("İslemler bitti...")
deletetable()


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

# mesela select *,* from students dedik bize gelen her veri ('emre','aytas','20','emre','aytas','20') olarak gelir her bir veri içeriği ile bir tane tupple içerisinde gelir.
# select * from sqlite_master where type = 'table' # tipi tablo olanları aldık...

# cursor() ile bir imleç oluşturmamızın sebebi şudur = istediğimiz sorguları bağlantıya yani db'ye yollayabilmek için.

'''
create table if not exists users(id int primary key, name text,surname text) # gibi bir yapı ile kurarız. users() yaparak tablonun yapsını () arasında belirleriz.  

'''
# eğer bir değer primary key ise o zaman atama yapmaya illaki gerek yok otomatik olarak artan bir atama olacak örneğin id int primary key olursa her veri geldiğinde sıralı olarak dizilecek.
# bir diğer husus ise mesela bir id var primary key otomatik olarak artmasını istiyoruz o zaman insert into users(name,surname,username,password) values('emre','aytas','emreaytas','12345') olarak ekleme yapmamız users() kısmında onu boş bırakmamız gerekir. 

# conn.commit() ile verdiğimiz sorguları geçerli hale getiririz. işlem veritabanına gider.
# conn.close() ile ise bu bağlantıyı kapatırız.

# drop table tablename ile bir tablo sileriz.
# drop table if exists tablename # yaparsak eğer bu eğer o tablo varsa sil demektir. if not exists olursa yoksa demek if exists demek ise eğer varsa demek. 

# drop table if exists users ile eğer users tablosu varsa o tabloyu sileriz.

# cursor.executemany(addcommand,datas) # ile sırası ile birden fazla işlem yaptırabiliriz.

# cursor = conn.cursor()    cursor.execute() ile ise komutları verebiliriz.

# update tablename set name = "emre",lastname = "ford"... where koşul. yapısı ile güncelleme yapabiliriz..
                        # set age = age + 1 dersek eğer elde olan değer üzerinden işlem yapabiliriz.

# addcommandda str gelecekse '{}' ama int vs ise {} kullanırız.

# delete from tablename where kpşul yapısı ile silme yapacağız. or ve and kullanabiliriz. direkt olarak sağlanan koşuldaki satırı silecek.

# sorgu verdikten sonra cursor.fetchall() ile tüm verileri bir array içersinde alırız. bunu return eder bu yüzden atama yapmamız lazım. fecthone() ile ise tek tek return ederiz değerleri ama array içerisinde döndürmez direkt olarak değeri dönderir.

# fetchmany(sayi) ile istenen kadarını return ederiz bir array içerisinde 0 verirsek sayiya o zaman hepsini bir array içerisinde return eder. eğer verilen sayı eleman sayısından fazla ise sorun yok hepsini bir array içerisinde dönderir. 

# rowid ile biz satırların numaralarını alabiliriz. buda bir sutundur. 

# executemany() ile değerler atamak istersek eğer .... addcommand = """insert into calisanlar(name,lastname,age)  values(?,?,?)""" yapmamız lazım ? işareti her seferinde yeni gelecek olan değerin yerine geçecek.
 
# where name in ('emre','ford','msutang','focus') olursa eğer namenin bu tupple içerisinde olanları kabul edecek.

# from math import * dersek eğer math.sqrt yapmamıza gerek kalmaz modüldeki her şeyi direkt olarak kullanabiliriz.

# sqlde bir şey ararız select * from where ile eğer veri olmazsa None olur...

# if exists eğer varsa demek if not exists ise eğer yoksa demek. eğer primary keye mesela int primary keye değer vermezsek otomatik olarak atran bir yapı kurar kendisine NULL olarak bırakmaz...

# eğer select * from users where name = '{name}' olarak bir sorgu gönderir ve user1 = cursor.fetchone() yaparsak ve o değer yoksa o zaman user None olacak...





















