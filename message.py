from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn To Code')
root.iconbitmap('favicon.ico')

# showinfo, showwaning, showerror, askquestion, askokcancel, askyesno


def popup():
    response = messagebox.askyesno("This is my Popup!", 'Hello World!')
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You Clicked      yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()


Button(root, text="Popup", command=popup).pack()

root.mainloop()
