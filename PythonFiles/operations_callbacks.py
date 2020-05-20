# Callback Function when Adding raw material
from operations import *
from PyQt5 import QtWidgets,QtCore,QtGui
import datetime


def callback_add_raw_material(self):
    product_code = self.uiWindow.rm_new_product_code.text()
    product_name = self.uiWindow.rm_new_product_name.text()
    product_price = self.uiWindow.rm_new_product_price.text()
    product_type = ""
    if self.uiWindow.radioButton_9.isChecked():
        product_type = "R"
    elif self.uiWindow.radioButton_10.isChecked():
        product_type = "C"
    if product_code and product_name and product_price and product_type:
        try:
            if add_raw_material(product_code, product_name, int(product_price),product_type):
                message = "Raw Material Added Successfully"
                self.uiWindow.rm_new_product_code.clear()
                self.uiWindow.rm_new_product_name.clear()
                self.uiWindow.rm_new_product_price.clear()
                if self.uiWindow.radioButton_9.isChecked():
                    self.uiWindow.radioButton_9.setChecked(False)
                else:
                    self.uiWindow.radioButton_10.setChecked(False)
                self.show_info_popup(message)
            else:
                message = "Product Code Already Exists"
                self.show_warning_info(message)
        except Exception as e:
            print(e)
            pass
            # TODO exception
    else:
        # TODO Error handling if any of the fields empty
        self.show_warning_info("Please fill out the info")


OLD_PRODUCT_CODE = ""
OLD_SHADE_NUMBER = ""

def show_modify_raw_data(self):
    # TODO modify product code also
    # print("Called")
    product_code = self.uiWindow.new_rm_modify_product_code.text()
    try:
        results = return_modify_info(product_code)
        if results:
            self.uiWindow.new_rm_modify_product_name.setText(results['product_name'])
            self.uiWindow.new_rm_modify_product_price.setText(str(results['product_price']))
            if results['product_type'] == "R":
                self.uiWindow.radioButton_7.setChecked(True)
            else:
                self.uiWindow.radioButton_8.setChecked(True)
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
    product_type = ""
    if  self.uiWindow.radioButton_7.isChecked():
        product_type = "R"
    elif self.uiWindow.radioButton_8.isChecked():
        product_type = "C"
    if product_code and product_name and product_price and product_type:
        if product_code == OLD_PRODUCT_CODE:
            try:
                modify_info(product_code, product_name, product_price,product_type)
                self.show_info_popup("Details Modified Successfully")
            except:
                pass
        else:
            try:
                # modify_info(OLD_PRODUCT_CODE, product_name, product_price, product_code_changed=product_code)
                self.show_warning_info("Cannot Modify Product Code")
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
            if results['product_type'] == "R":
                self.uiWindow.radioButton_6.setChecked(True)
            else:
                self.uiWindow.radioButton_5.setChecked(True)
        else:
            product_code.clear()
            product_price.clear()
            product_name.clear()
            self.show_warning_info("No Product Code Found")
    except:
        pass


def del_new_rm(self, btn=False):
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
                    self.show_info_popup("Deleted Successfully")
                else:
                    self.show_info_popup("Deleted UnSuccessfull")
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
    # print(results)
    for row_number, row_data in enumerate(results):
        self.uiWindow.tableWidget_2.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            if data == "C":
                data = "Colour"
            elif data == "R" :
                data="Raw Material"
            self.uiWindow.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


def display_product_name(row, column, self, col, product_type,tableWidget):
    try:
        code = tableWidget.item(row, column).text()
        list_of_entries=[]
        if column == col:
                for i in range(tableWidget.currentRow()):
                    list_of_entries.append(tableWidget.item(i, col).text())
                try:
                    if code == "":
                        tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem(""))
                    elif code in list_of_entries:
                        tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem("Product already added above"))
                    else:
                        result = get_product_name(code,product_type)
                        if result == 'false':
                            tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem("No such product code"))
                        elif result == "Product mismatch":
                            if product_type == "R" :
                                tableWidget.removeRow(row)
                                tableWidget.insertRow(row)
                                self.show_warning_info("Select only from raw materials")
                                # tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem("Only Raw Material Allowed"))
                            else:
                                tableWidget.removeRow(row)
                                tableWidget.insertRow(row)
                                self.show_warning_info("Select only from Colours")
                                # tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem("Only Colour Allowed"))
                        else:
                            tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem(result))
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)


def display_product_name_sales(row, column, self, col,tableWidget):
    if column == col or column == col -1:
        try:
            product_code = tableWidget.item(row,col).text()
            shade_number = tableWidget.item(row,col-1).text()
            list_of_entries = []
            # print(product_code)
            for i in range(tableWidget.currentRow()):
                try:
                    shade_number_before = tableWidget.item(i,col-1).text()
                    product_code_before = tableWidget.item(i,col).text()
                    list_of_entries.append((shade_number_before,product_code_before))
                except:
                    pass
            product_type = "R"
            # print(product_code)
            if (shade_number,product_code) in list_of_entries:
                tableWidget.setItem(row,col+1,QtWidgets.QTableWidgetItem("Product code already exists"))
            else:
                result = get_product_name(product_code,product_type)
                if result == 'false':
                    tableWidget.setItem(row, col + 1, QtWidgets.QTableWidgetItem("No such product code"))
                elif result == "Product mismatch":
                    if product_type == "R" :
                        tableWidget.removeRow(row)
                        tableWidget.insertRow(row)
                        self.show_warning_info("Select only from raw materials")
                        # tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem("Only Raw Material Allowed"))
                    else:
                        tableWidget.removeRow(row)
                        tableWidget.insertRow(row)
                        self.show_warning_info("Select only from Colours")
                        # tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem("Only Colour Allowed"))
                else:
                    tableWidget.setItem(row, col + 1, QtWidgets.QTableWidgetItem(result))
        except:
            pass




def add_shade_material(self):
    flag=0
    i = 0
    shade_no = self.uiWindow.rm_new_product_code_2.text()
    if shade_no and self.uiWindow.tableWidget.item(0, 0).text():
        try:
            for i in range(10):
                try:
                    if self.uiWindow.tableWidget.item(i, 0).text():
                        try:
                            if self.uiWindow.tableWidget.item(i, 0).text() and self.uiWindow.tableWidget.item(i, 2).text():
                                pass
                            if self.uiWindow.tableWidget.item(i, 0).text()=="" or self.uiWindow.tableWidget.item(i, 2).text()=="":
                                self.show_info_popup(f"Please fill the table at row '{i + 1}'")
                                flag=1
                                break
                        except:
                            self.show_info_popup(f"Please fill the table at row '{i + 1}'")
                            flag = 1
                            break
                except Exception as e:
                    print(e)
                    break
            if flag==0:
                if check_for_no_product_code(self.uiWindow.tableWidget,'C'):
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
                else:
                    message = "Please enter proper Product code"
                    self.show_warning_info(message)
        except Exception as e:
            print(e)
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
                self.uiWindow.shade_new_view_details_table.setItem(row_number, column_number,
                                                                   QtWidgets.QTableWidgetItem(str(data)))
    else:
        self.show_warning_info("Shade number does not exist")

def show_new_shade_del_info(self):
    shade_no = self.uiWindow.shade_new__delete_number.text()
    try:
        results = get_shade_details(shade_no)
        if results:
            self.uiWindow.shade_new_delete_details_table.setRowCount(0)
            for row_number, row_data in enumerate(results):
                self.uiWindow.shade_new_delete_details_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.uiWindow.shade_new_delete_details_table.setItem(row_number, column_number,
                                                                       QtWidgets.QTableWidgetItem(str(data)))
        else:
            self.uiWindow.shade_new__delete_number.clear()
            self.show_warning_info("Shade number does not exist")
    except:
        pass


def show_new_shade_modify_info(self):
    shade_no = self.uiWindow.shade_new__modify_number.text()
    try:
        results = get_shade_details(shade_no)
        if results:
            global OLD_SHADE_NUMBER
            OLD_SHADE_NUMBER=shade_no
            self.uiWindow.shade_new_modify_details_table.setRowCount(0)
            for row_number, row_data in enumerate(results):
                self.uiWindow.shade_new_modify_details_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.uiWindow.shade_new_modify_details_table.setItem(row_number, column_number,
                                                                       QtWidgets.QTableWidgetItem(str(data)))
            self.uiWindow.shade_new_modify_details_table.setRowCount(10)
        else:
            self.uiWindow.shade_new__modify_number.clear()
            self.show_warning_info("Shade number does not exist")
    except Exception as e:
        print(e)


def del_new_shade(self, btn=False):
    shade_no = self.uiWindow.shade_new__delete_number.text()
    if shade_no:
        if not btn:
            self.delete_confirm_dialog_shade_number()
        elif btn.text() == "&Yes":
            try:
                if new_shade_delete(shade_no):
                    self.uiWindow.shade_new__delete_number.clear()
                    self.uiWindow.shade_new_delete_details_table.clearContents()
                    self.show_info_popup("Deleted Successfully")
                else:
                    self.show_info_popup("Deleted Unsuccessfull")
            except Exception as e:
                print(e)
        elif btn.text() == "&No":
            self.uiWindow.shade_new__delete_number.clear()
            self.uiWindow.shade_new_delete_details_table.clearContents()
    else:
        self.show_warning_info("Please fill out the form")

def modify_new_shade_data(self,show=1):
    flag=0
    shade_no = self.uiWindow.shade_new__modify_number.text()
    if shade_no and self.uiWindow.shade_new_modify_details_table.item(0, 0).text():
        try:
            for i in range(10):
                try:
                    if self.uiWindow.shade_new_modify_details_table.item(i, 0).text():
                        try:
                            if self.uiWindow.shade_new_modify_details_table.item(i, 0).text() and self.uiWindow.shade_new_modify_details_table.item(i, 2).text():
                                pass
                            if self.uiWindow.shade_new_modify_details_table.item(i,2).text()=="":
                                self.show_info_popup(f"Please fill the table at row '{i + 1}'")
                                flag = 1
                                break
                        except:
                            self.show_info_popup(f"Please fill the table at row '{i + 1}'")
                            flag = 1
                            break
                except Exception as e:
                    # print("inside exception")
                    break
            if flag==0:
                if shade_no == OLD_SHADE_NUMBER:
                    try:
                        if check_for_no_product_code(self.uiWindow.shade_new_modify_details_table,'C'):
                            if remove_previous_data(shade_no):
                                for i in range(10):
                                    try:
                                        self.uiWindow.shade_new_modify_details_table.item(i, 0).text()
                                        row_data0 = self.uiWindow.shade_new_modify_details_table.item(i, 0).text()
                                        row_data2 = self.uiWindow.shade_new_modify_details_table.item(i, 2).text()
                                        try:
                                            modify_shade_data(shade_no, row_data0, row_data2)
                                        except:
                                            pass
                                    except:
                                        break
                            if show==1:
                                self.show_info_popup("Details Modified Successfully")
                        else:
                            message = "Please enter proper Product code"
                            self.show_warning_info(message)
                    except:
                        pass
                else:
                    try:
                        if check_for_no_product_code(self.uiWindow.shade_new_modify_details_table,'C'):
                            if readd_shade_material_on_modify(self):
                                self.show_info_popup("Details Modified Successfully")
                        else:
                            message = "Please enter proper Product code"
                            self.show_warning_info(message)
                    except:
                        pass
                self.uiWindow.shade_new__modify_number.clear()
                self.uiWindow.shade_new_modify_details_table.clearContents()
        except:
            pass
    else:
        self.show_warning_info("Please fill out the form")


