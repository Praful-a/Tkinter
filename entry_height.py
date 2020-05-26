from tkinter import *

root = Tk()
root.title("Lear To Code!")
root.iconbitmap('favicon.ico')
root.geometry("400x400")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, END)
    myLabel.pack(pady=10)


e = Entry(root, width=50, font=('Helvetica', 18))
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack(pady=10)

root.mainloop()
