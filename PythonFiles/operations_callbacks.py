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

OLD_PRODUCT_CODE = ""

def show_modify_raw_data(self):
    #TODO modify product code also
    # print("Called")
    product_code = self.uiWindow.new_rm_modify_product_code.text()
    try:
        results = return_modify_info(product_code)
        if results:
            self.uiWindow.new_rm_modify_product_name.setText(results['product_name'])
            self.uiWindow.new_rm_modify_product_price.setText(str(results['product_price']))
            self.uiWindow.new_rm_modify_product_name.setReadOnly(False)
            self.uiWindow.new_rm_modify_product_price.setReadOnly(False)
            global OLD_PRODUCT_CODE
            OLD_PRODUCT_CODE = product_code
        else:
            # TODO display popup for product code not found
            # pass
            # self.uiWindow.new_rm_modify_product_code.clear()
            self.show_info_popup("Product Code not found")
    except:
        pass


def modify_new_rm_data(self):
    product_code = self.uiWindow.new_rm_modify_product_code.text()
    product_name = self.uiWindow.new_rm_modify_product_name.text()
    product_price = self.uiWindow.new_rm_modify_product_price.text()
    if product_code and product_name and product_price:
        if product_code == OLD_PRODUCT_CODE:
            try:
                modify_info(product_code,product_name,product_price)
                self.show_info_popup("Details Modified Sucessfully")
            except:
                pass
        else:
            try:
                modify_info(OLD_PRODUCT_CODE,product_name,product_price,product_code_changed=product_code)
                self.show_info_popup("Details Modified Sucessfully")
            except:
                pass
        self.uiWindow.new_rm_modify_product_code.clear()
        self.uiWindow.new_rm_modify_product_name.clear()
        self.uiWindow.new_rm_modify_product_price.clear()
    else:
        self.show_warning_info("Please fill out the form")


def show_new_rm_del_info(self):
    product_code = self.uiWindow.new_rm_delete_product_code
    product_name = self.uiWindow.new_rm_delete_product_name
    product_price = self.uiWindow.new_rm_delete_product_price
    try:
        results = return_modify_info(product_code.text())
        if results:
            product_name.setText(str(results['product_name']))
            product_price.setText(str(results['product_price']))
        else:
            product_code.clear()
            product_price.clear()
            product_name.clear()
            self.show_warning_info("No Product Code Found")
    except:
        pass

def del_new_rm(self,btn=False):
    product_code = self.uiWindow.new_rm_delete_product_code.text()
    product_name = self.uiWindow.new_rm_delete_product_name.text()
    product_price = self.uiWindow.new_rm_delete_product_price.text()
    if product_code and product_name and product_price:
        if not btn:
            self.delete_confirm_dialog()
        elif btn.text() == "&Yes":
                try:
                    if delete_new_rm(product_code):
                        self.uiWindow.new_rm_delete_product_code.clear()
                        self.uiWindow.new_rm_delete_product_name.clear()
                        self.uiWindow.new_rm_delete_product_price.clear()
                        self.show_info_popup("Deleted Sucessfully")
                    else:
                        self.show_info_popup("Deleted Unsucessfull")
                except:
                    pass      
        elif btn.text() == "&No":
            self.uiWindow.new_rm_delete_product_code.clear()
            self.uiWindow.new_rm_delete_product_name.clear()
            self.uiWindow.new_rm_delete_product_price.clear()
                
    else:
            self.show_warning_info("Please fill out the form")

def view_new_rm_data(self):
    self.uiWindow.tableWidget_2.setRowCount(0)
    results = get_rm_data()
    # print(re sults)
    for row_number, row_data in enumerate(results):
        self.uiWindow.tableWidget_2.insertRow(row_number)
        for column_number,data in enumerate(row_data):
            self.uiWindow.tableWidget_2.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))




def display_product_name(row, column,self,col,tableWidget):
    code = tableWidget.item(row,column).text()
    if column==col:
        result = get_product_name(code)
        if result == 'false':
            tableWidget.setItem(row,column+1,QtWidgets.QTableWidgetItem("No such product code"))
        else:
            tableWidget.setItem(row, column+1, QtWidgets.QTableWidgetItem(result))


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
    # print(results)
    if results:
        self.uiWindow.shade_new__view_number.clear()
        self.uiWindow.shade_new_view_details_table.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.uiWindow.shade_new_view_details_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.uiWindow.shade_new_view_details_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    else:
        self.show_warning_info("Shade number does not exist")





# Add Raw Material Transaction 

def add_rm_transaction(self):