def readd_shade_material_on_modify(self):
    global OLD_SHADE_NUMBER
    shade_no = self.uiWindow.shade_new__modify_number.text()
    if shade_no and self.uiWindow.shade_new_modify_details_table.item(0, 0).text():
        try:
            if modify_new_shade_material(shade_no,OLD_SHADE_NUMBER):
                OLD_SHADE_NUMBER=shade_no
                modify_new_shade_data(self,2)
                return True
            else:
                self.show_warning_info("Shade Number Already Exists")
                return False
        except Exception as e:
            print(e)
    else:
        self.show_warning_info("Please fill out the info")


def shade_view_all(self):
    self.uiWindow.shade_new_viewall_details_table.setRowCount(0)
    results = get_shade_all()
    # print(results)
    for row_number, row_data in enumerate(results):
        self.uiWindow.shade_new_viewall_details_table.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.uiWindow.shade_new_viewall_details_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


# Add Raw Material Transaction

def set_raw_material_data(self):
    trans_id = get_trans_id("rm_stock",'RMT')
    date = datetime.date.today().strftime("%d-%m-%Y")
    self.uiWindow.rm_transaction_id.setText(str(trans_id))
    self.uiWindow.date.setText(str(date))


def add_raw_material_callback(self):
    # print("Inside")
    # TODO check if table is empty or not
    trans_id_widget = self.uiWindow.rm_transaction_id                                                                                                                                                                     
    date_widget = self.uiWindow.date
    customer_widget = self.uiWindow.rm_customer
    remark_widget = self.uiWindow.rw_remark
    trans_id = 'RMT' +  str(trans_id_widget.text())
    date = date_widget.text()
    customer = customer_widget.currentText()
    remark = remark_widget.text()
    if customer and remark:
        check_table = check_for_no_product_code(self.uiWindow.rm_addtable,"R")
        if check_table == "True":
            products = []
            for i in range(8):
                try:
                    if self.uiWindow.rm_addtable.item(i,0).text() and self.uiWindow.rm_addtable.item(i,2).text() and self.uiWindow.rm_addtable.item(i,3).text():
                        product_code = self.uiWindow.rm_addtable.item(i,0).text()
                        quantity = self.uiWindow.rm_addtable.item(i,2).text()
                        lot = self.uiWindow.rm_addtable.item(i, 3).text()
                        products.append((product_code,float(quantity),"R",lot))
                except:
                    try:
                        self.uiWindow.rm_addtable.item(i,0).text()
                        self.show_warning_info("Please fill info")
                        break
                    except:
                        # print("inside exception")
                        if products:
                            # print(products)
                            if add_raw_material_data(self,trans_id,date,customer,remark,products):
                                # print("Inside")
                                set_raw_material_data(self)
                                customer_widget.clearEditText()
                                remark_widget.clear()
                                self.uiWindow.rm_addtable.clearContents()
                                self.show_info_popup("Transaction Added Successfully")
                                break
                        else:
                            print("in")
                            self.show_warning_info("Please fill info")
                            break
        elif check_table == "False" :
            self.show_warning_info("Please fill out from available product code")
        elif check_table == "Product Mismatch":
            self.show_warning_info("Please fill only Raw Material")
    else:
        self.show_warning_info("Please fill out the form")


def view_rm_by_id(self):
    #TODO make table uneditable
    trans_id = "RMT" + str(self.uiWindow.rw_view_transaction_id.text()).zfill(5)
    results = get_rm_transacs(by_Id=trans_id)
    # print(results)
    if results:
        date = results[0][1]
        remark = results[0][2]
        customer = results[0][3]
        self.uiWindow.rm_view_date.setText(str(date))
        self.uiWindow.rm_view_remark.setText(str(remark))
        self.uiWindow.rm_view_customer.setCurrentText(customer)
        self.uiWindow.rm_view_table_4.setRowCount(0)
        for row in range(len(results[1])):
            self.uiWindow.rm_view_table_4.insertRow(row)
            for column in range(len(results[1][row])):
                value = results[1][row][column]
                # print(value)
                if value != '-':
                    self.uiWindow.rm_view_table_4.setItem(row,column,QtWidgets.QTableWidgetItem(str(value)))
    else:
        self.uiWindow.rw_view_transaction_id.clear()
        self.uiWindow.rm_view_date.clear()
        self.uiWindow.rm_view_remark.clear()
        self.uiWindow.rm_view_table_4.clearContents()
        self.uiWindow.rm_view_table_4.setRowCount(0)
        self.uiWindow.rm_view_customer.clearEditText()
        self.show_warning_info("Transaction id not found")


def view_rm_by_today(self):
    self.uiWindow.rm_view_today_date.setDate(QtCore.QDate.currentDate())
    self.uiWindow.rm_view_table_5.setRowCount(0)
    results = get_rm_transacs(by_Today=True)
    if results:
        trans_list=[]
        for row in range(len(results)):
            self.uiWindow.rm_view_table_5.insertRow(row)
            for column in range(len(results[row])):
                if column == 0:
                    if str(results[row][column]) not in trans_list:
                        trans_list.append(str(results[row][column]))
                        self.uiWindow.rm_view_table_5.setItem(row,column,QtWidgets.QTableWidgetItem(str(results[row][column])))
                elif results[row][column] != '-':
                    self.uiWindow.rm_view_table_5.setItem(row,column,QtWidgets.QTableWidgetItem(str(results[row][column])))

    else:
        self.show_info_popup("No Transactions Done Today")

def set_delete_rm(self):
    trans_id = "RMT" + str(self.uiWindow.rw_delete_transaction_id.text()).zfill(5)
    # print(trans_id)
    if check_rm_transacs(trans_id) :
        results = get_rm_transacs(by_Id=trans_id)
        # print(results)
        if results:
            date = results[0][1]
            remark = results[0][2]
            customer = results[0][3]
            self.uiWindow.rm_delete_date.setText(str(date))
            self.uiWindow.rm_delete_remark.setText(str(remark))
            self.uiWindow.rm_delete_customer.setCurrentText(customer)
            self.uiWindow.rm_delete_table.setRowCount(0)
            for row in range(len(results[1])):
                self.uiWindow.rm_delete_table.insertRow(row)
                for column in range(len(results[1][row])):
                    value = results[1][row][column]
                    # print(value)
                    if value != '-' :
                        self.uiWindow.rm_delete_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(value)))

    else:
        self.show_warning_info("Invalid Transaction Code")

def delete_rm(self,btn):
    trans_id = "RMT" + str(self.uiWindow.rw_delete_transaction_id.text()).zfill(5)
    if check_rm_transacs(trans_id):
        if btn.text() == "&Yes":
            delete_rm_transacs(trans_id)
            self.show_info_popup("Deleted Successfully")
            self.uiWindow.rw_delete_transaction_id.clear()
            self.uiWindow.rm_delete_date.clear()
            self.uiWindow.rm_delete_customer.clearEditText()
            self.uiWindow.rm_delete_remark.clear()
            self.uiWindow.rm_delete_table.clearContents()
            self.uiWindow.rm_delete_table.setRowCount(0)
    else:
        self.show_warning_info("Invalid Transaction Code")


def set_modify_rm(self):
    trans_id = "RMT" + str(self.uiWindow.rw_modify_transaction_id.text()).zfill(5)
    # print(trans_id)
    if check_rm_transacs(trans_id) :
        results = get_rm_transacs(by_Id=trans_id)
        # print(results)
        if results:
            date = results[0][1]
            remark = results[0][2]
            customer = results[0][3]
            self.uiWindow.rm_modify_date.setText(str(date))
            self.uiWindow.rm_modify_remark.setText(str(remark))
            self.uiWindow.rm_modify_customer.setCurrentText(customer)
            self.uiWindow.rm_view_table.setRowCount(0)
            for row in range(len(results[1])):
                self.uiWindow.rm_view_table.insertRow(row)
                for column in range(len(results[1][row])):
                    value = results[1][row][column]
                    # print(value)
                    if str(value)!='-':
                        self.uiWindow.rm_view_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(value)))
            self.uiWindow.rm_view_table.setRowCount(8)

    else:
        self.show_warning_info("Invalid Transaction Code")
        self.uiWindow.rw_modify_transaction_id.clear()
        self.uiWindow.rm_modify_date.clear()
        self.uiWindow.rm_modify_customer.clearEditText()
        self.uiWindow.rm_modify_remark.clear()
        self.uiWindow.rm_view_table.clearContents()


def modify_rm(self):
    # print("Inside")
    trans_id = "RMT" + str(self.uiWindow.rw_modify_transaction_id.text()).zfill(5)
    if check_rm_transacs(trans_id):
        # print("Deleted")
        trans_id_widget = self.uiWindow.rw_modify_transaction_id
        date_widget = self.uiWindow.rm_modify_date
        customer_widget = self.uiWindow.rm_modify_customer
        remark_widget = self.uiWindow.rm_modify_remark
        trans_id = 'RMT' +  str(trans_id_widget.text()).zfill(5)
        date = date_widget.text()
        customer = customer_widget.currentText()
        remark = remark_widget.text()
        if customer and remark:
            check_table = check_for_no_product_code(self.uiWindow.rm_view_table,"R")
            if check_table == "True":
                products = []
                for i in range(8):
                    try:
                        if self.uiWindow.rm_view_table.item(i,0).text() and self.uiWindow.rm_view_table.item(i,2).text() and self.uiWindow.rm_view_table.item(i,3).text():
                            product_code = self.uiWindow.rm_view_table.item(i,0).text()
                            quantity = self.uiWindow.rm_view_table.item(i,2).text()
                            lot = self.uiWindow.rm_view_table.item(i,3).text()
                            products.append((product_code,float(quantity),"R",lot))
                    except:
                        try:
                            self.uiWindow.rm_view_table.item(i,0).text()
                            self.show_warning_info("Please fill info")
                            break
                        except:
                            # print("inside exception")
                            # print(products)
                            if products:
                                delete_rm_transacs(trans_id)
                                if add_raw_material_data(self,trans_id,date,customer,remark,products):
                                    # set_raw_material_data(self)
                                    self.uiWindow.rw_modify_transaction_id.clear()
                                    self.uiWindow.rm_modify_date.clear()
                                    customer_widget.clearEditText()
                                    remark_widget.clear()
                                    self.uiWindow.rm_view_table.clearContents()
                                    self.show_info_popup("Transaction Modified Successfully")
                                    break
                            else:
                                self.show_warning_info("Please fill info")
                                break
            elif check_table == "False" :
                self.show_warning_info("Please fill out from available product code")
            elif check_table == "Product Mismatch":
                self.show_warning_info("Please fill only Raw Material")
            
        else:
            self.show_warning_info("Please fill out the form")


