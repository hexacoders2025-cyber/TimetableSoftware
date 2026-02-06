import sqlite3
import random
from tkinter import messagebox
from timetable_ui import show_timetable_table

def generate_timetable():
    conn = sqlite3.connect("timetable.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM instructor")
    instructors = cursor.fetchall()

    cursor.execute("SELECT name FROM course")
    courses = cursor.fetchall()

    if not instructors or not courses:
        messagebox.showerror("Error", "Add data first!")
        return

    timetable = []
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    periods = [1,2,3,4,5,6,7]

    for course in courses:
        entry = (
            random.choice(days),
            random.choice(periods),
            course[0],
            random.choice(instructors)[0]
        )
        timetable.append(entry)

    conn.close()
    show_timetable_table(timetable)
