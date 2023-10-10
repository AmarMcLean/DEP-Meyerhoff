from tkinter import *
from tkinter import messagebox

root = Tk()


def popup():
    messagebox.showinfo("This is my popop", "Hello world!")


Button(root, text="Popup", command=popup).pack()


mainloop()
