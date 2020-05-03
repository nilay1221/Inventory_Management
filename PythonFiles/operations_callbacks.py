# Callback Function when Adding raw material
from operations import *
from PyQt5 import QtWidgets,QtCore
import datetime


def callback_add_raw_material(self):
    product_code = self.uiWindow.rm_new_product_code.text()
    product_name = self.uiWindow.rm_new_product_name.text()
    product_price = self.uiWindow.rm_new_product_price.text()
    if product_code and product_name and product_price:
        try:
            if add_raw_material(product_code, product_name, int(product_price)):
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
                modify_info(product_code, product_name, product_price)
                self.show_info_popup("Details Modified Sucessfully")
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
    # print(results)
    for row_number, row_data in enumerate(results):
        self.uiWindow.tableWidget_2.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.uiWindow.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


def display_product_name(row, column, self, col, tableWidget):
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
                result = get_product_name(code)
                if result == 'false':
                    tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem("No such product code"))
                else:
                    tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem(result))
        except Exception as e:
            print(e)


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
                        except:
                            self.show_info_popup(f"Please fill the table at row '{i + 1}'")
                            flag = 1
                            break
                except Exception as e:
                    print(e)
                    break
            if flag==0:
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
                    print("in")
                    break
            if flag==0:
                if shade_no == OLD_SHADE_NUMBER:
                    try:
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
                                self.show_info_popup("Details Modified Sucessfully")
                    except:
                        pass
                else:
                    try:
                        if readd_shade_material_on_modify(self):
                            self.show_info_popup("Details Modified Sucessfully")
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
# Add Raw Material Transaction

def set_raw_material_data(self):
    trans_id = get_trans_id("rm_stock")
    date = datetime.date.today().strftime("%d-%m-%Y")
    self.uiWindow.rm_transaction_id.setText(str(trans_id))
    self.uiWindow.date.setText(str(date))


def add_raw_material_callback(self):
    print("Inside")
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
        products = []
        for i in range(8):
            try:
                if self.uiWindow.rm_addtable.item(i,0).text() and self.uiWindow.rm_addtable.item(i,2).text():
                    product_code = self.uiWindow.rm_addtable.item(i,0).text()
                    quantity = self.uiWindow.rm_addtable.item(i,2).text()
                    products.append((product_code,float(quantity)))
            except:
                try:
                    self.uiWindow.rm_addtable.item(i,0).text()
                    self.show_warning_info("Please fill info")
                    break
                except:
                    print("inside exception")
                    if products:
                        # print(products)
                        if add_raw_material_data(trans_id,date,customer,remark,products):
                            # print("Inside")
                            set_raw_material_data(self)
                            customer_widget.clearEditText()
                            remark_widget.clear()
                            self.uiWindow.rm_addtable.clearContents()
                            self.show_info_popup("Transaction Added Sucessfully")
                            break
                    else:
                        self.show_warning_info("Please fill info")
                        break
        
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
                else:
                    self.uiWindow.rm_view_table_5.setItem(row,column,QtWidgets.QTableWidgetItem(str(results[row][column])))

    else:
        self.show_info_popup("No Transactions Done Today")

def set_delete_rm(self):
    trans_id = "RMT" + str(self.uiWindow.rw_delete_transaction_id.text()).zfill(5)
    print(trans_id)
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
                    self.uiWindow.rm_delete_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(value)))

    else:
        self.show_warning_info("Invalid Transaction Code")

def delete_rm(self,btn):
    trans_id = "RMT" + str(self.uiWindow.rw_delete_transaction_id.text()).zfill(5)
    if check_rm_transacs(trans_id):
        if btn.text() == "&Yes":
            delete_rm_transacs(trans_id)
            self.show_info_popup("Deleted Sucessfully")
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
    print(trans_id)
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
            self.uiWindow.rm_view_table.setRowCount(8)
            for row in range(len(results[1])):
                self.uiWindow.rm_view_table.insertRow(row)
                for column in range(len(results[1][row])):
                    value = results[1][row][column]
                    # print(value)
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
    print("Inside")
    trans_id = "RMT" + str(self.uiWindow.rw_modify_transaction_id.text()).zfill(5)
    if check_rm_transacs(trans_id):
        delete_rm_transacs(trans_id)
        print("Deleted")
        trans_id_widget = self.uiWindow.rw_modify_transaction_id
        date_widget = self.uiWindow.rm_modify_date
        customer_widget = self.uiWindow.rm_modify_customer
        remark_widget = self.uiWindow.rm_modify_remark
        trans_id = 'RMT' +  str(trans_id_widget.text()).zfill(5)
        date = date_widget.text()
        customer = customer_widget.currentText()
        remark = remark_widget.text()
        if customer and remark:
            products = []
            for i in range(8):
                try:
                    if self.uiWindow.rm_view_table.item(i,0).text() and self.uiWindow.rm_view_table.item(i,2).text():
                        product_code = self.uiWindow.rm_view_table.item(i,0).text()
                        quantity = self.uiWindow.rm_view_table.item(i,2).text()
                        products.append((product_code,float(quantity)))
                except:
                    try:
                        self.uiWindow.rm_view_table.item(i,0).text()
                        self.show_warning_info("Please fill info")
                        break
                    except:
                        # print("inside exception")
                        if products:
                            if add_raw_material_data(trans_id,date,customer,remark,products):
                                # set_raw_material_data(self)
                                self.uiWindow.rw_modify_transaction_id.clear()
                                self.uiWindow.rm_modify_date.clear()
                                customer_widget.clearEditText()
                                remark_widget.clear()
                                self.uiWindow.rm_view_table.clearContents()
                                self.show_info_popup("Transaction Modified Sucessfully")
                        else:
                            self.show_warning_info("Please fill info")
                            break
            
        else:
            self.show_warning_info("Please fill out the form")

def clear_view_by_id(self):
    self.uiWindow.rw_view_transaction_id.clear()
    self.uiWindow.rm_view_date.clear()
    self.uiWindow.rm_view_customer.clearEditText()
    self.uiWindow.rm_view_remark.clear()
    self.uiWindow.rm_view_table_4.clear()
    self.uiWindow.rm_view_table_4.setRowCount(9)

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
                        else:
                            self.uiWindow.rm_view_table_3.setItem(row, column, QtWidgets.QTableWidgetItem(
                                str(each_list[row][column])))
        else:
            pass
    else:
        self.show_warning_info("Please select correct date")
    
