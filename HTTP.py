# pip install requests ile yükleriz.
import requests # modülü çağırırız.
import json


print(json.__file__) # json modülünün kurulduğu yeri görürüz.
print(requests.__file__) # requests modülünün nerede bulunduğunun görebiliz
# herhangi bir link'e request attığımızda bize bir veri dönecek. bir talebi python aracılığıyla yaparız.

result = requests.get("https://jsonplaceholder.typicode.com/todos") # bir cevap gelecek.
print(result) # bir cevap dönecek response 200 gibi. bunun anlamı bağlantılı başarılı demektir.
resultText = result.text # bir str bilgi geldi.
print(resultText)
resultDicts = json.loads(resultText) # çoğul olan sistem.
for i in resultDicts: # tüm değerleri bir liste içerisinde tek tek dict olacak şekilde getirdi.
    print(i) 

for i in resultDicts: # tüm değerleri bir liste içerisinde tek tek dict olacak şekilde getirdi.
    print(i["id"])     

for i in resultDicts: # tüm değerleri bir liste içerisinde tek tek dict olacak şekilde getirdi.
    if int(i["id"]) % 2 == 0:
        print(i["title"])    

