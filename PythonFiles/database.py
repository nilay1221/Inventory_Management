import sqlite3

mydb = sqlite3.connect("newtable.db")

mycursor = mydb.cursor()

class MyQuery:
    def __init__(self,sql):
        self.sql = sql

    def sql_execute(self,mycursor):
        mycursor.execute(self.sql)


MyQuery("""CREATE TABLE Raw_Material(
    product_code varchar(255) NOT NULL UNIQUE PRIMARY KEY ,
    product_name varchar(255),
    product_price integer
); """).sql_execute(mycursor)

MyQuery("""
    CREATE TABLE consists_of(
        type varchar(255),
        quantity real NOT NULL,
        product_code NOT NULL,
        FOREIGN KEY(product_code) REFERENCES Raw_Material(product_code) ON UPDATE CASCADE ON DELETE CASCADE
    );
""").sql_execute(mycursor)

MyQuery("""
    CREATE TABLE RM_Stock(
        Trans_id varchar(255) NOT NULL UNIQUE PRIMARY KEY,
        date text,
        remark text,
        customer_id varchar(255)
    );
""").sql_execute(mycursor)


MyQuery("""
    CREATE TABLE has_rm(
        type varchar(255),
        quantity real NOT NULL,
        trans_id varchar(255) NOT NULL,
        product_code varchar(255) NOT NULL,
        FOREIGN KEY(trans_id) REFERENCES Rm_Stock(Trans_id) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY(product_code) REFERENCES Raw_Material(product_code) ON UPDATE CASCADE ON DELETE CASCADE,
        PRIMARY KEY (trans_id,product_code)
    );""").sql_execute(mycursor)

MyQuery("""
CREATE TABLE madeup_of(
        shade_number varchar(255), 
        product_code varchar(255) NOT NULL ,
        product_percentage real,
        FOREIGN KEY(shade_number) REFERENCES shade_number(shade_number) ON UPDATE CASCADE ON DELETE CASCADE
    );

""").sql_execute(mycursor)

MyQuery("""
    CREATE TABLE shade_stock(
        trans_id varchar(255) NOT NULL UNIQUE PRIMARY KEY,
        date text,
        customer_id varchar(255),
        remark varchar(255),
        shade_number varchar(255),
        FOREIGN KEY(shade_number) REFERENCES shade_number(shade_number) ON UPDATE CASCADE ON DELETE CASCADE
        )
""").sql_execute(mycursor)

MyQuery("""
     CREATE TABLE sales(
         trans_id varchar(255) NOT NULL UNIQUE PRIMARY KEY,
         customer_id varchar(255),
         date text ,
         remark varchar(255)
     );
""").sql_execute(mycursor)  

# MyQuery("""
#     CREATE TABLE madeup_of(
#         product_code varchar(255) NOT NULL UNIQUE PRIMARY KEY,
#         product_name varchar(255),
#         product_percentage real,
#         shade_number varchar(255),
#         FOREIGN KEY(shade_number) REFERENCES shade_number(shade_number)
#     )
# """).sql_execute(mycursor)

# MyQuery("""
#     CREATE TABLE shade_stock(
#         trans_id varchar(255) NOT NULL UNIQUE PRIMARY KEY,
#         date text,
#         customer_id varchar(255),
#         remark varchar(255),
#         shade_number varchar(255),
#         FOREIGN KEY(shade_number) REFERENCES shade_number(shade_number)
#         )
# """).sql_execute(mycursor)

# MyQuery("""
#      CREATE TABLE sales(
#          trans_id varchar(255) NOT NULL UNIQUE PRIMARY KEY,
#          customer_id varchar(255),
#          date text ,
#          remark varchar(255)
#      );
# """).sql_execute(mycursor)

MyQuery("""
CREATE TABLE shade_number(
         shade_number varchar(255) NOT NULL UNIQUE PRIMARY KEY
     );
""").sql_execute(mycursor)

MyQuery("""
    CREATE TABLE has_shade(
        type varchar(255),
        quantity real,
        trans_id varchar(255),
        shade_number varchar(255),
       product_code varchar(255),
        FOREIGN KEY(trans_id) REFERENCES shade_stock(trans_id) ON UPDATE CASCADE ON DELETE CASCADE,
       PRIMARY KEY(trans_id,shade_number,product_code)
);
""").sql_execute(mycursor)


MyQuery("""
    CREATE TABLE manages(
        product_code varchar(255),
        sales_trans_id varchar(255),
        shade_number varchar(255),
        FOREIGN KEY(product_code)  REFERENCES Raw_Material(product_code) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY(sales_trans_id) REFERENCES sales(trans_id) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY(shade_number) REFERENCES shade_number(shade_number) ON UPDATE CASCADE ON DELETE CASCADE,
        PRIMARY KEY(product_code,sales_trans_id,shade_number)
    );
""").sql_execute(mycursor)


# MyQuery("""
#     CREATE TABLE duplicates(
#         rm_trans_id varchar(255),
#         shade_trans_id varchar(255),
#         FOREIGN KEY(rm_trans_id) REFERENCES Rm_Stock(trans_id),
#         FOREIGN KEY(shade_trans_id) REFERENCES shade_stock(trans_id)
#     );
# """).sql_execute(mycursor)



MyQuery("""
    CREATE TABLE duplicates(
        rm_trans_id varchar(255),
        shade_trans_id varchar(255),
        FOREIGN KEY(rm_trans_id) REFERENCES Rm_Stock(trans_id) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY(shade_trans_id) REFERENCES shade_stock(trans_id) ON UPDATE CASCADE ON DELETE CASCADE,
        PRIMARY KEY (rm_trans_id,shade_trans_id)
    );
""").sql_execute(mycursor)

MyQuery("""
    CREATE TABLE rm_closing_stock(
        product_code varchar(255),
        closing stock real,
        FOREIGN KEY(product_code) REFERENCES Raw_Material(product_code) ON UPDATE CASCADE ON DELETE CASCADE
    );
""").sql_execute(mycursor)

MyQuery("""
CREATE TABLE sn_closing_stock(
        shade_number varchar(255),
        product_code varchar(255),
        closing_stock real,
        FOREIGN KEY(shade_number) REFERENCES shade_number(shade_number) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY(product_code) REFERENCES Raw_Material(product_code) ON UPDATE CASCADE ON DELETE CASCADE,
        PRIMARY KEY (shade_number,product_code)
    );
""").sql_execute(mycursor)

mydb.commit()
# mycursor.execute(sql)

SELECT rm_stock.trans_id,rm_stock.customer_id,rm_stock.remark,has_rm.product_code,'-',has_rm.quantity
            FROM rm_stock
            JOIN has_rm ON
            rm_stock.trans_id = has_rm.trans_id
            JOIN raw_material ON
            has_rm.product_code = raw_material.product_code
            WHERE rm_stock.date = '{by_Today}';