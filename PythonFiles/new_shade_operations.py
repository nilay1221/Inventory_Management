# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_shade_operations.ui'
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
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(50, 20, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.new_shade_view = QtWidgets.QPushButton(self.centralwidget)
        self.new_shade_view.setGeometry(QtCore.QRect(330, 410, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_shade_view.setFont(font)
        self.new_shade_view.setObjectName("new_shade_view")
        self.new_shade_add = QtWidgets.QPushButton(self.centralwidget)
        self.new_shade_add.setGeometry(QtCore.QRect(330, 100, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_shade_add.setFont(font)
        self.new_shade_add.setObjectName("new_shade_add")
        self.new_shade_delete = QtWidgets.QPushButton(self.centralwidget)
        self.new_shade_delete.setGeometry(QtCore.QRect(330, 310, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_shade_delete.setFont(font)
        self.new_shade_delete.setObjectName("new_shade_delete")
        self.new_shade_modify = QtWidgets.QPushButton(self.centralwidget)
        self.new_shade_modify.setGeometry(QtCore.QRect(330, 200, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_shade_modify.setFont(font)
        self.new_shade_modify.setObjectName("new_shade_modify")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 60, 201, 20))
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
        self.back.setText(_translate("MainWindow", "Back"))
        self.new_shade_view.setText(_translate("MainWindow", "VIEW"))
        self.new_shade_add.setText(_translate("MainWindow", "ADD"))
        self.new_shade_delete.setText(_translate("MainWindow", "DELETE"))
        self.new_shade_modify.setText(_translate("MainWindow", "MODIFY"))
        self.label.setText(_translate("MainWindow", "Shade Number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