def view_by_custom_dates(self):
    d1 = self.uiWindow.rw_view_starting_date_3.date()
    d2 = self.uiWindow.rw_view_ending_date_2.date()
    x = d1.toString('dd/MM/yyyy')
    y = d2.toString('dd/MM/yyyy')
    # print(type(x))
    x_date = datetime.datetime.strptime(x,'%d/%m/%Y')
    y_date = datetime.datetime.strptime(y,'%d/%m/%Y')
    delta = y_date - x_date
    if delta.days > 0:
        results = get_rm_transacs(by_custom=[x,y])
        if results:
            self.uiWindow.rm_view_table_3.setRowCount(0)
            trans_list=[]
            for each_list in results: 
                for row in range(len(each_list)):
                    self.uiWindow.rm_view_table_3.insertRow(row)
                    for column in range(len(each_list[row])):
                        if column ==0:
                            if str(each_list[row][column]) not in trans_list:
                                trans_list.append(str(each_list[row][column]))
                                self.uiWindow.rm_view_table_3.setItem(row,column,QtWidgets.QTableWidgetItem(str(each_list[row][column])))
                        elif each_list[row][column] != '-':
                            self.uiWindow.rm_view_table_3.setItem(row, column, QtWidgets.QTableWidgetItem(
                                str(each_list[row][column])))
        else:
            pass
    else:
        self.show_warning_info("Please select correct date")

# Set Transaction ID and date for Adding Shade Number Transaction
def set_shade_number_transacs(self):
    trans_id = str(get_trans_id('shade_stock','SNT'))
    date = datetime.date.today().strftime("%d-%m-%Y")
    self.uiWindow.shade_transaction_id.setText(trans_id)
    self.uiWindow.date_2.setText(date)

ORIGIGNAL_PRICES = []

def set_shade_number_details(self,shadeNumberwidget,rawTable,shadeTable,addTotal):
    global ORIGIGNAL_PRICES
    ORIGIGNAL_PRICES = []
    shade_number = shadeNumberwidget.text()
    if check_shade_number_exists(shade_number):
        results = get_shade_number_details(shade_number)
        shadeTable.setRowCount(0)
        for row in range(len(results)):
            shadeTable.insertRow(row)
            for column in range(len(results[0])):
                if column == 4:
                    ORIGIGNAL_PRICES.append(results[row][column])
                if results[row][column] != '-':
                    shadeTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(results[row][column])))
        if addTotal.text():
            # print("inside")
            set_total_quantity(0,2,self,rawTable,shadeTable,addTotal)
    else:
        self.show_warning_info("Shade Number Does not exists")

def set_total_quantity(row,column,self,tableWidget1,tableWidget2,quantitywidget):
    #TODO Check for empty
    if column == 2:
        # if self.uiWindow.shade_add_total.text():
        #     present_quantity = float(self.uiWindow.shade_add_total.text())
        # else:
        #     present_quantity = float(0)
        # new_quantity = float(self.uiWindow.shade_addtable_3.item(row,column).text())
        # total_quantity = present_quantity + new_quantity
        # self.uiWindow.shade_add_total.setText(str(total_quantity))
        total_quantity = 0
        for i in range(8):
            try:
                quantity = float(tableWidget1.item(i,2).text())
                total_quantity += quantity
            except:
                pass
                # pass
        # print(total_quantity)
        quantitywidget.setText(str(total_quantity))
        for i in range(tableWidget2.rowCount()):
            # print(i)
            try:
                percentage = float(tableWidget2.item(i,2).text())
                # print(percentage)
                quantity = (percentage * total_quantity)*10
                price = (quantity * float(ORIGIGNAL_PRICES[i]))/1000
                tableWidget2.setItem(i,3,QtWidgets.QTableWidgetItem(str(quantity)))
                tableWidget2.setItem(i,4,QtWidgets.QTableWidgetItem(str(price)))
            except:
                pass

def confirm_add_shade_number(self):
    repeat=[]
    flag=0
    checkrepeat=0
    trans_widget = self.uiWindow.shade_transaction_id
    date_widget = self.uiWindow.date_2
    customer_widget = self.uiWindow.shade_customer
    remark_widget = self.uiWindow.shade_remark
    shade_number_widget = self.uiWindow.shade_number_add
    trans_id = "SNT" +  str(trans_widget.text())
    date = date_widget.text()
    customer = customer_widget.currentText()
    remark = remark_widget.text()
    shade_number = shade_number_widget.text()
    if trans_id and date and customer and remark and shade_number:
        try:
            for i in range(self.uiWindow.shade_colortable.rowCount()):
                self.uiWindow.shade_colortable.item(i, 5).text()
        except:
            flag = 1
            self.show_warning_info(f"Please fill out the lot in second table at row '{i+1}'")
        if get_shade(shade_number) and flag==0:
            table_check = check_for_no_product_code(self.uiWindow.shade_addtable,"R")
            if table_check == "True":
                try:
                    row_count_1 = self.uiWindow.shade_addtable.rowCount()
                    row_count_2 = self.uiWindow.shade_colortable.rowCount()
                    try:
                        results = []
                        raw_details = []
                        for i in range(row_count_1):
                                if self.uiWindow.shade_addtable.item(i,0).text() and self.uiWindow.shade_addtable.item(i,2).text() and self.uiWindow.shade_addtable.item(i,3).text():
                                    x = self.uiWindow.shade_addtable.item(i,0).text()
                                    y = self.uiWindow.shade_addtable.item(i,2).text()
                                    z = self.uiWindow.shade_addtable.item(i,3).text()
                                    results.append((x,y,"R",z))
                                    raw_details.append((x,y,z))
                                else:
                                    raise Exception
                    except:
                        try:
                            if i!=0:
                                if not self.uiWindow.shade_addtable.item(i,0).text():
                                    raise Exception
                            self.show_warning_info("Please complete table")
                        except:
                            for i in range(row_count_2):
                                x = self.uiWindow.shade_colortable.item(i,0).text()
                                y = float(self.uiWindow.shade_colortable.item(i,3).text())/1000
                                z = self.uiWindow.shade_colortable.item(i,5).text()
                                for each in raw_details:
                                    if x == each[0]:
                                        # print(each[0])
                                        # print(x)
                                        raise Exception("Colour cannot be used")
                                results.append((x,y,"C",z))
                                # raw_details.append((x,y))
                            for i in range(len(raw_details)):
                                temp=[self.uiWindow.shade_addtable.item(i,0).text(),self.uiWindow.shade_addtable.item(i,3).text()]
                                if temp not in repeat:
                                    repeat.append(temp)
                                else:
                                    checkrepeat = 1
                                    message=f"Entry repeated for {temp[0]}"
                                    self.show_warning_info(message)
                                    break
                            if checkrepeat==0:
                                negative_trans_id = "SRT" + str(get_trans_id('rm_stock','SRT'))
                                # print(results)
                                if add_raw_material_data(self,negative_trans_id,date,customer,remark,results,type="OUT"):
                                    add_shade_stock_trans(self,trans_id,date,customer,remark,shade_number,raw_details)
                                    add_into_duplicates(trans_id,negative_trans_id)
                                    message1 = ""
                                    message2 = ""
                                    for each_raw in results:
                                        x = raw_material_closing_stock(each_raw[0],each_raw[3])
                                        try:
                                            if x < 0:
                                                message2 = message2 + f"Closing stock for {each_raw[0]}  is {x} in lot {each_raw[3]}<br>"
                                            else:
                                                message1 = message1 + f"Closing stock for {each_raw[0]}  is {x} in lot {each_raw[3]}<br>"
                                        except:
                                            pass
                                    self.show_stock_popup(message1, message2)
                                    self.show_info_popup("Transaction Completed Successfully")
                                    set_shade_number_transacs(self)
                                    self.uiWindow.shade_customer.clearEditText()
                                    self.uiWindow.shade_remark.clear()
                                    self.uiWindow.shade_number_add.clear()
                                    self.uiWindow.shade_addtable.clearContents()
                                    self.uiWindow.shade_colortable.clearContents()
                                    self.uiWindow.shade_add_total.clear()
                                else:
                                    self.show_warning_info("Transaction UnSuccessfull")
                except Exception as err:
                    self.show_warning_info(err.__str__())
            elif table_check == "False":
                self.show_warning_info("Please choose from available product codes")
            elif table_check == "Product Mismatch":
                self.show_warning_info("Please choose Raw Material only")
        else:
            if flag!=1:
                self.show_warning_info("Please enter correct shade number")
                self.uiWindow.shade_number_add.clear()
    else:
        self.show_warning_info("Please fill out the info")

def view_shade_stock_by_id(self):
    trans_id = "SNT" +  str(self.uiWindow.shade_view_transaction_id.text()).zfill(5)
    if check_shade_trans(trans_id):
        results = view_shade_transaction(by_Id=trans_id)
        trans_details = results['trans_details']
        self.uiWindow.date_3.setText(str(trans_details[0]))
        self.uiWindow.shade_view_customer.setEditText(str(trans_details[1]))
        self.uiWindow.shade_view_remark.setText(str(trans_details[2]))
        self.uiWindow.shade_number_add_view.setText(str(trans_details[3]))
        table1_details = results['table1_details']
        self.uiWindow.shade_addtable_4.setRowCount(0)
        total_quantity = 0 
        for each_row in range(len(table1_details)):
            self.uiWindow.shade_addtable_4.insertRow(each_row)
            for each_column in range(len(table1_details[each_row])):
                if each_column == 2:
                    total_quantity += table1_details[each_row][each_column]
                if table1_details[each_row][each_column] != '-':
                    self.uiWindow.shade_addtable_4.setItem(each_row,each_column,QtWidgets.QTableWidgetItem(str(table1_details[each_row][each_column])))
        table2_details = results['table2_detials']
        self.uiWindow.shade_colortable_4.setRowCount(0)
        for row in range(len(table2_details)):
            self.uiWindow.shade_colortable_4.insertRow(row)
            for column in range(len(table2_details[row])):
                if table2_details[row][column] != '-':
                    self.uiWindow.shade_colortable_4.setItem(row,column,QtWidgets.QTableWidgetItem(str(table2_details[row][column])))
        self.uiWindow.shade_add_total_4.setText(str(total_quantity))

    else:
        self.show_warning_info("Incorrect transaction id")



