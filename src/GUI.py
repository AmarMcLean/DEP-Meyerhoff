# GUY.py
from tkinter import *
from tkinter import filedialog
import excel_class as excel

root = Tk()
root.title("Data Entry Portal")
root.state("zoomed")
root.geometry("1920x1080")
root.colors = ["#F8F4E3", "#D4CDC3", "#D5D0CD", "#A2A392", "#9A998C"]

root.configure(bg=root.colors[0])


def file_click():
    # Disable search features
    if btnSearch.cget("state") == "disabled":
        placeholder.grid_forget()
        btnSearch.config(state="normal")
    # Disable reformat features
    if btnReformat.cget("state") == "disabled":
        btnView.grid_forget()
        btnCreate.grid_forget()
        btnReformat.config(state="normal")
    btnLoad.grid(row=0, column=0)
    btnSave.grid(row=1, column=0)
    btnFile.config(state="disabled")


def search_click():
    # Disable file features
    if btnFile.cget("state") == "disabled":
        btnLoad.grid_forget()
        btnSave.grid_forget()
        btnFile.config(state="normal")
    # Disable reformat features
    if btnReformat.cget("state") == "disabled":
        btnView.grid_forget()
        btnCreate.grid_forget()
        btnReformat.config(state="normal")
    placeholder.grid(row=0, column=0)
    btnSearch.config(state="disabled")


def reformat_click():
    # Disable file features
    if btnFile.cget("state") == "disabled":
        btnLoad.grid_forget()
        btnSave.grid_forget()
        btnFile.config(state="normal")
    # Disable search features
    if btnSearch.cget("state") == "disabled":
        placeholder.grid_forget()
        btnSearch.config(state="normal")
    btnView.grid(row=0, column=0)
    btnCreate.grid(row=1, column=0)
    btnReformat.config(state="disabled")


def load_click():
    root.filePath = filedialog.askopenfilename(initialdir="/Documents", title="Select an Excel File")
    root.wb = excel.Excel(root.filePath)
    for y in range(0, root.wb.columns):
        loaded_cells.append([])
        for x in range(0, root.wb.rows):
            # print(root.wb.sheet.cell(row=y + 1, column=x + 1).value)
            loaded_cells[y].append(Entry(frame, width=50))
            loaded_cells[y][x].grid(row=y, column=x, padx=10, pady=5)
            if root.wb.sheet.cell(row=y + 1, column=x + 1).value != None:
                loaded_cells[y][x].insert(0, root.wb.sheet.cell(row=y+1, column=x+1).value)

        frame.update_idletasks()
        canvasBot.config(scrollregion=canvasBot.bbox("all"))
        # Bind mouse scroll events to the canvas for vertical scrolling
        canvasBot.bind_all("<MouseWheel>", lambda event: canvasBot.yview_scroll(-1 * (event.delta), "units"))


loaded_cells = []

# Create Canvas for navbar
canvasTop = Canvas(root, width=1900, height=350, bg=root.colors[1])
canvasTop.pack_propagate(False)
canvasTop.grid_propagate(False)

canvasBot = Canvas(root, width=1900, height=600, bg=root.colors[1])
x_scrollbar = Scrollbar(canvasBot, orient="horizontal")
y_scrollbar = Scrollbar(canvasBot, orient="vertical")
frame = Frame(canvasBot, width=1887, height=587)

canvasBot.config(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
canvasBot.pack_propagate(False)
canvasBot.grid_propagate(False)
frame.pack_propagate(False)
frame.grid_propagate(False)

# Creates File and its buttons
btnFile = Button(root, text="File", padx=60, pady=10, bg=root.colors[1], command=file_click)
btnLoad = Button(canvasTop, text="Load", width=20, height=11, bg=root.colors[2], command=load_click)
btnSave = Button(canvasTop, text="Save", width=20, height=11, bg=root.colors[2])
frameFile = LabelFrame(root, padx=800, pady=20, fg='#E4E6EB', bg=root.colors[2])

# Creates Search and its entries
btnSearch = Button(root, text="Search", padx=60, pady=10, bg=root.colors[1], command=search_click)
placeholder = Entry(canvasTop, width=50)

# Creates Reformat and its buttons
btnReformat = Button(root, text="Reformat", padx=60, pady=10, bg=root.colors[1], command=reformat_click)
btnView = Button(canvasTop, text="View", width=20, height=11, bg=root.colors[2])
btnCreate = Button(canvasTop, text="Create", width=20, height=11, bg=root.colors[2])

# Puts everything onto the grid
btnFile.grid(row=0, column=0)
btnSearch.grid(row=0, column=1)
btnReformat.grid(row=0, column=2)
canvasTop.grid(row=1, column=0, padx=10, pady=10, columnspan=4)
canvasBot.grid(row=2, column=0, padx=10, pady=10, columnspan=4)
x_scrollbar.pack(side="bottom", fill="x")
y_scrollbar.pack(side="right", fill="y")

# For Scrollbar and Canvas Frame
x_scrollbar.config(command=canvasBot.xview)
y_scrollbar.config(command=canvasBot.yview)
canvasBot.create_window((0, 0), window=frame, anchor="nw")

file_click()
root.mainloop()
