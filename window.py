from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('favicon.ico')


def open():
    global my_img
    top = Toplevel()
    top.title('My second window')
    top.iconbitmap('favicon.ico')
    # lbl = Label(top, text="Hello World").pack()
    my_img = ImageTk.PhotoImage(Image.open(r'E:\python_tkinter\Tkinter\images\img_1.png'))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()


mainloop()
