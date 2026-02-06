from tkinter import *
import sqlite3

def open_room_window():
    win = Toplevel()
    win.title("Rooms Management")
    win.geometry("400x300")

    # ===== CENTER THE WINDOW =====
    win.update_idletasks()
    width = 400
    height = 300
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

    # ===== MAIN FRAME =====
    frame = Frame(win)
    frame.pack(expand=True)

    # ===== TITLE =====
    Label(frame, text="Add Room",
          font=("Arial", 16, "bold")).pack(pady=10)

    # ===== ROOM NUMBER =====
    Label(frame, text="Room Number",
          font=("Arial", 12, "bold")).pack()
    num_entry = Entry(frame, font=("Arial", 12))
    num_entry.pack(pady=5)

    # ===== CAPACITY =====
    Label(frame, text="Capacity",
          font=("Arial", 12, "bold")).pack()
    cap_entry = Entry(frame, font=("Arial", 12))
    cap_entry.pack(pady=5)

    # ===== SAVE FUNCTION =====
    def save():
        conn = sqlite3.connect("timetable.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO room(number,capacity) VALUES(?,?)",
                       (num_entry.get(), cap_entry.get()))
        conn.commit()
        conn.close()
        num_entry.delete(0, END)
        cap_entry.delete(0, END)

    Button(frame, text="Save Room",
           font=("Arial", 12, "bold"),
           bg="#ff69b4", fg="white",
           width=15).pack(pady=15)
