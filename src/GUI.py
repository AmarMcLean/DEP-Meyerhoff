# GUI.py
from tkinter import *
from tkinter import filedialog
import pandas as pd
from pandastable import Table


root = Tk()
root.title("Data Entry Portal")
root.state("zoomed")
root.geometry("1920x1080")
root.colors = ["#F8F4E3", "#D4CDC3", "#D5D0CD", "#A2A392", "#9A998C"]
root.df = None
checkboxes_view = []
checkboxes_split = []
searchbars = []
root.file_path = None

root.configure(bg=root.colors[0])


#
#
#
#
# File tab and the load button and save button
def file_click():
    # Disable search features
    if btnSearch.cget("state") == "disabled":
        btnSearch.config(state="normal")
        top_row_frame_2.grid_forget()
    # Disable reformat features
    if btnReformat.cget("state") == "disabled":
        btnView.grid_forget()
        btnSplit.grid_forget()
        btnCreate.grid_forget()
        top_row_frame.grid_forget()
        btnReformat.config(state="normal")
    btnLoad.grid(row=0, column=0)
    btnSave.grid(row=1, column=0)
    btnFile.config(state="disabled")


def load_click():
    root.file_path = filedialog.askopenfilename(initialdir="/Documents", title="Select an Excel File")

    if root.file_path:
        # Load the data from the Excel file
        root.df = pd.read_excel(root.file_path)
        root.df.name = root.file_path.split('/')[-1].split('.')[0]

        # Create a PandasTable
        pt = Table(canvasBot, dataframe=root.df)
        pt.show()
        pt.redraw()

        checkbox_font = ("Helvetica", 20)

        for col in root.df.columns:
            var = IntVar()
            checkbox = Checkbutton(top_row_frame, bg=root.colors[2], text=col, variable=var, onvalue=1, offvalue=0, font=checkbox_font)
            checkboxes_view.append([checkbox, var])

        for col in root.df.columns:
            var = IntVar()
            checkbox = Checkbutton(top_row_frame, bg=root.colors[2], text=col, variable=var, onvalue=1, offvalue=0, font=checkbox_font)
            checkboxes_split.append([checkbox, var])

        for col in root.df.columns:
            searchbar = Entry(top_row_frame_2, bg=root.colors[2], font=checkbox_font)
            searchbar.insert(0, col)
            searchbars.append(searchbar)


def save_click():
    if root.df is not None:

        # Save the DataFrame to the same Excel file
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile=root.df.name)
        if file_path:
            root.df.to_excel(file_path, index=False)


#
#
#
#
# Search click and it's checkboxes
def search_click():
    # Disable file features
    if btnFile.cget("state") == "disabled":
        btnLoad.grid_forget()
        btnSave.grid_forget()
        btnFile.config(state="normal")
    # Disable reformat features
    if btnReformat.cget("state") == "disabled":
        btnView.grid_forget()
        btnSplit.grid_forget()
        btnCreate.grid_forget()
        top_row_frame.grid_forget()
        btnReformat.config(state="normal")
    btnSearch.config(state="disabled")

    top_row_frame_2.grid(row=0, column=0, padx=10, pady=10)

    total_items = len(searchbars)
    num_rows = (total_items + 3) // 4  # Round up to the nearest integer
    num_columns = (total_items + num_rows - 1) // num_rows
    for i, searchbar in enumerate(searchbars):
        row = i // num_columns  # Calculate the row based on the index
        column = i % num_columns  # Calculate the column based on the index
        searchbar.grid(row=row, column=column)


#
#
#
#
# Reformat and it's two buttons
def reformat_click():
    # Disable file features
    if btnFile.cget("state") == "disabled":
        btnLoad.grid_forget()
        btnSave.grid_forget()
        btnFile.config(state="normal")
    # Disable search features
    if btnSearch.cget("state") == "disabled":
        btnSearch.config(state="normal")
        top_row_frame_2.grid_forget()
    btnView.grid(row=0, column=0)
    btnSplit.grid(row=1, column=0)
    btnReformat.config(state="disabled")

    top_row_frame.grid(row=0, column=1, padx=10, pady=10, columnspan=4, rowspan=2)


