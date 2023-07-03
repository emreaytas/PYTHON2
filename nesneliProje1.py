import json as jsn
import time as tm
import sqlite3 as sql

def createTable():
    conn = sql.connect("nesneliProje.db")
    cursor = conn.cursor()
    
    cursor.execute("""
                   create table if not exists system(
                       name TEXT,
                       surname TEXT,
                       
                       
                   )
                   
                   """)
    
class Person():
    def __init__(self):
        
        self.name = input("Plase enter new person's name: ")
        self.name = input("Plase enter new person's surname: ")
        age = None
        while True:
            try:
                age = int(input("Plase enter new person's age: "))
                while (age < 18) or (age > 65):
                    age = int(input("Plase enter new person's age: "))
                break    
            except:
                print("We have a problem...")  
        self.age = age        
        
            
class System():
    def __init__(self):
        self.active = True
        
        pass        
    
person1 = Person()



while True:
    pass
     
     
     
print("Exiting...")        
tm.sleep(1.45)
print("Exited the system...")    
    
    
    
    