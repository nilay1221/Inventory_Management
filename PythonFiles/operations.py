import sqlite3 


mydb = sqlite3.connect("inventory.db")
mycursor = mydb.cursor()


# For addding new raw material 
def add_raw_material(product_code,product_name,product_price):
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

# For modifiying raw_material

# Return product name and price from the database
def return_modify_info(product_code):
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

def modify_info(product_code,product_name,product_price):
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


# View raw material 

def get_rm_data():
    sql = " SELECT * from Raw_Material;"
    try:
        results = mycursor.execute(sql)
        # results = mycursor.fetchall()
        return results
    except:
        pass

