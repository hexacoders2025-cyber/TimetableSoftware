from tkinter import *
from tkinter import messagebox
from main import open_main_window
from PIL import Image, ImageTk

# ===== CREATE ROOT =====
root = Tk()
root.title("Admin Login")
root.state("zoomed")
root.configure(bg="#ebdde0")
root.resizable(False, False)

# ===== CENTER LOGIN BOX (WITH BORDER) =====
center = Frame(
    root,
    bg="#fad6dc",
    bd=3,            # border thickness
    relief=SOLID,    # solid border
    padx=40,         # inner padding
    pady=30
)
center.place(relx=0.5, rely=0.5, anchor=CENTER)

# ===== VARIABLE TO STORE SELECTED DEPARTMENT =====
selected_dept = StringVar()
selected_dept.set("Select Department")

# ===== LOGIN FUNCTION =====
def admin_login():
    username = user_entry.get().strip()
    password = pass_entry.get().strip()
    dept = selected_dept.get()

    dept_passwords = {
        "Computer": "comp123",
        "Civil": "civil123",
        "Mechanical": "mech123",
        "First Year": "fy123",
        "Information Technology": "it123",
        "ENTC": "entc123"
    }

    if dept == "Select Department":
        messagebox.showerror("Error", "Please select a department")
        return

    if username == "admin" and password == dept_passwords.get(dept):
        messagebox.showinfo("Login Success", f"Welcome Admin ({dept})")
        root.destroy()
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials for selected department")

# ===== HEADING =====
Label(center, text="ADMIN LOGIN",
      font=("Arial", 28, "bold"),
      bg="#fad6dc").pack(pady=20)

# ===== DEPARTMENT DROPDOWN =====
dept_btn = Menubutton(
    center,
    textvariable=selected_dept,
    font=("Arial", 14, "bold"),
    width=24,
    bg="#ff69b4",
    fg="white",
    activebackground="#ff85c1",
    activeforeground="white",
    bd=2,
    relief=SOLID
)
dept_btn.pack(pady=10)

dept_menu = Menu(dept_btn, tearoff=0, bg="#ffc0cb", fg="black")
dept_btn.config(menu=dept_menu)

dept_menu.add_command(label="Computer",
                      command=lambda: selected_dept.set("Computer"))
dept_menu.add_command(label="Civil",
                      command=lambda: selected_dept.set("Civil"))
dept_menu.add_command(label="Mechanical",
                      command=lambda: selected_dept.set("Mechanical"))
dept_menu.add_command(label="First Year",
                      command=lambda: selected_dept.set("First Year"))
dept_menu.add_command(label="Information Technology",
                      command=lambda: selected_dept.set("Information Technology"))
dept_menu.add_command(label="ENTC",
                      command=lambda: selected_dept.set("ENTC"))

# ===== LOGO (TOP RIGHT) =====
logo_img = Image.open("bg.png")
logo_img = logo_img.resize((150, 150))
logo_photo = ImageTk.PhotoImage(logo_img)

logo_label = Label(root, image=logo_photo, bd=0)
logo_label.place(relx=1.0, y=10, anchor="ne")

# ===== USERNAME =====
Label(center, text="Username", font=("Arial", 14), bg="#fad6dc").pack()
user_entry = Entry(center, font=("Arial", 14), width=25, bd=2, relief=SOLID)
user_entry.pack(pady=6)

# ===== PASSWORD =====
Label(center, text="Password", font=("Arial", 14), bg="#fad6dc").pack()
pass_entry = Entry(center, show="*", font=("Arial", 14), width=25, bd=2, relief=SOLID)
pass_entry.pack(pady=6)

# ===== LOGIN BUTTON =====
Button(center, text="Login",
       command=admin_login,
       font=("Arial", 16, "bold"),
       bg="#ff69b4",
       fg="white",
       width=24,
       bd=2,
       relief=SOLID).pack(pady=25)

root.mainloop()