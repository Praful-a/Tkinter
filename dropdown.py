from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('favicon.ico')
root.geometry("400x400")


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = [
    "Monday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