def view_click():
    btnView.config(state="disabled")
    btnCreate.grid_forget()
    for checkbox in checkboxes_split:
        checkbox[0].grid_forget()

    total_items = len(checkboxes_view)
    num_rows = (total_items + 3) // 4  # Round up to the nearest integer
    num_columns = (total_items + num_rows - 1) // num_rows
    for i, checkbox in enumerate(checkboxes_view):
        row = i // num_columns  # Calculate the row based on the index
        column = i % num_columns  # Calculate the column based on the index
        checkbox[0].grid(row=row, column=column)

    btnSplit.config(state="normal")


def split_click():
    btnSplit.config(state="disabled")
    btnCreate.grid(row=0, column=10, rowspan=2)
    for checkbox in checkboxes_view:
        checkbox[0].grid_forget()

    total_items = len(checkboxes_split)
    num_rows = (total_items + 3) // 4  # Round up to the nearest integer
    num_columns = (total_items + num_rows - 1) // num_rows
    for i, checkbox in enumerate(checkboxes_split):
        row = i // num_columns  # Calculate the row based on the index
        column = i % num_columns  # Calculate the column based on the index
        checkbox[0].grid(row=row, column=column)

    btnView.config(state="normal")


def create_click():
    checked_columns = []
    for checkbox in checkboxes_split:
        if checkbox[1].get() == 1:  # Check if the checkbox is checked (value is 1)
            print("found")
            checked_columns.append(checkbox[0]['text'])

    if not checked_columns:
        # error_label.config(text="No columns selected.")
        print("error")
        return

    if root.df is not None:
        # Create a new DataFrame with only the selected columns
        new_df = root.df[checked_columns]

        # Save the new DataFrame to a new Excel file
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile=f"{root.df.name}_filtered")
        if file_path:
            new_df.to_excel(file_path, index=False)
            error_label.config(text="File created successfully.")
        else:
            error_label.config(text="File creation canceled.")
    else:
        error_label.config(text="No data loaded to create a file.")


# Create Canvas for navbar
canvasTop = Canvas(root, width=1900, height=350, bg=root.colors[1])
canvasTop.pack_propagate(False)
canvasTop.grid_propagate(False)

canvasBot = Canvas(root, width=1900, height=600, bg=root.colors[1])
canvasBot.pack_propagate(False)
canvasBot.grid_propagate(False)

# Creates File and its buttons
btnFile = Button(root, text="File", padx=60, pady=10, bg=root.colors[1], command=file_click)
btnLoad = Button(canvasTop, text="Load", width=20, height=11, bg=root.colors[2], command=load_click)
btnSave = Button(canvasTop, text="Save", width=20, height=11, bg=root.colors[2], command=save_click)
frameFile = LabelFrame(root, padx=800, pady=20, fg='#E4E6EB', bg=root.colors[2])

# Creates Search and its entries
btnSearch = Button(root, text="Search", padx=60, pady=10, bg=root.colors[1], command=search_click)
top_row_frame_2 = Frame(canvasTop, bg=root.colors[1])

# Creates Reformat and its buttons
btnReformat = Button(root, text="Reformat", padx=60, pady=10, bg=root.colors[1], command=reformat_click)
btnView = Button(canvasTop, text="View", width=20, height=11, bg=root.colors[2], command=view_click)
btnSplit = Button(canvasTop, text="Split", width=20, height=11, bg=root.colors[2], command=split_click)
btnCreate = Button(canvasTop, text="Create", width=20, height=22, bg=root.colors[2], command=create_click)
top_row_frame = Frame(canvasTop, bg=root.colors[1])

# Puts everything onto the grid
btnFile.grid(row=0, column=0)
btnSearch.grid(row=0, column=1)
btnReformat.grid(row=0, column=2)
canvasTop.grid(row=1, column=0, padx=10, pady=10, columnspan=4)

error_label = Label(canvasBot, text="", foreground="red")
error_label.grid(row=1, column=0)
canvasBot.grid(row=2, column=0, padx=10, pady=10, columnspan=4)

file_click()
root.mainloop()