def view_shade_transaction_today(self):
    trans_list=[]
    self.uiWindow.shade_view_today_date.setDate(QtCore.QDate.currentDate())
    results = view_shade_transaction(by_today=True)
    if results:
        # print(results)
        self.uiWindow.shade_view_table_2.setRowCount(0)
        for row in range(len(results)):
            self.uiWindow.shade_view_table_2.insertRow(row)
            for column in range(len(results[row])):
                if column == 0:
                    if str(results[row][column]) not in trans_list:
                        trans_list.append(str(results[row][column]))
                        self.uiWindow.shade_view_table_2.setItem(row, column,
                                                               QtWidgets.QTableWidgetItem(str(results[row][column])))
                elif results[row][column] != '-':
                    self.uiWindow.shade_view_table_2.setItem(row,column,QtWidgets.QTableWidgetItem(str(results[row][column])))
    else:
        self.show_info_popup("No Transactions Done Today")


def set_delete_shade_transaction(self):
    trans_id = "SNT" + str(self.uiWindow.shade_delete_transaction_id.text()).zfill(5)
    if check_shade_trans(trans_id):
        results = view_shade_transaction(by_Id=trans_id)
        trans_details = results['trans_details']
        self.uiWindow.shade_delete_date.setText(str(trans_details[0]))
        self.uiWindow.shade_delete_customer.setEditText(str(trans_details[1]))
        self.uiWindow.shade_delete_remark.setText(str(trans_details[2]))
        self.uiWindow.shade_number_delete.setText(str(trans_details[3]))
        table1_details = results['table1_details']
        self.uiWindow.shade_addtable_2.setRowCount(0)
        total_quantity = 0 
        for each_row in range(len(table1_details)):
            self.uiWindow.shade_addtable_2.insertRow(each_row)
            for each_column in range(len(table1_details[each_row])):
                if each_column == 2:
                    total_quantity += table1_details[each_row][each_column]
                if table1_details[each_row][each_column] != '-':
                    self.uiWindow.shade_addtable_2.setItem(each_row,each_column,QtWidgets.QTableWidgetItem(str(table1_details[each_row][each_column])))
        table2_details = results['table2_detials']
        self.uiWindow.shade_colortable_2.setRowCount(0)
        for row in range(len(table2_details)):
            self.uiWindow.shade_colortable_2.insertRow(row)
            for column in range(len(table2_details[row])):
                if table2_details[row][column] != '-':
                    self.uiWindow.shade_colortable_2.setItem(row,column,QtWidgets.QTableWidgetItem(str(table2_details[row][column])))
        self.uiWindow.shade_add_total_2.setText(str(total_quantity))
    else:
        self.show_warning_info("Transaction id does not exists")


def delete_shade_transaction(self,btn):
    trans_id = "SNT" + str(self.uiWindow.shade_delete_transaction_id.text()).zfill(5)
    if check_shade_trans(trans_id):
        if btn.text() == "&Yes":
            if delete_shade_trans(trans_id):
                self.show_info_popup("Deleted Successfully")
                self.uiWindow.shade_delete_transaction_id.clear()
                self.uiWindow.shade_delete_date.clear()
                self.uiWindow.shade_delete_customer.clearEditText()
                self.uiWindow.shade_delete_remark.clear()
                self.uiWindow.shade_number_delete.clear()
                self.uiWindow.shade_addtable_2.clearContents()
                self.uiWindow.shade_colortable_2.clearContents()
                self.uiWindow.shade_add_total_2.clear()
            else:
                self.show_warning_info("Deletion UnSuccessful")


def set_modify_shade_transaction(self):
    # print("Called")
    trans_id = "SNT" +  str(self.uiWindow.shade_modify_transaction_id.text()).zfill(5)
    if check_shade_trans(trans_id):
        results = view_shade_transaction(by_Id=trans_id)
        trans_details = results['trans_details']
        self.uiWindow.shade_modify_date.setText(str(trans_details[0]))
        self.uiWindow.shade_modify_customer.setEditText(str(trans_details[1]))
        self.uiWindow.shade_modify_remark.setText(str(trans_details[2]))
        self.uiWindow.shade_number_modify.setText(str(trans_details[3]))
        table1_details = results['table1_details']
        # print(table1_details)
        self.uiWindow.shade_addtable_3.setRowCount(0)
        total_quantity = 0 
        for each_row in range(len(table1_details)):
            self.uiWindow.shade_addtable_3.insertRow(each_row)
            for each_column in range(len(table1_details[each_row])):
                if each_column == 2:
                    total_quantity += table1_details[each_row][each_column]
                if table1_details[each_row][each_column] != '-':
                    self.uiWindow.shade_addtable_3.setItem(each_row,each_column,QtWidgets.QTableWidgetItem(str(table1_details[each_row][each_column])))
        table2_details = results['table2_detials']
        self.uiWindow.shade_add_total_3.setText(str(total_quantity))
        # set_shade_number_details(self,self.uiWindow.shade_number_modify,self.uiWindow.shade_addtable_3,self.uiWindow.shade_colortable_3,self.uiWindow.shade_add_total_3)
        self.uiWindow.shade_colortable_3.setRowCount(0)
        for row in range(len(table2_details)):
            self.uiWindow.shade_colortable_3.insertRow(row)
            for column in range(len(table2_details[row])):
                if table2_details[row][column] != '-':
                    self.uiWindow.shade_colortable_3.setItem(row,column,QtWidgets.QTableWidgetItem(str(table2_details[row][column])))
        self.uiWindow.shade_addtable_3.setRowCount(8)
    else:
        self.show_warning_info("Incorrect transaction id")


def confirm_modify_shade_trans(self):
    repeat=[]
    checkrepeat=0
    trans_id = "SNT" + str(self.uiWindow.shade_modify_transaction_id.text()).zfill(5)
    flag=0
    try:
        if check_shade_trans(trans_id):
                negative_trans_id = get_raw_trans(trans_id)
                # print(negative_trans_id)
                trans_widget = self.uiWindow.shade_modify_transaction_id
                date_widget = self.uiWindow.shade_modify_date
                customer_widget = self.uiWindow.shade_modify_customer
                remark_widget = self.uiWindow.shade_modify_remark
                shade_number_widget = self.uiWindow.shade_number_modify
                # trans_id = "SNT" +  str(trans_widget.text())
                date = date_widget.text()
                customer = customer_widget.currentText()
                remark = remark_widget.text()
                shade_number = shade_number_widget.text()
                if trans_id and date and customer and remark and shade_number:
                    try:
                        for i in range(self.uiWindow.shade_colortable_3.rowCount()):
                            self.uiWindow.shade_colortable_3.item(i,5).text()
                    except:
                        flag=1
                        self.show_warning_info(f"Please fill out the lot in second table at row '{i+1}'")
                    if get_shade(shade_number) and flag==0:
                        table_check = check_for_no_product_code(self.uiWindow.shade_addtable_3,"R")
                        if table_check == "True":
                            try:
                                row_count_1 = self.uiWindow.shade_addtable_3.rowCount()
                                row_count_2 = self.uiWindow.shade_colortable_3.rowCount()
                                try:
                                    results = []
                                    raw_details = []
                                    for i in range(row_count_1):
                                            if self.uiWindow.shade_addtable_3.item(i,0).text() and self.uiWindow.shade_addtable_3.item(i,2).text() and self.uiWindow.shade_addtable_3.item(i,3).text():
                                                x = self.uiWindow.shade_addtable_3.item(i,0).text()
                                                y = self.uiWindow.shade_addtable_3.item(i,2).text()
                                                z = self.uiWindow.shade_addtable_3.item(i,3).text()
                                                results.append((x,y,"R",z))
                                                raw_details.append((x,y,z))
                                            else:
                                                raise Exception
                                except:
                                    try:
                                        if i!=0:
                                            if not self.uiWindow.shade_addtable_3.item(i,0).text():
                                                raise Exception
                                        self.show_warning_info("Please complete table")
                                    except:
                                        for i in range(row_count_2):
                                            x = self.uiWindow.shade_colortable_3.item(i,0).text()
                                            y = float(self.uiWindow.shade_colortable_3.item(i,3).text())/1000
                                            z = self.uiWindow.shade_colortable_3.item(i,5).text()
                                            for each in raw_details:
                                                if x == each[0]:
                                                    # print(each[0])
                                                    # print(x)
                                                    raise Exception("Colour cannot be used")
                                            results.append((x,y,"C",z))
                                            # raw_details.append((x,y))

                                        # negative_trans_id = "SRT" + str(get_trans_id('rm_stock','SRT'))
                                        # print(results)
                                        for i in range(len(raw_details)):
                                            temp = [self.uiWindow.shade_addtable_3.item(i, 0).text(),
                                                    self.uiWindow.shade_addtable_3.item(i, 3).text()]
                                            if temp not in repeat:
                                                repeat.append(temp)
                                            else:
                                                checkrepeat = 1
                                                message = f"Entry repeated for {temp[0]}"
                                                self.show_warning_info(message)
                                                break
                                        if checkrepeat == 0:
                                            delete_shade_trans(trans_id)
                                            if add_raw_material_data(self,negative_trans_id,date,customer,remark,results,type="OUT"):
                                                add_shade_stock_trans(self,trans_id,date,customer,remark,shade_number,raw_details)
                                                add_into_duplicates(trans_id,negative_trans_id)
                                                message1 = ""
                                                message2 = ""
                                                for each_raw in results:
                                                    x= raw_material_closing_stock(each_raw[0],each_raw[3])
                                                    if x < 0:
                                                        message2 = message2 + f"Closing stock for {each_raw[0]}  is {x} in lot {each_raw[3]} in lot {each_raw[3]}<br>"
                                                    else:
                                                        message1 = message1 + f"Closing stock for {each_raw[0]}  is '{x} in lot {each_raw[3]} in lot {each_raw[3]}<br>"
                                                self.show_stock_popup(message1, message2)
                                                self.show_info_popup("Transaction Modified Successfully")
                                                # set_shade_number_transacs(self)
                                                self.uiWindow.shade_modify_transaction_id.clear()
                                                self.uiWindow.shade_modify_date.clear()
                                                self.uiWindow.shade_modify_customer.clearEditText()
                                                self.uiWindow.shade_modify_remark.clear()
                                                self.uiWindow.shade_number_modify.clear()
                                                self.uiWindow.shade_addtable_3.clearContents()
                                                self.uiWindow.shade_colortable_3.clearContents()
                                                self.uiWindow.shade_add_total_3.clear()
                                            else:
                                                self.show_warning_info("Transaction UnSuccessfull")
                            except Exception as err:
                                self.show_warning_info(err.__str__())
                        elif table_check == "False":
                            self.show_warning_info("Please fill out from available product code")
                        elif table_check == "Product Mismatch":
                            self.show_warning_info("Please select Raw Materials Only")
                    else:
                        if flag!=1:
                            self.show_warning_info("Please enter correct shade number")
                            self.uiWindow.shade_number_modify.clear()
                else:
                    self.show_warning_info("Please fill out the info")
    except Exception as e:
        print(e)


