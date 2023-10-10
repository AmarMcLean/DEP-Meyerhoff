from tkinter import *
import sqlite3


root = Tk()
root.title("Database Thing")
root.geometry("400x400")

# Create or connect to a database
conn = sqlite3.connect('./data/cells.db')

# Create cursor
c = conn.cursor()

# Create table

c.execute("""CREATE TABLE addresses (
first_name text,
last_name text,
address text,
city text,
state text,
zipcode integer
)""")