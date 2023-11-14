import tkinter as tk
from pandastable import Table, TableModel


class MyTableApp:
    def __init__(self, root, data):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack(fill='both', expand=True)
        self.table = Table(self.frame, dataframe=data,
                           showtoolbar=True, showstatusbar=True)
        self.table.show()
        self.add_tooltips()

    def add_tooltips(self):
        for col_idx, col_name in enumerate(self.table.model.df.columns):
            header = self.table.header[column = col_idx, row = 0]
            tooltip_text = "Description for {}".format(col_name)  # Add your descriptions here
            self.create_tooltip(header, tooltip_text)

    def create_tooltip(self, widget, text):
        tooltip = tk.Toplevel(self.root)
        tooltip.wm_overrideredirect(True)
        tooltip.wm_geometry(f"+{self.root.winfo_pointerx()}+{self.root.winfo_pointery() + 20}")

        label = tk.Label(tooltip, text=text, justify='left', background='#ffffe0', relief='solid', borderwidth=1)
        label.pack(ipadx=1)

        def leave(event):
            tooltip.destroy()

        widget.bind("<Enter>", lambda event: tooltip.lift())
        widget.bind("<Leave>", lambda event: leave(event))
        widget.bind("<Motion>", lambda event: tooltip.wm_geometry(f"+{event.x_root}+{event.y_root + 20}"))


if __name__ == "__main__":
    data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']}
    root = tk.Tk()
    app = MyTableApp(root, data)
    root.mainloop()