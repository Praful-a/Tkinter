from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Resizes Images')
root.iconbitmap('favicon.ico')
root.geometry("600x500")

# Open Image
image = Image.open('images/img_1.png')

# Resize Image
resized = image.resize((250, 188), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)

# Label to show image.
my_label = Label(root, image=new_pic)
my_label.pack(pady=20)

root.mainloop()
