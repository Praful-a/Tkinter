from tkinter import *
from tkcalendar import *

root = Tk()
root.title('Calendar')
root.iconbitmap('favicon.ico')
root.geometry("600x400")

cal = Calendar(root, selectmode="day", year=2020, month=5, day=22)
cal.pack(pady=20, fill="both", expand=True)


def grab_date():
    my_label.config(text="Today's Date Is " + cal.get_date())

my_button = Button(root, text="Get Date", command=grab_date)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
