import numpy as np

x = np.random.random((2,3)) # 2 satır 3 sutundan oluşan bir matris elde ederiz sayılar ise 0 ile 1 arasında rastgele sayılar olur. 1' e eşit olmaz.
y = np.random.randint(4,50,size = (2,3))  # 4den başla 50 dahil değil aralıkta rastgele bir array oluştur. size  ile nasıl bir yapıda olacağını belirtiriz. size = 5 desek tek boyutlu bir array oluştururuz. ama mesela shape ile ilgili bir işlem yapacaksak ve tek boyutlu olmayacaksa genellikle () tuple içerisnde gönderilir.
