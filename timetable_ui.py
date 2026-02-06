from tkinter import *
from tkinter import ttk

def show_timetable_table(data):
    win = Toplevel()
    win.title("Generated Timetable")
    win.geometry("600x400")

    columns = ("Day", "Period", "Course", "Instructor")
    tree = ttk.Treeview(win, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    for row in data:
        tree.insert("", END, values=row)

    tree.pack(expand=True, fill="both")
