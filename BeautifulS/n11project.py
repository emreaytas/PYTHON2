from bs4 import BeautifulSoup as bs
import json
import requests

site_url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar" # dizüstü bilgisayarlar sekmesi...

html = requests.get(site_url).content

soup = bs(html,'html.parser') # parse etmek istediğimiz içerik ve onun parser tipini belirledik...

liste = soup.find_all("li",{"class":"column"}) # classı column olan li'leri aldık...
 
for li in liste:
    name = li.div.a.h3.text.strip() # sırası ile tek tek içeri girerek bilgiyi çektik... strip ile bolşukları sildik...
    link = li.div.a.get("href") # a etiketi içerisinden get ile href yani link aldık...
    fiyat = li.find("div",{"class":"proDetail"}).find_all("a")[0] 
    newfiyat = li.find("div",{"class":"proDetail"}).find_all("a")[1]
     
    print(f"{fiyat} -> {newfiyat}")

