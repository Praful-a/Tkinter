from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Learn To Code")
root.iconbitmap('favicon.ico')
root.geometry("400x400")


def selected(event):
    myLabel = Label(root, text=clicked.get()).pack()


def comboclick(event):
    message = "Hey It's " + myCombo.get()
    myLabel = Label(root, text=message).pack()


options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()

# myButton = Button(root, text="select from list", command=selected)
# myButton.pack()

root.mainloop()
