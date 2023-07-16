import numpy as np

x = np.arange(20)
z = x % 2 == 0
print(z) # [ True False  True False  True False  True False  True False  True False True False  True False  True False  True False]
print(x[z]) # [ 0  2  4  6  8 10 12 14 16 18] biz eğer x[(x % 2 == 0)] yaparsak aslında x[] içerisine bir array gelir x % 2 == 0 ile .True ve False den oluşan bir array ve arrayin her elemanı tek tek işlem görür True ile eşleşenler yeni arraye gelir. False ile eşleşenler ise es geçilir.    x % 2 == 0 yapısı bize True ve Falselerden oluşan bir array return eder.