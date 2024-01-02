import tkinter as tk
from pandastable import Table, TableModel
import pandas as pd

class PandasTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PandasTable with Search")

        # Create a sample DataFrame
        data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Age': [25, 30, 35, 40, 22],
            'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Seattle']
        }
        self.df = pd.DataFrame(data)

        # Create a TableModel
        self.table_model = TableModel(dataframe=self.df)

        # Create a frame to hold the Table widget
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        # Create the pandastable widget inside the frame
        self.table = Table(self.frame, model=self.table_model)
        self.table.show()

        # Create a search entry and button
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=1, column=0, padx=10, pady=10)

        self.search_button = tk.Button(self.root, text="Search", command=self.search_data)
        self.search_button.grid(row=1, column=1, padx=10, pady=10)

    def search_data(self):
        # Get the search query from the entry widget
        query = self.search_entry.get().lower()

        # Filter the DataFrame based on the search query
        filtered_df = self.df[self.df.apply(lambda row: any(query in str(cell).lower() for cell in row), axis=1)]

        # Update the pandastable widget with the filtered data
        self.table.model.df = filtered_df
        self.table.redraw()

if __name__ == "__main__":
    root = tk.Tk()
    app = PandasTableApp(root)
    root.mainloop()