from tkinter import *

root = Tk()
root.title("Learn To Code")
root.iconbitmap('favicon.ico')
root.geometry("400x400")


def clicker(event):
    # myLabel = Label(root, text="You Clicked a button" + str(event.x) + " " + str(event.y))
    myLabel = Label(root, text="You Clicked a button" + event.char)
    myLabel.pack()


myButton = Button(root, text="Click Me")
# myButton.bind("<Button-3>", clicker)
# myButton.bind("<Leave>", clicker)
# myButton.bind("<FocusIn>", clicker)
myButton.bind("<Key>", clicker)
myButton.pack(pady=20)

root.mainloop()
