from tkinter import *
from PIL import ImageTk, Image
import pymysql

root = Tk()
root.title('Learn To Code!')
root.iconbitmap('favicon.ico')
root.geometry("400x400")

mydb = pymysql.connect('localhost', 'root', '', 'codemy')

# Check to see if connector to MySQL was created
# print(mydb)

# Create a cursor and Initialize it
my_cursor = mydb.cursor()

# Create database
# my_cursor.execute("CREATE DATABASE codemy")

# Test to see if database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# Create a table
# my_cursor.execute("CREATE TABLE customers(first_name VARCHAR(255), last_name VARCHAR(255), zipcode INT(10), price_paid DECIMAL(10, 2), user_id INT AUTO_INCREMENT PRIMARY KEY)")

# Show TABle
my_cursor.execute("SELECT * FROM customers")
print(my_cursor.description)

root.mainloop()
