import numpy as np

x = np.array([1.5,2.5,3.6,4.3],dtype=np.int32) # veriler int olarak tutulacak. yani noktadan sonrası gidecek upcasting değil downcasting olacak. float veriden int dönüşümü yaptırdık bunu dtype ile yaptık.  
print(x) #[1 2 3 4]
print(x.dtype) # int 3