from tkinter import *

def open_main_window():

    root = Toplevel()
    root.title("Timetable Scheduling Software")
    root.state("zoomed")
    root.configure(bg="#f8eff0")

    # Center frame
    center = Frame(root, bg="#ffb6c1")
    center.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Heading
    Label(
        center,
        text="Timetable Scheduling Software",
        font=("Arial", 34, "bold"),
        bg="#ffb6c1"
    ).pack(pady=35)

    # Admin buttons
    Button(
        center,
        text="Manage Instructors",
        font=("Arial", 18, "bold"),
        width=28,
        height=2
    ).pack(pady=15)

    Button(
        center,
        text="Manage Rooms",
        font=("Arial", 18, "bold"),
        width=28,
        height=2
    ).pack(pady=15)

    Button(
        center,
        text="Manage Courses",
        font=("Arial", 18, "bold"),
        width=28,
        height=2
    ).pack(pady=15)

   

    # Logout button
    Button(
        center,
        text="Logout",
        command=root.destroy,
        font=("Arial", 16, "bold"),
        bg="red",
        fg="white",
        width=16
    ).pack(pady=35)