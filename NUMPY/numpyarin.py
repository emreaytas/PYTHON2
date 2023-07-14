import numpy as np

x = np.arange(9).reshape(3,3)
x = np.insert(x,1,[100,100,100],axis=0) # axis 0 olduğu için satıra ekleme olacak. ilk olarak işlem görecek olanı gireriz sonra index sonra ne eklenecek sonra axis ve np.insert() bize işlemden çıkmış arrayin referansını return eder. atama olduğu için referans kalır bellekten silinmez.
print(x)
"""
[[  0   1   2]
 [100 100 100]
 [  3   4   5]
 [  6   7   8]]
 
"""