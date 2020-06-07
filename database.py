from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Learn To Code')
root.iconbitmap('favicon.ico')
root.geometry("400x400")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")


# Commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
