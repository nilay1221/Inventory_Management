import sqlite3 
from PyQt5 import QtWidgets


# For addding new raw material 
def add_raw_material(product_code,product_name,product_price):
    mydb = sqlite3.connect("inventory.db")
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
        return True
    except:
        pass
    finally:
        mydb.close()

# For modifiying raw_material

# Return product name and price from the database
def return_modify_info(product_code):
    mydb = sqlite3.connect("inventory.db")
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

def modify_info(product_code,product_name,product_price):
    mydb = sqlite3.connect("inventory.db")
    mycursor = mydb.cursor()
    try:
        sql = f"""
            UPDATE Raw_Material
            SET product_name = '{product_name}' , product_price = {product_price}
            WHERE product_code = '{product_code}';
        """
        try:
            mycursor.execute(sql)
            mydb.commit()
        except:
            #TODO check for exceptions
            pass
    except:
        pass
    finally:
        mydb.close()


# View raw material 

def get_rm_data():
    mydb = sqlite3.connect("inventory.db")
    mycursor = mydb.cursor()
    try:
        sql = " SELECT * from Raw_Material order by product_code;"
        try:
            results = mycursor.execute(sql)
            print(results)
            # results = mycursor.fetchall()
            return results
        except:
            pass
    except:
        pass


def get_product_name(code):
    mydb = sqlite3.connect("inventory.db")
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
    mydb = sqlite3.connect("inventory.db")
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
    mydb = sqlite3.connect("inventory.db")
    mycursor = mydb.cursor()
    try:
        sql = f"""INSERT into madeup_of VALUES('{shade_no}','{code}',{percentage});"""
        try:
            mycursor.execute(sql)
        except sqlite3.IntegrityError as e:
            print(e)
        mydb.commit()
    except:
        pass
    finally:
        mydb.close()


def get_shade_details(shade_no):
    mydb = sqlite3.connect("inventory.db")
    mycursor = mydb.cursor()
    try:
        sql = f"""
                Select product_code,product_name,product_percentage FROM (
                Select madeup_of.shade_number,madeup_of.product_code,
                madeup_of.product_percentage,Raw_Material.product_name 
                from madeup_of 
                join Raw_Material where Raw_Material.product_code=madeup_of.product_code)
                where shade_number={shade_no}"""
        try:
            mycursor.execute(sql)
            results=mycursor.fetchall()
            return results
        except:
            return "false"
    except:
        pass
    finally:
        mydb.close()