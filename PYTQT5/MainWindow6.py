# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow6.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listitems = QtWidgets.QListWidget(self.centralwidget)
        self.listitems.setGeometry(QtCore.QRect(20, 20, 351, 361))
        self.listitems.setObjectName("listitems")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 20, 161, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnadd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnadd.setObjectName("btnadd")
        self.verticalLayout.addWidget(self.btnadd)
        self.btnedit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnedit.setObjectName("btnedit")
        self.verticalLayout.addWidget(self.btnedit)
        self.btnremove = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnremove.setObjectName("btnremove")
        self.verticalLayout.addWidget(self.btnremove)
        self.btnup = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnup.setObjectName("btnup")
        self.verticalLayout.addWidget(self.btnup)
        self.btndown = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btndown.setObjectName("btndown")
        self.verticalLayout.addWidget(self.btndown)
        self.btnsort = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnsort.setObjectName("btnsort")
        self.verticalLayout.addWidget(self.btnsort)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnexit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnexit.setObjectName("btnexit")
        self.verticalLayout.addWidget(self.btnexit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnadd.setText(_translate("MainWindow", "ADD"))
        self.btnedit.setText(_translate("MainWindow", "EDIT"))
        self.btnremove.setText(_translate("MainWindow", "REMOVE"))
        self.btnup.setText(_translate("MainWindow", "UP"))
        self.btndown.setText(_translate("MainWindow", "DOWN"))
        self.btnsort.setText(_translate("MainWindow", "SORT"))
        self.btnexit.setText(_translate("MainWindow", "EXIT"))
