import tkinter as tk

def on_configure(event):
    # Update the scroll region to encompass the interior of the frame
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Scrollable Frame")

# Create a canvas to act as the scrolling frame
canvas = tk.Canvas(root)
canvas.grid(row=0, column=0, sticky="nsew")

# Create a frame inside the canvas to contain the entry widgets
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Create horizontal scrollbar
x_scrollbar = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
x_scrollbar.grid(row=1, column=0, sticky="ew")

# Create vertical scrollbar
y_scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
y_scrollbar.grid(row=0, column=1, sticky="ns")

# Bind the canvas to the scrollbars
canvas.config(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)

# Add entry widgets to the frame in a grid
for i in range(20):  # You can adjust this number based on your needs
    entry = tk.Entry(frame)
    entry.grid(row=i, column=0)

# Update the canvas scroll region when the frame size changes
frame.update_idletasks()
canvas.bind("<Configure>", on_configure)

# Make the grid rows and columns expand when the window is resized
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()