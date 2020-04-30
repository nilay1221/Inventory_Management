import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass@123",
    database="PANKITPROCESS"
)
mycursor=mydb.cursor()
#mycursor.execute("show tables")
#mycursor.execute( "CREATE TABLE Raw_Material( Product_code VARCHAR(10) PRIMARY KEY NOT NULL, Product_name VARCHAR(200) NOT NULL,Price VARCHAR(30) NOT NULL)")
#mycursor.execute( "CREATE TABLE Raw_Material_Stock( TRANS_ID VARCHAR(10) PRIMARY KEY NOT NULL,Customer_ID VARCHAR(20) NOT NULL ,Stock_Date DATE ,Remark VARCHAR(250))")
#mycursor.execute( "CREATE TABLE Rm_material_stock(Type VARCHAR(50) NOT NULL, Quantity VARCHAR(20) NOT NULL, Trans_id VARCHAR(10) PRIMARY KEY NOT NULL,Product_code VARCHAR(10) NOT NULL ,FOREIGN KEY(Trans_id) REFERENCES Raw_Material_Stock(TRANS_ID),FOREIGN KEY(Product_code) REFERENCES Raw_Material(Product_code))")
#mycursor.execute("CREATE TABLE Shade_Number(ShadeNum VARCHAR(20) PRIMARY KEY NOT NULL, Percentage VARCHAR (10) not null)")
#mycursor.execute("DROP TABLE Shade_Number")
#mycursor.execute("CREATE TABLE Made_of_shade_num(Product_code VARCHAR(20) PRIMARY KEY NOT NULL, Percentage VARCHAR(10) NOT NULL)")
#mycursor.execute("ALTER TABLE Made_of_shade_num ADD FOREIGN KEY(Product_code) REFERENCES Raw_Material(Product_code)")
#mycursor.execute( "CREATE TABLE Admin(username VARCHAR(50) PRIMARY KEY NOT NULL,password VARCHAR (50) NOT NULL)")
#mycursor.execute( "CREATE TABLE Shade_Stock(Trans_id VARCHAR (10) primary key not null,stock_date DATE ,customer_id varchar(10) not null,remark varchar (250) , ShadeNum VARCHAR(20) NOT NULL)")
#mycursor.execute("ALTER TABLE Shade_Stock(FOREIGN KEY(ShadeNum varchar(20)) REFERENCES Shade_Number(ShadeNum varchar(20)))")
#mycursor.execute("CREATE TABLE Sales(Trans_id varchar(20) primary key not null, Customer_id varchar(20) not null, Sales_date DATE , Remark varchar(250) )")
#mycursor.execute("CREATE TABLE ShadeNum_Shadestock(Type varchar(50) not null, Quantity varchar(20) not null ,Trans_id varchar(10) primary key not null , Shade_Num varchar(20) not null ) ")
#mycursor.execute("ALTER TABLE ShadeNum_Shadestock add FOREIGN KEY(Shade_Num) REFERENCES Shade_Number(ShadeNum)")
#mycursor.execute("CREATE TABLE Rm_stock_Shade_stock(rm_trans_id varchar(20) not null,shade_trans_id varchar (20) not null,FOREIGN KEY(rm_trans_id) REFERENCES raw_material_stock(trans_id) on delete cascade on update cascade,FOREIGN KEY(shade_trans_id) REFERENCES shade_stock(trans_id) on delete cascade on update cascade)")
#mycursor.execute("CREATE table rm_closing_stock(Product_code varchar(20) primary key not null,closing_stock varchar(20) )")
#mycursor.execute("CREATE table shade_closing_stock(Product_code varchar(20) primary key not null,closing_stock varchar(20),shade_num varchar(20) not null)")
#mycursor.execute("CREATE TABLE admin_rm_material(username varchar(50) not null, Product_code varchar(20) not null, sales_trans_id varchar(20) not null, shade_num varchar(20) not null)")
mycursor.execute("alter table admin_rm_material add FOREIGN KEY(username) REFERENCES Admin(username),add FOREIGN KEY(Product_code) REFERENCES Raw_Material(Product_code),add FOREIGN KEY(sales_trans_id) REFERENCES Sales(Trans_id), add FOREIGN KEY(shade_num) REFERENCES Shade_Number(ShadeNum)")
#mycursor.execute("create table rm_material_sales_consist_of(Type varchar(50) not null, Quantity varchar(20) not null ,Trans_id varchar(10) primary key not null , Shade_Num varchar(20) not null,Product_code varchar(50) not null)")
#mycursor.execute("alter table rm_material_sales_consist_of ADD FOREIGN KEY(Product_code) REFERENCES Raw_Material(Product_code), ADD FOREIGN KEY(Trans_id) REFERENCES Sales(Trans_id),ADD FOREIGN KEY(shade_num) REFERENCES Shade_Number(ShadeNum)")
# for x in mycursor:
#     print(x)
#mycursor.execute("drop table rm_material_sales_consist_of")