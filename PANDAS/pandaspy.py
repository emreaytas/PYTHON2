import pandas as pd
import numpy as np

# dataframe ve series nasıl çalışır = aldığı verileri(sql,csv,list,dict,excel) pandas bu verileri alır ve bu verileri sutun ve satırlardan oluşan verileri çevirir.  tek boyutlu olursa eğer pandas series'tir birden fazla boyutlu olursa aslında çift boyutlu olursa dataframe olurlar.
# pandas yapıları pythonun yapılarından daha hızlıdır. daha seridir. kendine özgü panda series ve pandas dataframe ile vs daha hızlı çalışır.

student = ['Arin',20,'ce']
print(student) 
print(type(student)) #<class 'list'>

ps_student = pd.Series(student) #içerisine gönderilen yapıyı panda serisi olarak return edece.

print(ps_student)
"""
0    Arin
1      20
2      ce
dtype: object

""" # tek boyutludur seriler. series yapısının verdiği tablodur. bir index yapısıdır.
# panda seris farklı veri tiplerini alabilir.hem string hem int verileri aynı anda aldı eğer numpy olsa idi hepsini en üst olan veriye çevirirdi homojen bir yapı elde ederdi.
print(type(ps_student)) # <class 'pandas.core.series.Series'> 

dict1 = {"name":"emre","surname":"aytas","age":20}
pd_dict1 = pd.Series(dict1) # dict'i bir panda series'e çevirdik bunu nasıl yaptı. key'leri ilk sutuna valueleri ikinci sutuna koyarak key value yapısını bozmadı. key'leri panda series'te indexleme için kullandı. 
print(pd_dict1)  
"""
name        emre
surname    aytas
age           20
dtype: object

"""
print(type(pd_dict1)) # <class 'pandas.core.series.Series'>    panda series yapısı dictler ilede çalışır.  tek boyutludur. keyler indexleme için kullandıldı. 











