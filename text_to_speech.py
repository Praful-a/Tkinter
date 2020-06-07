from tkinter import *
import pyttsx3

root = Tk()
root.title('Text To Speech')
root.iconbitmap('favicon.ico')
root.geometry("600x600")

# Learn more about pyttsx3 - https://pyttsx3.readthedocs.io/en/latest/

def talk():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0, 'end')

my_entry = Entry(root, font=("Helvetica", 28))
my_entry.pack(pady=20)

my_button = Button(root, text="Speak", command=talk)
my_button.pack(pady=20)

root.mainloop()
