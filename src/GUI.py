# GUI.py
# Meyerhoff Data Entry Portal
# Authored by Amar McLean
# https://ttkthemes.readthedocs.io/en/latest/themes.html#adapta
from tkinter import *
from tkinter import filedialog, ttk
from pandas import read_excel
from pandastable import Table

root = Tk()
root.title("Data Entry Portal")
root.state("zoomed")
root.colors = ["#000000", "#FFFFFF", "#fdb515"]
# root.colors = ["#F8F4E3", "#D4CDC3", "#D5D0CD", "#A2A392", "#9A998C"]
root.file_path = None
root.df = None
root.pt = None
checkboxes_view = []
checkboxes_split = []
searchbars = []
entries = []
root.pt1 = None
root.file_path2 = None
root.df2 = None
root.pt2 = None

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
root.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")


root.configure(bg=root.colors[1])


#################################################
#
# File tab and the load button and save button
#
#################################################
def file_click():
    if btn2.cget("state") == "disabled":
        btnLoad2.grid(row=0, column=2)
    btn1.grid(row=0, column=0)
    btn2.grid(row=1, column=0)
    btnLoad.grid(row=0, column=1)
    btnSave.grid(row=1, column=1)


def btn1_click():
    btn1.config(state="disabled")
    if btn2.cget("state") == "disabled":
        canvasBot1.pack_forget()
        canvasBot2.pack_forget()
        btnLoad2.grid_forget()
        btn2.config(state="normal")
    # Puts bot canvas onto grid
    canvasBot1.pack_propagate(False)
    canvasBot1.grid_propagate(False)
    canvasBot.pack_propagate(False)
    canvasBot.grid_propagate(False)
    canvasBot2.pack_propagate(False)
    canvasBot2.grid_propagate(False)
    canvasBot.pack(fill='both', side="bottom")


def btn2_click():
    btn2.config(state="disabled")
    if btn1.cget("state") == "disabled":
        canvasBot.pack_forget()
        btn1.config(state="normal")
    # Puts bot canvas onto grid
    canvasBot1.pack_propagate(False)
    canvasBot1.grid_propagate(False)
    canvasBot.pack_propagate(False)
    canvasBot.grid_propagate(False)
    canvasBot2.pack_propagate(False)
    canvasBot2.grid_propagate(False)
    canvasBot1.pack(fill='both', side="left")
    canvasBot2.pack(fill='both', side="right")
    btnLoad2.grid(row=0, column=2)


def load_click():
    root.file_path = filedialog.askopenfilename(initialdir="/Documents", title="Select an Excel File")

    if root.file_path:
        # Load the data from the Excel file
        root.df = read_excel(root.file_path)
        root.df.name = root.file_path.split('/')[-1].split('.')[0]

        # Create a PandasTable
        root.pt = Table(canvasBot, dataframe=root.df)
        root.pt.show()
        root.pt.redraw()

        root.pt1 = Table(canvasBot1, dataframe=root.df)
        root.pt1.show()
        root.pt1.redraw()

        checkbox_font = ("Helvetica", 20)
        btnEntry.config(state="normal")

        if checkboxes_view:
            checkboxes_view.clear()
        if checkboxes_split:
            checkboxes_split.clear()
        if searchbars:
            searchbars.clear()

        for i, col in enumerate(root.df.columns):
            var = IntVar(value=1)
            checkbox = Checkbutton(top_row_frame, bg=root.colors[2], text=col, variable=var, onvalue=1, offvalue=0,
                                   font=checkbox_font)
            box_list = [checkbox, var]
            checkboxes_view.append(box_list)
            checkbox.config(command=lambda index=i: checkbox_view_click(index))

        for col in root.df.columns:
            var = IntVar()
            checkbox = Checkbutton(top_row_frame, bg=root.colors[2], text=col, variable=var, onvalue=1, offvalue=0,
                                   font=checkbox_font)
            checkboxes_split.append([checkbox, var])