def shade_view_by_custom_dates(self):
    d1 = self.uiWindow.shade_view_start_date.date()
    d2 = self.uiWindow.shade_view_end_date.date()
    x = d1.toString('dd/MM/yyyy')
    y = d2.toString('dd/MM/yyyy')
    # print(type(x))
    x_date = datetime.datetime.strptime(x,'%d/%m/%Y')
    y_date = datetime.datetime.strptime(y,'%d/%m/%Y')
    delta = y_date - x_date
    if delta.days > 0:
        results = view_shade_transaction(by_custom=[x,y])
        if results:
            self.uiWindow.shade_view_table.setRowCount(0)
            trans_list=[]
            for each_list in results: 
                for row in range(len(each_list)):
                    self.uiWindow.shade_view_table.insertRow(row)
                    for column in range(len(each_list[row])):
                        if column ==0:
                            if str(each_list[row][column]) not in trans_list:
                                trans_list.append(str(each_list[row][column]))
                                self.uiWindow.shade_view_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(each_list[row][column])))
                        elif each_list[row][column] != '-':
                            self.uiWindow.shade_view_table.setItem(row, column, QtWidgets.QTableWidgetItem(
                                str(each_list[row][column])))
        else:
            pass
    else:
        self.show_warning_info("Please select correct date")


def check_for_no_product_code(tableWidget,product_type):
    results = tableWidget.findItems("No such product code",QtCore.Qt.MatchExactly)
    if product_type == "R":
        results1 = tableWidget.findItems("Only Raw Material Allowed",QtCore.Qt.MatchExactly)
    elif product_type == "C" :
        results1 = tableWidget.findItems("Only Colour Allowed",QtCore.Qt.MatchExactly)
    if results:
        return "False"
    elif results1:
        return "Product Mismatch"
    else:
        return "True"


def set_sales_data(self):
    trans_id = get_trans_id("sales",'SLS')
    date = datetime.date.today().strftime("%d-%m-%Y")
    self.uiWindow.sales_add_transid.setText(str(trans_id))
    self.uiWindow.sales_add_date.setText(str(date))


def add_sales_callback(self):
    # print("Inside")
    # TODO check if table is empty or not
    flag = 0
    tableflag=0
    try:
        trans_id_widget = self.uiWindow.sales_add_transid
        date_widget = self.uiWindow.sales_add_date
        customer_widget = self.uiWindow.sales_add_customer
        remark_widget = self.uiWindow.sales_add_remark
        trans_id = 'SLS' +  str(trans_id_widget.text())
        date = date_widget.text()
        customer = customer_widget.currentText()
        remark = remark_widget.text()
        if customer and remark:
            try:
                for i in range(self.uiWindow.sales_add_table.rowCount()):
                    self.uiWindow.sales_add_table.item(i,0).text()
                    self.uiWindow.sales_add_table.item(i, 1).text()
                    self.uiWindow.sales_add_table.item(i, 3).text()
                    self.uiWindow.sales_add_table.item(i, 4).text()
            except:
                try:
                    if i != 0:
                        if not self.uiWindow.shade_addtable.item(i, 0).text():
                            raise Exception
                    tableflag=1
                    self.show_warning_info(f"Please fill out the table at row {i+1}")
                except:
                    pass
            checktable = check_for_no_product_code(self.uiWindow.sales_add_table,'R')
            if checktable=="True" and tableflag==0:
                sales = []
                for i in range(8):
                    try:
                        if self.uiWindow.sales_add_table.item(i, 0).text():
                            try:
                                self.uiWindow.sales_add_table.item(i, 1).text()
                                self.uiWindow.sales_add_table.item(i, 3).text()
                                if self.uiWindow.sales_add_table.item(i, 0).text() == '' or self.uiWindow.sales_add_table.item(i, 1).text()=='' or self.uiWindow.sales_add_table.item(i, 3).text()=='':
                                    self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                    flag = 1
                                    break
                            except:
                                self.show_warning_info(f"Please fill info in the table at '{i+1}'")
                                flag = 1
                                break
                        if self.uiWindow.sales_add_table.item(i, 1).text():
                            try:
                                self.uiWindow.sales_add_table.item(i, 0).text()
                                self.uiWindow.sales_add_table.item(i, 3).text()
                                if self.uiWindow.sales_add_table.item(i, 0).text() == '' or self.uiWindow.sales_add_table.item(i, 1).text()=='' or self.uiWindow.sales_add_table.item(i, 3).text()=='':
                                    self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                    flag = 1
                                    break
                            except:
                                self.show_warning_info(f"Please fill info in the table at '{i+1}'")
                                flag = 1
                                break
                        if self.uiWindow.sales_add_table.item(i, 3).text():
                            try:
                                self.uiWindow.sales_add_table.item(i, 0).text()
                                self.uiWindow.sales_add_table.item(i, 1).text()
                                if self.uiWindow.sales_add_table.item(i, 0).text() == '' or self.uiWindow.sales_add_table.item(
                                        i, 1).text() == '' or self.uiWindow.sales_add_table.item(i, 3).text() == '':
                                    self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                    flag = 1
                                    break
                            except:
                                self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                flag = 1
                                break
                    except:
                        try:
                            if self.uiWindow.sales_add_table.item(i,1).text() != '' or self.uiWindow.sales_add_table.item(i, 3).text() != '':
                                self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                flag = 1
                                break
                        except Exception as e:
                            print(e)
                            break
                if flag == 0:
                    for i in range(8):
                        try:
                            if self.uiWindow.sales_add_table.item(i,0).text() and self.uiWindow.sales_add_table.item(i,1).text() and self.uiWindow.sales_add_table.item(i,3).text():
                                shade_number= self.uiWindow.sales_add_table.item(i,0).text()
                                product_code = self.uiWindow.sales_add_table.item(i,1).text()
                                quantity = self.uiWindow.sales_add_table.item(i,3).text()
                                lot = self.uiWindow.sales_add_table.item(i,4).text()
                                sales.append((shade_number,product_code,float(quantity),lot))
                        except:
                            try:
                                self.uiWindow.sales_add_table.item(i,0).text()
                                self.uiWindow.sales_add_table.item(i, 1).text()
                                self.uiWindow.sales_add_table.item(i, 3).text()
                                self.uiWindow.sales_add_table.item(i, 4).text()
                                self.show_warning_info("Please fill info")
                                break
                            except:
                                # print("inside exception")
                                # print(sales)
                                if sales:
                                    # print(sales)
                                    if add_sales_data(self,trans_id,date,customer,remark,sales):
                                        # print("Inside")
                                        message1 = ""
                                        message2 = ""
                                        for each in sales:
                                            x = shade_raw_closing_stock(each[0], each[1],each[3])
                                            if x < 0:
                                                message2 = message2 + f"Closing stock for {each[0]} and {each[1]} is {x} in lot {each[3]}<br>"
                                            else:
                                                message1 = message1 + f"Closing stock for {each[0]} and {each[1]} is {x} in lot {each[3]}<br>"
                                        self.show_stock_popup(message1, message2)
                                        set_sales_data(self)
                                        customer_widget.clearEditText()
                                        remark_widget.clear()
                                        self.uiWindow.sales_add_table.clearContents()
                                        self.show_info_popup("Transaction Added Successfully")
                                        break
                                else:
                                    self.show_warning_info("Please fill info")
                                    break
            else:
                if tableflag!=1:
                    self.show_warning_info("Please fill out from available product code")
        else:
            self.show_warning_info("Please fill out the form")
    except Exception as e:
        print(e)


def view_sales_by_today(self):
    self.uiWindow.sales_view_by_today_date.setDate(QtCore.QDate.currentDate())
    self.uiWindow.sales_view_today_table.setRowCount(0)
    results = get_sales_transacs(by_Today=True)
    # print(results)
    if results:
        trans_list=[]
        for row in range(len(results)):
            self.uiWindow.sales_view_today_table.insertRow(row)
            for column in range(len(results[row])):
                if column == 0:
                    if str(results[row][column]) not in trans_list:
                        trans_list.append(str(results[row][column]))
                        self.uiWindow.sales_view_today_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(results[row][column])))
                elif results[row][column] != '-':
                    self.uiWindow.sales_view_today_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(results[row][column])))
    else:
        self.show_info_popup("No Transactions Done Today")

def find_shade(row, column, self, col, tableWidget):
    code = tableWidget.item(row, column).text()
    if column==col:
        try:
            if code=="":
                pass
            else:
                results=get_shade(code)
                if results:
                    pass
                else:
                    self.show_warning_info("The shade number entered does not exist")
                    tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem(""))
        except:
            pass

def view_sales_by_id(self):
    #TODO make table uneditable
    trans_id = "SLS" + str(self.uiWindow.sales_view_by_id_transaction_id.text()).zfill(5)
    results = get_sales_transacs(by_Id=trans_id)
    # print(results)
    if results:
        date = results[0][2]
        remark = results[0][3]
        customer = results[0][1]
        self.uiWindow.sales_view_by_id_date.setText(str(date))
        self.uiWindow.sales_view_by_id_remark.setText(str(remark))
        self.uiWindow.sales_view_by_id_customer.setCurrentText(customer)
        self.uiWindow.sales_view_by_id_table.setRowCount(0)
        for row in range(len(results[1])):
            self.uiWindow.sales_view_by_id_table.insertRow(row)
            for column in range(len(results[1][row])):
                value = results[1][row][column]
                # print(value)
                if value != '-':
                    self.uiWindow.sales_view_by_id_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(value)))
    else:
        self.uiWindow.sales_view_by_id_transaction_id.clear()
        self.uiWindow.sales_view_by_id_date.clear()
        self.uiWindow.sales_view_by_id_remark.clear()
        self.uiWindow.sales_view_by_id_table.clearContents()
        self.uiWindow.sales_view_by_id_table.setRowCount(0)
        self.uiWindow.sales_view_by_id_customer.clearEditText()
        self.show_warning_info("Transaction id not found")


