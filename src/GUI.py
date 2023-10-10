from tkinter import *
from tkinter import filedialog
import excel_class as excel

root = Tk()
root.title("Data Entry Portal")
root.geometry("1920x1080")


def file_click():
    btnLoad.grid(row=0, column=0)
    btnSave.grid(row=1, column=0)


def search_click():
    placeholder.grid(row=0, column=0)


def reformat_click():
    btnView.grid(row=0, column=0)
    btnCreate.grid(row=1, column=0)


def load_click():
    root.filePath = filedialog.askopenfilename(initialdir="/Documents", title="Select an Excel File")
    root.wb = excel.Excel(root.filePath)

    for x in range(1, root.wb.columns+1):
        for y in range(1, root.wb.rows + 1):
            root.wb.sheet.cell(row=y, column=x)


# Create Frame for navbar
frameTop = LabelFrame(root, padx=870, pady=70, fg='#E4E6EB', bg='#3A3B3C')
frameBot = LabelFrame(root, padx=870, pady=70, fg='#E4E6EB', bg='#3A3B3C')

# Creates File and its buttons
btnFile = Button(root, text="File", padx=60, pady=10, fg='#E4E6EB', bg='#242526', command=file_click)
btnLoad = Button(frameTop, text="Load", padx=60, pady=20, fg='#E4E6EB', bg='#242526', command=load_click)
btnSave = Button(frameTop, text="Save", padx=60, pady=20, fg='#E4E6EB', bg='#242526')

# Creates Search and its entries
btnSearch = Button(root, text="Search", padx=60, pady=10, fg='#E4E6EB', bg='#242526', command=search_click)
placeholder = Entry(frameTop, width=50)

# Creates Reformat and its buttons
btnReformat = Button(root, text="Reformat", padx=60, pady=10, fg='#E4E6EB', bg='#242526', command=reformat_click)
btnView = Button(frameTop, text="Save", padx=60, pady=20, fg='#E4E6EB', bg='#242526')
btnCreate = Button(frameTop, text="Load", padx=60, pady=20, fg='#E4E6EB', bg='#242526')

# Puts everything onto the grid
btnFile.grid(row=0, column=0)
btnSearch.grid(row=0, column=1)
btnReformat.grid(row=0, column=2)
frameTop.grid(row=1, column=0, padx=10, pady=10, columnspan=4)
frameBot.grid(row=2, column=0, padx=10, pady=10, columnspan=4)

# Automatically starts program with File clicked
btnLoad.grid(row=0, column=0)
btnSave.grid(row=1, column=0)

file_click()
root.mainloop()
