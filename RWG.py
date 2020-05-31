from tkinter import *
from random import randint

root = Tk()
root.title("Learn To Code!")
root.iconbitmap('favicon.ico')
root.geometry("400x400")


def pick():
    # 20 entries
    entries = ['Sanbid Roy Chowdhury', 'The refuge Malik', 'Google India', 'The Rock', 'Praful Dubey', 'Akash Yadav', 'Shivam',
               'Kaushal', 'Ashok', 'Amit', 'Govind', 'Vipul', 'Rishabh', 'krishna', 'Ashwani', 'John', 'Mily', 'Vin', 'Keanau', 'Iron Man']

    # convert to a set
    entries_set = set(entries)
    # convert back to list
    unique_entries = list(entries_set)

    # create our list size variable
    our_number = len(unique_entries) - 1

    # Create a random number between 0 and 20
    rando = randint(0, our_number)

    winnerLabel = Label(root, text=unique_entries[rando], font=("Helvetica", 24))
    winnerLabel.pack(pady=50)


topLabel = Label(root, text="Win-O-Rama!", font=("Helvetica", 24))
topLabel.pack(pady=20)

winButton = Button(root, text="PICK OUR WINNER!!", font=("helvetica", 24), command=pick)
winButton.pack(pady=20)

root.mainloop()
