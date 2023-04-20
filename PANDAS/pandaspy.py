import pandas as pd
import numpy as np
#data
numbers = [20,30,40,50]
letters = ['a','b','c','d']

pandas_series = pd.Series()
print(pandas_series) # Series([], dtype: object)  ... aslında tek boyutlu bir liste tanımlanası yaparız..
  
pandas_series1 = pd.Series(numbers)
print(pandas_series1) 
"""
0    20
1    30
2    40
3    50
dtype: int64
""" # bilgiler index atanarak tutulur... ve type olarak int belirlenmiş...

pandas_series2 = pd.Series(letters) # bilgilerimiz yine indexlenerek tutulur ama tipi object olarak geçmiş biz str verdik ama object olarak tuttu. çünkü genel olarak nesneler üzerinden çalışacağız..
print(pandas_series2)

pandas_series3 = pd.Series(5) # tek bir değer ile de seri oluşturabiliriz...

pandas_series4 = pd.Series("a",[0,1,2,3,4]) # iki tane eleman verdik ve farklı tiplerden değerleri Series'te tanımlayabildik... 
"""
0    a
1    a
2    a
3    a
4    a
dtype: object
""" # bize gelen budur... sağdaki ile soldakini birleştirdi...

dict = {"a":10,"b":20,"c":30,"d":40}
pandas_series5 = pd.Series(dict) # dictin key ve valuesi ile kolaylıkla seri oluşturabilir... keyler ile valueleri aynı satırda olur...
print(pandas_series5)
"""
a    10
b    20
c    30
d    40
dtype: int64
"""

randomnumbers = np.random.randint(10,100,6)
randompandas = pd.Series(randomnumbers)

"""
0    35
1    52
2    96
3    82
4    22
5    35
dtype: int32
""" 

pandas_series6 = pd.Series([1,2,3,4],["a","b","c","d"])
print(pandas_series6[:2]) # ilk iki sıra gelecek...
print(pandas_series6["a"]) # anın denk geldiği gelecek dict gibi...
print(pandas_series6["a","c"]) # keyleri olanların satılarını getirir... eğer olmayan bir key girersek o zaman hata vermez bulunamadı der...
print(pandas_series6.ndim) # .ndim ile seri kaç boyutlu bunu görebiliriz...
print(pandas_series6.shape) # .shape ile boyut değerini görebiliriz...
print(pandas_series6.dtype) # .dtype ile ise dtype değerini görrebiliriz...
print(pandas_series6.sum()) # elemanların toplamını verir...
print(pandas_series6.max()) # max() ile max değer min() ile min değer mean() ile ise ortalama değer elde edilir... 

result1 = pandas_series6 + pandas_series6 # bununla olan ise keyler değişmez ama valueler indexe göre toplanır yani aslında hepsi iki katına çıkar...
result1 += 50 # bunula ise her value 50 artar...
result1 = np.sqrt(result1) # böylece her dğeerin karekökünü aldık...
result2 = result1 >= 50 # 50'dan fazla olan değerler için True olmayanlar için False verecek ve bir seri oluşacak...

result3 = pandas_series6[pandas_series6 >= 50] # bu koşulu sağlayan değerlerden oluşan bir seri olacak böylece...

opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([20,30,40,10],["astra","corsa","opc","insignia"])

total = opel2018 + opel2019
print(total)
"""
astra       40.0
corsa       60.0
insignia    20.0
mokka        NaN
opc          NaN
dtype: float64
""" # sayısal olmayan veriler için Nan not a number verir... toplama yaptık ve ikiisndede olmayan değerler Nanoldu...
print(total["astra"]) # key value mantığı ile bize değeri getirir... 




