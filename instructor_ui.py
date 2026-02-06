from tkinter import *
import sqlite3

def open_instructor_window():
    win = Toplevel()
    win.title("Instructors")

    Label(win, text="Instructor Name").pack()
    name_entry = Entry(win)
    name_entry.pack()

    def save():
        conn = sqlite3.connect("timetable.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO instructor(name) VALUES(?)", (name_entry.get(),))
        conn.commit()
        conn.close()
        name_entry.delete(0, END)

    Button(win, text="Save", command=save).pack()