def view_sales_by_custom(self):
    d1 = self.uiWindow.sales_view_custom_start_date.date()
    d2 = self.uiWindow.sales_view_custom_end_date.date()
    x = d1.toString('dd/MM/yyyy')
    y = d2.toString('dd/MM/yyyy')
    # print(type(x))
    x_date = datetime.datetime.strptime(x,'%d/%m/%Y')
    y_date = datetime.datetime.strptime(y,'%d/%m/%Y')
    delta = y_date - x_date
    if delta.days > 0:
        results = get_sales_transacs(by_custom=[x,y])
        # print(results)
        if results:
            self.uiWindow.sales_view_custom_table.setRowCount(0)
            trans_list=[]
            for each_list in results:
                for row in range(len(each_list)):
                    self.uiWindow.sales_view_custom_table.insertRow(row)
                    for column in range(len(each_list[row])):
                        if column == 0:
                            if str(each_list[row][column]) not in trans_list:
                                trans_list.append(str(each_list[row][column]))
                                self.uiWindow.sales_view_custom_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(each_list[row][column])))
                        elif each_list[row][column] != '-':
                            self.uiWindow.sales_view_custom_table.setItem(row, column, QtWidgets.QTableWidgetItem(
                                str(each_list[row][column])))
        else:
            pass
    else:
        self.show_warning_info("Please select correct date")


def set_delete_sales(self):
    trans_id = "SLS" + str(self.uiWindow.sales_delete_trans_id.text()).zfill(5)
    if check_sales_transacs(trans_id):
        results = get_sales_transacs(by_Id=trans_id)
        # print(results)
        if results:
            date = results[0][2]
            remark = results[0][3]
            customer = results[0][1]
            self.uiWindow.sales_delete_date.setText(str(date))
            self.uiWindow.sales_delete_remark.setText(str(remark))
            self.uiWindow.sales_delete_customer.setCurrentText(customer)
            self.uiWindow.sales_delete_table.setRowCount(0)
            for row in range(len(results[1])):
                self.uiWindow.sales_delete_table.insertRow(row)
                for column in range(len(results[1][row])):
                    value = results[1][row][column]
                    # print(value)
                    if value != '-' :
                        self.uiWindow.sales_delete_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(value)))

    else:
        self.uiWindow.sales_delete_date.setText("")
        self.uiWindow.sales_delete_remark.setText("")
        self.uiWindow.sales_delete_customer.setCurrentText("")
        self.uiWindow.sales_delete_table.clearContents()
        self.show_warning_info("Invalid Transaction Code")

def delete_sales(self,btn=False):
    trans_id = "SLS" + str(self.uiWindow.sales_delete_trans_id.text()).zfill(5)
    if check_sales_transacs(trans_id):
        if not btn:
            self.delete_confirm_dialog_sales()
        elif btn.text() == "&Yes":
            delete_sales_transacs(trans_id)
            self.show_info_popup("Deleted Successfully")
            self.uiWindow.sales_delete_trans_id.clear()
            self.uiWindow.sales_delete_date.clear()
            self.uiWindow.sales_delete_customer.clearEditText()
            self.uiWindow.sales_delete_remark.clear()
            self.uiWindow.sales_delete_table.clearContents()
            self.uiWindow.sales_delete_table.setRowCount(0)
    else:
        self.show_warning_info("Invalid Transaction Code")

def set_modify_sales(self):
    trans_id = "SLS" + str(self.uiWindow.sales_modify_trans_id.text()).zfill(5)
    if check_sales_transacs(trans_id):
        results = get_sales_transacs(by_Id=trans_id)
        # print(results)
        if results:
            date = results[0][2]
            remark = results[0][3]
            customer = results[0][1]
            self.uiWindow.sales_modify_date.setText(str(date))
            self.uiWindow.sales_modify_remark.setText(str(remark))
            self.uiWindow.sales_modify_customer.setCurrentText(customer)
            self.uiWindow.sales_modify_table.setRowCount(0)
            for row in range(len(results[1])):
                self.uiWindow.sales_modify_table.insertRow(row)
                for column in range(len(results[1][row])):
                    value = results[1][row][column]
                    # print(value)
                    if value != '-' :
                        self.uiWindow.sales_modify_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(value)))
        self.uiWindow.sales_modify_table.setRowCount(8)
    else:
        self.uiWindow.sales_modify_date.setText("")
        self.uiWindow.sales_modify_remark.setText("")
        self.uiWindow.sales_modify_customer.setCurrentText("")
        self.uiWindow.sales_modify_table.clearContents()
        self.show_warning_info("Invalid Transaction Code")


def modify_sales(self):
    # print("Inside")
    flag=0
    tableflag=0
    trans_id = "SLS" + str(self.uiWindow.sales_modify_trans_id.text()).zfill(5)
    if check_sales_transacs(trans_id):
        # print("Deleted")
        trans_id_widget = self.uiWindow.sales_modify_trans_id
        date_widget = self.uiWindow.sales_modify_date
        customer_widget = self.uiWindow.sales_modify_customer
        remark_widget = self.uiWindow.sales_modify_remark
        trans_id = 'SLS' + str(trans_id_widget.text()).zfill(5)
        date = date_widget.text()
        customer = customer_widget.currentText()
        remark = remark_widget.text()
        if customer and remark:
            try:
                for i in range(self.uiWindow.sales_modify_table.rowCount()):
                    self.uiWindow.sales_modify_table.item(i,0).text()
                    self.uiWindow.sales_modify_table.item(i, 1).text()
                    self.uiWindow.sales_modify_table.item(i, 3).text()
                    self.uiWindow.sales_modify_table.item(i, 4).text()
            except:
                try:
                    if i != 0:
                        if not self.self.uiWindow.sales_modify_table.item(i, 0).text():
                            raise Exception
                    tableflag=1
                    self.show_warning_info(f"Please fill out the table at row {i+1}")
                except:
                    pass
            checktable = check_for_no_product_code(self.uiWindow.sales_modify_table, 'R')
            if checktable == "True" and tableflag==0:
                sales = []
                for i in range(8):
                    try:
                        if self.uiWindow.sales_modify_table.item(i, 0).text():
                            try:
                                self.uiWindow.sales_modify_table.item(i, 1).text()
                                self.uiWindow.sales_modify_table.item(i, 3).text()
                                if self.uiWindow.sales_modify_table.item(i,
                                                                      0).text() == '' or self.uiWindow.sales_modify_table.item(
                                        i, 1).text() == '' or self.uiWindow.sales_modify_table.item(i, 3).text() == '':
                                    self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                    flag = 1
                                    break
                            except:
                                self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                flag = 1
                                break
                        if self.uiWindow.sales_modify_table.item(i, 1).text():
                            try:
                                self.uiWindow.sales_modify_table.item(i, 0).text()
                                self.uiWindow.sales_modify_table.item(i, 3).text()
                                if self.uiWindow.sales_modify_table.item(i,
                                                                      0).text() == '' or self.uiWindow.sales_modify_table.item(
                                        i, 1).text() == '' or self.uiWindow.sales_modify_table.item(i, 3).text() == '':
                                    self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                    flag = 1
                                    break
                            except:
                                self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                flag = 1
                                break
                        if self.uiWindow.sales_modify_table.item(i, 3).text():
                            try:
                                self.uiWindow.sales_modify_table.item(i, 0).text()
                                self.uiWindow.sales_modify_table.item(i, 1).text()
                                if self.uiWindow.sales_modify_table.item(i,
                                                                      0).text() == '' or self.uiWindow.sales_modify_table.item(
                                        i, 1).text() == '' or self.uiWindow.sales_modify_table.item(i, 3).text() == '':
                                    self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                    flag = 1
                                    break
                            except:
                                self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                flag = 1
                                break
                    except:
                        try:
                            if self.uiWindow.sales_modify_table.item(i,1).text() != '' or \
                                    self.uiWindow.sales_modify_table.item(i, 3).text() != '':
                                self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                flag = 1
                                break
                        except Exception as e:
                            print(e)
                            break
                if flag == 0:
                    for i in range(8):
                        try:
                            if self.uiWindow.sales_modify_table.item(i, 0).text() and \
                                    self.uiWindow.sales_modify_table.item(i,1).text() and \
                                    self.uiWindow.sales_modify_table.item(i, 3).text():
                                shade_number = self.uiWindow.sales_modify_table.item(i, 0).text()
                                product_code = self.uiWindow.sales_modify_table.item(i, 1).text()
                                quantity = self.uiWindow.sales_modify_table.item(i, 3).text()
                                lot = self.uiWindow.sales_modify_table.item(i, 4).text()
                                sales.append((shade_number, product_code, float(quantity),lot))
                        except:
                            try:
                                self.uiWindow.sales_modify_table.item(i, 0).text()
                                self.uiWindow.sales_modify_table.item(i, 1).text()
                                self.uiWindow.sales_modify_table.item(i, 3).text()
                                self.uiWindow.sales_modify_table.item(i, 4).text()
                                self.show_warning_info("Please fill info")
                                break
                            except:
                                # print("inside exception")
                                # print(sales)
                                if sales:
                                    delete_sales_transacs(trans_id)
                                    # print(sales)
                                    if add_sales_data(self,trans_id, date, customer, remark, sales):
                                        # print("Inside")
                                        message1=""
                                        message2=""
                                        for each in sales:
                                            x=shade_raw_closing_stock(each[0],each[1],each[3])
                                            if x<0:
                                                message2=message2+f"Closing stock for {each[0]} and {each[1]} is {x} in lot {each[3]}<br>"
                                            else:
                                                message1=message1+f"Closing stock for {each[0]} and {each[1]} is {x} in lot {each[3]}<br>"
                                        self.show_stock_popup(message1,message2)
                                        set_sales_data(self)
                                        customer_widget.clearEditText()
                                        remark_widget.clear()
                                        date_widget.clear()
                                        self.uiWindow.sales_modify_table.clearContents()
                                        trans_id_widget.clear()
                                        self.show_info_popup("Transaction Modified Successfully")
                                        break
                                else:
                                    self.show_warning_info("Please fill info")
                                    break
            else:
                if tableflag!=1:
                    self.show_warning_info("Please fill out from available product code")
        else:
            self.show_warning_info("Please fill out the form")


def set_product_name(self):
    try:
        code =self.uiWindow.rw_view_stock_code_2.text()
        result = get_product_name(code,'RC')
        # print("result")
        if result == "false":
            self.uiWindow.rw_view_stock_name_2.setText("No such product Code")
        else:
            self.uiWindow.rw_view_stock_name_2.setText(result)
    except Exception as e:
        print(e)



