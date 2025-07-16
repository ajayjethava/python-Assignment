import pymysql


mydb = pymysql.connect(
    host="localhost",
    user = "root",
    password = ""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS hotel_management")

mycursor.execute("USE hotel_management")


mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),address VARCHAR(255),phone VARCHAR(15),checkin_date DATE,checkout_date DATE,balance DECIMAL(10,2))")

mydb.commit()