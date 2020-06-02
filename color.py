from tkinter import colorchooser
from tkinter import *

root = Tk()
root.title("Learn To Code!")
root.geometry("400x400")
root.iconbitmap("favicon.ico")


def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label2 = Label(root, text="You Picked a color!",
                      font=("Helvetica", 32), bg=my_color).pack()


my_Button = Button(root, text="Pick A Color", command=color).pack()

root.mainloop()
