# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shade_add.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1304, 862)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shade_customer = QtWidgets.QComboBox(self.centralwidget)
        self.shade_customer.setGeometry(QtCore.QRect(240, 200, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_customer.setFont(font)
        self.shade_customer.setEditable(True)
        self.shade_customer.setObjectName("shade_customer")
        self.shade_customer.addItem("")
        self.shade_customer.setItemText(0, "")
        self.shade_customer.addItem("")
        self.shade_customer.addItem("")
        self.shade_customer.addItem("")
        self.shade_customer.addItem("")
        self.shade_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.shade_confirm.setGeometry(QtCore.QRect(890, 660, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_confirm.setFont(font)
        self.shade_confirm.setObjectName("shade_confirm")
        self.shade_addtable = QtWidgets.QTableWidget(self.centralwidget)
        self.shade_addtable.setGeometry(QtCore.QRect(40, 360, 411, 251))
        self.shade_addtable.setRowCount(8)
        self.shade_addtable.setColumnCount(3)
        self.shade_addtable.setObjectName("shade_addtable")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_addtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_addtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_addtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(7, 1, item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 120, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.date = QtWidgets.QLineEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(660, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date.setFont(font)
        self.date.setObjectName("date")
        self.shade_transaction_id = QtWidgets.QLineEdit(self.centralwidget)
        self.shade_transaction_id.setGeometry(QtCore.QRect(240, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_transaction_id.setFont(font)
        self.shade_transaction_id.setObjectName("shade_transaction_id")
        self.back_add_rm = QtWidgets.QPushButton(self.centralwidget)
        self.back_add_rm.setGeometry(QtCore.QRect(40, 50, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_add_rm.setFont(font)
        self.back_add_rm.setObjectName("back_add_rm")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 190, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 120, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.shade_remark = QtWidgets.QLineEdit(self.centralwidget)
        self.shade_remark.setGeometry(QtCore.QRect(680, 200, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_remark.setFont(font)
        self.shade_remark.setObjectName("shade_remark")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 40, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 190, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.shade_colortable = QtWidgets.QTableWidget(self.centralwidget)
        self.shade_colortable.setGeometry(QtCore.QRect(500, 350, 661, 291))
        self.shade_colortable.setRowCount(8)
        self.shade_colortable.setColumnCount(5)
        self.shade_colortable.setObjectName("shade_colortable")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_colortable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_colortable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_colortable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_colortable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_colortable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(7, 1, item)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 270, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.shade_number_add = QtWidgets.QLineEdit(self.centralwidget)
        self.shade_number_add.setGeometry(QtCore.QRect(480, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_number_add.setFont(font)
        self.shade_number_add.setObjectName("shade_number_add")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(140, 640, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.shade_add_total = QtWidgets.QLineEdit(self.centralwidget)
        self.shade_add_total.setGeometry(QtCore.QRect(290, 650, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_add_total.setFont(font)
        self.shade_add_total.setObjectName("shade_add_total")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.shade_customer.setItemText(1, _translate("MainWindow", "Rajesh"))
        self.shade_customer.setItemText(2, _translate("MainWindow", "Nishit"))
        self.shade_customer.setItemText(3, _translate("MainWindow", "Nilay"))
        self.shade_customer.setItemText(4, _translate("MainWindow", "Parth"))
        self.shade_confirm.setText(_translate("MainWindow", "Confirm"))
        item = self.shade_addtable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Code"))
        item = self.shade_addtable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.shade_addtable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        __sortingEnabled = self.shade_addtable.isSortingEnabled()
        self.shade_addtable.setSortingEnabled(False)
        self.shade_addtable.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "Date :"))
        self.back_add_rm.setText(_translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow", "Shade Number "))
        self.label_6.setText(_translate("MainWindow", "Customer Name:"))
        self.label_5.setText(_translate("MainWindow", "Transaction ID : "))
        self.pushButton.setText(_translate("MainWindow", "Back to Main Menu"))
        self.label_7.setText(_translate("MainWindow", "Remark :"))
        item = self.shade_colortable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Code"))
        item = self.shade_colortable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.shade_colortable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Percentage"))
        item = self.shade_colortable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.shade_colortable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Price"))
        __sortingEnabled = self.shade_colortable.isSortingEnabled()
        self.shade_colortable.setSortingEnabled(False)
        self.shade_colortable.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "Shade Number :"))
        self.label_9.setText(_translate("MainWindow", "Total Quantity :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
