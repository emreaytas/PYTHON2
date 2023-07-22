import pymysql  # mysql.connector yerine bunu kullandık pip install pymysql ile indirebilir ve import ederiz lib klasörüne yerleşir neredeyse her paket gibi.
import datetime

def createTable():  
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        user = "root",        
        database= "schooldb"
    )
    cursor = connection.cursor()
    
    cursor.execute("""
                   
  CREATE TABLE if not exists `schooldb`.`students` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `number` VARCHAR(5) NOT NULL,
  `birthdate` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `number_UNIQUE` (`number` ASC) VISIBLE);
      
           """)
    
    try:
        connection.commit()
    except pymysql.Error as err:
        print("Hata: "+str(err))
    finally:        
        connection.close()  
          
def viewStudents():
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        user = "root",        
        database= "schooldb"
    )   
    cursor = connection.cursor()
    cursor.execute("""
                   select * from students
                   """)
    
    for x in cursor:
        print(f"{x[0]}-{x[1]} {x[2]} {x[4].year}/{x[4].month}/{x[4].day}  ")
    
    try:
        connection.commit()
    except pymysql.Error as err:
        print("Hata: ",err)
    finally:        
        connection.close()    
    
def insertData(name,surname,number,datetime):
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        user = "root",        
        database= "schooldb"
    )
    cursor = connection.cursor()
    sql = """insert into students(name,surname,number,birthdate) values (%s,%s,%s,%s)"""
    
    datas = (name,surname,number,datetime)
    
    cursor.execute(sql,datas)    

    try:
        connection.commit()
    except pymysql.Error as err:
        print("Hata: ",err)
    finally:        
        connection.close()  

    
def insertDatas():
    pass    

def deleteData(number):
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        user = "root",        
        database= "schooldb"
    )
    cursor = connection.cursor()
    
    cursor.execute(f"""delete from students where number = {number}""")
    
     
    try:
        connection.commit()
    except pymysql.Error as err:
        print("Hata: ",err)
    finally:        
        connection.close()  




createTable()

print("Sisteme hos geldiniz...\n")


def menu1():
    print("""
        1-Sisteme giris yap
        2-Ogrenci ekle
        3-Ogrencileri goruntule
        4-Ogrenci sil
        5-Sistemden cikis yap  
          """)

hak = 3

while True:
    
    if hak == 0:
        print("Sistemden atildiniz...")
        break
    
    menu1()
    DD = input("Seciminizi yapiniz: ")
    if DD == '5':
        print("Sistemden cikiliyor.")
        break
    elif DD == '4':
        number = input("Silinecek ogrenci numarasini giriniz: ")
        deleteData(number)
    elif DD == '3':
        viewStudents()
    
    elif DD == '2':
        name = input("Ogrencinin adini giriniz: ")
        surname = input("Ogrencinin soyadini giriniz: ")
        number = input("Ogrencinin numarasini giriniz: ")
        while True:
            if len(number) == 5:
                break
            else:
                input("Ogrencinin numarasini dogru giriniz: ")
        ddyil = int(input("Ogrencinin dogum yilini giriniz: "))
        dday = int(input("Ogrencinin dogum ayini giriniz: "))
        ddgun = int(input("Ogrencinin dogum gunun giriniz: "))
        date = datetime.datetime(ddyil,dday,ddgun,0,0,0)
        insertData(name,surname,number,date)
    
    elif DD == '1':
        TC = input("Tc'nizi giriniz: ")
        sifre = input("Sifrenizi giriniz: ")
        
        if TC != "40708612266" or sifre != "3436":
            hak -= 1
        else:
            hak = 3    
         
        
        
    
    else:
        print("Yanlis bir secenek girdiniz...")
            
print("Sistemden cikildi.")    
    
    
    
    
    










