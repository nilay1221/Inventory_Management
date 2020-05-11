from stacked import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QShortcut
from PyQt5.QtGui import QKeySequence
import operations_callbacks
import clear

pagesDict = {
        'Home': 0,
        'new_rm_entry': 1,
        'new_shade_entry': 2,
        'rm_add': 3,
        'rm_delete': 4,
        'rm_modify': 5,
        'rm_operations': 6,
        'rm_stock_view': 7,
        'rm_view': 8,
        'rm_view_custom': 9,
        'rm_view_by_id': 10,
        'rm_view_by_today': 11,
        'shade_add': 12,
        'shade_delete': 13,
        'shade_modify': 14,
        'shade_operations': 15,
        'shade_view': 16,
        'shade_view_by_custom': 17,
        'shade_view_by_id': 18,
        'shade_view_by_today': 19,
        'rm_stock_view_2':20,
        'shade_stock_view':21,
        'sales_operations':22,
        'new_rm_operations':23,
        'new_rm_modify': 24,
        'new_rm_delete':25,
        'new_rm_view':26,
        'new_shade_operations':27,
        'new_shade_modify':28,
        'new_shade_delete':29,
        'new_shade_view':30,
        'new_shade_view_all':31,
        'sales_add':32,
        'sales_modify':33,
        'sales_delete':34,
        'sales_view': 35,
        'sales_view_by_id': 36,
        'sales_view_by_today': 37,
        'sales_view_by_custom': 38,
        'rm_closing_stock': 39,
        'colour_closing_stock': 40,
        'shade_closing_stock': 41,
        'rm_opening_operation': 42,
        'rm_opening_add': 43,
        'rm_opening_modify': 44,
        'rm_opening_delete': 45,
        'rm_opening_view': 46,
        'shade_opening_operation': 47,
        'shade_opening_add': 48,
        'shade_opening_modify': 49,
        'shade_opening_delete': 50,
        'shade_opening_view': 51,
    }

