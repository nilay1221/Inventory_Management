import sqlite3
from PyQt5 import QtWidgets
import datetime

DATABASE_NAME = "newtable.db"


def foreign_key_support(mycursor):
    sql = "PRAGMA Foreign_keys = ON;"
    mycursor.execute(sql)

# For addding new raw material
def add_raw_material(product_code,product_name,product_price):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"""
            INSERT into Raw_Material VALUES('{product_code}','{product_name}',{product_price});
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
            SELECT product_name,product_price from Raw_Material where product_code = '{product_code}';
        """
        try:
            mycursor.execute(sql)
            results = mycursor.fetchone()
            return {
                'product_name':results[0],
                'product_price':results[1]
            }
        except :
            #TODO Checking for exception if product code not exists
            pass
    except:
        pass
    finally:
        mydb.close()

def modify_info(product_code,product_name,product_price,product_code_changed=False):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    foreign_key_support(mycursor)
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
                SET product_name = '{product_name}' , product_price = {product_price}
                WHERE product_code = '{product_code}';
            """
        # print(sql)
        try:
            mycursor.execute("PRAGMA foreign_keys = ON;")
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
            results = mycursor.execute(sql)
            # print(results)
            # results = mycursor.fetchall()
            return results
        except:
            pass
    except:
        pass


# Delete new Raw Material

def delete_new_rm(product_code):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    foreign_key_support(mycursor)
    try:
        sql = f"DELETE FROM Raw_Material WHERE product_code = '{product_code}';"
        mycursor.execute("PRAGMA foreign_keys = ON;")
        #mycursor.execute("PRAGMA foreign_keys")
        #result=mycursor.fetchall()
        #print(result)
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        print("false")
        return False

def get_product_name(code):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        sql = f"SELECT product_name from raw_material where product_code='{code}';"
        try:
            mycursor.execute(sql)
            result = mycursor.fetchall()
            return result[0][0]
        except:
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



# Getting the last transaction id in the database
def get_trans_id(tableName):
    sql = f"SELECT * from {tableName} WHERE trans_id LIKE 'RMT%' ORDER BY trans_id DESC LIMIT 1"
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    try:
        mycursor.execute(sql)
        results = mycursor.fetchone()
        # print(results)
        if results:
            trans_id = int(results[0].split("RMT")[1]) + 1
            return str(trans_id).zfill(5)        
        else:
            return "00001"
    except:
        pass
    finally:
        mydb.close()

def add_raw_material_data(trans_id,date,customer,remark,productDetails,type="IN"):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    sql = f"INSERT INTO rm_stock VALUES('{trans_id}','{date}','{remark}','{customer}');"
    try:
        mycursor.execute(sql)
        mydb.commit()
        for each in productDetails:
            sql = f"INSERT into has_rm VALUES('{type}',{each[1]},'{trans_id}','{each[0]}')"
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


# View Raw Material Transaction

def get_rm_transacs(by_Id=False,by_Today=False,by_custom=False):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    if by_Id:
        trans_id = by_Id
        sql = f"SELECT * from rm_stock WHERE trans_id = '{trans_id}' ;"
        mycursor.execute(sql)
        results = mycursor.fetchone()
        if results:
            sql = f"SELECT has_rm.product_code,raw_material.product_name,has_rm.quantity from raw_material JOIN has_rm ON has_rm.product_code = raw_material.product_code WHERE has_rm.trans_id = '{trans_id}';"
            mycursor.execute(sql)
            products = mycursor.fetchall()
            return [results,products]
            pass
        else:
            return None
    if by_Today:
        by_Today = datetime.date.today().strftime("%d-%m-%Y")
        sql =f"""
            SELECT rm_stock.trans_id,rm_stock.customer_id,rm_stock.remark,has_rm.product_code,raw_material.product_name,has_rm.quantity
            FROM rm_stock
            JOIN has_rm ON
            rm_stock.trans_id = has_rm.trans_id
            JOIN raw_material ON
            has_rm.product_code = raw_material.product_code
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
                SELECT rm_stock.trans_id,rm_stock.date,rm_stock.customer_id,rm_stock.remark,has_rm.product_code,raw_material.product_name,has_rm.quantity
                FROM rm_stock
                JOIN has_rm ON
                rm_stock.trans_id = has_rm.trans_id
                JOIN raw_material ON
                has_rm.product_code = raw_material.product_code
                WHERE rm_stock.date = '{each_date}';
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
        mydb.close()


        
# print(get_rm_transacs(by_custom=['02/05/2020','05/05/2020']))
      
# get_rm_transacs(by_Today=True)

def check_rm_transacs(trans_id):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    sql = f""" SELECT EXISTS(SELECT trans_id from rm_stock where trans_id = '{trans_id}') ; """
    mycursor.execute(sql)
    results = mycursor.fetchone()
    # print(results)
    mydb.close()
    if results[0] == 1:
        return True
    else:
        return False

def delete_rm_transacs(trans_id):
    mydb = sqlite3.connect(DATABASE_NAME)
    mycursor = mydb.cursor()
    foreign_key_support(mycursor)
    sql = f"DELETE from rm_stock where trans_id = '{trans_id}';"
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()


# print(get_trans_id('rm_stock'))
# print(check_rm_transacs('RMT001'))