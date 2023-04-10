from bs4 import BeautifulSoup as bs
import json
import requests

top250url = "https://www.imdb.com/chart/top/" # urlmizi yolladık.
sayfakaynagi = requests.get(top250url).content # tüm sayfa kaynagini elde etmis olduk...
soup = bs(sayfakaynagi,'html.parser') # tüm etiketlere ulaşabileceğiz...

deger = int(input("Ilk kac filmi gormek istersiniz: "))

liste = soup.find('tbody',{"class":"lister-list"}).find_all("tr",limit=deger) # tek bir body geldi ve içersindeki tüm tr etikeleri geldi...#finf ile tek bir tane bulabiliriz ama hangisini istediğimizide belirtebiliriz... 

#find_all("tr",limit = 10 veya 20) falan dersek eğer limite göre ilk sıradan getirir sayılı şekilde getirir. bu durumda mesela ilk kac tane gelecek belirleyebiliriz...
sayi = 1
for tr in liste:
    title = tr.find('td',{"class":"titleColumn"}).find("a").text # tr içerisinden td'lerden classı title olanın a etiketini alacaz ve onun içindende yazı kısmını alacağız...
    year = tr.find('td',{"class":"titleColumn"}).find("span").text.strip("()") # strip ile silinicek karakterleri koyabiliriz...
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text 
    if sayi < 10:
        print(f"{sayi} -film: {title.ljust(60)} yil: {year} degerlendirme: {rating}") # ljust ile boşluklarla tamamlama yaparız... böylece sonrasına gelecek olan değerler sırası düz hizada dizilecekler... ljust boşluklar ile tamamlama yapar...
    else:
        print(f"{sayi}-film: {title.ljust(60)} yil: {year} degerlendirme: {rating}") # ljust ile boşluklarla tamamlama yaparız... böylece sonrasına gelecek olan değerler sırası düz hizada dizilecekler... ljust boşluklar ile tamamlama yapar...
    sayi += 1
    
    




