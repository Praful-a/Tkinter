from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Move images')
root.iconbitmap('favicon.ico')
root.geometry("800x600")

w = 600
h = 400
x = w//2
y = h//2

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

# Add Image To Canvas
image = Image.open('cur.png')
new_image = image.resize((30, 70))
img = ImageTk.PhotoImage(new_image)

def move(e):
    # e.x
    # e.y
    global new_image, image, img
    image = Image.open('cur.png')
    new_image = image.resize((30, 70))
    img = ImageTk.PhotoImage(new_image)
    my_image = my_canvas.create_image(e.x, e.y, anchor=NW, image=img)
    my_label.config(text="Coordinates: x: " + str(e.x) + " y: " + str(e.y))

my_label = Label(root, text="")
my_label.pack(pady=20)

# moving mouse by holding left button
# my_canvas.bind('<B1-Motion>', move)
my_canvas.bind('<Motion>', move)


root.mainloop()
