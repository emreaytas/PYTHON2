
import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtWidgets import QMessageBox,QLineEdit,QTableWidgetItem # mesaj kutusu için import ettik mesaj verecek bize...
from PyQt5.QtGui import QIcon # ikon eklemek için kullanırız.
from PyQt5.QtCore import QDate,QTime,QDateTime # tarih,zaman,tarih zaman kullanmak için çağırdık...
from PyQt5.QtWidgets import QInputDialog # bir input oluşturacak add dediğimiz zaman...

from MainWindow7 import Ui_MainWindow # oluşturduğumuz sayfayı çağırdık...


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__() # aslında bir döngü oluşturdum...
        self.ui = Ui_MainWindow() # burada aslında biz qtdesigner ile oluşturduğumuz yapıyı kendi kodumuzaa dökmeye başlarız.     
        self.ui.setupUi(self)
        
        self.loadproducts()
         
        self.ui.pushButton.clicked.connect(self.load)
        self.ui.tableWidget.doubleClicked.connect(self.double)
    
    def double(self):
        for item in self.ui.tableWidget.selectedItems():
            print(item.row(),item.column(),item.text())
        

            
    def load(self):
        
        name = self.ui.lineEdit.text()
        price = self.ui.lineEdit_2.text()
        
        if name and price is not None:
            rowcount = self.ui.tableWidget.rowCount() # kaç adet satır var görürürüz.
            self.ui.tableWidget.insertRow(rowcount) # yani bir indexaçtık...
            self.ui.tableWidget.setItem(rowcount,0, QTableWidgetItem(name)) # satır,sutun  sonra tablo elemanı ekledik...
            self.ui.tableWidget.setItem(rowcount,1, QTableWidgetItem(price)) # satır,sutun  sonra tablo elemanı ekledik...
            
        
              
    def loadproducts(self):
        
        products = [
            
            {"name":"samsung s5","price":5000}, 
            {"name":"samsung s6","price":6000},
            {"name":"samsung s7","price":7000}
            ,{"name":"samsung s8","price":8000}
        ]
        
        self.ui.tableWidget.setRowCount(len(products)) # 3 satırlı oldu.
        self.ui.tableWidget.setColumnCount(2) # 2 sutunlu oldu...
        self.ui.tableWidget.setHorizontalHeaderLabels(("Name","Price")) # başlık belirledik...   Vertical ile ise istersek satır indexlemesi yapabilriiz.
        self.ui.tableWidget.setColumnWidth(0,220) # 0. kolon 120 olsun...
        self.ui.tableWidget.setColumnWidth(0,110)        
        
        rowindex = 0
        for i in products:
            self.ui.tableWidget.setItem(rowindex,0, QTableWidgetItem(i["name"])) # satır,sutun  sonra tablo elemanı ekledik...
            self.ui.tableWidget.setItem(rowindex,1, QTableWidgetItem(str(i["price"]))) # satır,sutun  sonra tablo elemanı ekledik...
            
            rowindex += 1
        
        
        
            
        """
        self.ui.tableWidget.setItem(0,0, QTableWidgetItem("Samsung s5")) # satır,sutun  sonra tablo elemanı ekledik...
        self.ui.tableWidget.setItem(0,1, QTableWidgetItem("5000")) # satır,sutun  sonra tablo elemanı ekledik...
        self.ui.tableWidget.setItem(1,0, QTableWidgetItem("Samsung s6")) # satır,sutun  sonra tablo elemanı ekledik...
        self.ui.tableWidget.setItem(1,1, QTableWidgetItem("6000")) # satır,sutun  sonra tablo elemanı ekledik...
        self.ui.tableWidget.setItem(2,0, QTableWidgetItem("Samsung s7")) # satır,sutun  sonra tablo elemanı ekledik...
        self.ui.tableWidget.setItem(2,1, QTableWidgetItem("7000")) # satır,sutun  sonra tablo elemanı ekledik...
        """
        
        
        
         
         
        
def app():
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()








