import numpy as np

x = np.random.randint(1,20,size=(10,))
print(x) # [ 3  5 14 14 14 13  1 12 11  9]
y = np.sort(x) #  np.sort(x) bize bir ndarray return eder içerisinde verilen arrayın sıralanomış halini return ederr ancak verilen arrayi kalıcı olarak sıralmaz x.sort() olsa idi x'de kalıcı olarak sıralanırdı ama np.sort() sadece verileri alır değişim yapmaz. bir ndarray return eder. 
print(x) # [ 3  5 14 14 14 13  1 12 11  9]
print(y) # [ 1  3  5  9 11 12 13 14 14 14]