def load_click2():
    root.file_path2 = filedialog.askopenfilename(initialdir="/Documents", title="Select an Excel File")

    if root.file_path2:
        # Load the data from the Excel file
        root.df2 = read_excel(root.file_path2)
        root.df2.name = root.file_path2.split('/')[-1].split('.')[0]

        # Create a PandasTable
        root.pt2 = Table(canvasBot2, dataframe=root.df2)
        root.pt2.show()
        root.pt2.redraw()


def save_click():
    if root.df is not None:

        # Save the DataFrame to the same Excel file
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile=root.df.name)
        if file_path:
            root.df.to_excel(file_path, index=False)


#################################################
#
# Search click and it's checkboxes
#
#################################################
def search_click():
    searchLabel.grid(row=0, column=0, padx=5, pady=10)
    searchBox.grid(row=0, column=1, padx=5, pady=10)
    btnFind.grid(row=0, column=2, padx=10, pady=10)


def search_data():
    query = searchBox.get().lower()
    filtered_df = root.df[root.df.apply(lambda row: any(query in str(cell).lower() for cell in row), axis=1)]

    if btn1.cget("state") == "disabled":
        root.pt.model.df = filtered_df
        root.pt.redraw()

    else:
        root.pt1.model.df = filtered_df
        root.pt1.redraw()


#################################################
#
# Reformat and it's two buttons
#
#################################################
def reformat_click():
    btnView.grid(row=0, column=0)
    btnSplit.grid(row=1, column=0)

    top_row_frame.grid(row=0, column=1, padx=10, pady=10, columnspan=4, rowspan=2)


def view_click():
    btnView.config(state="disabled")
    btnCreate.grid_forget()
    for checkbox in checkboxes_split:
        checkbox[0].grid_forget()

    total_items = len(checkboxes_view)
    if total_items != 0:
        num_rows = (total_items + 3) // 4  # Round up to the nearest integer
        num_columns = (total_items + num_rows - 1) // num_rows
        for i, checkbox in enumerate(checkboxes_view):
            row = i // num_columns  # Calculate the row based on the index
            column = i % num_columns  # Calculate the column based on the index
            checkbox[0].grid(row=row, column=column)

    btnSplit.config(state="normal")


def checkbox_view_click(index):
    column_name = checkboxes_split[index][0]['text']

    # Get the value of the checkbox (1 for checked, 0 for unchecked)
    checkbox_value = checkboxes_split[index][1].get()
    print(column_name)

    if checkbox_value == 0:
        # Filter out the rows where the column value matches the checkbox name
        None

    root.pt.show()
    root.pt.redraw()


def split_click():
    btnSplit.config(state="disabled")
    btnCreate.grid(row=0, column=10, rowspan=2)
    for checkbox in checkboxes_view:
        checkbox[0].grid_forget()

    total_items = len(checkboxes_split)
    if total_items != 0:
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
            print("Column found")
            checked_columns.append(checkbox[0]['text'])

    if not checked_columns:
        # error_label.config(text="No columns selected.")
        print("No columns loaded or checked")
        return

    if root.df is not None:
        # Create a new DataFrame with only the selected columns
        new_df = root.df[checked_columns]

        # Save the new DataFrame to a new Excel file
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile=f"{root.df.name}_filtered")
        if file_path:
            new_df.to_excel(file_path, index=False)


#################################################
#
# Entry button and it's Add button
#
#################################################
def entry_click():
    entry_window = Toplevel(root)
    entry_window.title("Form Entry")
    entry_window.geometry("500x700")

    # Make Frame
    main_frame = Frame(entry_window)
    main_frame.pack(fill=BOTH, expand=1)

    # Make Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Make Scroll bar and put it in Frame
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Make Second Frame
    frame = Frame(my_canvas)

    my_canvas.create_window((0, 0), window=frame, anchor="nw")

    # Make add button
    btn_add = Button(frame, text="Add", padx=45, pady=5, bg=root.colors[1], command=lambda: add_click(entries))
    num_col = 0

    if entries:
        entries.clear()

    for col in root.df.columns:
        label = Label(frame, text=col, padx=10, pady=10)
        entry = Entry(frame, bg=root.colors[2])
        var = IntVar()
        checkbox = Checkbutton(frame, variable=var, onvalue=1, offvalue=0)

        label.grid(row=num_col, column=0)
        entry.grid(row=num_col, column=1)
        checkbox.grid(row=num_col, column=2)
        entries.append([entry, var, col])

        num_col += 1

    btn_add.grid(row=num_col, column=1)


