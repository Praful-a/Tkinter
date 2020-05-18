from tkinter import *

root = Tk()

root.title('Learn To Code With Praful')
root.iconbitmap('favicon.ico')

# r = IntVar()
# r.set('2')
pizza = StringVar()
pizza.set("Papperconi")

Modes = [
    ("Papperconi", "Papperconi"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

for text, mode in Modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()


myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
