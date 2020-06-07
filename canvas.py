from tkinter import *

root = Tk()
root.title('Canvas')
root.iconbitmap('favicon.ico')
root.geometry("400x400")

my_canvas = Canvas(root, width=300, height=200)
my_canvas.pack(pady=20)

# my_canvas.create_rectangle(x1, y1, x2, y2, fill="pink")
# Rectangle x1, y1 = Top Left
# Rectangle x2, y2 = Botton Right

my_canvas.create_rectangle(50, 150, 250, 50, fill="pink")

# Create Oval
# Oval x1, y1 = Top Left
# Oval x2, y2 = Botton Right
my_canvas.create_oval(50, 150, 250, 50, fill="cyan")

# create line
# my_canvas.create_line(x1, y1, x2, y2, fill="color")
my_canvas.create_line(0, 100, 300, 100, fill="red")
my_canvas.create_line(150, 0, 150, 200, fill="red")


root.mainloop()
