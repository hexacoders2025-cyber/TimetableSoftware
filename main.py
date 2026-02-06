from tkinter import *
from PIL import Image, ImageTk
from instructor_ui import open_instructor_window
from scheduler import generate_timetable
from room_ui import open_room_window
from course_ui import open_course_window


# ===== MAIN WINDOW =====
root = Tk()
root.title("AI Timetable Generator")
root.state("zoomed")  # Fullscreen

# ===== GET SCREEN SIZE =====
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# ===== BACKGROUND IMAGE =====
bg_img = Image.open("background.jpg")
bg_img = bg_img.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg_photo)
bg_label.image = bg_photo
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ===== LOGO (TOP RIGHT) =====
logo_img = Image.open("bg.png")
logo_img = logo_img.resize((150, 150))
logo_photo = ImageTk.PhotoImage(logo_img)

logo_label = Label(root, image=logo_photo, bd=0)
logo_label.place(relx=1.0, y=10, anchor="ne")

# ===== LIGHT PINK CENTER FRAME =====
box_color = "#FFC0CB"  # light pink

center_frame = Frame(root, bg=box_color)
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# ===== TITLE =====
Label(center_frame, text="Timetable Scheduling Software",
      font=("Arial", 26, "bold"),
      bg=box_color, fg="black").pack(pady=20)

# ===== BUTTONS =====
Button(center_frame, text="Manage Instructors",
       command=open_instructor_window,
       width=25, height=2,
       font=("Arial", 12),
       bg="#ff9eb5").pack(pady=10)

Button(center_frame, text="Generate Timetable",
       command=generate_timetable,
       width=25, height=2,
       font=("Arial", 12),
       bg="#ff6f91", fg="white").pack(pady=10)

Button(center_frame, text="Manage Rooms",
       command=open_room_window,
       width=25, height=2).pack(pady=10)

Button(center_frame, text="Manage Courses",
       command=open_course_window,
       width=25, height=2).pack(pady=10)


root.mainloop()
