from tkinter import *
from PIL import ImageTk, Image
import pymysql

root = Tk()
root.title('Learn To Code!')
root.iconbitmap('favicon.ico')
root.geometry("400x400")

mydb = pymysql.connect('localhost', 'root', '')

print(mydb)

root.mainloop()
