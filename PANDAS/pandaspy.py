import pandas as pd

# pandas NaN veriler ile çok iyi şekilde sorunsuz çalışabilir.

students = {"Hale":pd.Series(data=[25,"Cetin","CE",161],index=["age","surname","department","height"]),
                        "Ahmet":pd.Series(data=[32,"M","EE",100],index=["age","gender","department","weight"]),"Fatma":pd.Series(data=[32,"Gulsen","EE",175],index=["age","surname","department","height"])
        }

df_students = pd.DataFrame(students)
print(df_students)
"""
             Hale Ahmet   Fatma
age            25    32      32
department     CE    EE      EE
gender        NaN     M     NaN
height        161   NaN     175
surname     Cetin   NaN  Gulsen
weight        NaN   100     NaN

""" # var olan tüm satırları indexlemek için kullanır ve olmayan veriler için ise NaN der.  mesela Fatma sutunun weight bilgisi yok bu yüzden NaN verdi hata vermedi.



# isnull()
x = df_students.isnull()
print(x)
"""
             Hale  Ahmet  Fatma
age         False  False  False
department  False  False  False
gender       True  False   True
height      False   True  False
surname     False   True  False
weight       True  False   True

""" # verinin var olup olmamasına göre True False verir tüm değerlere veri yoksa True varsa False NaN olanlara True verdi.
print(type(x)) # <class 'pandas.core.frame.DataFrame'>  bu bir DataFrame çünkü ndim = 2 ...



y = df_students.isnull().sum() # her sutunda kaç tane True var yani boşdeğer var göreceğiz.
print(y)
"""
Hale     2
Ahmet    2
Fatma    2
dtype: int64

""" # her sutunda kaç adet True var yani her suttunda kaç adet satır boşdeğer bunu görebiliriz.  
print(type(y)) # <class 'pandas.core.series.Series'>  bu bir seridir ndim = 1   çünkü sutun boyutu yok tek boyutlu. bir seridir.




z = df_students.isnull().sum().sum() # ikinci .sum() ile komple DataFramede kaç tane boş veri var bunu görebiliriz. Series'in elemanlarını topladı ve numpy.int veri haline geldi.
print(z)  # 6
print(type(z)) # <class 'numpy.int64'>








# notnull()

t = df_students.notnull() # isnull'ın tersidir. değer varsa True yoksa False verir..
print(t)
"""
             Hale  Ahmet  Fatma
age          True   True   True
department   True   True   True
gender      False   True  False
height       True  False   True
surname      True  False   True
weight      False   True  False
"""

f = df_students.notnull().sum() # her sutunda kaç adet dolu değer var görebiliriz.
print(f)
"""
Hale     4
Ahmet    4
Fatma    4
dtype: int64

"""
print(type(f)) # <class 'pandas.core.series.Series'>  bu bir seridir. sutun bilgisi yoktur. tek boyutludur.


g = df_students.notnull().sum().sum() # komple DataFramede kaç tane dolu veri var görebiliriz.
print(g) # 12  
print(type(g)) # <class 'numpy.int64'>





# .count()

h = df_students.count() # .count() = .notnull().sum()
print(h)
"""
Hale     4
Ahmet    4
Fatma    4
dtype: int64
""" 

j = df_students.count().sum()
print(j) # 12
print(type(j)) # <class 'numpy.int64'>





# dropna()  

x = df_students.dropna() # içerisinde NaN veri olan satırları kaldırır.
print(x)
"""
           Hale Ahmet Fatma
age          25    32    32
department   CE    EE    EE

""" # herhangi bir satırda NaN veri varsa o satırı kaldırır. sadece NaN verisi olmayan verileri kalır 
print(type(x)) # <class 'pandas.core.frame.DataFrame'>

df_students1 = df_students2 = df_students

df_students.dropna()  # .dropna() anaDataFramede bir değişim yapmaz ama işlem görmüş DataFrame'yi return eder. ancak içerisinde inplace = True dersek o zaman kalıcı bir değişim sağlar kalıcı olarak eksik verisi olan satırlar yok olur.
print(df_students)
"""
             Hale Ahmet   Fatma
age            25    32      32
department     CE    EE      EE
gender        NaN     M     NaN
height        161   NaN     175
surname     Cetin   NaN  Gulsen
weight        NaN   100     NaN
""" # .dropna() anaDataFramede bir değişim yapmaz ama işlem görmüş DataFrame'yi return eder.


