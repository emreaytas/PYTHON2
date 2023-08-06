import matplotlib.pyplot as plt
import numpy as np

"""
x = [1,2,3,4]
plt.plot(x)
plt.show()
"""

"""
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y) # x listesi x eksenine y listesi ve değerleri y eksenine yerleşti.
plt.axis([0,6,0,20]) # 0 ile 6 arasında olsun x ekseninin aralığı.  0 ile 20 arasında değer alsın y ekseninin aralığı deriz.
plt.show() # plt.show() ile grafiği görebiliriz.
"""

"""
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y,color = "red",linewidth = "5") # x listesi x eksenine y listesi ve değerleri y eksenine yerleşti.  color ile çizgi rengi belirleriz.     linewidth ile ise kalınlık belirleriz.
plt.axis([0,6,0,20]) # 0 ile 6 arasında olsun x ekseninin aralığı.  0 ile 20 arasında değer alsın y ekseninin aralığı deriz.  axis ile önce iki değer x aralığı son iki değer ise y aralığını belirleriz.
plt.title("...GRAFIK BASLIGI...") # ana başlığı belirleriz.
plt.xlabel("X EKSENI") # x ekseninin başlığını belirleriz.
plt.ylabel("Y EKSENI") # y ekseninin baslıgını belirleriz.
plt.show() # plt.show() ile grafiği görebiliriz.
"""

"""
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y,"-g") # x listesi x eksenine y listesi ve değerleri y eksenine yerleşti. üçüncü parametre olarak "-g" vererek biz düz yeşil çizgi yaparız.  --g olsa idi kesik çizgi olurdu yeşil renkli.   "o--r" olsa idi mesela değerlerin kesiştiği yerler içi dolu kesikli kırmızı çizgi olurdu.
plt.axis([0,6,0,20]) # 0 ile 6 arasında olsun x ekseninin aralığı.  0 ile 20 arasında değer alsın y ekseninin aralığı deriz.  axis ile önce iki değer x aralığı son iki değer ise y aralığını belirleriz.
plt.title("...GRAFIK BASLIGI...") # ana başlığı belirleriz.
plt.xlabel("X EKSENI") # x ekseninin başlığını belirleriz.
plt.ylabel("Y EKSENI") # y ekseninin baslıgını belirleriz.
plt.show() # plt.show() ile grafiği görebiliriz.
"""

x = np.linspace(0,2,100)
plt.plot(x,x,label = "lineer",color = "red") # önce x ekseninin değerleri sonra ise x ** 2 diyerek bir numpy array elde ederiz. oda y eksenin değerleri olaral label ile ise çizginin ismini belirleriz.
plt.plot(x,x**2,label = "quadratic",color = "green")
plt.plot(x,x**3,label="cubic",color = "gray")
plt.title("BASLIK ISTE AMK")
plt.xlabel("x ekseni...")
plt.ylabel("y ekseni...")
plt.legend() # labellere verdiğimiz değerler ekranda gözüksün istedik. 
plt.axis([-1,3,-1,10]) # önce x sonra y ekseninin aralığnı belirledik. eksi değerler verebiliriz.
plt.show()





