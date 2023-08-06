import pandas as pd
import numpy as np

data = {
    "col1":[1,2,3,4,5],
    "col2":[10,20,13,20,25],
    "col3":["abc","bca","ade","cba","dea"]
    
    
}

df = pd.DataFrame(data)
print(df)
"""
   col1  col2 col3
0     1    10  abc
1     2    20  bca
2     3    13  ade
3     4    20  cba
4     5    25  dea
"""

result = df["col1"].unique() # her verinin adeti 1 olunca elde edilen liste.
print(result) 
"""
[1 2 3 4 5]
"""

result1 = df["col1"].nunique() 
print(result1) # 5 kaç tane unique sayı var görebiliriz.


print(df["col2"].value_counts()) # her eleman kaç tane görebiliriz.
"""
col2
20    2
10    1
13    1
25    1
Name: count, dtype: int64
"""

print(df["col2"] * 2) # her eleman tek tek işlem görür ve hepsi iki ile çarpılır.

def kareal(x):
    return x ** 2

print(df["col2"].apply(kareal)) # direkt olarak df["col2"]'yi apply sayesinde gönderebilmiş olduk.
print(df["col2"].apply(lambda x:x ** 2)) # böylede olabilir.


df["col4"] = df["col3"].apply(len) # her col3 satırındaki stringin boyutu col4'un elemanı olacak index sırası ile.
print(df["col4"])
"""
0    3
1    3
2    3
3    3
4    3
Name: col4, dtype: int64
"""


