DEFAULT_SHOW = "RC"

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.uiWindow = Ui_MainWindow()
        self.startUIWindow()
        self.maintain_operations()
        self.show()


    def startUIWindow(self):
        self.uiWindow.setupUi(self)
        self.uiWindow.EP.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.RM.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.RM_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_operations']))
        self.uiWindow.RM_3.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_operations']))
        #self.uiWindow.RM_4.clicked.connect(lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_stock_view']))
        self.uiWindow.back_add_rm.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_operations']))
        self.uiWindow.pushButton.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_operations']))
        self.uiWindow.pushButton_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.back_add_rm_3.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.pushButton_3.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.back_add_rm_4.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.pushButton_4.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_2.clicked.connect(lambda : self.uiWindow
.stackedWidget.setCurrentIndex(pagesDict['new_shade_operations']))
        self.uiWindow.back_view_rm_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.pushButton_5.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.rm_add_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_add']))
        self.uiWindow.rm_modify_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_modify']))
        self.uiWindow.rm_delete_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_delete']))
        self.uiWindow.rm_view.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.pushButton_6.clicked.connect(lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_3.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.op_back.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.view_trans.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view_by_id']))
        self.uiWindow.view_today.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view_by_today']))
        self.uiWindow.view_custom.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view_custom']))
        self.uiWindow.back_view_rm_4.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.pushButton_7.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_5.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.pushButton_8.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_5.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.pushButton_9.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_6.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.pushButton_10.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        #self.uiWindow.back_view_rm_4.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.back_view_rm_7.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.pushButton_11.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_12.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_8.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.back_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.shade_add_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_add']))
        self.uiWindow.shade_modify_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_modify']))
        self.uiWindow.shade_delete_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_delete']))
        self.uiWindow.shade_view.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view']))
        self.uiWindow.op_back_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.view_trans_2.clicked.connect(lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view_by_id']))
        self.uiWindow.view_today_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view_by_today']))
        self.uiWindow.view_custom_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view_by_custom']))
        self.uiWindow.pushButton_13.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_9.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view']))
        self.uiWindow.back_add_rm_5.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view']))
        self.uiWindow.pushButton_14.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_15.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_10.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view']))
        self.uiWindow.RM_4.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_stock_view_2']))
        self.uiWindow.RM_5.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_stock_view']))
        self.uiWindow.RM_6.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_operations']))
        self.uiWindow.back_view_rm_11.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_16.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_12.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_17.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_18.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_18.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_19.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_20.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_21.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_22.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_23.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_24.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_26.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_6.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_3.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.new_rm_add.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_entry']))
        self.uiWindow.new_rm_modify.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_modify']))
        self.uiWindow.new_rm_delete.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_delete']))
        self.uiWindow.new_rm_view.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_view']))
        self.uiWindow.back_add_rm_7.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_operations']))
        self.uiWindow.back_add_rm_8.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_operations']))
        self.uiWindow.back_add_rm_9.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_operations']))
        self.uiWindow.back_add_rm_9.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_operations']))
        self.uiWindow.back_4.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.new_shade_add.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_entry']))
        self.uiWindow.new_shade_modify.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_modify']))
        self.uiWindow.new_shade_delete.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_delete']))
        self.uiWindow.new_shade_view.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_view']))
        self.uiWindow.new_shade_view_all.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_view_all']))
        self.uiWindow.back_add_rm_10.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_operations']))
        self.uiWindow.back_add_rm_11.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_operations']))
        self.uiWindow.back_add_rm_12.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_operations']))
        self.uiWindow.back_add_rm_13.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_operations']))
        self.uiWindow.sales_add.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_add']))
        self.uiWindow.sales_modify.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_modify']))
        self.uiWindow.sales_delete.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_delete']))
        self.uiWindow.sales_view.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_view']))
        self.uiWindow.sales_view_transaction.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_view_by_id']))
        self.uiWindow.sales_view_today.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_view_by_today']))
        self.uiWindow.sales_view_custom.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_view_by_custom']))
        self.uiWindow.sales_view_back.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_operations']))
        self.uiWindow.sales_delete_back.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_operations']))
        self.uiWindow.sales_modify_back.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_operations']))
        self.uiWindow.sales_add_back.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_operations']))
        self.uiWindow.back_5.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_27.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_18.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.sales_modify_backmenu.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_25.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_28.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_29.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.sales_view_back.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_operations']))
        self.uiWindow.back_add_rm_6.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_view']))
        self.uiWindow.sales_view_custom_back.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_view']))
        self.uiWindow.sales_view_today_back.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['sales_view']))
        self.uiWindow.rm_end_stock.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_closing_stock']))
        self.uiWindow.colour_end_stock.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['colour_closing_stock']))
        self.uiWindow.shade_end_stock.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_closing_stock']))
        self.uiWindow.rm_opening_stock.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_opening_operation']))
        self.uiWindow.shade_opening_stock.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_opening_operation']))
        self.uiWindow.back_add_rm_14.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_29.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_30.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_6.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_30.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_31.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_32.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_33.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_34.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_35.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_36.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_37.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_15.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_opening_operation']))
        self.uiWindow.back_add_rm_16.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_opening_operation']))
        self.uiWindow.back_add_rm_17.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_opening_operation']))
        self.uiWindow.back_add_rm_18.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_opening_operation']))
        self.uiWindow.back_add_rm_19.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_opening_operation']))
        self.uiWindow.back_add_rm_20.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_opening_operation']))
        self.uiWindow.back_add_rm_21.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_opening_operation']))
        self.uiWindow.back_add_rm_22.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_opening_operation']))
        self.uiWindow.opening_rm_add.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_opening_add']))
        self.uiWindow.opening_rm_modify.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_opening_modify']))
        self.uiWindow.opening_rm_delete.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_opening_delete']))
        self.uiWindow.opening_rm_view.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_opening_view']))
        self.uiWindow.opening_shade_add.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_opening_add']))
        self.uiWindow.opening_shade_modify.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_opening_modify']))
        self.uiWindow.opening_shade_delete.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_opening_delete']))
        self.uiWindow.opening_shade_view.clicked.connect(
            lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_opening_view']))
        self.uiWindow.new_rm_delete_product_name.setReadOnly(True)
        self.uiWindow.new_rm_delete_product_price.setReadOnly(True)
        self.uiWindow.new_rm_modify_product_name.setReadOnly(True)
        self.uiWindow.new_rm_modify_product_price.setReadOnly(True)
        self.uiWindow.rm_view_date.setReadOnly(True)
        self.uiWindow.rm_view_remark.setReadOnly(True)
        # TODO combo box disable 



        self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home'])
    
    def show_info_popup(self,message):
        #TODO change icon
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def show_warning_info(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()

    
    def delete_confirm_dialog(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("Are you sure want to Delete?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msg.buttonClicked.connect(lambda i: operations_callbacks.del_new_rm(self,btn=i))
        x = msg.exec_()

    def delete_confirm_dialog_shade_number(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("Are you sure want to Delete?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msg.buttonClicked.connect(lambda i: operations_callbacks.del_new_shade(self,btn=i))
        x = msg.exec_()

    
    def delete_confirm_dialog_rm(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("Are you sure want to Delete?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msg.buttonClicked.connect(lambda i: operations_callbacks.delete_rm(self,btn=i))
        x = msg.exec_()

    def delete_confirm_dialog_shade_trans(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("Are you sure want to Delete?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msg.buttonClicked.connect(lambda i: operations_callbacks.delete_shade_transaction(self,btn=i))
        x = msg.exec_()

    def delete_confirm_dialog_sales(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("Are you sure want to Delete?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msg.buttonClicked.connect(lambda i: operations_callbacks.delete_sales(self,btn=i))
        x = msg.exec_()

    def show_stock_popup(self,message1,message2):
        # TODO change icon
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(f"""<P><FONT COLOR='#800000'>{message2}</FONT></P>
                    <P><FONT COLOR='#000080'>{message1}</FONT></P>""")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def maintain_operations(self):
        self.uiWindow.rm_new_confirm.clicked.connect(lambda: operations_callbacks.callback_add_raw_material(self))
        self.uiWindow.new_rm_view.clicked.connect(lambda: operations_callbacks.view_new_rm_data(self))
        self.uiWindow.tableWidget.cellChanged.connect(lambda row, column: operations_callbacks.display_product_name(row, column, self, 0,
                                                                          "C",self.uiWindow.tableWidget))
        self.uiWindow.shade_new_confirm.clicked.connect(lambda: operations_callbacks.add_shade_material(self))
        self.uiWindow.shade_new__view_number.returnPressed.connect(
            lambda: operations_callbacks.view_new_shade_details(self))
        self.uiWindow.new_shade_view.clicked.connect(lambda: self.uiWindow.shade_new_view_details_table.clearContents())
        self.uiWindow.new_shade_view.clicked.connect(lambda: self.uiWindow.shade_new_view_details_table.setRowCount(10))
        self.uiWindow.new_rm_modify_product_code.returnPressed.connect(
            lambda: operations_callbacks.show_modify_raw_data(self))
        self.uiWindow.rm_new_modify_confirm.clicked.connect(lambda: operations_callbacks.modify_new_rm_data(self))
        self.uiWindow.new_rm_delete_product_code.returnPressed.connect(
            lambda: operations_callbacks.show_new_rm_del_info(self))
        self.uiWindow.rm_new_delete_confirm.clicked.connect(lambda: operations_callbacks.del_new_rm(self))
        self.uiWindow.rm_addtable.cellChanged.connect(
            lambda row, column: operations_callbacks.display_product_name(row, column, self, 0,"RC",self.uiWindow.rm_addtable))
        self.uiWindow.shade_new__delete_number.returnPressed.connect(lambda : operations_callbacks.show_new_shade_del_info(self))
        self.uiWindow.shade_new__modify_number.returnPressed.connect(
            lambda: operations_callbacks.show_new_shade_modify_info(self))
        self.uiWindow.rm_new_delete_confirm_2.clicked.connect(lambda: operations_callbacks.del_new_shade(self))
        self.uiWindow.rm_new_modify_confirm_2.clicked.connect(lambda :operations_callbacks.modify_new_shade_data(self))
        self.uiWindow.shade_new_modify_details_table.cellChanged.connect(lambda row, column: operations_callbacks.display_product_name(row, column, self, 0,
                                                                          "C",self.uiWindow.shade_new_modify_details_table))
        self.uiWindow.new_shade_view_all.clicked.connect(lambda : operations_callbacks.shade_view_all(self))
        self.uiWindow.rm_add_2.clicked.connect(lambda : operations_callbacks.set_raw_material_data(self))
        self.uiWindow.rm_confirm.clicked.connect(lambda : operations_callbacks.add_raw_material_callback(self))
        self.uiWindow.rw_view_transaction_id.returnPressed.connect(lambda:operations_callbacks.view_rm_by_id(self))
        self.uiWindow.view_today.clicked.connect(lambda:operations_callbacks.view_rm_by_today(self))
        self.uiWindow.rw_delete_transaction_id.returnPressed.connect(lambda : operations_callbacks.set_delete_rm(self))
        self.uiWindow.rm_delete_confirm.clicked.connect(self.delete_confirm_dialog_rm)
        self.uiWindow.rw_modify_transaction_id.returnPressed.connect(lambda : operations_callbacks.set_modify_rm(self))
        self.uiWindow.rm_view_table.cellChanged.connect(
            lambda row, column: operations_callbacks.display_product_name(row, column, self, 0,
                                                                          "RC",self.uiWindow.rm_view_table))
        self.uiWindow.rm_modify_confirm.clicked.connect(lambda: operations_callbacks.modify_rm(self))
        self.uiWindow.view_trans.clicked.connect(lambda :operations_callbacks.clear_view_by_id(self))
        # self.uiWindow.rw_view_starting_date_3.dateChanged.connect(lambda : operations_callbacks.view_by_custom_dates(self))
        shortcut1 = QShortcut(QKeySequence('Return'),self.uiWindow.rw_view_ending_date_2)
        shortcut1.activated.connect(lambda : operations_callbacks.view_by_custom_dates(self))
        self.uiWindow.shade_add_2.clicked.connect(lambda: operations_callbacks.set_shade_number_transacs(self))
        self.uiWindow.shade_number_add.returnPressed.connect(lambda : operations_callbacks.set_shade_number_details(self,self.uiWindow.shade_number_add,self.uiWindow.shade_addtable,self.uiWindow.shade_colortable,self.uiWindow.shade_add_total))
        self.uiWindow.shade_addtable.cellChanged.connect(lambda row,column : operations_callbacks.display_product_name(row,column,self,0,"R",self.uiWindow.shade_addtable))
        self.uiWindow.shade_addtable.cellChanged.connect(lambda row,column: operations_callbacks.set_total_quantity(row,column,self,self.uiWindow.shade_addtable,self.uiWindow.shade_colortable,self.uiWindow.shade_add_total))
        self.uiWindow.shade_confirm.clicked.connect(lambda : operations_callbacks.confirm_add_shade_number(self))
        self.uiWindow.shade_view_transaction_id.returnPressed.connect(lambda:operations_callbacks.view_shade_stock_by_id(self))
        self.uiWindow.view_today_2.clicked.connect(lambda: operations_callbacks.view_shade_transaction_today(self))
        self.uiWindow.shade_delete_transaction_id.returnPressed.connect(lambda : operations_callbacks.set_delete_shade_transaction(self))
        self.uiWindow.shade_delete_confirm.clicked.connect(lambda : self.delete_confirm_dialog_shade_trans())
        self.uiWindow.shade_modify_transaction_id.returnPressed.connect(lambda:operations_callbacks.set_modify_shade_transaction(self))
        self.uiWindow.shade_addtable_3.cellChanged.connect(lambda row,column:operations_callbacks.display_product_name(row,column,self,0,"R",self.uiWindow.shade_addtable_3))
        self.uiWindow.shade_addtable_3.cellChanged.connect(lambda row,column:operations_callbacks.set_total_quantity(row,column,self,self.uiWindow.shade_addtable_3,self.uiWindow.shade_colortable_3,self.uiWindow.shade_add_total_3))
        # self.uiWindow.shade_modify_transaction_id.returnPressed.connect(lambda:operations_callbacks.set_modify_shade_transaction(self))
        self.uiWindow.shade_number_modify.returnPressed.connect(lambda : operations_callbacks.set_shade_number_details(self,self.uiWindow.shade_number_modify,self.uiWindow.shade_addtable_3,self.uiWindow.shade_colortable_3,self.uiWindow.shade_add_total_3))
        self.uiWindow.shade_modify_confirm.clicked.connect(lambda:operations_callbacks.confirm_modify_shade_trans(self))
        shortcut2 = QShortcut(QKeySequence('Return'),self.uiWindow.shade_view_end_date)
        shortcut2.activated.connect(lambda : operations_callbacks.shade_view_by_custom_dates(self))
        self.uiWindow.view_trans_2.clicked.connect(lambda:operations_callbacks.clear_shade_view_by_today(self))
        self.uiWindow.shade_view_table_2.cellChanged.connect(lambda row,column:operations_callbacks.display_product_name(row,column,self,4,DEFAULT_SHOW,self.uiWindow.shade_view_table_2))
        self.uiWindow.shade_view_table.cellChanged.connect(lambda row,column:operations_callbacks.display_product_name(row,column,self,5,DEFAULT_SHOW,self.uiWindow.shade_view_table))
        self.uiWindow.rm_view_table_5.cellChanged.connect(lambda row,column:operations_callbacks.display_product_name(row,column,self,3,DEFAULT_SHOW,self.uiWindow.rm_view_table_5))
        self.uiWindow.rm_view_table_3.cellChanged.connect(lambda row,column: operations_callbacks.display_product_name(row,column,self,4,DEFAULT_SHOW,self.uiWindow.rm_view_table_3))
        self.uiWindow.rm_view_table_4.cellChanged.connect(lambda row,column: operations_callbacks.display_product_name(row,column,self,0,DEFAULT_SHOW,self.uiWindow.rm_view_table_4))
        self.uiWindow.shade_addtable_3.cellChanged.connect(lambda row,column:operations_callbacks.display_product_name(row,column,self,0,"R",self.uiWindow.shade_addtable_3))
        self.uiWindow.rm_delete_table.cellChanged.connect(lambda row,column: operations_callbacks.display_product_name(row,column,self,0,"RC",self.uiWindow.rm_delete_table))
        self.uiWindow.shade_addtable_2.cellChanged.connect(lambda row,column:operations_callbacks.display_product_name(row,column,self,0,"R",self.uiWindow.shade_addtable_2))
        self.uiWindow.shade_colortable_2.cellChanged.connect(lambda row,column: operations_callbacks.display_product_name(row,column,self,0,"C",self.uiWindow.shade_colortable_2))
        self.uiWindow.shade_colortable_3.cellChanged.connect(
            lambda row, column: operations_callbacks.display_product_name(row, column, self, 0, "C",
                                                                          self.uiWindow.shade_colortable_3))
        self.uiWindow.shade_addtable_4.cellChanged.connect(lambda row,column: operations_callbacks.display_product_name(row,column,self,0,"R",self.uiWindow.shade_addtable_4))
        self.uiWindow.shade_colortable_4.cellChanged.connect(lambda row,column: operations_callbacks.display_product_name(row,column,self,0,"C",self.uiWindow.shade_colortable_4))
        self.uiWindow.sales_add.clicked.connect(lambda: operations_callbacks.set_sales_data(self))
        self.uiWindow.sales_add_confirm.clicked.connect(lambda: operations_callbacks.add_sales_callback(self))
        self.uiWindow.sales_view_today.clicked.connect(lambda: operations_callbacks.view_sales_by_today(self))
        self.uiWindow.sales_add_table.cellChanged.connect(
            lambda row,column: operations_callbacks.find_shade(row,column,self,0,self.uiWindow.sales_add_table))
        self.uiWindow.sales_add_table.cellChanged.connect(lambda row,column: operations_callbacks.display_product_name_sales(row,column,self,1,self.uiWindow.sales_add_table))
        self.uiWindow.sales_view_today_table.cellChanged.connect(
            lambda row, column: operations_callbacks.display_product_name(row, column, self, 4,'R',
                                                                          self.uiWindow.sales_view_today_table))
        self.uiWindow.sales_view_by_id_table.cellChanged.connect(
            lambda row, column: operations_callbacks.display_product_name(row, column, self, 1,'R',
                                                                          self.uiWindow.sales_view_by_id_table))
        self.uiWindow.sales_view_custom_table.cellChanged.connect(
            lambda row, column: operations_callbacks.display_product_name(row, column, self, 5, 'R',
                                                                          self.uiWindow.sales_view_custom_table))
        self.uiWindow.sales_view_by_id_transaction_id.returnPressed.connect(
            lambda: operations_callbacks.view_sales_by_id(self))
        shortcut3 = QShortcut(QKeySequence('Return'), self.uiWindow.sales_view_custom_end_date)
        shortcut3.activated.connect(lambda: operations_callbacks.view_sales_by_custom(self))
        self.uiWindow.sales_delete_trans_id.returnPressed.connect(lambda: operations_callbacks.set_delete_sales(self))
        self.uiWindow.sales_delete_confirm.clicked.connect(lambda : operations_callbacks.delete_sales(self))
        self.uiWindow.sales_modify_trans_id.returnPressed.connect(lambda: operations_callbacks.set_modify_sales(self))
        self.uiWindow.sales_modify_confirm.clicked.connect(lambda: operations_callbacks.modify_sales(self))
        self.uiWindow.sales_modify_table.cellChanged.connect(
            lambda row, column: operations_callbacks.display_product_name_sales(row, column, self, 1,
                                                                          self.uiWindow.sales_modify_table)
        )
        self.uiWindow.sales_delete_table.cellChanged.connect(
            lambda row, column: operations_callbacks.display_product_name_sales(row, column, self, 1,
                                                                          self.uiWindow.sales_delete_table)
        )
        self.uiWindow.sales_modify_table.cellChanged.connect(
            lambda row, column: operations_callbacks.find_shade(row, column, self, 0, self.uiWindow.sales_modify_table))
        self.uiWindow.rw_view_stock_code_2.returnPressed.connect(lambda: operations_callbacks.set_product_name(self))
        self.uiWindow.rm_view_stock_confirm.clicked.connect(lambda: operations_callbacks.product_stock_view(self))
        self.uiWindow.shade_view_stock_shade_number.returnPressed.connect(
            lambda: operations_callbacks.check_shade(self))
        self.uiWindow.shade_view_stock_code.returnPressed.connect(lambda: operations_callbacks.set_sales_product_name(self))
        self.uiWindow.shade_view_stock_confirm.clicked.connect(lambda: operations_callbacks.shade_stock_view(self))
        self.uiWindow.rm_end_stock.clicked.connect(lambda : operations_callbacks.raw_material_display_closing(self))
        self.uiWindow.colour_end_stock.clicked.connect(lambda: operations_callbacks.colour_display_closing(self))
        try:
            self.uiWindow.shade_closing_stock_table.cellChanged.connect(
                lambda row, column: operations_callbacks.display_product_name_sales(row, column, self, 1,
                                                                                    self.uiWindow.shade_closing_stock_table))
        except Exception as e:
            print(e)
        self.uiWindow.shade_closing_stock_table.cellChanged.connect(
            lambda row, column: operations_callbacks.find_shade(row, column, self, 0, self.uiWindow.shade_closing_stock_table))
        self.uiWindow.shade_end_stock_view_confirm.clicked.connect(lambda: operations_callbacks.shade_display_closing(self))
        self.uiWindow.new_rm_entry_clear.clicked.connect(lambda: clear.new_rm_entry_clear_button(self))
        self.uiWindow.new_rm_add_clear.clicked.connect(lambda: clear.new_rm_add_clear_button(self))
        self.uiWindow.new_rm_modify_clear.clicked.connect(lambda: clear.new_rm_modify_clear_button(self))
        self.uiWindow.new_shade_delete_clear.clicked.connect(lambda: clear.new_shade_delete_clear_button(self))
        self.uiWindow.new_shade_entry_clear.clicked.connect(lambda: clear.new_shade_entry_clear_button(self))
        self.uiWindow.new_shade_modify_clear.clicked.connect(lambda: clear.new_shade_modify_clear_button(self))
        self.uiWindow.new_shade_view_clear.clicked.connect(lambda: clear.new_shade_view_clear_button(self))
        self.uiWindow.rm_add_clear.clicked.connect(lambda: clear.rm_add_clear_button(self))
        self.uiWindow.rm_delete_clear.clicked.connect(lambda: clear.rm_delete_clear_button(self))
        self.uiWindow.rm_modify_clear.clicked.connect(lambda: clear.rm_modify_clear_button(self))
        self.uiWindow.rm_stock_view_clear.clicked.connect(lambda: clear.rm_stock_view_clear_button(self))
        self.uiWindow.rm_view_by_id_clear.clicked.connect(lambda: clear.rm_view_by_id_clear_button(self))
        self.uiWindow.sales_add_clear.clicked.connect(lambda: clear.sales_add_clear_button(self))
        self.uiWindow.sales_delete_clear.clicked.connect(lambda: clear.sales_delete_clear_button(self))
        self.uiWindow.sales_modify_clear.clicked.connect(lambda: clear.sales_modify_clear_button(self))
        self.uiWindow.sales_view_by_id_clear.clicked.connect(lambda: clear.sales_view_by_id_clear_button(self))
        self.uiWindow.shade_add_clear.clicked.connect(lambda: clear.shade_add_clear_button(self))
        self.uiWindow.shade_delete_clear.clicked.connect(lambda: clear.shade_delete_clear_button(self))
        self.uiWindow.shade_modify_clear.clicked.connect(lambda: clear.shade_modify_clear_button(self))
        self.uiWindow.shade_stock_view_clear.clicked.connect(lambda: clear.shade_stock_view_clear_button(self))
        self.uiWindow.rm_stock_view_clear_2.clicked.connect(lambda: clear.rm_stock_view_clear_2_clear_button(self))
        self.uiWindow.shade_view_by_id_clear.clicked.connect(lambda: clear.shade_view_by_id_clear_button(self))
        self.uiWindow.sales_view_custom_back.clicked.connect(lambda: clear.sales_view_custom_back_button(self))
        self.uiWindow.back_view_rm_4.clicked.connect(lambda: clear.back_view_rm_4_back_button(self))
        self.uiWindow.back_view_rm_9.clicked.connect(lambda: clear.back_view_rm_9_back_button(self))
        self.uiWindow.shade_end_stock_view_clear.clicked.connect(lambda: clear.clear_shade_closing_stock(self))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.move(275,10)
    sys.exit(app.exec_())




