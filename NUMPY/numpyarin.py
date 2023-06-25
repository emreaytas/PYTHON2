import numpy as np

x = np.array([1,2,3,4,5],dtype=np.int64)
np.save("fordfocus",x) # np.save ile array kaydederiz. önce kaydedilecek yer sonra ise kaydedilecek değeri gireriz ve .npy uzantılı bir dosyaya değerleri kaydeder.

y = np.load("fordfocus.npy") # y = dosya içerisindeki ndarray olacak aslında. np.load() parametre alacak oda arrayin kaydedildiği .npy dosyası.

print(y) # [1 2 3 4 5]