def product_stock_view(self):
    total_in = 0
    total_out = 0
    flag =0
    try:
        code = self.uiWindow.rw_view_stock_code_2.text()
        lot = self.uiWindow.rw_stock_view_lot.text()
        d1 = self.uiWindow.rw_view_starting_date_4.date()
        d2 = self.uiWindow.rw_view_ending_date_3.date()
        x = d1.toString('dd/MM/yyyy')
        y = d2.toString('dd/MM/yyyy')
        # print(type(x))
        x_date = datetime.datetime.strptime(x,'%d/%m/%Y')
        y_date = datetime.datetime.strptime(y,'%d/%m/%Y')
        delta = y_date - x_date
        if self.uiWindow.rw_view_stock_name_2.text() != "No such product Code":
            if delta.days > 0:
                results = get_product_stock(code,lot,by_custom=[x,y])
                if results:
                    # print(results)
                    try:
                        self.uiWindow.rm_view_table_6.setRowCount(0)
                        trans_list = []
                        for each_list in results:
                            for row in range(len(each_list)):
                                self.uiWindow.rm_view_table_6.insertRow(row)
                                for column in range(len(each_list[row])):
                                    if column == 0:
                                        if str(each_list[row][column]) not in trans_list:
                                            trans_list.append(str(each_list[row][column]))
                                            self.uiWindow.rm_view_table_6.setItem(row, column,
                                                                                     QtWidgets.QTableWidgetItem(
                                                                                         str(each_list[
                                                                                                 row][
                                                                                                 column])))
                                    else:
                                        self.uiWindow.rm_view_table_6.setItem(row, column,
                                                                                 QtWidgets.QTableWidgetItem(
                                                                                     str(each_list[row][
                                                                                             column])))
                                        if column == 2 and str(each_list[row][column]) != '-':
                                            total_in = total_in + float(each_list[row][column])
                                        if column == 3 and str(each_list[row][column]) != '-':
                                            total_out = total_out + float(each_list[row][column])
                        self.uiWindow.rm_view_stock_total_in.setText(str(total_in))
                        self.uiWindow.rm_view_stock_total_out.setText(str(total_out))
                    except Exception as e:
                        print(e)
                else:
                    self.show_info_popup("No transactions in given dates")
                    flag=1
                closing = raw_material_closing_stock(code,lot)
                if flag==0:
                    self.uiWindow.rm_view_opening.setText(str(closing+total_out-total_in))
                self.uiWindow.rw_view_closing.setText(str(closing))
            else:
                self.show_warning_info("Please select correct date")
        else:
            self.show_warning_info("Please select correct product code")
    except:
        self.show_warning_info("Please enter all details")

def shade_stock_view(self):
    total_in=0
    total_out=0
    flag=0
    try:
        if check_for_shade(self):
            code = self.uiWindow.shade_view_stock_code.text()
            shade = self.uiWindow.shade_view_stock_shade_number.text()
            lot = self.uiWindow.shade_view_stock_lot.text()
            d1 = self.uiWindow.shade_view_starting_date.date()
            d2 = self.uiWindow.shade_view_ending_date.date()
            x = d1.toString('dd/MM/yyyy')
            y = d2.toString('dd/MM/yyyy')
            # print(type(x))
            x_date = datetime.datetime.strptime(x,'%d/%m/%Y')
            y_date = datetime.datetime.strptime(y,'%d/%m/%Y')
            delta = y_date - x_date
            if shade!="":
                if self.uiWindow.shade_view_stock_name.text() != "No such product Code":
                    if delta.days > 0:
                        results = get_shade_stock(shade,code,lot,by_custom=[x,y])
                        # print(results)
                        if results:
                            # print(results)
                            try:
                                self.uiWindow.shade_view_table_3.setRowCount(0)
                                trans_list = []
                                for each_list in results:
                                    for row in range(len(each_list)):
                                        self.uiWindow.shade_view_table_3.insertRow(row)
                                        for column in range(len(each_list[row])):
                                            if column == 0:
                                                if str(each_list[row][column]) not in trans_list:
                                                    trans_list.append(str(each_list[row][column]))
                                                    self.uiWindow.shade_view_table_3.setItem(row, column,
                                                                                                  QtWidgets.QTableWidgetItem(
                                                                                                      str(each_list[
                                                                                                              row][
                                                                                                              column])))
                                            else:
                                                self.uiWindow.shade_view_table_3.setItem(row, column,
                                                                                              QtWidgets.QTableWidgetItem(
                                                                                                  str(each_list[row][
                                                                                                          column])))
                                                if column==2 and str(each_list[row][column])!='-':
                                                    total_in = total_in + float(each_list[row][column])
                                                if column==3 and str(each_list[row][column])!='-':
                                                    total_out= total_out + float(each_list[row][column])
                                self.uiWindow.shade_view_stock_total_in.setText(str(total_in))
                                self.uiWindow.shade_view_stock_total_out.setText(str(total_out))
                            except Exception as e:
                                print(e)
                        else:
                            self.show_info_popup("No transactions in given dates")
                            flag=1
                        closing = shade_raw_closing_stock(shade, code,lot)
                        if flag==0:
                            self.uiWindow.shade_view_opening.setText(str(closing + total_out - total_in))
                        self.uiWindow.shade_view_closing.setText(str(closing))
                    else:
                        self.show_warning_info("Please select correct date")
                else:
                    self.show_warning_info("Please select correct product code")
            else:
                self.show_warning_info("Please enter shade number")
    except Exception as e:
        print(e)
        self.show_warning_info("Please enter all details")

def check_shade(self,inputbox):
    code = inputbox.text()
    try:
        if code=="":
            pass
        else:
            results=get_shade(code)
            if results:
                pass
            else:
                self.show_warning_info("The shade number entered does not exist")
                inputbox.setText("")
    except:
        pass

def check_for_shade(self):
    code = self.uiWindow.shade_view_stock_shade_number.text()
    try:
        if code=="":
            pass
        else:
            results=get_shade(code)
            if results:
                return True
            else:
                self.show_warning_info("The shade number entered does not exist")
                return False
        return False
    except:
        pass

def set_sales_product_name(self):
    try:
        code =self.uiWindow.shade_view_stock_code.text()
        result = get_product_name(code,'R')
        # print("result")
        if result == "false":
            self.uiWindow.shade_view_stock_name.setText("No such product Code")
        elif result=="Product mismatch":
            self.uiWindow.shade_view_stock_name.setText("")
            self.uiWindow.shade_view_stock_code.setText("")
            self.show_warning_info("Only raw material is allowed")
        else:
            self.uiWindow.shade_view_stock_name.setText(result)
    except Exception as e:
        print(e)


def raw_material_display_closing(self):
    try:
        self.uiWindow.rm_closing_stock_table.setRowCount(0)
        results = get_all_rm_data('R')
        # print(results)
        for row_number, row_data in enumerate(results):
            self.uiWindow.rm_closing_stock_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.uiWindow.rm_closing_stock_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                if column_number==0:
                    self.uiWindow.rm_closing_stock_table.setItem(row_number, column_number+2, QtWidgets.QTableWidgetItem(str(raw_material_closing_stock(data,'all'))))
                    if raw_material_closing_stock(data,'all') != "None":
                        if raw_material_closing_stock(data,'all') > 0 :
                            self.uiWindow.rm_closing_stock_table.item(row_number,column_number+2).setBackground(QtGui.QColor(84, 237, 78))
                        else:
                            self.uiWindow.rm_closing_stock_table.item(row_number,column_number+2).setBackground(QtGui.QColor(240, 79, 79))

    except Exception as e:
        print(e)


def colour_display_closing(self):
    try:
        self.uiWindow.colour_closing_stock_table.setRowCount(0)
        results = get_all_rm_data('C')
        # print(results)
        for row_number, row_data in enumerate(results):
            self.uiWindow.colour_closing_stock_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.uiWindow.colour_closing_stock_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                if column_number==0:
                    self.uiWindow.colour_closing_stock_table.setItem(row_number, column_number+2, QtWidgets.QTableWidgetItem(str(raw_material_closing_stock(data,'all'))))
                    if raw_material_closing_stock(data,'all') != "None" :
                        if raw_material_closing_stock(data,'all') > 0 :
                            self.uiWindow.colour_closing_stock_table.item(row_number,column_number+2).setBackground(QtGui.QColor(84, 237, 78))
                        else:
                            self.uiWindow.colour_closing_stock_table.item(row_number,column_number+2).setBackground(QtGui.QColor(240, 79, 79))
    except Exception as e:
        print(e)

def shade_display_closing(self):
    try:
        flag=0
        # print(results)
        if "True"==check_for_no_product_code(self.uiWindow.shade_closing_stock_table,'R'):
            try:
                for i in range(20):
                    try:
                        if self.uiWindow.shade_closing_stock_table.item(i, 0).text():
                            try:
                                self.uiWindow.shade_closing_stock_table.item(i, 1).text()
                                if self.uiWindow.shade_closing_stock_table.item(i,0).text() == '' or \
                                        self.uiWindow.shade_closing_stock_table.item(i, 1).text() == '':
                                    self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                    flag = 1
                                    break
                            except:
                                self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                flag = 1
                                break
                        if self.uiWindow.shade_closing_stock_table.item(i, 1).text():
                            try:
                                self.uiWindow.shade_closing_stock_table.item(i, 0).text()
                                if self.uiWindow.shade_closing_stock_table.item(i,0).text() == '' or \
                                        self.uiWindow.shade_closing_stock_table.item(i, 1).text() == '' :
                                    self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                    flag = 1
                                    break
                            except:
                                self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                flag = 1
                                break
                    except:
                        try:
                            if self.uiWindow.shade_closing_stock_table.item(i,1).text() != '' :
                                self.show_warning_info(f"Please fill info in the table at '{i + 1}'")
                                flag = 1
                                break
                        except Exception as e:
                            print(e)
                            break
            except:
                pass
            if flag == 0:
                for row_number in range(20):
                    for column_number in range(1):
                        if column_number == 0:
                            if self.uiWindow.shade_closing_stock_table.item(row_number,
                                                                            column_number).text() and self.uiWindow.shade_closing_stock_table.item(
                                                                            row_number, column_number+1).text():
                                x = shade_raw_closing_stock(
                                    self.uiWindow.shade_closing_stock_table.item(row_number, column_number).text(),
                                    self.uiWindow.shade_closing_stock_table.item(row_number, column_number+1).text(),'all')
                                # print(x)
                                self.uiWindow.shade_closing_stock_table.setItem(row_number, column_number + 3,
                                                                                 QtWidgets.QTableWidgetItem(str(x)))
                                if str(x) != "None":
                                    if x > 0:
                                        self.uiWindow.shade_closing_stock_table.item(row_number, column_number + 3).setBackground(QtGui.QColor(84, 237, 78))
                                    else:
                                        self.uiWindow.shade_closing_stock_table.item(row_number, column_number + 3).setBackground(QtGui.QColor(240, 79, 79))

        else:
            self.show_warning_info("Please select correct product code")
    except Exception as e:
        print(e)



