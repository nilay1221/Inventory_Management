import sqlite3
from PyQt5 import QtWidgets
import datetime

DATABASE_NAME = "newtable.db"


def foreign_key_support(mycursor):
    sql = "PRAGMA Foreign_keys = ON;"
    mycursor.execute(sql)

# For addding new raw material
def add_raw_material(product_code,product_name,product_price,product_type):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""
            INSERT into Raw_Material VALUES('{product_code}','{product_name}',{product_price},'{product_type}');
        """
        try:
            mycursor.execute(sql)
        # Checking if product code already exists or not in Database
        except sqlite3.IntegrityError as e:
            print(e)
            return False
        mydb.commit()
        sql = f"""
                    INSERT into rm_closing_stock VALUES('{product_code}',{0});
                """
        try:
            mycursor.execute(sql)
        except:
            pass
        mydb.commit()
        return True
    except:
        pass
    finally:
        mydb.close()

# For modifiying raw_material

# Return product name and price from the database
def return_modify_info(product_code):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""
            SELECT product_name,product_price,product_type from Raw_Material where product_code = '{product_code}';
        """
        try:
            mycursor.execute(sql)
            results = mycursor.fetchone()
            return {
                'product_name':results[0],
                'product_price':results[1],
                'product_type':results[2]
            }
        except :
            #TODO Checking for exception if product code not exists
            pass
    except:
        pass
    finally:
        mydb.close()

def get_all_raw_material():
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = "SELECT product_code from raw_material where product_type = 'R' ;"
        mycursor.execute(sql)
        results = mycursor.fetchall()
        myList = [each[0] for each in results]
        return myList
    except:
        pass
    finally:
        mydb.close

def modify_info(product_code,product_name,product_price,product_type,product_code_changed=False):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    # foreign_key_support(mycursor)
    try:
        if product_code_changed:
            sql = f"""
            UPDATE Raw_Material
            SET product_code='{product_code_changed}',product_name = '{product_name}' , product_price = {product_price}
            WHERE product_code = '{product_code}';
            """
        else:
            sql = f"""
                UPDATE Raw_Material
                SET product_name = '{product_name}' , product_price = {product_price} , product_type = '{product_type}'
                WHERE product_code = '{product_code}';
            """
        # print(sql)
        try:
            # mycursor.execute("PRAGMA foreign_keys = ON;")
            mycursor.execute(sql)
            mydb.commit()
        except Exception as e:
            print(e)
            #TODO check for exceptions
            return e
    except:
        pass
    finally:
        mydb.close()

# modify_info("49","test",12)
# View raw material

def get_rm_data():
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = " SELECT * from Raw_Material order by product_code;"
        try:
            mycursor.execute(sql)
            # print(results)
            results = mycursor.fetchall()
            return results
        except:
            pass
    except:
        pass
    finally:
        mydb.close()


# Delete new Raw Material

def delete_new_rm(product_code):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    # foreign_key_support(mycursor)
    try:
        sql = f"DELETE FROM Raw_Material WHERE product_code = '{product_code}';"
        # mycursor.execute("PRAGMA foreign_keys = OFF;")
        #mycursor.execute("PRAGMA foreign_keys")
        #result=mycursor.fetchall()
        #print(result)
        mycursor.execute(sql)
        sql = f"DELETE FROM madeup_of WHERE product_code = '{product_code}';"
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        print("false")
        return False

def get_product_name(code,product_type):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"SELECT product_name,product_type from raw_material where product_code='{code}';"
        try:
            mycursor.execute(sql)
            result = mycursor.fetchall()
            if product_type != "RC" and result[0][1] == product_type:
                return result[0][0]
            elif product_type == "RC":
                return result[0][0]
            else:
                return "Product mismatch"
        except Exception as e:
            return "false"
    except:
        pass
    finally:
        mydb.close()


def add_new_shade_material(shade_no):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql= f"INSERT INTO SHADE_NUMBER VALUES('{shade_no}')"
        try:
            mycursor.execute(sql)
        except sqlite3.IntegrityError as e:
            print(e)
            return False
        mydb.commit()
        return True
    except:
        pass
    finally:
        mydb.close()


