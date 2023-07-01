import numpy as np

# ndarray[başlamanoktası:end(dahil değil):artış miktarı], ndarray[start:] başlama elemanında sona kadar git demektir. ndarray[:end] başlangıç noktasından ende kadar ama end dahil değil.

x = np.arange(10)
y = x[5:] # x'in bir bölümünü alır ve bir array oluşturur bunuda y'ye atar y'de bir array olur.
print(type(y)) #<class 'numpy.ndarray'>

print(x[:6]) # 6. indexe kadar gidecek 6 dahil değil. başlangıç noktasından itibaren. arrayden bir array oluşturur. 

print(x[::-1]) # en sondan en başa teker teker gel demek.
print(x[-1::-2]) # en sondan en başa ikişer ikişer gel demek

print(x[-4:-2]) # en sondan 4. elemandan en sondan 2. elemana ama en sondan 2. eleman dahil değil.

t = np.arange(25).reshape(5,5)
print(t)
"""
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
 
"""

print(t[:2]) # birinci satırı ve ikinci satırı getirir. pointer mantığı ile eleman aslında satırdır. ilk olarak girilen satırdır 2:4,1:3 bu parametrelerde eğer sutun bilgisi vermezsek o zaman satırlar üzerinden işlem yaparız.

"""
[[0 1 2 3 4]
 [5 6 7 8 9]]
 
"""

print(t[:2,2:]) # satır ve sutun ayrı olarak işlem olacak :2 satır başlangıç satırından 2. satıra kadar 2.satır dahil değil VE 2. sutundan sonuncu sutuna kadar son dahil olan aralığı al demek.

"""
[[2 3 4]
 [7 8 9]]

"""

print(t[:,1:4]) # tüm satırlar dahil sutun olarak ise 1. indexten 4. indexe 4 dahil değil.

"""
[[ 1  2  3]
 [ 6  7  8]
 [11 12 13]
 [16 17 18]
 [21 22 23]]
 
"""

print(t[:,:]) # satırlar ve sutunlar için bir kısıtlama yok t'nin aynısı olur.

"""
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
"""



u = np.arange(9).reshape(3,3)
print(u)

"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]

"""

i = u[1:2,0:2] # 1. satır olacak ve sutunlardan ise 0. ve 1. index dahil olacak.
print(i)
"""
[[3 4]]

"""

u[1,1] = 100 # 2.satır 2.sutundaki eleman 100 oldu.   : işareti ile aralık belirleriz. , ile ise satır sutun belirlemesi yaparız.
i[0,0] = 333 # ilk satır ilk sutundaki eleman 333 oldu...
print(u)
"""
[[  0   1   2]
 [333 100   5]
 [  6   7   8]]

""" # u'nun bir parçası olan i üzerinde işlem yapmamıza rağmen u'da değişim oldu bunun nedeni referanslar ile bellek adresleri ile işlem yapmak aslında bellek adresinin bir kısmını alıp array olarak atıyoruz. bu yüzden parçada olan değişim ana arraydede etki eder çünkü o bellek alanı üzerinde değişim oldu.

print(np.shares_memory(u,i)) # aynı bellek adresinde mi çalışıyorlar True verir... hafızadaki yerleri aynı ortak elemanların bu yüzden yapılan bir değişim diğerinede etki ediyor.

# farklı bellek adresleri olsun istersek o zaman .copy() metotunu kullanacağız...


g = np.arange(16).reshape(4,4)

h = np.copy(g[:3,1:4]) # g'den kopyala ve yeni bir yere ata. değerler farklı bellek gözlerinde olsun istiyoruz.
print(h)
"""
[[ 1  2  3]
 [ 5  6  7]
 [ 9 10 11]]
 
"""

print(np.shares_memory(g,h)) # False verir çünkü değerleri aynı bellek adreslerinde saklamıyor. .copy() ile sadece değerler alınır bellek adreslerinin farklı olması sağlanır.  
















