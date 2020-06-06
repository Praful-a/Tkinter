from tkinter import *

root = Tk()
root.title('Learn To Code')
root.iconbitmap('favicon.ico')
root.geometry("400x400")

def something():
    my_label.config(text="This is new text!!", font=("Helvetica", 12))
    root.config(bg="blue")
    my_button.config(text="You've been configged!", state=DISABLED, pady=30)

global my_label
my_label = Label(root, text="This is my text", font=("Helvetica", 18))
my_label.pack(pady=10)

global my_button
my_button = Button(root, text="Click Me", command=something)
my_button.pack(pady=10)

root.mainloop()