def add_madeup_of(shade_no,code,percentage):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""INSERT into madeup_of VALUES('{shade_no}','{code}',{percentage});"""
        try:
            # print("Adding")
            # print(sql)
            mycursor.execute(sql)
        except sqlite3.IntegrityError as e:
            print(e)
        mydb.commit()
    except:
        pass
    finally:
        mydb.close()


def get_shade_details(shade_no):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""
                Select product_code,product_name,product_percentage FROM (
                Select madeup_of.shade_number,madeup_of.product_code,
                madeup_of.product_percentage,Raw_Material.product_name 
                from madeup_of 
                join Raw_Material where Raw_Material.product_code=madeup_of.product_code)
                where shade_number={shade_no};"""
        try:
            mycursor.execute(sql)
            # print(sql)
            results=mycursor.fetchall()
            # print(results)
            return results
        except:
            return "false"
    except:
        pass
    finally:
        mydb.close()


#Delete shade number data and delete
def new_shade_delete(shade_no):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"DELETE FROM shade_number WHERE shade_number = {shade_no};"
        mycursor.execute("PRAGMA foreign_keys = OFF;")
        # mycursor.execute("PRAGMA foreign_keys")
        # result=mycursor.fetchall()
        # print(result)
        mycursor.execute(sql)
        sql=f"Delete from madeup_of where shade_number = {shade_no};"
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        return False
    finally:
        mydb.close()

def remove_previous_data(shade_no):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"DELETE FROM madeup_of WHERE shade_number = {shade_no};"
        mycursor.execute("PRAGMA foreign_keys = ON;")
        # mycursor.execute("PRAGMA foreign_keys")
        # result=mycursor.fetchall()
        # print(result)
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        return False
    finally:
        mydb.close()


