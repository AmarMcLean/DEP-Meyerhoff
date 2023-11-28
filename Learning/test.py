from tkinter import *
from tkinter import ttk
root = Tk()


style = ttk.Style()
style.configure("TEntry", padding=10, relief="flat", foreground="black", background="lightgray")

entry = ttk.Entry(root, style="TEntry")
entry.pack()


mainloop()