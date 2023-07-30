import pandas as pd 

# boyut demek aslında şudur. = tek boyutlu demek tek ifade ile bir veriyi tanımlayabiliriz ama dataframe olunca iki ifade ile yer belirtebiliriz. 

students = [ # bir liste ve içerisinde dict veriler var. dictlerden oluşan bir liste. 
    {
        "name":"arin",
        "age":21,
        "gender":"F"
    },
        {
        "name":"Fatih",
        "age":22,
        "gender":"M"
    },
        {
        "name":"elis",
        "age":24,
        "gender":"F"
    }
    
]

print(type(students)) # <class 'list'>

df_students = pd.DataFrame(students)
print(df_students)
"""
    name  age gender
0   arin   21      F
1  Fatih   22      M
2   elis   24      F

"""   # indexleme var.  sutunlar ve değerleri var listenin elemanlarını kullanarak bir dataframe oluşturdu.  dict'teki keyleri sutun indexi olarak kullandı valueleri ise değerler olarak kullanır. konum belirtmek için hem satır indexi hemde sutun indexi kullanmamız lazım bunu nedeni bu bir DataFrame'dir.
print()
print(type(df_students)) # <class 'pandas.core.frame.DataFrame'>    bir DataFrame ...






# veriyi iki boyutlu olarak ifade edebilirsek DataFrame olarak kullanabiliriz.

teachers = {
    "names":[
        "ahmet",
        "cansu",
        "hakan"
    ],
    "ages":[
        41,36,40
        
    ],
    "genders":[
        "M","F","M"
    ]
    
}

print(type(teachers)) # <class 'dict'>

df_teachers = pd.DataFrame(teachers) # bir dict içerisndeki veriler ile dataframe oluşturdk...
print(df_teachers)
"""
   names  ages genders
0  ahmet    41       M
1  cansu    36       F
2  hakan    40       M

"""
print(type(teachers)) # <class 'pandas.core.frame.DataFrame'>    bir DataFrame ...





list_of_list = [
    ["ahmet","mehmet","ayşe"],
    [44,39,51]
    
]
print(list_of_list) # [['ahmet', 'mehmet', 'ayşe'], [44, 39, 51]]
print(type(list_of_list)) # <class 'list'>

df_listoflist = pd.DataFrame(list_of_list)
print(df_listoflist)
"""
       0       1     2
0  ahmet  mehmet  ayşe
1     44      39    51

""" # bir sutun bilgisi olmadığı için sutun ve satiri 0'dan indexledi.  listenin içindeki her bir listeyi bir satır olarak aldı her her veri bir sutuna denk geldi. 2 liste var 2 satir var listelerin içinde 3 eleman var 3 sutun var...
print(type(df_listoflist)) # # <class 'pandas.core.frame.DataFrame'>    bir DataFrame ...

# eğer bir yapı ile çift katlı yapı kurabilirsek DataFrame yapabiliriz.



names = ["ahmet","mahmut","fatih"]
print(type(names)) # <class 'list'>

df_names = pd.DataFrame(names)
print(df_names)
"""
        0
0   ahmet
1  mahmut
2   fatih

""" # liste tek boyutlu olsa bile biz bir DataFrame kurabiliriz... sonuçta satır ve sutun yapısı var  default olarka sutuna 0.index verildi ve her eleman bir satıra atandı..
print(type(df_names)) # <class 'pandas.core.frame.DataFrame'>
print(df_names.ndim) # 2 verdi yani 2 boyutlu o zmaan bir DataFrame yapısı...







students1 = {"name":"hale","age":24}
print(type(students1)) # <class 'dict'> 

#   df_stt = pd.DataFrame(students1)    # hata verir bunun nedeni klasik dict ile biz direkt olarak dataframe kuramayız bir index belirlememiz lazım
# hata vermesinin sebebi indexlemeyi dict'in keyleri ile yapamayız bunun yüzünden indexleme yapmamız lazım.

students2 = {"Hale":pd.Series(data=[25,"F","CE"],index=["age","gender","department"]),
             "Ahmet":pd.Series(data=[32,"M","EE"],index=["age","gender","department"])}

# series ile biz indexleme kurduk data ve index belirterek.
print(type(students2)) # <class 'dict'>

df_stt1 = pd.DataFrame(students2)
print(df_stt1)
"""
           Hale Ahmet
age          25    32
gender        F     M
department   CE    EE

""" # keyleri sutun olarka kullandık bu yapı ile. indexler ise satırlar oldular indexlendiler her birinin indexe gelen değeri ise satıra yerleşti valueler indexler ile eşlenerek satırlara yerleştiler.
print(type(df_stt1)) # <class 'pandas.core.frame.DataFrame'>    bir DataFrame ...




# indexlemede değişim yaparsak.....


students3 = {"Hale":pd.Series(data=[25,"F","CE",172],index=["age","gender","department","height"]),
             "Ahmet":pd.Series(data=[32,"M","EE",100],index=["age","gender","department","weight"])}

# series ile biz indexleme kurduk data ve index belirterek.
print(type(students3)) # <class 'dict'>

df_stt2 = pd.DataFrame(students3)
print(df_stt2)
"""
           Hale Ahmet
age          25    32
department   CE    EE
gender        F     M
height      172   NaN
weight      NaN   100

""" # indexlemenin hepsini yaptı ancak sutunlardan birinde eksik değer varsa NaN dedi indexlemeyi ihmal etmedi.  olabildiğince indexleme yaptı eğer sutunlardan birisinde eksik veri varsa NaN dedi.
print(type(df_stt2)) # <class 'pandas.core.frame.DataFrame'>    bir DataFrame ...





