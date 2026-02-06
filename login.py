from tkinter import *
from PIL import Image, ImageTk
import os

def open_main():
    os.system("python main.py")

def login(role):
    username = user_entry.get()
    password = pass_entry.get()

    if role == "admin" and username == "admin" and password == "123":
        open_main()
        root.destroy()
    elif role == "faculty" and username == "faculty" and password == "123":
        open_main()
        root.destroy()
    else:
        status_label.config(text="Invalid Login!", fg="red")

# ===== WINDOW =====
root = Tk()
root.title("Login")
root.state("zoomed")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# ===== PINK BACKGROUND =====
bg = Image.new("RGB", (screen_width, screen_height), "#ffc0cb")
bg_photo = ImageTk.PhotoImage(bg)
Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

# ===== LOGO TOP RIGHT =====
logo_img = Image.open("bg.png")
logo_img = logo_img.resize((120, 120))
logo_photo = ImageTk.PhotoImage(logo_img)

Label(root, image=logo_photo, bd=0).place(relx=1.0, y=10, anchor="ne")

# ===== GLASS LOGIN BOX =====
glass = Frame(root, bg="#ffffff", bd=0)
glass.place(relx=0.5, rely=0.5, anchor=CENTER)

glass.config(highlightbackground="#ffffff", highlightthickness=1)
glass.pack_propagate(False)
glass.config(width=400, height=450)

# Soft glass color
glass_bg = "#ffffff"

Label(glass, text="Login", font=("Arial", 28, "bold"),
      bg=glass_bg, fg="#ff69b4").pack(pady=20)

Label(glass, text="Username", bg=glass_bg).pack()
user_entry = Entry(glass, width=25, font=("Arial", 12))
user_entry.pack(pady=8)

Label(glass, text="Password", bg=glass_bg).pack()
pass_entry = Entry(glass, show="*", width=25, font=("Arial", 12))
pass_entry.pack(pady=8)

Button(glass, text="Admin Login", width=20, bg="#ff69b4",
       fg="white", font=("Arial", 12),
       command=lambda: login("admin")).pack(pady=10)

Button(glass, text="Faculty Login", width=20, bg="#ff1493",
       fg="white", font=("Arial", 12),
       command=lambda: login("faculty")).pack()

status_label = Label(glass, text="", bg=glass_bg)
status_label.pack(pady=10)

root.mainloop()
