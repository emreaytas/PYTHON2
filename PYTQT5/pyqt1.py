
import typing
from PyQt5 import QtCore, QtWidgets
import sys # uygulamaları komut satırından çalıştıracağız çünkü.
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget  # pyqt5 içerisindeki Qtwidgets içerisindeki metotları aldık.
from PyQt5.QtGui import QIcon  # ikon için çağırdık. ikon yerleştirmek vs için kullanırız.
from PyQt5.QtWidgets import QToolTip # tooltip için import ettik.


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        
        self.setWindowTitle("Calculator")
        self.setGeometry(500,300,500,400)
        self.setWindowIcon(QIcon("cal1.png"))  #  logo eklemesi yaptık. 
        self.setToolTip("Calculator...")
        self.initUI()
    
    def initUI(self):
        
        # sayi1 bilgileri
        
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayi1: ")
        self.lbl_sayi1.move(50,30)
        
        # sayi1 giris alani
        
        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)
              
        # sayi2 bilgileri
        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayi2: ")
        self.lbl_sayi2.move(50,80)
        
        # sayi2 giris alani
        
        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)
        
        # buton1
    
        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesapla)
        
        # buton2
    
        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Cikarma")
        self.btn_cikar.move(150,170)        
        self.btn_cikar.clicked.connect(self.hesapla)
    
        # buton3
    
        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText("Carp")
        self.btn_carp.move(150,210)
        self.btn_carp.clicked.connect(self.hesapla)
        
        # buton4
    
        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText("Bol")
        self.btn_bol.move(150,250)               
        self.btn_bol.clicked.connect(self.hesapla)
        
        # sonuç yazdirma:
        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("Sonuc: ")
        self.lbl_sonuc.move(150,290)
    
    
    def hesapla(self): # tek tek farklı farklı fonksiyon yazmamak için...
        sender = self.sender() # tüm butonlar tek fonksiyonu çalıştıracak ama hangisinden basıldığımı self.sender() ile bulacağız...
          # sender aslında butonun referansıdır... 
          
        if sender.text() == "Topla":
            self.lbl_sonuc.setText("Sonuc: "+str(int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())))
        elif sender.text() == "Cikarma":
            self.lbl_sonuc.setText("Sonuc: "+str(int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())))
        elif sender.text() == "Carp":
            self.lbl_sonuc.setText("Sonuc: "+str(int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())))
        else:
            self.lbl_sonuc.setText("Sonuc: "+str(int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())))

           
def window():
    app = QApplication(sys.argv)
    win = MainForm()
    
    win.show()
    sys.exit(app.exec_())
    
    
window()    
    
    