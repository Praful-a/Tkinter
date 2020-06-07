from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Rounded Button")
root.iconbitmap('favicon.ico')
root.geometry("400x400")

def thing():
    my_label.config(text="You clicked the button...")

image = Image.open('round.jpg')
login_btn = ImageTk.PhotoImage(image)

img_label = Label(image=login_btn)
# img_label.pack(pady=20)

my_button = Button(root, image=login_btn, command=thing, borderwidth=0)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()
