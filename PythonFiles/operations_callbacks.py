# Callback Function when Adding raw material
from operations import *
from PyQt5 import QtWidgets


def callback_add_raw_material(self):
    product_code = self.uiWindow.rm_new_product_code.text()
    product_name = self.uiWindow.rm_new_product_name.text()
    product_price = self.uiWindow.rm_new_product_price.text()
    if product_code and product_code and product_price:
        try:    
            if add_raw_material(product_code,product_name,int(product_price)):
                message = "Raw Material Added Succesfully"
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