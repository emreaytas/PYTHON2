ogrenciAdeti = int(input("Kac adet ogrenci gireceksiniz: "))

students = {}
i = 0
for i in range(ogrenciAdeti):
    numara = int(input(str(i + 1)+". ogrencinin numarasini giriniz: "))
    if numara in students:
        print("Bu kisi bulunuyor...")
        i = i-1
        continue
    
    elif numara < 100 or numara > 999:
        print("Tanimlanamaz numara...")
        i = i-1
        continue
    else:
        name = input("Ogrencinin ismini giriniz: ")
        surname = input("Ogrencinin soyadini giriniz: ")
        phone = None
        phone = input("Ogrencinin numarasini giriniz: ")
        while not len(phone) == 11:
            
            phone = input("Ogrencinin numarasini giriniz: ")
            
        students[str(numara)] = {
            'ad':name,
            'soyad':surname,
            'phone':phone
        }
        
for i in students:
    print(str(i) +": "+students[i]["ad"]+" "+students[i]["soyad"]+" "+students[i]["phone"])