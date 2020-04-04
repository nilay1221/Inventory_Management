# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\shade_view.ui'
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
        self.op_back = QtWidgets.QPushButton(self.centralwidget)
        self.op_back.setGeometry(QtCore.QRect(50, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.op_back.setFont(font)
        self.op_back.setObjectName("op_back")
        self.view_today = QtWidgets.QPushButton(self.centralwidget)
        self.view_today.setGeometry(QtCore.QRect(330, 260, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.view_today.setFont(font)
        self.view_today.setObjectName("view_today")
        self.view_custom = QtWidgets.QPushButton(self.centralwidget)
        self.view_custom.setGeometry(QtCore.QRect(332, 347, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.view_custom.setFont(font)
        self.view_custom.setObjectName("view_custom")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.view_trans = QtWidgets.QPushButton(self.centralwidget)
        self.view_trans.setGeometry(QtCore.QRect(330, 170, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.view_trans.setFont(font)
        self.view_trans.setObjectName("view_trans")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.op_back.setText(_translate("MainWindow", "Back"))
        self.view_today.setText(_translate("MainWindow", "Today"))
        self.view_custom.setText(_translate("MainWindow", "Custom Dates"))
        self.label.setText(_translate("MainWindow", "Shade Number"))
        self.view_trans.setText(_translate("MainWindow", "Transaction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