def set_opening_product_name_raw(self,inputbox,outputbox):
    try:
        code = inputbox.text()
        result = get_product_name(code,'RC')
        # print("result")
        if result == "false":
            outputbox.setText("No such product Code")
        elif result=="Product mismatch":
            inputbox.setText("")
            outputbox.setText("")
            self.show_warning_info("Only raw material is allowed")
        else:
            outputbox.setText(result)
    except Exception as e:
        print(e)


def add_raw_opening(self):
    try:
        product_code = self.uiWindow.rm_opening_product_code.text()
        opening = self.uiWindow.rm_opening_add_stock.text()
        lot = self.uiWindow.rm_opening_add_lot.text()
        if ""!=self.uiWindow.rm_opening_product_name.text() and "No such product code"!=self.uiWindow.rm_opening_product_name.text():
            if product_code and opening and lot:
                try:
                    if add_rm_opening(product_code, lot, float(opening)):
                        message = "Raw Material Added Successfully"
                        self.uiWindow.rm_opening_product_code.clear()
                        self.uiWindow.rm_opening_product_name.clear()
                        self.uiWindow.rm_opening_add_stock.clear()
                        self.uiWindow.rm_opening_add_lot.clear()
                        self.show_info_popup(message)
                    else:
                        message = "Product Code and lot Already Exists"
                        self.show_warning_info(message)
                except Exception as e:
                    print(e)
                    pass
                    # TODO exception
            else:
                # TODO Error handling if any of the fields empty
                self.show_warning_info("Please fill out the info")
        else:
            self.show_warning_info("Please fill correct product code")
    except:
        self.show_warning_info("Please fill out the info")

def view_raw_opening(self):
    try:
        code = self.uiWindow.rm_opening_view_product_code.text()
        lot = self.uiWindow.rm_opening_view_lot.text()
        result = view_rm_opening(code,lot)
        if result:
            self.uiWindow.rm_opening_view_stock.setText(str(result))
        else:
            self.show_warning_info("No details found")
    except Exception as e:
        print(e)
        self.show_warning_info("Please fill complete info")

def set_delete_raw_opening(self):
    try:
        code = self.uiWindow.rm_opening_delete_product_code.text()
        lot = self.uiWindow.rm_opening_delete_lot.text()
        result = view_rm_opening(code,lot)
        if result:
            self.uiWindow.rm_opening_delete_stock.setText(str(result))
        else:
            self.show_warning_info("No details found")
    except Exception as e:
        print(e)
        self.show_warning_info("Please fill complete info")


def delete_raw_opening(self):
    try:
        code = self.uiWindow.rm_opening_delete_product_code.text()
        lot = self.uiWindow.rm_opening_delete_lot.text()
        if ""!=self.uiWindow.rm_opening_delete_product_name.text() and "No such product code"!=self.uiWindow.rm_opening_delete_product_name.text():
            if code and lot:
                try:
                    if del_rm_opening(code, lot):
                        message = "Raw Material deleted Successfully"
                        self.uiWindow.rm_opening_delete_product_code.clear()
                        self.uiWindow.rm_opening_delete_product_name.clear()
                        self.uiWindow.rm_opening_delete_stock.clear()
                        self.uiWindow.rm_opening_delete_lot.clear()
                        self.show_info_popup(message)
                except Exception as e:
                    print(e)
                    pass
                    # TODO exception
            else:
                # TODO Error handling if any of the fields empty
                self.show_warning_info("Please fill out the info")
        else:
            self.show_warning_info("Please fill correct product code")
    except:
        self.show_warning_info("Please fill out the info")


OLD_RM_LOT_NO=""
OLD_SHADE_LOT_NO=""

def set_modify_raw_opening(self):
    global OLD_RM_LOT_NO
    try:
        code = self.uiWindow.rm_opening_modify_product_code.text()
        lot = self.uiWindow.rm_opening_modify_lot.text()
        OLD_RM_LOT_NO = lot
        result = view_rm_opening(code,lot)
        if result:
            self.uiWindow.rm_opening_modify_stock.setText(str(result))
        else:
            self.show_warning_info("No details found")
    except Exception as e:
        print(e)
        self.show_warning_info("Please fill complete info")


def modify_raw_opening(self):
    global OLD_RM_LOT_NO
    try:
        code = self.uiWindow.rm_opening_modify_product_code.text()
        lot = self.uiWindow.rm_opening_modify_lot.text()
        opening = self.uiWindow.rm_opening_modify_stock.text()
        if ""!=self.uiWindow.rm_opening_modify_product_name.text() and "No such product code"!=self.uiWindow.rm_opening_modify_product_name.text():
            if code and lot and opening:
                try:
                    if del_rm_opening(code, OLD_RM_LOT_NO):
                        OLD_RM_LOT_NO = ""
                        if add_rm_opening(code,lot,opening):
                            message = "Raw Material Modified Successfully"
                            self.uiWindow.rm_opening_modify_product_code.clear()
                            self.uiWindow.rm_opening_modify_product_name.clear()
                            self.uiWindow.rm_opening_modify_stock.clear()
                            self.uiWindow.rm_opening_modify_lot.clear()
                            self.show_info_popup(message)
                except Exception as e:
                    print(e)
                    pass
                    # TODO exception
            else:
                # TODO Error handling if any of the fields empty
                self.show_warning_info("Please fill out the info")
        else:
            self.show_warning_info("Please fill correct product code")
    except:
        self.show_warning_info("Please fill out the info")


def add_shade_opening(self):
    try:
        shade = self.uiWindow.shade_opening_add_number.text()
        product_code = self.uiWindow.shade_opening_product_code.text()
        opening = self.uiWindow.shade_opening_add_stock.text()
        lot = self.uiWindow.shade_opening_add_lot.text()
        if ""!=self.uiWindow.shade_opening_product_name.text() and "No such product code"!=self.uiWindow.shade_opening_product_name.text():
            if shade and product_code and opening and lot:
                try:
                    if shade_add_opening(shade,product_code, lot, float(opening)):
                        message = "Shade number Added Successfully"
                        self.uiWindow.shade_opening_add_number.clear()
                        self.uiWindow.shade_opening_product_code.clear()
                        self.uiWindow.shade_opening_product_name.clear()
                        self.uiWindow.shade_opening_add_stock.clear()
                        self.uiWindow.shade_opening_add_lot.clear()
                        self.show_info_popup(message)
                    else:
                        message = "Product Code and lot Already Exists"
                        self.show_warning_info(message)
                except Exception as e:
                    print(e)
                    pass
                    # TODO exception
            else:
                # TODO Error handling if any of the fields empty
                self.show_warning_info("Please fill out the info")
        else:
            self.show_warning_info("Please fill correct product code")
    except:
        self.show_warning_info("Please fill out the info")

def shade_view_opening(self):
    try:
        shade = self.uiWindow.shade_opening_view_number.text()
        code = self.uiWindow.shade_opening_view_product_code.text()
        lot = self.uiWindow.shade_opening_view_lot.text()
        result = view_shade_opening(shade,code,lot)
        if result:
            self.uiWindow.shade_opening_view_stock.setText(str(result))
        else:
            self.show_warning_info("No details found")
    except Exception as e:
        print(e)
        self.show_warning_info("Please fill complete info")


def set_modify_shade_opening(self):
    global OLD_SHADE_LOT_NO
    try:
        shade = self.uiWindow.shade_opening_modify_number.text()
        code = self.uiWindow.shade_opening_modify_product_code.text()
        lot = self.uiWindow.shade_opening_modify_lot.text()
        OLD_SHADE_LOT_NO = lot
        result = view_shade_opening(shade,code,lot)
        if result:
            self.uiWindow.shade_opening_modify_stock.setText(str(result))
        else:
            self.show_warning_info("No details found")
    except Exception as e:
        print(e)
        self.show_warning_info("Please fill complete info")


def set_delete_shade_opening(self):
    try:
        shade = self.uiWindow.shade_opening_delete_number.text()
        code = self.uiWindow.shade_opening_delete_product_code.text()
        lot = self.uiWindow.shade_opening_delete_lot.text()
        result = view_shade_opening(shade,code,lot)
        if result:
            self.uiWindow.shade_opening_delete_stock.setText(str(result))
        else:
            self.show_warning_info("No details found")
    except Exception as e:
        print(e)
        self.show_warning_info("Please fill complete info")


def delete_shade_opening(self):
    try:
        shade = self.uiWindow.shade_opening_delete_number.text()
        code = self.uiWindow.shade_opening_delete_product_code.text()
        lot = self.uiWindow.shade_opening_delete_lot.text()
        if ""!=self.uiWindow.shade_opening_delete_product_name.text() and "No such product code"!=self.uiWindow.shade_opening_delete_product_name.text():
            if shade and code and lot:
                try:
                    if shade_del_opening(shade,code, lot):
                        message = "Shade number deleted Successfully"
                        self.uiWindow.shade_opening_delete_number.clear()
                        self.uiWindow.shade_opening_delete_product_code.clear()
                        self.uiWindow.shade_opening_delete_product_name.clear()
                        self.uiWindow.shade_opening_delete_stock.clear()
                        self.uiWindow.shade_opening_delete_lot.clear()
                        self.show_info_popup(message)
                except Exception as e:
                    print(e)
                    pass
                    # TODO exception
            else:
                # TODO Error handling if any of the fields empty
                self.show_warning_info("Please fill out the info")
        else:
            self.show_warning_info("Please fill correct product code")
    except:
        self.show_warning_info("Please fill out the info")


def modify_shade_opening(self):
    global OLD_SHADE_LOT_NO
    try:
        shade = self.uiWindow.shade_opening_modify_number.text()
        code = self.uiWindow.shade_opening_modify_product_code.text()
        lot = self.uiWindow.shade_opening_modify_lot.text()
        opening = self.uiWindow.shade_opening_modify_stock.text()
        if ""!=self.uiWindow.shade_opening_modify_product_name.text() and "No such product code"!=self.uiWindow.shade_opening_modify_product_name.text():
            if shade and code and lot and opening:
                try:
                    if shade_del_opening(shade,code, OLD_SHADE_LOT_NO):
                        OLD_SHADE_LOT_NO = ""
                        if shade_add_opening(shade,code,lot,opening):
                            message = "Shade number Modified Successfully"
                            self.uiWindow.shade_opening_modify_number.clear()
                            self.uiWindow.shade_opening_modify_product_code.clear()
                            self.uiWindow.shade_opening_modify_product_name.clear()
                            self.uiWindow.shade_opening_modify_stock.clear()
                            self.uiWindow.shade_opening_modify_lot.clear()
                            self.show_info_popup(message)
                except Exception as e:
                    print(e)
                    pass
                    # TODO exception
            else:
                # TODO Error handling if any of the fields empty
                self.show_warning_info("Please fill out the info")
        else:
            self.show_warning_info("Please fill correct product code")
    except:
        self.show_warning_info("Please fill out the info")