x = df_students1.dropna(how="all")  # bunun mantığı şudur. eğer bir satırda tüm veriler NaN ise o satırı sil demek eğer  bir satırda bir tane bile veri varsa ona dokunmaz...
print(x)
"""
age            25    32      32
department     CE    EE      EE
gender        NaN     M     NaN
height        161   NaN     175
surname     Cetin   NaN  Gulsen
weight        NaN   100     NaN

""" # 
print(type(x)) # <class 'pandas.core.frame.DataFrame'> bu bir DataFrame çünkü iki boyutlu...


df_students1["Ahmet"]["weight"] = None # bu yapı ile atama yapabiliriz. önce sutun sonra satır bilgisi ile direkt olarak kalıcı atama yapabiliriz
u = df_students1.dropna(how="all")  # bunun mantığı şudur. eğer bir satırda tüm veriler NaN ise o satırı sil demek eğer  bir satırda bir tane bile veri varsa ona dokunmaz...
print(u)
"""
             Hale Ahmet   Fatma
age            25    32      32
department     CE    EE      EE
gender        NaN     M     NaN
height        161   NaN     175
surname     Cetin   NaN  Gulsen

""" # tüm verileri NaN olan satıları sildi mesela weight satırını sildi çünkü weight'te ahmete None verdik böylece satır kayboldu.




g = df_students2.dropna(thresh=2) # thresh = 1 olursa 2 Tane Nan veriye izin verir. Ama eğer thresh = 2 olursa o zaman iki tane NaN olanları siler. thresh = 2 olursa max bir tane NaN'a izin verir. eşit ve daha fazla olanlar elenir.
print(g)
"""
age            25    32      32
department     CE    EE      EE
height        161   NaN     175
surname     Cetin   NaN  Gulsen 
""" # bir bir DataFrame   

l = df_students2.dropna(axis=0) # NaN olan satırlar gitti...
print(l)
"""
           Hale Ahmet Fatma
age          25    32    32
department   CE    EE    EE
"""

m = df_students2.dropna(axis=1) # içerisinde NaN olan sutunları silecek komple.. how = "all" dersek o zaman tüm satırları NaN olan sutunu silecek.
print(m)
"""
Empty DataFrame
Columns: [] 
Index: [age, department, gender, height, surname, weight]
""" # boş bir DataFrame oldu... çünkü veri kalmadı bunun nedeni her sutunda NaN veri var...










students = {"Hale":pd.Series(data=[25,"Cetin","CE",161],index=["age","surname","department","height"]),
                        "Ahmet":pd.Series(data=[32,"M","EE",100],index=["age","gender","department","weight"]),"Fatma":pd.Series(data=[32,"Gulsen","EE",175],index=["age","surname","department","height"])
        }

df_students3 = pd.DataFrame(students)

df_students3.dropna(inplace=True) # DataFrame kalıcı olarak değişir...
df_students4 = pd.DataFrame(students)


x = df_students4.fillna(method="ffill")  
print(x)
"""
             Hale Ahmet   Fatma
age            25    32      32
department     CE    EE      EE
gender         CE     M      EE
height        161     M     175
surname     Cetin     M  Gulsen
weight      Cetin   100  Gulsen
""" # NaN verileri o NaN'dan önce gelen verileri verdi...  mesela gender'i NaN olan birisi gender olarak department'in değerini alır...

y = df_students4.fillna(method="ffill",axis=1) # default olarak axis = 0. NaN veri bir önceki satırdan alınırdı ama eğer axis = 1 olursa NaN veri bir önceki sutun ile tamamlanır...
print(y)
"""
             Hale  Ahmet   Fatma
age            25     32      32
department     CE     EE      EE
gender        NaN      M       M
height        161    161     175
surname     Cetin  Cetin  Gulsen
weight        NaN    100     100

""" # bazı veriler NaN olarak kaldı bunun nedeni kendinden önce bir veri olmaması... kendisinden önce verisi olan bir sutun yoksa NaN olarak kalır...

z = df_students4.fillna(method="backfill",axis=1) # kendisinden sonrakine bakarak doldurur backfill...
print(z) # acis = 1 olduğu için alışveriş sutunlar arasında olacak yani değişim aynı satır düzleminde olacak sağdan sola şekilde. axis = 0 olsa idi ki zaten default olara 0 o zaman verileri NaN verileri Altındaki satırlardan alarak dolduracak.
"""

             Hale   Ahmet   Fatma
age            25      32      32
department     CE      EE      EE
gender          M       M     NaN
height        161     175     175
surname     Cetin  Gulsen  Gulsen
weight        100     100     NaN

"""

 









