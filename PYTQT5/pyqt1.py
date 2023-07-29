from PyQt5 import QtWidgets
import sys # uygulamaları komut satırından çalıştıracağız çünkü.
from PyQt5.QtWidgets import QApplication,QMainWindow  # pyqt5 içerisindeki Qtwidgets içerisindeki metotları aldık.
from PyQt5.QtGui import QIcon  # ikon için çağırdık.
from PyQt5.QtWidgets import QToolTip # tooltip için import ettik.



def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    
    
    win.setWindowTitle("First app") #  Bir title belirtiriz böylece. pencere başlığı.
    win.setGeometry(600,300,700,700) #konum bilgisi bekler... yatay ve dikey olarak ne kadar sağa ve aşağı başlayacağını belirtiriz.   sonraki iki değer ile ise genişlik ve yükseklik belirtilir.   eğer ilk iki parametre sıfır olursa uygulamanın sol üst köşeşi ekranın sol üst köşeşi ile bitişik olur.
    win.setWindowIcon(QIcon("icon.png"))  #  logo eklemesi yaptık. 
    win.setToolTip("mouse yazısı...")
    
    
    lbl_name =  QtWidgets.QLabel(win) # win'in bir elemanı olacak.
    lbl_name.setText("Adiniz:") # Adiniz adında bir text elemanı ekledi.
    lbl_name.move(50,30) # x ve y koordinatlarında hareket ettireceğiz. # soldan sağa 50 pixel yukarından aşağı 30 pixel.
    
    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadiniz: ")
    lbl_surname.move(50,60) # aynı hizada ancak birisi öbürünün altında olacak. 30 px fark olacak.
    
    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150,30) # 50 + 100 fark yarattık.
    
        
    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,60) # 50 + 100 fark yarattık. 60 yaptık karşılık gelsin diye.
    
        
    def clicked(self): # bunu yapmamızın sebebi = window fonksiyonun elemanlarına ulaşmaktır.  ve tanımlanmış elemanların altına eklenmelidir.
        print("Butona tıklandi: "+txt_name.text()+" "+txt_surname.text()) # içeri girilen değerleri alırız .text() fonksiyonu ile...
    
    btn_save = QtWidgets.QPushButton(win) #win formu üzerinde çalışacak.
    btn_save.setText("Kaydet") # buton üzerine isim.
    btn_save.move(150,110) # izalama işlemi uygulamanın en sol üst köşesinden başlar.    ilk parametre soldan sağa ikincisi ise yukarıdan aşağı işlemler için vardır.
    btn_save.clicked.connect(clicked)  # tıklama olunca clicked fonksiyonu çalışacak.
    
    
    
    win.show() # bununla uygulama çalışır.
    sys.exit(app.exec_()) # çarpı ikonu ile uygulama duracak.
    
window()

    