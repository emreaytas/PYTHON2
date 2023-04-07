import requests
import json
result = requests.get("https://jsonplaceholder.typicode.com/todos") #get ile getir komutu verdik. # bize bir sonuç dönecek ve biz bunu bir değişkene atadaık.
result1 = result.text #bunu yaparsak eğer o zmaan bir text oalrak görürüz sonucu. bize bir string bilgi verdi.

result2 = json.loads(result1) #çoklu olursa eğer loads yaparız. ve böylece stringten çıkarır ve dict olarak kullanmamızı sağlar.

for i in result2:
    if i["userId"] == 1:
        print(i["tittle"])



