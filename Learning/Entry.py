from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")


def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()

root.mainloop()
