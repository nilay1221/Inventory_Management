# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_rm_delete.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back_add_rm = QtWidgets.QPushButton(self.centralwidget)
        self.back_add_rm.setGeometry(QtCore.QRect(10, 50, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_add_rm.setFont(font)
        self.back_add_rm.setObjectName("back_add_rm")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 280, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.rm_new_delete_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.rm_new_delete_confirm.setGeometry(QtCore.QRect(320, 440, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rm_new_delete_confirm.setFont(font)
        self.rm_new_delete_confirm.setObjectName("rm_new_delete_confirm")
        self.new_rm_delete_product_code = QtWidgets.QLineEdit(self.centralwidget)
        self.new_rm_delete_product_code.setGeometry(QtCore.QRect(410, 220, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_rm_delete_product_code.setFont(font)
        self.new_rm_delete_product_code.setObjectName("new_rm_delete_product_code")
        self.new_rm_delete_product_name = QtWidgets.QLineEdit(self.centralwidget)
        self.new_rm_delete_product_name.setGeometry(QtCore.QRect(410, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_rm_delete_product_name.setFont(font)
        self.new_rm_delete_product_name.setObjectName("new_rm_delete_product_name")
        self.new_rm_delete_product_price = QtWidgets.QLineEdit(self.centralwidget)
        self.new_rm_delete_product_price.setGeometry(QtCore.QRect(410, 350, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_rm_delete_product_price.setFont(font)
        self.new_rm_delete_product_price.setObjectName("new_rm_delete_product_price")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 350, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 210, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 40, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_add_rm.setText(_translate("MainWindow", "Back"))
        self.label_4.setText(_translate("MainWindow", "Enter Product Name : "))
        self.label_3.setText(_translate("MainWindow", "Raw Material"))
        self.rm_new_delete_confirm.setText(_translate("MainWindow", "Confirm"))
        self.label_6.setText(_translate("MainWindow", "Enter Product Price : "))
        self.label_5.setText(_translate("MainWindow", "Enter Product Code :"))
        self.pushButton.setText(_translate("MainWindow", "Back to Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
