from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('Open External file.')
root.iconbitmap('favicon.ico')
root.geometry("600x400")

def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    # Open the Program
    os.system('"%s"' % my_program)


def open_notepad():
    os.system('c:/Windows/system32/notepad.exe')

my_button = Button(root, text="Open Program", command=open_program)
my_button.pack(pady=20)

my_button2 = Button(root, text="Open Notepad", command=open_notepad)
my_button2.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
