import tkinter as tk
from tkinter import ttk
import pandas as pd
from pandastable import Table


def display_excel_file():
    file_path = file_entry.get()
    try:
        df = pd.read_excel(file_path)
        display_table(df)
    except Exception as e:
        error_label.config(text=f"Error: {str(e)}")


def display_table(dataframe):
    if hasattr(root, 'table_frame'):
        root.table_frame.destroy()

    root.table_frame = ttk.Frame(root)
    root.table_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    table = Table(root.table_frame, dataframe=dataframe, showtoolbar=True, showstatusbar=True)
    table.show()


root = tk.Tk()
root.title("Excel Viewer")

file_label = ttk.Label(root, text="Enter Excel File Path:")
file_label.pack(pady=10)
file_entry = ttk.Entry(root)
file_entry.pack(pady=10)

display_button = ttk.Button(root, text="Display Excel File", command=display_excel_file)
display_button.pack(pady=10)

error_label = ttk.Label(root, text="", foreground="red")
error_label.pack()

root.mainloop()