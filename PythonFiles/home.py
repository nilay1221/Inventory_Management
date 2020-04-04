# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\home.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import new_shade_entry

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RM = QtWidgets.QPushButton(self.centralwidget)
        self.RM.setGeometry(QtCore.QRect(308, 140, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RM.setFont(font)
        self.RM.setObjectName("RM")
        self.EP = QtWidgets.QPushButton(self.centralwidget)
        self.EP.setGeometry(QtCore.QRect(310, 220, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EP.setFont(font)
        self.EP.setObjectName("EP")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(622, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logout.setFont(font)
        self.logout.setObjectName("logout")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(380, 620, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.RM_2 = QtWidgets.QPushButton(self.centralwidget)
        self.RM_2.setGeometry(QtCore.QRect(270, 400, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RM_2.setFont(font)
        self.RM_2.setObjectName("RM_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 80, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 340, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.RM_3 = QtWidgets.QPushButton(self.centralwidget)
        self.RM_3.setGeometry(QtCore.QRect(270, 490, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RM_3.setFont(font)
        self.RM_3.setObjectName("RM_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RM.setText(_translate("MainWindow", "Raw Material"))
        self.EP.setText(_translate("MainWindow", "Shade Number"))
        self.logout.setText(_translate("MainWindow", "Logout"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.RM_2.setText(_translate("MainWindow", "Add New Raw Material"))
        self.label.setText(_translate("MainWindow", "Enter Transactions : "))
        self.label_2.setText(_translate("MainWindow", "Add new Materail Details : "))
        self.RM_3.setText(_translate("MainWindow", "Add New Shade Number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
