#api.github.com bu aslında github tarafaından oluşturulmuş vw bir çok veriye ulaşabilmemizi sağlayan api'dir.
#api.github.com/users/username(mesela emreaytas gibi) bunu yololayınca bilgilerin hepsini getiriyor. 
"""
     {
  "login": "emreaytas",
  "id": 111369656,
  "node_id": "U_kgDOBqNduA",
  "avatar_url": "https://avatars.githubusercontent.com/u/111369656?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/emreaytas",
  "html_url": "https://github.com/emreaytas",
  "followers_url": "https://api.github.com/users/emreaytas/followers",
  "following_url": "https://api.github.com/users/emreaytas/following{/other_user}",
  "gists_url": "https://api.github.com/users/emreaytas/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/emreaytas/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/emreaytas/subscriptions",
  "organizations_url": "https://api.github.com/users/emreaytas/orgs",
  "repos_url": "https://api.github.com/users/emreaytas/repos",
  "events_url": "https://api.github.com/users/emreaytas/events{/privacy}",
  "received_events_url": "https://api.github.com/users/emreaytas/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Emre Aytaş",
  "company": null,
  "blog": "",
  "location": "Kocaeli Universty",
  "email": null,
  "hireable": null,
  "bio": "Computer Engineering - Kocaeli University",
  "twitter_username": "Emreayts_",
  "public_repos": 3,
  "public_gists": 0,
  "followers": 12,
  "following": 20,
  "created_at": "2022-08-16T14:38:00Z",
  "updated_at": "2023-04-02T18:05:28Z"
}
""" # api.github.com/users/emreaytas(user) ile biz bu verilere bir dict içersinde ulaştık aslında bir json string ve biz bunu json kütüphanesi ile dict haline çevireceğiz... bu bilgiler pıuıblic bilgilerdir. ancak kendi hessabımız üzerinde bir repo oluşturmak vs istersek eğer o zaman izin vermek lazım bir kullanıcı giriş işlemleri çeitleri var biz token bilgisi ile işlem yapacağız. 

# token oluşturmak için ise settings - developer settings kısmından personal acsess token kullanacağız tokeni kullanacağız böylece griiş yapmış gibi olacak ve hesabın içerisindeki özel bilgilere vs ulaşabileceğiz ve işlem yapabileceğiz...
# generate new token dediğimiz zaman çıkan sistemde o token ile hangilerine ulaşabileceğiz seçebiliriz. tokenler ile o hesabın izin verilen işlemlerini yapabiliriz...

#api.gihtub.com/users/emreaytas(kullaniciadi)/followers ile takipçileri görürüz...


""" 
import requests
import json

result = requests.get("https://api.github.com/users/emreaytas")
result1 = result.text
result2 = json.loads(result1) #loads ile biz json string olan verideki dict yapısını çektik. ve bir dict haline getirdik...
print(result2)
print(result2["bio"]) #dict üzerinden bio'da ne yazdığını aldık...
print(result2["followers_url"]) # bu ise bize followers linkini dönndürür(https://api.github.com/users/emreaytas/followers). böylece bir uygulamada istenen sayfalar arasında bu şekilde geçiş yapabiliriz.
print(result2["followers"]) # kaç tane takipçisi var görebiliriz.
print(result2["following"]) # kaç kişiyi takip ediyor görebiliriz...
print(result2["repos_url"]) # https://api.github.com/users/emreaytas/repos" bunu return eder... böylece repolara ulaşabiliriz...
"""

import requests
import json
import time

class Github():
    def __init__(self):
        self.api_url = "https://api.github.com"
        
    def getUser(self,username):
        response = requests.get(self.api_url+"/users/"+username) # böylece biz kullanicinin bilgilerini api ile aldık text sonra loads ile bilgiler bir dict içerisnde olacak..
        return response.json() # bu şekilde gelen bilgiyi biz direkt olarak dict hale gelecek pythondaki .json() sayesinde...
    
        
            


while True:
    secim = input("1-Find user\n2-Get Repository\n3-Create Repository\n4-Exit\n\n what's your selection: ")
    if secim == "4":
        print("Exiting the system...")
        time.sleep(1)
    elif secim == "1":
        pass
    elif secim == "2":
        pass
    elif secim == "3":
        pass
    else:
        print("\nWrong selection...\n")
            


