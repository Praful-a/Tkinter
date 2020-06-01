from tkinter import *

root = Tk()
root.title("Lear To Code!")
root.iconbitmap('favicon.ico')
root.geometry("400x400")

myLabel = Label(root)

# def myDelete():
#
#     # myLabel.destroy()
#     myLabel.grid_forget()
#     myButton['state'] = NORMAL
#     print(myButton.winfo_exists())


def myClick():
    global myLabel
    myLabel.destroy()
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.grid(row=3, column=0, pady=10)
    # myButton['state'] = DISABLED


e = Entry(root, width=17, font=('Helvetica', 30))
e.grid(row=0, column=0, padx=10, pady=10)

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.grid(row=1, column=0, pady=10)

# DeleteButton = Button(root, text="Delete Text")
# DeleteButton.grid(row=2, column=0, pady=10)

root.mainloop()
