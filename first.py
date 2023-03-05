names = ["emre","arif","ford","aysa"]
surnames = ["aytas","aytas","focus","liya"]



dict1 = {"emre":"aytas","ford":"focus",6:"dddd",56:24.4,"emre":"dddd"}


users ={
    
    "emre":{
       "isim":"emre",
       "soyisim":"aytas",
       "yas":20
    }
,
    "ford":{
       "isim":"ford",
       "soyisim":"focus",
       "yas":7
    }

}

print(users["emre"]["isim"])
print(users["emre"]["yas"])

users["emre"] = {       "isim":"emre",
       "soyisim":"aytas",
       "yas":31}

for i in users:
    print(i)