from tkinter import *
import sqlite3

def open_course_window():
    win = Toplevel()
    win.title("Courses Management")
    win.geometry("400x350")

    # ===== CENTER WINDOW =====
    win.update_idletasks()
    width = 400
    height = 350
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

    # ===== MAIN FRAME =====
    frame = Frame(win)
    frame.pack(expand=True)

    # ===== TITLE =====
    Label(frame, text="Add Course",
          font=("Arial", 16, "bold")).pack(pady=10)

    # ===== COURSE NAME =====
    Label(frame, text="Course Name",
          font=("Arial", 12, "bold")).pack()
    name_entry = Entry(frame, font=("Arial", 12))
    name_entry.pack(pady=5)

    # ===== MAX STUDENTS =====
    Label(frame, text="Max Students",
          font=("Arial", 12, "bold")).pack()
    max_entry = Entry(frame, font=("Arial", 12))
    max_entry.pack(pady=5)

    # ===== LAB FIELD =====
    Label(frame, text="Is Lab? (1 = Yes, 0 = No)",
          font=("Arial", 12, "bold")).pack()
    lab_entry = Entry(frame, font=("Arial", 12))
    lab_entry.pack(pady=5)

    # ===== SAVE FUNCTION =====
    def save():
        conn = sqlite3.connect("timetable.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO course(name,max_students,is_lab) VALUES(?,?,?)",
            (name_entry.get(), max_entry.get(), lab_entry.get())
        )
        conn.commit()
        conn.close()

        name_entry.delete(0, END)
        max_entry.delete(0, END)
        lab_entry.delete(0, END)

    # ===== SAVE BUTTON =====
    Button(frame, text="Save Course",
           font=("Arial", 12, "bold"),
           bg="#ff69b4", fg="white",
           width=15, command=save).pack(pady=15)