def modify_shade_data(shade_no,code,percentage,changed=1):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""INSERT into madeup_of VALUES('{shade_no}','{code}',{percentage});"""
        try:
            # print("Adding")
            # print(sql)
            mycursor.execute(sql)
        except sqlite3.IntegrityError as e:
            print(e)
        mydb.commit()
    except:
        pass
    finally:
        mydb.close()

def modify_new_shade_material(shade_no,old_shade_no):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql= f"Update SHADE_NUMBER set shade_number={shade_no} where shade_number={old_shade_no};"
        try:
            mycursor.execute("PRAGMA foreign_keys = ON;")
            mycursor.execute(sql)
        except Exception as e:
            print(e)
            return False
        mydb.commit()
        return True
    except:
        pass
    finally:
        mydb.close()

def get_shade_all():
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = " SELECT * from shade_number order by shade_number;"
        try:
            mycursor.execute(sql)
            # print(results)
            results = mycursor.fetchall()
            return results
        except:
            pass
    except:
        pass
    finally:
        mydb.close()

# Getting the last transaction id in the database
def get_trans_id(tableName,fieldName):
    sql = f"SELECT * from {tableName} WHERE trans_id LIKE '{fieldName}%' ORDER BY trans_id DESC LIMIT 1"
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        mycursor.execute(sql)
        results = mycursor.fetchone()
        # print(results)
        if results:
            trans_id = int(results[0].split(fieldName)[1]) + 1
            return str(trans_id).zfill(5)        
        else:
            return "00001"
    except:
        pass
    finally:
        mydb.close()

def add_raw_material_data(self,trans_id,date,customer,remark,productDetails,type="IN"):
    try:
        mydb = sqlite3.connect(DATABASE_NAME)
        mycursor = mydb.cursor()
        sql = f"INSERT INTO rm_stock VALUES('{trans_id}','{date}','{remark}','{customer}');"
        try:
            mycursor.execute(sql)
            mydb.commit()
            for each in productDetails:
                sql = f"INSERT into has_rm VALUES('{type}',{each[1]},'{trans_id}','{each[0]}','{each[2]}','{each[3]}')"
                # print(sql)
                try:
                    mycursor.execute(sql)
                except:
                    self.show_warning_info(f"Repeated entry of '{each[0]}' is rejected")
            mydb.commit()
            return True
        except Exception as e:
            # print(e)
            pass
        finally:
            mydb.close()
    except Exception as e:
        print(e)

# View Raw Material Transaction

def get_rm_transacs(by_Id=False,by_Today=False,by_custom=False):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        if by_Id:
            trans_id = by_Id
            sql = f"SELECT * from rm_stock WHERE trans_id = '{trans_id}' ;"
            mycursor.execute(sql)
            results = mycursor.fetchone()
            if results:
                sql = f"SELECT has_rm.product_code,'-',has_rm.quantity,has_rm.lot_no from has_rm WHERE has_rm.trans_id = '{trans_id}';"
                # print(sql)
                mycursor.execute(sql)
                products = mycursor.fetchall()
                # print(products)
                return [results,products]
                pass
            else:
                return None
        if by_Today:
            by_Today = datetime.date.today().strftime("%d-%m-%Y")
            sql =f"""
                SELECT rm_stock.trans_id,rm_stock.customer_id,rm_stock.remark,has_rm.product_code,'-',has_rm.quantity,has_rm.lot_no
                FROM rm_stock
                JOIN has_rm ON
                rm_stock.trans_id = has_rm.trans_id
                WHERE rm_stock.date = '{by_Today}';
            """
            # print(sql)
            mycursor.execute(sql)
            results = mycursor.fetchall()
            return results
        if by_custom:
            start_date = datetime.datetime.strptime(by_custom[0],'%d/%m/%Y').date()
            end_date = datetime.datetime.strptime(by_custom[1],'%d/%m/%Y').date()
            delta = end_date - start_date
            all_dates = []
            for i in range(delta.days + 1):
                day = end_date - datetime.timedelta(days=i)
                all_dates.append(day.strftime('%d-%m-%Y'))
            results=[]
            for each_date in all_dates:
                sql =f"""
                    SELECT rm_stock.trans_id,rm_stock.date,rm_stock.customer_id,rm_stock.remark,has_rm.product_code,'-',has_rm.quantity,has_rm.lot_no
                    FROM rm_stock
                    JOIN has_rm ON
                    rm_stock.trans_id = has_rm.trans_id
                    WHERE rm_stock.date = '{each_date}' order by date,rm_stock.trans_id;
                """
                try:
                    # print(sql)
                    mycursor.execute(sql)
                    result = mycursor.fetchall()
                    # print(result)
                    if result:
                        results.append(result)
                except:
                    pass
            return results
    except:
        pass
    finally:
        mydb.close()


        
# print(get_rm_transacs(by_custom=['02/05/2020','05/05/2020']))
      
# get_rm_transacs(by_Today=True)

def check_rm_transacs(trans_id):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f""" SELECT EXISTS(SELECT trans_id from rm_stock where trans_id = '{trans_id}') ; """
        mycursor.execute(sql)
        results = mycursor.fetchone()
        # print(results)
        if results[0] == 1:
            return True
        else:
            return False
    except:
        pass
    finally:
        mydb.close()

def delete_rm_transacs(trans_id):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    foreign_key_support(mycursor)
    sql = f"DELETE from rm_stock where trans_id = '{trans_id}';"
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()


# print(get_trans_id('shade_stock','SNT'))
# print(check_rm_transacs('RMT001'))\

def check_shade_number_exists(shade_number):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"SELECT EXISTS(SELECT * from shade_number where shade_number = '{shade_number}');"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result[0] == 0:
            return False
        elif result[0] == 1:
            return True
    except:
        pass
    finally:
        mydb.close()
                
def get_shade_number_details(shade_number):
    if check_shade_number_exists(shade_number):
        mydb = sqlite3.connect(DATABASE_NAME)
        mycursor = mydb.cursor()
        sql = f"""
                SELECT madeup_of.product_code , raw_material.product_name ,madeup_of.product_percentage,'-',raw_material.product_price
                FROM madeup_of
                JOIN raw_material
                ON madeup_of.product_code = raw_material.product_code
                WHERE shade_number = '{shade_number}';
            """
        mycursor.execute(sql)
        results = mycursor.fetchall()
        mydb.close()
        return results
    else:
        return False

def add_shade_stock_trans(self,trans_id,date,customer,remark,shade_number,productDetails,type="IN"):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f" INSERT INTO shade_stock VALUES('{trans_id}','{date}','{customer}','{remark}','{shade_number}'); "
        mycursor.execute(sql)
        mydb.commit()
        try:
            for each in productDetails:
                sql = f"INSERT INTO has_shade VALUES('{type}',{each[1]},'{trans_id}','{shade_number}','{each[0]}','{each[2]}'); "
                try:
                    mycursor.execute(sql)
                except:
                    # self.show_warning_info(f"Repeated entry of '{each[0]}' is rejected")
                    pass
            mydb.commit()
        except:
            pass
    except:
        pass
    finally:
        mydb.close()

def add_into_duplicates(shade_trans,raw_trans):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"INSERT INTO duplicates VALUES('{raw_trans}','{shade_trans}');"
        mycursor.execute(sql)
        mydb.commit()
    except:
        pass
    finally:
        mydb.close()

def check_shade_trans(trans_id):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"SELECT EXISTS(SELECT * from shade_stock WHERE trans_id = '{trans_id}');"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result[0] == 0:
            return False
        else:
            return True
    except Exception as e:
        print(e)
    finally:
        mydb.close()


def view_shade_transaction(by_Id=False,by_today=False,by_custom=False):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        if by_Id:
            shade_trans_id = by_Id
            sql = f"SELECT rm_trans_id from duplicates where shade_trans_id = '{shade_trans_id}';"
            mycursor.execute(sql)
            raw_trans_id = mycursor.fetchone()[0]
            sql = f"SELECT date,customer_id,remark,shade_number from shade_stock where trans_id = '{shade_trans_id}';"
            mycursor.execute(sql)
            trans_details = mycursor.fetchone()
            shade_number = trans_details[3]
            sql = f"""
                    SELECT has_shade.product_code , '-' ,has_shade.quantity,has_shade.lot_no 
                    FROM has_shade
                    WHERE has_shade.trans_id = '{shade_trans_id}';
            """
            mycursor.execute(sql)
            table1_details = mycursor.fetchall()
            sql = f"""
                SELECT has_rm.product_code,'-',madeup_of.product_percentage,has_rm.quantity*1000,has_rm.quantity * raw_material.product_price * 1000,has_rm.lot_no  FROM
                has_rm
                JOIN madeup_of ON
                has_rm.product_code = madeup_of.product_code
                JOIN raw_material ON
                madeup_of.product_code = raw_material.product_code
                WHERE has_rm.trans_id = "{raw_trans_id}"
                AND madeup_of.shade_number = "{shade_number}"
                AND has_rm.product_code NOT IN(SELECT has_shade.product_code from has_shade WHERE trans_id = "{shade_trans_id}");
                """
            # print(sql)
            mycursor.execute(sql)
            table2_details = mycursor.fetchall()
            # print(table2_details)
            return {
                'trans_details':trans_details,
                'table1_details':table1_details,
                'table2_detials':table2_details,
            }
        if by_today:
            today_date = datetime.date.today().strftime('%d-%m-%Y')
            sql = f"""
                 SELECT shade_stock.trans_id , shade_stock.customer_id , shade_stock.remark , shade_stock.shade_number , has_shade.product_code ,'-',has_shade.quantity,has_shade.lot_no  FROM shade_stock
                 JOIN has_shade
                 ON shade_stock.trans_id = has_shade.trans_id
                 WHERE shade_stock.date = '{today_date}';
            """
            mycursor.execute(sql)
            results = mycursor.fetchall()
            return results
        if by_custom:
            start_date = datetime.datetime.strptime(by_custom[0],'%d/%m/%Y').date()
            end_date = datetime.datetime.strptime(by_custom[1],'%d/%m/%Y').date()
            delta = end_date - start_date
            all_dates = []
            for i in range(delta.days + 1):
                day = end_date - datetime.timedelta(days=i)
                all_dates.append(day.strftime('%d-%m-%Y'))
            results=[]
            for each_date in all_dates:
                sql = f"""
                 SELECT shade_stock.trans_id , shade_stock.date, shade_stock.customer_id , shade_stock.remark , shade_stock.shade_number , has_shade.product_code ,'-',has_shade.quantity,has_shade.lot_no  FROM shade_stock
                 JOIN has_shade
                 ON shade_stock.trans_id = has_shade.trans_id
                 WHERE shade_stock.date = '{each_date}' order by date,shade_stock.trans_id;
                """
                try:
                    # print(sql)
                    mycursor.execute(sql)
                    result = mycursor.fetchall()
                    # print(result)
                    if result:
                        results.append(result)
                except:
                    pass
            return results
    except Exception as e:
        print(e)
        pass
    finally:
        mydb.close()
        
# print(view_shade_transaction(by_today=True))
# print(check_shade_trans("SNT00009"))


def delete_shade_trans(trans_id):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        foreign_key_support(mycursor)
        sql =  f"SELECT rm_trans_id from duplicates where shade_trans_id = '{trans_id}';"
        mycursor.execute(sql)
        rm_trans_id = mycursor.fetchone()[0]
        sql = f"DELETE from shade_stock where trans_id = '{trans_id}';"
        mycursor.execute(sql)
        sql = f"DELETE from rm_stock where trans_id = '{rm_trans_id}';"
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        return False
    finally:
        mydb.close()

def get_raw_trans(shade_trans_id):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"SELECT rm_trans_id from duplicates where shade_trans_id = '{shade_trans_id}';"
        # print(sql)
        mycursor.execute(sql)
        return mycursor.fetchone()[0]
    except:
        pass
    finally:
        mydb.close()

# print(delete_shade_trans)

def add_sales_data(self,trans_id,date,customer,remark,productDetails,type="OUT"):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    sql = f"INSERT INTO sales VALUES('{trans_id}','{customer}','{date}','{remark}');"
    try:
        mycursor.execute(sql)
        mydb.commit()
        for each in productDetails:
            sql = f"INSERT into consists_of VALUES('{type}',{each[2]},'{trans_id}','{each[0]}','{each[1]}','{each[3]}')"
            try:
                mycursor.execute(sql)
            except:
                self.show_warning_info(f"Repeated entry of '{each[0]}' and '{each[1]}' is rejected")
        mydb.commit()
        return True
    except Exception as e:
        print(e)
    finally:
        mydb.close()


def get_sales_transacs(by_Id=False,by_Today=False,by_custom=False):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        if by_Id:
            trans_id = by_Id
            sql = f"SELECT * from sales WHERE trans_id = '{trans_id}' ;"
            mycursor.execute(sql)
            results = mycursor.fetchone()
            if results:
                sql = f"""SELECT consists_of.shade_number,consists_of.product_code,'-',consists_of.quantity,consists_of.lot_no
                from consists_of WHERE consists_of.trans_id = '{trans_id}';"""
                # print(sql)
                mycursor.execute(sql)
                products = mycursor.fetchall()
                # print(products)
                return [results,products]
                pass
            else:
                return None
        if by_Today:
            by_Today = datetime.date.today().strftime("%d-%m-%Y")
            sql =f"""
                SELECT sales.trans_id,sales.customer_id,sales.remark,
                consists_of.shade_number,consists_of.product_code,'-',consists_of.quantity,consists_of.lot_no
                FROM sales
                JOIN consists_of ON
                sales.trans_id = consists_of.trans_id
                WHERE sales.date = '{by_Today}';
            """
            # print(sql)
            mycursor.execute(sql)
            results = mycursor.fetchall()
            # print(results)
            return results
        if by_custom:
            start_date = datetime.datetime.strptime(by_custom[0],'%d/%m/%Y').date()
            end_date = datetime.datetime.strptime(by_custom[1],'%d/%m/%Y').date()
            delta = end_date - start_date
            all_dates = []
            for i in range(delta.days + 1):
                day = end_date - datetime.timedelta(days=i)
                all_dates.append(day.strftime('%d-%m-%Y'))
            results=[]
            for each_date in all_dates:
                sql =f"""
                    SELECT sales.trans_id,sales.date,sales.customer_id,sales.remark,
                    consists_of.shade_number,consists_of.product_code,'-',consists_of.quantity,consists_of.lot_no
                    FROM sales
                    JOIN consists_of ON
                    sales.trans_id = consists_of.trans_id
                    WHERE sales.date = '{each_date}' order by date,sales.trans_id;
                """
                try:
                    # print(sql)
                    mycursor.execute(sql)
                    result = mycursor.fetchall()
                    # print(result)
                    if result:
                        results.append(result)
                except:
                    pass
            return results
    except Exception as e:
        print(e)
    finally:
        mydb.close()


def get_shade(shade):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql=f"Select * from shade_number where shade_number={shade};"
        mycursor.execute(sql)
        results=mycursor.fetchone()
        if results[0]:
            return True
        else:
            return False
    except:
        pass
    finally:
        mydb.close()


def check_sales_transacs(trans_id):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f""" SELECT EXISTS(SELECT trans_id from sales where trans_id = '{trans_id}'); """
        mycursor.execute(sql)
        results = mycursor.fetchone()
        return results[0]
    except:
        pass
    finally:
        mydb.close()


def delete_sales_transacs(trans_id):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        foreign_key_support(mycursor)
        sql = f"DELETE from sales where trans_id = '{trans_id}';"
        mycursor.execute(sql)
        mydb.commit()
    except:
        pass
    finally:
        mydb.close()


# Closing stock view for Raw material
def get_product_stock(code,lot,by_custom):
    start_date = datetime.datetime.strptime(by_custom[0], '%d/%m/%Y').date()
    end_date = datetime.datetime.strptime(by_custom[1], '%d/%m/%Y').date()
    delta = end_date - start_date
    all_dates = []
    for i in range(delta.days + 1):
        day = end_date - datetime.timedelta(days=i)
        all_dates.append(day.strftime('%d-%m-%Y'))
    results = []
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        if lot == "All" or lot == "all" or lot == "ALL":
            for each in all_dates:
                sql = f"""select * from 
                 (select RM_Stock.trans_id,RM_Stock.date,has_rm.quantity,'-',has_rm.lot_no from has_rm join RM_Stock on RM_Stock.trans_id= has_rm.trans_id 
                  where type = "IN" and product_code = '{code}' and date='{each}'
                  UNION
                  select RM_Stock.trans_id,RM_Stock.date,'-',has_rm.quantity,has_rm.lot_no from has_rm join RM_Stock on RM_Stock.trans_id= has_rm.trans_id
                  where type = "OUT" and product_code = '{code}' and date='{each}') order by date;"""
                mycursor.execute(sql)
                result=mycursor.fetchall()
                if result:
                    results.append(result)
            return results
        else:
            for each in all_dates:
                sql = f"""select * from 
                 (select RM_Stock.trans_id,RM_Stock.date,has_rm.quantity,'-',has_rm.lot_no from has_rm join RM_Stock on RM_Stock.trans_id= has_rm.trans_id 
                  where type = "IN" and product_code = '{code}' and date='{each}'and lot_no='{lot}'
                  UNION
                  select RM_Stock.trans_id,RM_Stock.date,'-',has_rm.quantity,has_rm.lot_no from has_rm join RM_Stock on RM_Stock.trans_id= has_rm.trans_id
                  where type = "OUT" and product_code = '{code}' and date='{each}'and lot_no='{lot}') order by date;"""
                mycursor.execute(sql)
                result=mycursor.fetchall()
                if result:
                    results.append(result)
            return results
    except:
        pass
    finally:
        mydb.close()


def raw_material_closing_stock(code,lot):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        if lot=="All" or lot=="all" or lot=="ALL":
            sql = f"""Select sum(opening) from rm_opening_stock where product_code='{code}'"""
            mycursor.execute(sql)
            opening = mycursor.fetchone()
            if not opening[0]:
                stock_opening = 0
            else:
                stock_opening = opening[0]
            sql = f"""Select sum(quantity) from has_rm where product_code='{code}' and type = 'IN'"""
            mycursor.execute(sql)
            total_in = mycursor.fetchone()
            if not total_in[0]:
                total_in = "None"
            else:
                total_in = total_in[0]
            sql = f"""Select sum(quantity) from has_rm where product_code='{code}' and type = 'OUT'"""
            mycursor.execute(sql)
            total_out = mycursor.fetchone()
            if total_in == "None":
                if not total_out[0]:
                    if stock_opening!=0:
                        return str(stock_opening)
                    else:
                        return "None"
                else:
                    total_in = 0
            if not total_out[0]:
                total_out = 0
            else:
                total_out = total_out[0]
            # print(stock_opening)
            total = stock_opening + total_in - total_out
            # print(total - stock_opening)
            return round(total, 2)
        else:
            sql = f"""Select sum(opening) from rm_opening_stock where product_code='{code}' and lot_no='{lot}'"""
            mycursor.execute(sql)
            opening = mycursor.fetchone()
            if not opening[0]:
                stock_opening = 0
            else:
                stock_opening = opening[0]
            sql = f"""Select sum(quantity) from has_rm where product_code='{code}' and type = 'IN' and lot_no='{lot}'"""
            mycursor.execute(sql)
            total_in = mycursor.fetchone()
            if not total_in[0]:
                total_in = "None"
            else:
                total_in = total_in[0]
            sql = f"""Select sum(quantity) from has_rm where product_code='{code}' and type = 'OUT' and lot_no='{lot}'"""
            mycursor.execute(sql)
            total_out = mycursor.fetchone()
            if total_in=="None":
                if not total_out[0]:
                    if stock_opening != 0:
                        return str(stock_opening)
                    else:
                        return "None"
                else:
                    total_in=0
            if not total_out[0]:
                total_out = 0
            else:
                total_out = total_out[0]
            total= stock_opening + total_in - total_out
            return round(total,2)
    except Exception as e:
        # print("inside")
        print(e)
    finally:
        mydb.close()


def get_shade_stock(shade,code,lot,by_custom):
    start_date = datetime.datetime.strptime(by_custom[0], '%d/%m/%Y').date()
    end_date = datetime.datetime.strptime(by_custom[1], '%d/%m/%Y').date()
    delta = end_date - start_date
    all_dates = []
    for i in range(delta.days + 1):
        day = end_date - datetime.timedelta(days=i)
        all_dates.append(day.strftime('%d-%m-%Y'))
    results = []
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        if lot == "All" or lot == "all" or lot == "ALL":
            for each in all_dates:
                sql=f"""select * from 
                        (select has_shade.trans_id,date,quantity,'-',has_shade.lot_no from has_shade 
                        join shade_Stock on shade_stock.trans_id= has_shade.trans_id 
                        where product_code = '{code}' and has_shade.shade_number = {shade}
                        UNION select consists_of.trans_id,date,'-',quantity,consists_of.lot_no from consists_of 
                        join sales on sales.trans_id= consists_of.trans_id 
                        where product_code = '{code}' and consists_of.shade_number = {shade}) where date='{each}'"""
                mycursor.execute(sql)
                result=mycursor.fetchall()
                if result:
                    results.append(result)
            return results
        else:
            for each in all_dates:
                sql=f"""select * from 
                        (select has_shade.trans_id,date,quantity,'-',has_shade.lot_no from has_shade 
                        join shade_Stock on shade_stock.trans_id= has_shade.trans_id 
                        where product_code = '{code}' and has_shade.shade_number = {shade} and lot_no = '{lot}'
                        UNION select consists_of.trans_id,date,'-',quantity,consists_of.lot_no from consists_of 
                        join sales on sales.trans_id= consists_of.trans_id 
                        where product_code = '{code}' and consists_of.shade_number = {shade} and lot_no = '{lot}') where date='{each}'"""
                mycursor.execute(sql)
                result=mycursor.fetchall()
                if result:
                    results.append(result)
            return results
    except Exception as e:
        print(e)
    finally:
        mydb.close()


def shade_raw_closing_stock(shade,code,lot):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        if lot == "All" or lot == "all" or lot == "ALL":
            sql = f"""Select sum(opening_stock) from sn_opening_stock where product_code='{code}' and shade_number='{shade}'"""
            mycursor.execute(sql)
            opening = mycursor.fetchone()
            if not opening[0]:
                stock_opening = 0
            else:
                stock_opening = opening[0]
            sql = f"""Select sum(quantity) from has_shade where product_code='{code}' and shade_number='{shade}' and type = 'IN'"""
            mycursor.execute(sql)
            total_in = mycursor.fetchone()
            if not total_in[0]:
                total_in = "None"
            else:
                total_in = total_in[0]
            sql = f"""Select sum(quantity) from consists_of where product_code='{code}' and shade_number='{shade}' and type = 'OUT'"""
            mycursor.execute(sql)
            total_out = mycursor.fetchone()
            if total_in == "None":
                if not total_out[0]:
                    if stock_opening != 0:
                        return str(stock_opening)
                    else:
                        return "None"
                else:
                    total_in = 0
            if not total_out[0]:
                total_out = 0
            else:
                total_out = total_out[0]
            total = stock_opening + total_in - total_out
            return round(total,2)
        else:
            sql = f"""Select sum(opening_stock) from sn_opening_stock where product_code='{code}' and shade_number='{shade}' and lot_no='{lot}'"""
            mycursor.execute(sql)
            opening = mycursor.fetchone()
            if not opening[0]:
                stock_opening = 0
            else:
                stock_opening = opening[0]
            sql = f"""Select sum(quantity) from has_shade where product_code='{code}' and shade_number={shade} and type = 'IN' and lot_no='{lot}'"""
            mycursor.execute(sql)
            total_in = mycursor.fetchone()
            if not total_in[0]:
                total_in = "None"
            else:
                total_in = total_in[0]
            sql = f"""Select sum(quantity) from consists_of where product_code='{code}' and shade_number={shade} and type = 'OUT' and lot_no='{lot}'"""
            mycursor.execute(sql)
            total_out = mycursor.fetchone()
            if total_in == "None":
                if not total_out[0]:
                    if stock_opening != 0:
                        return str(stock_opening)
                    else:
                        return "None"
                else:
                    total_in = 0
            if not total_out[0]:
                total_out = 0
            else:
                total_out = total_out[0]
            # print(stock_opening)
            total = stock_opening + total_in - total_out
            # print(total-stock_opening)
            return round(total, 2)
    except Exception as e:
        print(e)
    finally:
        mydb.close()

def get_all_rm_data(type):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"SELECT product_code,product_name from Raw_Material where product_type='{type}' order by product_code;"
        try:
            mycursor.execute(sql)
            results = mycursor.fetchall()
            return results
        except Exception as e:
            print(e)
    except:
        pass
    finally:
        mydb.close()

def add_rm_opening(product_code, lot, opening):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""
            INSERT into rm_opening_stock VALUES('{product_code}','{lot}',{opening});
        """
        try:
            mycursor.execute(sql)
        # Checking if product code already exists or not in Database
        except sqlite3.IntegrityError as e:
            print(e)
            return False
        mydb.commit()
        return True
    except:
        pass
    finally:
        mydb.close()