def add_click(elements):
    # Find rows that match the selected search criteria
    selected_rows = root.df.copy()
    new = True

    for info in elements:
        searchbar, value, name = info

        # Only include the condition if the checkbox is checked
        if value.get() == 1:
            query = searchbar.get().lower()
            selected_rows = selected_rows[
                selected_rows.apply(lambda row: any(query in str(cell).lower() for cell in row), axis=1)]
            new = False

    # Iterate through the entries to update the selected row
    if not new:
        for info in elements:
            searchbar, value, name = info

            # Only update the column value if the checkbox is unchecked and a value is entered
            if value.get() == 0 and searchbar.get():
                # Update the original DataFrame with the modified values
                root.df.at[selected_rows.index[0], name] = searchbar.get()

    # Redraw the PandasTable with the updated DataFrame
    root.pt.show()
    root.pt.redraw()


# Create Top Notebook
nbTop = ttk.Notebook(root)
nbTop.pack_propagate(False)
nbTop.grid_propagate(False)

fFile = ttk.Frame(nbTop)
fSearch = ttk.Frame(nbTop)
fFormat = ttk.Frame(nbTop)
fEntry = ttk.Frame(nbTop)

nbTop.add(fFile, text='File')
nbTop.add(fSearch, text='Search')
nbTop.add(fFormat, text='Format')
nbTop.add(fEntry, text='Entry')

# Create Bottom Canvas
canvasBot = Canvas(root, width=1900, height=600, bg=root.colors[1])
canvasBot.pack_propagate(False)
canvasBot.grid_propagate(False)

canvasBot1 = Canvas(root, width=950, height=600, bg=root.colors[1])
canvasBot1.pack_propagate(False)
canvasBot1.grid_propagate(False)
canvasBot2 = Canvas(root, width=950, height=600, bg=root.colors[1])
canvasBot2.pack_propagate(False)
canvasBot2.grid_propagate(False)

# Create Entry Window

# Creates File and its buttons
btnLoad = Button(fFile, text="Load", width=20, height=11, bg=root.colors[1], command=load_click)
btnSave = Button(fFile, text="Save", width=20, height=11, bg=root.colors[1], command=save_click)
btnLoad2 = Button(fFile, text="Load", width=20, height=11, bg=root.colors[1], command=load_click2)
btn1 = Button(fFile, text="1", width=20, height=11, bg=root.colors[1], command=btn1_click)
btn2 = Button(fFile, text="2", width=20, height=11, bg=root.colors[1], command=btn2_click)

# Creates Search and its entries
searchLabel = Label(fSearch, text="Search:", padx=5, pady=10, bg=root.colors[1])
searchBox = Entry(fSearch, width=20, font=("Helvetica", 20), bg=root.colors[1])
btnFind = Button(fSearch, text="Search", padx=60, pady=10, bg=root.colors[1], command=search_data)


# Creates Reformat and its buttons
btnView = Button(fFormat, text="View", width=20, height=11, bg=root.colors[1], command=view_click)
btnSplit = Button(fFormat, text="Split", width=20, height=11, bg=root.colors[1], command=split_click)
btnCreate = Button(fFormat, text="Create", width=20, height=22, bg=root.colors[1], command=create_click)
top_row_frame = Frame(fFormat, bg=root.colors[2])

# Creates Entry Button
btnEntry = Button(fEntry, text="Entry", padx=60, pady=10, command=entry_click)
btnEntry.config(state="disabled")
btnEntry.pack()

# Puts top canvas onto grid
nbTop.pack(fill="x", side=TOP)

file_click()
btn1_click()
search_click()
reformat_click()
root.mainloop()
