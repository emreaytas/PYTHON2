
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
        
        
        
        
        
        
        
         
        
def app():
    
    
    
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
    

app()


    
    






