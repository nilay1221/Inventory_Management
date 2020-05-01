# Callback Function when Adding raw material
from operations import *
from PyQt5 import QtWidgets


def callback_add_raw_material(self):
    product_code = self.uiWindow.rm_new_product_code.text()
    product_name = self.uiWindow.rm_new_product_name.text()
    product_price = self.uiWindow.rm_new_product_price.text()
    if product_code and product_name and product_price:
        try:    
            if add_raw_material(product_code,product_name,int(product_price)):
                message = "Raw Material Added Successfully"
                self.uiWindow.rm_new_product_code.clear()
                self.uiWindow.rm_new_product_name.clear()
                self.uiWindow.rm_new_product_price.clear()
                self.show_info_popup(message)
            else:
                message = "Product Code Already Exists"
                self.show_warning_info(message)
        except Exception as e:
            print(e)
            pass
            #TODO exception
    else:
        #TODO Error handling if any of the fields empty
        self.show_warning_info("Please fill out the info")


def show_modify_raw_data(self):
    product_code = self.uiWindow.rm_new_product_code.text()
    try:
        results = return_modify_info(product_code)
        self.uiWindow.rm_new_product_name.setText(results['product_name'])
    except:
        pass


def view_new_rm_data(self):
    self.uiWindow.tableWidget_2.setRowCount(0)
    results = get_rm_data()
    for row_number, row_data in enumerate(results):
        self.uiWindow.tableWidget_2.insertRow(row_number)
        for column_number,data in enumerate(row_data):
            self.uiWindow.tableWidget_2.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))


def display_product_name(row, column,self,col):
    code = self.uiWindow.tableWidget.item(row,column).text()
    if column==col:
        result = get_product_name(code)
        if result == 'false':
             self.uiWindow.tableWidget.setItem(row,column+1,QtWidgets.QTableWidgetItem("No such product code"))
        else:
            self.uiWindow.tableWidget.setItem(row, column+1, QtWidgets.QTableWidgetItem(result))


def add_shade_material(self):
    i=0
    shade_no = self.uiWindow.rm_new_product_code_2.text()
    if shade_no and self.uiWindow.tableWidget.item(0,0).text():
        try:
            if add_new_shade_material(shade_no):
                for i in range(10):
                    try:
                        self.uiWindow.tableWidget.item(i, 0).text()
                        row_data0 = self.uiWindow.tableWidget.item(i, 0).text()
                        row_data2 = self.uiWindow.tableWidget.item(i, 2).text()
                        try:
                            add_madeup_of(shade_no, row_data0, row_data2)
                        except:
                            pass
                    except:
                        break
                message = "Shade Number Added Successfully"
                self.uiWindow.rm_new_product_code_2.clear()
                self.uiWindow.tableWidget.clearContents()
                self.show_info_popup(message)
            else:
                message = "Shade Number Already Exists"
                self.show_warning_info(message)
        except:
            pass
    else:
        self.show_warning_info("Please fill out the info")


def view_new_shade_details(self):
    results = get_shade_details(self.uiWindow.shade_new__view_number.text())
    if results:
        self.uiWindow.shade_new__view_number.clear()
        self.uiWindow.shade_new_view_details_table.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.uiWindow.shade_new_view_details_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.uiWindow.shade_new_view_details_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    else:
        self.show_warning_info("Shade number does not exist")