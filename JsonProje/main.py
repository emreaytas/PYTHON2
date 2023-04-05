import json
import os
class User():
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
    
       
class UserRepository():
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
    #load users from .json file
        self.loadUser()
    
    def loadUsers(self):
        if os.path.exists("Datas.json"): # eğer bu dosya varsa o zaman True verecek...
            with open("Datas.json","r",encoding="utf-8") as file:
                users = json.load(file) # tüm bilgileri alacağız her nesne bir dict halinde ama string dict halinde gelecek.ve hepsi bir liste içerisinde gelecek.
                for user in users:
                    user = json.loads(user) # loads ile biz string dict olan json verisini dict haline getirebildik.
                    print(user["username"]+" "+user["email"])
                    newUser = User(username=user["username"],password=user["password"],email=user["email"]) # dict hale gelen nesneyi tekrar nesne haline getirdik.
                    self.users.append(newUser)
                #print(self.users)
                
                     
    def register(self, user:User): # gelecek olan verinin User tipinde olacağını belirtiriz bu yapı ile.
        self.users.append(user)
        self.saveToFile()
        print('kullanici olusturuldu...')
    
    def login(self,username,password):
        if self.isLoggedIn:
            print("Zaten login oldunuz...")
        else:
            for user in self.users:
                if user.username == username and user.password == password:
                    self.isLoggedIn = True
                    self.currentUser = user
                    print("Login yapildi...")

    def saveToFile(self):
        liste = []
        for user in self.users:
            liste.append(json.dumps(user.__dict__)) # user.__dict__ ile biz aslında bir nesneyi dict yapısına çevirdik. böylece dumps için kullanılacak hale getirdik... yoksa class ile direkt olarak işlem yapamazdık.
    
        with open('Datas.json',"w") as file: # her şeyi siler ve biz elde olanları sıfırdan yazdıracağız. 
            json.dump(liste,file) # dump ile jsona yazdırma yapacağız. ve biz buna bir liste içinde classlar olarak yolladık. dumps ise jsona uygun hale getirir. 
    
    def logOut(self):
        self.isLoggedIn = False
        self.currentUser = {}        
        print("Cikis basarili...")
    
    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser["username"]}')
        else:
            print("Giris yapilmamis...")    
            
repository = UserRepository()

while True:
    print("MENU".center(50,'*'))
    print("")
    secim = input("1-Register \n2-Login\n3-Logout\n4-Identy\n5-Exit\n\nPlase enter your choose: ")
    if secim == '5':
        break
    elif secim == '4':
        repository.identity()
    elif secim == '3':
        repository.logOut()
    elif secim == '2':
        username = input("Kullanici adini giriniz: ")
        password = input("Parola giriniz: ")
        repository.login(username,password)
        
    elif secim == '1':
        username = input("Kullanici adini giriniz: ")
        password = input("Parola giriniz: ")
        email = input("E mail giriniz: ")
        user = User(username,password,email) # user = User(username = username,password=password,email = email) bu şekilde de istenen bölüme istenen değeri direkt olarak atayabiliriz ama klasil çalışmada default olarak sırası ile kabul eder.
        repository.register(user)
        print("kullanici olustu...\n")
    else:
        print("Wrong choose...\n")
        continue
    
    