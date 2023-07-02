import json as jsn
import time as tm

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
tm.sleep(1)
    
    
    
    
    