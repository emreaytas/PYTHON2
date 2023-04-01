import time   
    
    
class Student():
    def __init__(self):
        self.name = input("Ogrencinin ismini giriniz: ")
        self.surname = input("Ogrencinin soyismini giriniz: ")
        self.setnote1()
           
    def setnote1(self):
        note1 = int(input("Ogrencinin birinci sinav notunu giriniz: "))
        if note1 < 0 or note1 > 100:
            self.setnote1()
        else:
            self.note1 = note1
    
    def setnote2(self):
        note2 = int(input("Ogrencinin ikinci sinav notunu giriniz: "))
        if note2 < 0 or note2 > 100:
            self.setnote2()
        else:
            self.note2 = note2        
    
    def getName(self):
        return self.name
    
    def getsurname(self):
        return self.surname
    
    def getOrt(self):
        return self.ortalama
    
            
class Teacher():
    def __init__(self):
        self.name = input("Isminizi giriniz: ")
        self.surname = input("Soyisminizi giriniz: ")
        self.setPassword()
        self.izin = False
    
    def sifreGir(self):
        passw = int(input("Sifrenizi giriniz: "))
        if self.pasword == passw:
            self.izin = True
            return
        else:
            print("Sifre Yanlis tekrar giriniz...")
            self.sifreGir()
    
    def islemler(self):
        secim = self.Menu()  
        if secim == 6:
            print("Sistemden cikildi.") 
            self.izin = False      
        elif secim == 5:
            self.ogrenciNotGuncelle()
        elif secim == 4:
            self.kalanOgrencileriGoruntule()
        elif secim == 3:
            self.gecenOgrencileriGoster()
        elif secim == 2:
            self.ogrenciSil()
        else:
            self.ogrenciEkle()
    
    
    def ogrenciEkle(self):
        print("Ogrenci Ekleme...")
        time.sleep(1)
    def ogrenciSil(self):
        print("Ogrenci silme...")    
        time.sleep(1)
    def gecenOgrencileriGoster(self):
        print("Gencen ogrenciler gosteriliyor...")
        time.sleep(1)
    def kalanOgrencileriGoruntule(self):
        print("Kalan ogrenciler gosteriliyor...")
        time.sleep(1)
    def ogrenciNotGuncelle(self):
        print("Ogrenci guncelleniyor...")
        time.sleep(1)
                
                
    def setPassword(self):
        passW = int(input("Sifre belirleyiniz: "))
        if passW < 1000 or passW > 9999:
            print("Dogru bir parola giriniz...")
            self.setPassword()
        else:
            self.pasword = passW
            return     
        
    def Menu(self):
        secim = int(input("1-Ogrenci Ekle\n2-Ogrenci sil\n3-Gecen Ogrencileri goruntule\n4-Kalan ogrencileri goruntule\5-Ogrenci not guncelle\n6-Cikis yap\n\nYapacaginiz islemi seciniz: "))
        if secim < 1 or secim > 6:
            print("Yanlis bir secim yaptiniz...Dogru secim yapiniz...\n")
            self.Menu()
        else:
            return secim
                
         
Teacher1 = Teacher()


while True:
    if Teacher1.izin:
        Teacher1.islemler() 
    else:
        Teacher1.sifreGir()
             

    

    