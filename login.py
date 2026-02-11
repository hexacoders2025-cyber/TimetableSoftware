from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from homepp import open_home_window

# ================= ROOT WINDOW =================
root = Tk()
root.title("AI Timetable Generator - Login")
root.state("zoomed")
root.configure(bg="#c9dcf4")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

# ================= BACKGROUND =================
canvas = Canvas(root, bg="#c9dcf4", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ================= LEFT SIDE (LOGO + COLLEGE NAME) =================
left_frame = Frame(root, bg="#c9dcf4")
left_frame.place(x=120, y=screen_h // 2 - 180)

# ---- Logo ----
try:
    img = Image.open("bg.png")
    img = img.resize((140, 140))
    logo = ImageTk.PhotoImage(img)
    Label(left_frame, image=logo, bg="#c9dcf4").pack(pady=(0, 20))
except:
    pass

# ---- College Name ----
Label(
    left_frame,
    text="Sinhgad Academy of Engineering,\nKondhwa – Pune",
    font=("Segoe UI", 24, "bold"),
    bg="#c9dcf4",
    fg="#0f172a",
    justify="center"
).pack()

# ================= ADMIN LOGIN CARD =================
card_width = 450
card_height = 480

x = screen_w // 2 + 150
y = screen_h // 2 - card_height // 2

# Shadow
canvas.create_rectangle(
    x + 8, y + 8,
    x + card_width + 8, y + card_height + 8,
    fill="#97b7dd",
    outline="",
    stipple="gray25"
)

# Card
canvas.create_rectangle(
    x, y,
    x + card_width, y + card_height,
    fill="#87acd1",
    outline="#e5e7eb"
)

# ================= LOGIN FRAME =================
center = Frame(root, bg="#f8fafc")
center.place(x=x, y=y, width=card_width, height=card_height)

# ================= TITLE =================
Label(
    center,
    text="Admin Login",
    font=("Segoe UI", 22, "bold"),
    bg="#f8fafc",
    fg="#0f172a"
).pack(pady=(30, 10))

Label(
    center,
    text="AI Timetable Generator",
    font=("Segoe UI", 10),
    bg="#f8fafc",
    fg="#64748b"
).pack(pady=(0, 25))

# ================= VARIABLES =================
selected_dept = StringVar(value="Select Department")

# ================= DEPARTMENT =================
Label(
    center,
    text="Department",
    font=("Segoe UI", 11, "bold"),
    bg="#f8fafc",
    fg="#334155"
).pack(anchor="w", padx=45)

dept_frame = Frame(center, bg="#e2e8f0")
dept_frame.pack(fill="x", padx=45, pady=(5, 15), ipady=6)

dept_btn = Menubutton(
    dept_frame,
    textvariable=selected_dept,
    font=("Segoe UI", 12),
    bg="#e2e8f0",
    fg="#0f172a",
    bd=0,
    relief=FLAT,
    anchor="w",
    padx=10
)
dept_btn.pack(side=LEFT, fill="x", expand=True)

dept_menu = Menu(dept_btn, tearoff=0)
dept_btn.config(menu=dept_menu)

for d in ["Computer", "Civil", "Mechanical", "First Year",
          "Information Technology", "ENTC"]:
    dept_menu.add_command(
        label=d,
        command=lambda x=d: selected_dept.set(x)
    )

def open_dept_menu(event=None):
    dept_menu.post(
        dept_btn.winfo_rootx(),
        dept_btn.winfo_rooty() + dept_btn.winfo_height()
    )

dept_btn.bind("<Button-1>", open_dept_menu)

arrow_lbl = Label(
    dept_frame,
    text="▼",
    font=("Segoe UI", 10, "bold"),
    bg="#e2e8f0",
    fg="#334155",
    padx=12,
    cursor="hand2"
)
arrow_lbl.pack(side=RIGHT)
arrow_lbl.bind("<Button-1>", open_dept_menu)

# ================= USERNAME =================
Label(
    center,
    text="Username",
    font=("Segoe UI", 11, "bold"),
    bg="#f8fafc",
    fg="#334155"
).pack(anchor="w", padx=45)

user_entry = Entry(
    center,
    font=("Segoe UI", 12),
    bg="#e2e8f0",
    bd=0
)
user_entry.pack(fill="x", padx=45, pady=(5, 15), ipady=8)

# ================= PASSWORD =================
Label(
    center,
    text="Password",
    font=("Segoe UI", 11, "bold"),
    bg="#f8fafc",
    fg="#334155"
).pack(anchor="w", padx=45)

pass_entry = Entry(
    center,
    font=("Segoe UI", 12),
    bg="#e2e8f0",
    bd=0,
    show="*"
)
pass_entry.pack(fill="x", padx=45, pady=(5, 30), ipady=8)

# ================= LOGIN FUNCTION =================
def admin_login(event=None):  # <-- event added for Enter key
    dept_passwords = {
        "Computer": "comp123",
        "Civil": "civil123",
        "Mechanical": "mech123",
        "First Year": "fy123",
        "Information Technology": "it123",
        "ENTC": "entc123"
    }

    if selected_dept.get() == "Select Department":
        messagebox.showerror("Error", "Please select a department")
        return

    if user_entry.get() == "admin" and \
       pass_entry.get() == dept_passwords[selected_dept.get()]:
        messagebox.showinfo(
            "Login Success",
            f"Welcome Admin ({selected_dept.get()})"
        )
        root.destroy()
        open_home_window()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")

# ================= LOGIN BUTTON =================
Button(
    center,
    text="Login",
    font=("Segoe UI", 13, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    bd=0,
    cursor="hand2",
    command=admin_login
).pack(ipadx=90, ipady=8)

# ================= ENTER KEY BINDING =================
root.bind("<Return>", admin_login)

# Auto focus on username field
user_entry.focus_set()

root.mainloop()