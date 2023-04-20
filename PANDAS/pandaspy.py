import pandas as pd
import numpy as np

s1 = pd.Series([3,0,2,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1,oranges = s2) #s1 ve s2 ile dict oluşturudk ve isimlendirme yaprık apples = s1,oranges = s2 diyerek...

df = pd.DataFrame(data) # böylece dict ile dataframe oluşturduk...
print(df)
"""
    apples  oranges
0       3        0
1       0        3
2       2        7
3       1        2
""" # böylece bir dataframe oldu ve indexlendi kolonların isimlerinide koyabildik...


df1 = pd.DataFrame()
print(df1)
"""
Empty DataFrame
Columns: []
Index: []
"""

df2 = pd.DataFrame([1,2,3,4])
print(df2)
"""
   0 # her hangi bir kolon ismi olmadığı için default olarak 0 yazdırdı... aslında kolonun indexi olarak 0 verdi bir tane daha kolon olsa oda sıfır alacaktı...
0  1
1  2
2  3
3  4
""" # bir liste ilede indexlenmiş yapı oluşturabildik...

df3 = pd.DataFrame([["Ahmet",50],["Ali",60],["Veli",70],["Emre",80]])
print(df3)
"""
       0   1
0  Ahmet  50
1    Ali  60
2   Veli  70
3   Emre  80
    
""" # her bir listeyi bir satır olarak kabul etti. ve kolonları ismi olmadığı için default olarak sıfırdan indexledi... her bir liste ile bir satrı oluşturdu ve onlarıda indexledi... 
