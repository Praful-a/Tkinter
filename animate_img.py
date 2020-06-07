from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Open External file.')
root.iconbitmap('favicon.ico')
root.geometry("600x600")

def change(e):
    img = Image.open('images/img_2.png')
    my_pic = ImageTk.PhotoImage(img)
    my_label.config(image=my_pic)
    my_label.image = my_pic

def change_back(e):
        img = Image.open('images/img_1.png')
        my_pic = ImageTk.PhotoImage(img)
        my_label.config(image=my_pic)
        my_label.image = my_pic

def do_something():
    label2 = Label(root, text="You clicked the button!")
    label2.pack()


image = Image.open('images/img_1.png')
img = ImageTk.PhotoImage(image)
my_label = Button(root, image=img, command=do_something)
my_label.pack(pady=20)



my_label.bind('<Enter>', change)
my_label.bind("<Leave>", change_back)


root.mainloop()
