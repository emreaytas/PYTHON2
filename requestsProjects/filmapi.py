# themoviedb.org = film ve dizi arşivi...
# themoviedb'nin sunduğu apiyı  kullanacağız... hesaba kayıt olarak api kısmını kullanabiliriz...
# anahtar kelimeye göre arama yapacağız...
# en popüler film listesi...
# vizyondaki film listesi...


# BİR APİ ANAHTARI OLUŞTURDUK 2c10770efcff92fbfccfc7cde579faad GİBİ...
# MESELA BİR APİ ÖRENEĞİ https://api.themoviedb.org/3/movie/550?api_key=2c10770efcff92fbfccfc7cde579faad   ... BU ŞEKİLDE BİZ ANAHTARI KULLANABİLECEĞİZ...
import json 
import requests

class theMovieDB():
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "2c10770efcff92fbfccfc7cde579faad"
        
    def getPopulars(self):
        response = requests.get(self.api_url+"movie/popular?api_key="+self.api_key+"&language=en-US&page=1")
        response = response.json()
        return response
    

themovie = theMovieDB()


while True:
    secim = input("1-Popular movies\n2-Exit\n\n what's your selection: ")
    if secim == "2":
        print("Exiting the system...")
        time.sleep(1)
    elif secim == "1":
        
        
    
    else:
        print("\nWrong selection...\n")