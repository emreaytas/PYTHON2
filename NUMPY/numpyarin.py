import numpy as np

x = np.linspace(1,21,11)
print(x) # [ 1.  3.  5.  7.  9. 11. 13. 15. 17. 19. 21.]
y = np.array([2,4,7])
print(x[y]) # [ 5.  9. 15.] bu ne demek = x'in içindeki y değerlerindeki indexlerden oluşan değerlerden bir array elde et ve getir demek. yani bir array halinde gitti y buraada her değeri bir işlem gördü ve bir array döndürdük. 

t = np.arange(25).reshape(5,5)
print(t)
z = np.array([1,2])
print(t[z,:]) # satırlarda z yani 1. index ve 2. index sutunlarda ise hepsini alacağız. z'nin tüm değerleri işlem görecek.
"""
[[ 5  6  7  8  9]
 [10 11 12 13 14]]
 
"""














