# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\rm_operations.ui'
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
        self.rm_add = QtWidgets.QPushButton(self.centralwidget)
        self.rm_add.setGeometry(QtCore.QRect(300, 90, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rm_add.setFont(font)
        self.rm_add.setObjectName("rm_add")
        self.rm_modify = QtWidgets.QPushButton(self.centralwidget)
        self.rm_modify.setGeometry(QtCore.QRect(300, 190, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rm_modify.setFont(font)
        self.rm_modify.setObjectName("rm_modify")
        self.rm_delete = QtWidgets.QPushButton(self.centralwidget)
        self.rm_delete.setGeometry(QtCore.QRect(300, 300, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rm_delete.setFont(font)
        self.rm_delete.setObjectName("rm_delete")
        self.rm_view = QtWidgets.QPushButton(self.centralwidget)
        self.rm_view.setGeometry(QtCore.QRect(300, 400, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rm_view.setFont(font)
        self.rm_view.setObjectName("rm_view")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 10, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rm_add.setText(_translate("MainWindow", "ADD"))
        self.rm_modify.setText(_translate("MainWindow", "MODIFY"))
        self.rm_delete.setText(_translate("MainWindow", "DELETE"))
        self.rm_view.setText(_translate("MainWindow", "VIEW"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Raw Material"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
