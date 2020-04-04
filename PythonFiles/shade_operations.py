# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\shade_operations.ui'
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
        self.shade_add = QtWidgets.QPushButton(self.centralwidget)
        self.shade_add.setGeometry(QtCore.QRect(310, 110, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_add.setFont(font)
        self.shade_add.setObjectName("shade_add")
        self.shade_modify = QtWidgets.QPushButton(self.centralwidget)
        self.shade_modify.setGeometry(QtCore.QRect(310, 200, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_modify.setFont(font)
        self.shade_modify.setObjectName("shade_modify")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 60, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.shade_delete = QtWidgets.QPushButton(self.centralwidget)
        self.shade_delete.setGeometry(QtCore.QRect(310, 290, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_delete.setFont(font)
        self.shade_delete.setObjectName("shade_delete")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(30, 20, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.shade_view = QtWidgets.QPushButton(self.centralwidget)
        self.shade_view.setGeometry(QtCore.QRect(310, 380, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_view.setFont(font)
        self.shade_view.setObjectName("shade_view")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.shade_add.setText(_translate("MainWindow", "ADD"))
        self.shade_modify.setText(_translate("MainWindow", "MODIFY"))
        self.label.setText(_translate("MainWindow", "Shade number"))
        self.shade_delete.setText(_translate("MainWindow", "DELETE"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.shade_view.setText(_translate("MainWindow", "VIEW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
