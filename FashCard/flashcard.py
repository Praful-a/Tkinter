from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title("Learn To Code!")
root.iconbitmap(r'C:\Users\Praful\Desktop\Tkinter\Tkinter\favicon.ico')
root.geometry("500x500")

# Create State FlashCard Function


def states():
    # hide previous frames
    hide_all_frames()
    state_frame.pack(fill="both", expand=1)
    # my_label = Label(state_frame, text="Something").pack()

    # Create a list of state names
    our_states = ['brazil', 'colombia', 'indonesia', 'philippines',
                  'romania', 'saudi', 'taiwan', 'thailand', 'united-arab', 'vietnam']

    # Generate a random number
    rando = randint(0, len(our_states)-1)
    state = 'Images/' + our_states[rando] + ".jpg"

    # Create our state Images
    global state_img
    state_img = ImageTk.PhotoImage(Image.open(state))
    show_state = Label(state_frame, image=state_img)
    show_state.pack(pady=15)

    # Create Button To Randomize State Images
    rando_button = Button(state_frame, text="Next State", command=states)
    rando_button.pack(pady=10)

# Create State Capital FlashCard Function


def state_capitals():
    # hide previous frames
    hide_all_frames()
    state_capitals_frame.pack(fill="both", expand=1)
    my_label = Label(state_capitals_frame, text="Capitals").pack()

# Hide all previous Frames


def hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()

    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()


# create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Geography menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geograph", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="State capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

# Create our Frames
state_frame = Frame(root, width=500, height=500)
state_capitals_frame = Frame(root, width=500, height=500)

root.mainloop()