def view_rm_opening(code,lot):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""
                select opening from rm_opening_stock where product_code='{code}' and lot_no='{lot}';
            """
        mycursor.execute(sql)
        result=mycursor.fetchone()
        return result[0]
    except Exception as e:
        print(e)
    finally:
        mydb.close()

def del_rm_opening(code, lot):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""
                    delete from rm_opening_stock where product_code='{code}' and lot_no='{lot}';
                """
        mycursor.execute(sql)
        mydb.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        mydb.close()


def shade_add_opening(shade,product_code, lot, opening):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""
            INSERT into sn_opening_stock VALUES('{shade}','{product_code}','{lot}',{opening});
        """
        try:
            mycursor.execute(sql)
        # Checking if product code already exists or not in Database
        except sqlite3.IntegrityError as e:
            print(e)
            return False
        mydb.commit()
        return True
    except:
        pass
    finally:
        mydb.close()

def view_shade_opening(shade,code,lot):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""
                select opening_stock from sn_opening_stock where shade_number='{shade}' and product_code='{code}' and lot_no='{lot}';
            """
        mycursor.execute(sql)
        result=mycursor.fetchone()
        return result[0]
    except Exception as e:
        print(e)
    finally:
        mydb.close()


def shade_del_opening(shade,code, lot):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""
                    delete from sn_opening_stock where shade_number='{shade}' and product_code='{code}' and lot_no='{lot}';
                """
        mycursor.execute(sql)
        mydb.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        mydb.close()

