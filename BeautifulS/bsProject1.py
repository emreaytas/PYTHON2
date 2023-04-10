htmlbilgisi = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MY NEW SİTE</title>  
</head>
<body>
    <h1>ANA BAŞLIK</h1>
    <div class="grup1">
            <h2>PROGRAMLAMA</h2>
        <li>
            Menu1
        </li>
        <li>
            Menu2
        </li>
        <li>
            Menu3
        </li>
    </div>

    <div class="grup1">
            <h2>Moduller</h2>
        <li>
            Menu1
        </li>
        <li>
            Menu2
        </li>
        <li>
            Menu3
        </li>
    </div>
    
    <img src="peace-out.gif" alt="100">
     
</body>
</html>
""" # bir web sayfasnının html dökümanını getirdik...

#.........................................................

"""
from bs4 import BeautifulSoup # bs4 içerisinden biz direkt olrak bs'i çağırdık...

soup = BeautifulSoup(htmlbilgisi,'html.parser') # ilk olarak html verdik... ve parser vereceğiz... böylece htmlye göre çalışacak...
result = soup.prettify()
print(result) # bize html kaynağını daha düzgün bir hale çevirip getirdi...

"""
#.........................................................
"""
from bs4 import BeautifulSoup 

soup = BeautifulSoup(htmlbilgisi,'html.parser') 
result = soup.prettify()
print(result.title) # gidip title kısmını alabiliriz...
print(result.head) # bize head kısmını getirir...
print(result.body) # bizde body etiketini getirir...
print(result.title.name) # title etiketinin ismi gelir yani
print(result.title.string) # title etiketinin içeriği gelir...

print(result.h1) # h1 etiketini aldık böylece...
print(result.h2) # birden fazla h2 var o zaman ilk h2'yi getirir..
print(result.h2.name) # h2 etiketinin ismini getirir.
print(result.h2.string) #  h2 etiketinin içeriğini getirir... ilk h1 etiketinin...

"""
#.........................................................
"""
from bs4 import BeautifulSoup 

soup = BeautifulSoup(htmlbilgisi,'html.parser') 
result = soup.prettify()
print(result.find_all("h2")) # böylece sayfada bulduğu tüm h2'leri bir liste içerisinde getirir...
print(result.find_all("h2")[1]) # en baştan ikinci h2 etiketi gelir elimize...
print(result.div) # bize ilk divi getirir...
print(result.find_all("div")) # tüm divleri bize bir liste içerisnde getirir... 

print(result.find_all("div")[1].ul) # 2. div'in ul etiketini getirir...
print(result.find_all("div")[1].ul.find_all("ul")) # 2.divin ul etiketinin tüm ul'lerini bir liste içerisinde getirir...

result1 = soup.div.findChildren() # aslında div altındaki tüm alt elemamları getirir... kardeş etiketleri getirir gibi düşünebiliriz...

result2 = soup.div.findNextSibling().findNextSibling().findPreviousSibling() # son iki tanesi bir işe yaramaz çünkü bir ileri bir geri yaptık bir önemi kalmadı...

result3 = soup.find_all("a") # bununla bize sayfadaki tüm a etiketleri gelir...

for i in result3:
    print(i) # tek tek tüm linkleri yazabiliriz...
    

""" 
#.........................................................

