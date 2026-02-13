from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from homepp import open_home_window

# ================= ROOT WINDOW =================
root = Tk()
root.title("AI Timetable Generator - Login")
root.state("zoomed")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# ================= BACKGROUND IMAGE =================
bg_img = Image.open("loginbg.png")
bg_img = bg_img.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ================= LOGO =================
try:
    img = Image.open("logoo.jpeg").convert("RGBA")
    img = img.resize((140, 120), Image.LANCZOS)
    logo = ImageTk.PhotoImage(img)

    logo_label = Label(root, image=logo, bd=0, highlightthickness=0)
    logo_label.image = logo
    logo_label.place(x=17, y=40)

except Exception as e:
    print("Logo error:", e)

# ================= COLLEGE NAME =================
#Label(
#    root,
#    text="Sinhgad Academy of Engineering,Kondhwa – Pune",
#    font=("Segoe UI",22, "bold"),
#    fg="white",
#    bg="#917672",
#    justify="center"
#).place(relx=0.5, rely=0.22, anchor="center")

# ================= LOGIN CARD =================
card_width = 420
card_height = 480
card_color = "#CCA7A1"

card_frame = Frame(root, bg=card_color, width=card_width, height=card_height)
card_frame.place(relx=0.5, rely=0.58, anchor="center")
card_frame.pack_propagate(False)

root.attributes("-alpha", 0.97)

# ================= TITLE =================
Label(
    card_frame,
    text="Login",
    font=("Segoe UI", 25, "bold"),
    bg=card_color,
    fg="white"
).pack(pady=(30, 10))

Label(
    card_frame,
    text="AI Timetable Generator",
    font=("Segoe UI", 10),
    bg=card_color,
    fg="black"
).pack(pady=(0, 25))

selected_dept = StringVar(value="Select Department")

# ================= DEPARTMENT =================
Label(
    card_frame,
    text="Department",
    font=("Segoe UI", 11, "bold"),
    bg=card_color,
    fg="white"
).pack(anchor="w", padx=45)

dept_frame = Frame(card_frame, bg="#78635F")
dept_frame.pack(fill="x", padx=45, pady=(5, 15), ipady=6)

dept_btn = Menubutton(
    dept_frame,
    textvariable=selected_dept,
    font=("Segoe UI", 12),
    bg="#78635F",
    fg="white",
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
    bg="#78635F",
    fg="white",
    padx=12,
    cursor="hand2"
)
arrow_lbl.pack(side=RIGHT)
arrow_lbl.bind("<Button-1>", open_dept_menu)

# ================= USERNAME =================
Label(
    card_frame,
    text="Username",
    font=("Segoe UI", 11, "bold"),
    bg=card_color,
    fg="white"
).pack(anchor="w", padx=45)

user_entry = Entry(
    card_frame,
    font=("Segoe UI", 12),
    bg="#78635F",
    fg="white",
    insertbackground="white",
    bd=0
)
user_entry.pack(fill="x", padx=45, pady=(5, 15), ipady=8)

# ================= PASSWORD =================
Label(
    card_frame,
    text="Password",
    font=("Segoe UI", 11, "bold"),
    bg=card_color,
    fg="white"
).pack(anchor="w", padx=45)

pass_entry = Entry(
    card_frame,
    font=("Segoe UI", 12),
    bg="#78635F",
    fg="white",
    insertbackground="white",
    bd=0,
    show="*"
)
pass_entry.pack(fill="x", padx=45, pady=(5, 30), ipady=8)

# ================= LOGIN FUNCTION =================
def admin_login(event=None):
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

# ================= ENTER KEY FEATURES =================
# Press Enter in Username → go to Password
def go_to_password(event):
    pass_entry.focus_set()

user_entry.bind("<Return>", go_to_password)

# Press Enter in Password → Login
pass_entry.bind("<Return>", admin_login)

# ================= LOGIN BUTTON =================
Button(
    card_frame,
    text="Login",
    font=("Segoe UI", 13, "bold"),
    bg="#433735",
    fg="white",
    activebackground="#433735",
    bd=0,
    cursor="hand2",
    command=admin_login
).pack(ipadx=90, ipady=8)

user_entry.focus_set()

root.mainloop()
