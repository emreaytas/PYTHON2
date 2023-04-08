# bir döviz çevirme programı yapacağız...
import json
import requests

api_url = "https://api.exchangeratesapi.io/latest?base=" # bu bize para brimlerinin değerlerini dönecek...

bozulucakdeger = input("Bozulan doviz turu: ")
alinandoviz = input("Alinacak dovizin turu: ")

miktar = input(f"Ne kadar {bozulucakdeger} bozdurmak istiyorsunuz: ")

result = requests.get(api_url+bozulucakdeger) # base = USD gibi olursa o zaman istenen değere göre seçim yaparız aslında.
result1 = result.text
result1 = json.loads(result1) # değerlerler string halden bir liste içerisindeki dictlere dönüştü...
a = result1["rates"][alinandoviz]
print(f"1 {bozulucakdeger}:{str(a)+' '} {alinandoviz}\n")

print(f"{miktar} {' '+bozulucakdeger}:{str(int(miktar * a))} {alinandoviz}\n")




