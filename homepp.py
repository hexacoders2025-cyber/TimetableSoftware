from tkinter import *
from PIL import Image, ImageTk


def open_home_window():
   
    root = Tk()
    root.title("College Timetable Generator")
    root.geometry("1400x800")
    root.configure(bg="white")

    SIDEBAR_WIDTH = 280
    sidebar_x = -SIDEBAR_WIDTH
    sidebar_open = False
    active_btn = None   # track selected button

    # ================= CONTAINER =================
    container = Frame(root, bg="white")
    container.pack(fill=BOTH, expand=True)

    # ================= SIDEBAR =================
    sidebar = Frame(container, bg="#e6e6e6")
    sidebar.place(x=sidebar_x, y=0, width=SIDEBAR_WIDTH, relheight=1)

    # ================= MAIN AREA =================
    main_area = Frame(container, bg="white")
    main_area.place(x=0, y=0, relwidth=1, relheight=1)

    # ================= ANIMATION =================
    def slide_in():
        nonlocal sidebar_x, sidebar_open

        if sidebar_x < 0:
            sidebar_x += 20

            # Move sidebar and main area
            sidebar.place(x=sidebar_x, y=0)
            main_area.place(x=sidebar_x + SIDEBAR_WIDTH, y=0)

            # 🔹 DYNAMIC WRAP WHILE MOVING
            available_width = root.winfo_width() - (SIDEBAR_WIDTH + sidebar_x)
            wrap = max(350, int(available_width * 0.75))

            title_label.configure(wraplength=wrap)
            title_label.update_idletasks()

            root.after(20, slide_in)
        else:
            sidebar_x = 0
            sidebar_open = True




    def slide_out():
        nonlocal sidebar_x, sidebar_open

        if sidebar_x > -SIDEBAR_WIDTH:
            sidebar_x -= 20

            sidebar.place(x=sidebar_x, y=0)
            main_area.place(x=sidebar_x + SIDEBAR_WIDTH, y=0)

            # ---- FORCE WRAPPING UPDATE ----
            available_width = root.winfo_width() - (SIDEBAR_WIDTH + sidebar_x)
            wrap = max(350, int(available_width * 0.75))

            title_label.configure(wraplength=wrap)
            title_label.update_idletasks()   # 🔥 THIS IS THE KEY LINE

            root.after(20, slide_out)
        else:
            sidebar_x = -SIDEBAR_WIDTH
            sidebar_open = False
            menu_btn.pack(side=LEFT, padx=15)




    def open_sidebar():
        menu_btn.pack_forget()
        slide_in()

    def close_sidebar():
        slide_out()

    # ================= SIDEBAR HEADER =================
    header = Frame(sidebar, bg="#d0d0d0", height=60)
    header.pack(fill=X)

    Button(
        header, text="✖",
        font=("Arial", 18, "bold"),
        bg="#d0d0d0", bd=0,
        command=close_sidebar
    ).pack(side=RIGHT, padx=15)

    Label(
        header, text="MENU",
        font=("Arial", 18, "bold"),
        bg="#d0d0d0"
    ).pack(side=LEFT, padx=20)

    # ================= SIDEBAR BUTTON LOGIC WITH HOVER SHADOW =================
    active_btn = None

    def set_active(btn):
        global active_btn
        if active_btn:
            active_btn.config(bg="#e6e6e6", fg="black", relief="flat", bd=0)
        btn.config(bg="#2563eb", fg="white", relief="flat", bd=0)
        active_btn = btn

    def on_hover(e):
        widget = e.widget
        if widget != active_btn:
            widget.config(relief="raised", bd=3)

    def on_leave(e):
        widget = e.widget
        if widget != active_btn:
            widget.config(relief="flat", bd=0)

    def sidebar_btn(text):
        btn = Button(
            sidebar,
            text=text,
            font=("Arial", 16),
            bg="#e6e6e6",
            fg="black",
            bd=0,
            relief="flat",
            anchor="w",
            padx=25,
            pady=15,
            activebackground="#2563eb",
            activeforeground="white",
            command=lambda b=None: None
        )

        btn.config(command=lambda b=btn: set_active(b))

        # Hover bindings
        btn.bind("<Enter>", on_hover)
        btn.bind("<Leave>", on_leave)

        btn.pack(fill=X, padx=12, pady=6)
        return btn

    # Sidebar options
    btn_instructor = sidebar_btn("👨‍🏫  Instructors")
    btn_instructor.config(command=lambda: open_modal("Instructor Details"))

    btn_rooms = sidebar_btn("🏫  Rooms")
    btn_rooms.config(command=lambda: open_modal("Room Details"))

    btn_meeting = sidebar_btn("📘  Meetings")
    btn_meeting.config(command=lambda: open_modal("Meeting Time Setup"))

    # ================= GENERATE TIMETABLE DROPDOWN =================
    gen_open = False
    student_open = False

    def toggle_generate():
        nonlocal gen_open
        if gen_open:
            gen_menu.pack_forget()
            gen_open = False
        else:
            gen_menu.pack(fill=X, padx=12)
            gen_open = True

    def open_teacher():
        gen_menu.pack_forget()
        student_menu.pack_forget()
        home_page.lift()
        teacher_page.lift()
        set_active(gen_btn)

    def toggle_student():
        nonlocal student_open
        if student_open:
            student_menu.pack_forget()
            student_open = False
        else:
            student_menu.pack(fill=X, padx=30)
            student_open = True

    def open_student(year):
        gen_menu.pack_forget()
        student_menu.pack_forget()
        home_page.lift()
        student_page.lift()
        print("Selected Student Year:", year)

    gen_btn = sidebar_btn("📅  Generate Timetable")
    gen_btn.config(command=toggle_generate)

    gen_menu = Frame(sidebar, bg="#f0f0f0")

    Button(
        gen_menu, text="👨‍🏫  Teacher",
        font=("Arial", 14),
        bg="#f0f0f0",
        bd=0,
        anchor="w",
        padx=45,
        pady=10,
        command=open_teacher
    ).pack(fill=X)

    Button(
        gen_menu, text="🎓  Student",
        font=("Arial", 14),
        bg="#f0f0f0",
        bd=0,
        anchor="w",
        padx=45,
        pady=10,
        command=toggle_student
    ).pack(fill=X)

    student_menu = Frame(sidebar, bg="#e8e8e8")

    for year in ("SE", "TE", "BE"):
        Button(
            student_menu,
            text=f"• {year}",
            font=("Arial", 13),
            bg="#e8e8e8",
            bd=0,
            anchor="w",
            padx=65,
            pady=8,
            command=lambda y=year: open_student(y)
        ).pack(fill=X)

    def close_sidebar():
        gen_menu.pack_forget()
        student_menu.pack_forget()
        slide_out()


    # ================= LOGOUT BUTTON =================
    logout_btn = Button(
        sidebar,
        text="↩ Logout",
        font=("Arial", 15),
        bg="#e6e6e6",
        fg="black",
        bd=0,
        relief="flat",
        padx=25,
        pady=14,
        activebackground="#2563eb",
        activeforeground="white"
    )

    logout_btn.config(command=lambda b=logout_btn: set_active(b))
    logout_btn.bind("<Enter>", on_hover)
    logout_btn.bind("<Leave>", on_leave)

    logout_btn.pack(side=BOTTOM, fill=X, padx=12, pady=20)


    # ================= TOP BAR =================
    topbar = Frame(main_area, bg="white", height=60)
    topbar.pack(fill=X)

    menu_btn = Button(
        topbar, text="☰",
        font=("Arial", 22),
        bg="white",
        bd=0,
        command=open_sidebar
    )
    menu_btn.pack(side=LEFT, padx=15)

    # ================= MAIN CONTENT =================
    content = Frame(main_area, bg="white")
    content.pack(fill=BOTH, expand=True)

    # ================= PAGES =================
    home_page = Frame(content, bg="white")
    teacher_page = Frame(content, bg="white")
    student_page = Frame(content, bg="white")

    for page in (home_page, teacher_page, student_page):
        page.place(relwidth=1, relheight=1)

    home_page.lift()   # default page

        # ================= CENTER MODAL (POPUP) =================
    modal_overlay = Frame(content, bg="#000000")
    modal_overlay.place(relwidth=1, relheight=1)
    modal_overlay.place_forget()

    modal_box = Frame(
        modal_overlay,
        bg="white",
        bd=2,
        relief=SOLID
    )
    modal_box.place(relx=0.5, rely=0.5, anchor=CENTER, width=520, height=360)

    def open_modal(title_text):
        modal_overlay.place(relwidth=1, relheight=1)
        modal_overlay.lift()
        # Clear old widgets
        for widget in modal_box.winfo_children():
            widget.destroy()

        Label(
            modal_box,
            text=title_text,
            font=("Arial", 20, "bold"),
            bg="white"
        ).pack(pady=20)

        # Example dropdown
        option = StringVar(value="Select Option")

        OptionMenu(
            modal_box,
            option,
            "SE", "TE", "BE"
        ).pack(pady=15)

        Button(
            modal_box,
            text="Save",
            font=("Arial", 12, "bold"),
            bg="#2563eb",
            fg="white",
            width=18
        ).pack(pady=10)

        Button(
            modal_box,
            text="Close",
            command=close_modal,
            width=18
        ).pack(pady=10)


    def close_modal():
        modal_overlay.place_forget()


    # ================= FIXED TOP-RIGHT IMAGE =================
    bg_img = Image.open("bg.png")

    # CHANGE SIZE HERE (width, height)
    bg_img = bg_img.resize((100, 100), Image.LANCZOS)

    bg_photo = ImageTk.PhotoImage(bg_img)


    bg_label = Label(root, image=bg_photo, bg="white")
    bg_label.image = bg_photo              # prevent GC

    # Fixed to window (will NOT move with sidebar)
    bg_label.place(relx=0.98, rely=0.02, anchor=NE)

    title_label = Label(
        home_page,
        text="COLLEGE TIMETABLE GENERATOR",
        font=("Arial", 42, "bold"),
        fg="#3f2b96",
        bg="white",
        justify="center",
        wraplength=900   # full width (sidebar closed)
    )

    title_label.place(relx=0.5, rely=0.15, anchor=CENTER)


    Label(
        teacher_page,
        text="TEACHER TIMETABLE PAGE",
        font=("Arial", 32, "bold"),
        bg="white"
    ).pack(pady=120)

    Label(
        student_page,
        text="STUDENT TIMETABLE PAGE",
        font=("Arial", 32, "bold"),
        bg="white"
    ).pack(pady=120)




    root.mainloop()
