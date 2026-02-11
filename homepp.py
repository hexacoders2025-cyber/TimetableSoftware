from tkinter import *
from tkinter import ttk
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
    btn_instructor.config(command=lambda: instructor_page.lift())

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
            gen_btn.config(text="📅  Generate Timetable  ▼")
            gen_open = False
        else:
            gen_menu.pack(fill=X, padx=12, after=gen_btn)
            gen_btn.config(text="📅  Generate Timetable  ▲")
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

    gen_btn = sidebar_btn("📅  Generate Timetable  ▼")


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

    instructor_page = Frame(content, bg="white")   # 👈 ADD THIS LINE

    for page in (home_page, teacher_page, student_page, instructor_page):  # 👈 ADD HERE
        page.place(relwidth=1, relheight=1)

    home_page.lift()   # default page
    
    def open_instructor_year(year):
        instructor_page.lift()
        print("Instructor Year Selected:", year)
        
    # ================= INSTRUCTOR PAGE CONTENT =================

    def create_staff_table(parent, title):

        frame = Frame(parent, bg="white")
        frame.pack(pady=20, fill=X)

        Label(
            frame,
            text=title,
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(anchor="w", padx=20)

        # Add Button
        def add_row():
            tree.insert("", END, values=("New Teacher", "New Subject", "Edit"))

        Button(
            frame,
            text="Add",
            bg="#2563eb",
            fg="white",
            width=10,
            command=add_row
        ).pack(anchor="e", padx=20, pady=5)

        columns = ("Teacher Name", "Subject", "Action")

        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            height=10
        )

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=180, anchor=CENTER)

        tree.pack(padx=20)

        # Insert 10 empty rows
        for _ in range(10):
            tree.insert("", END, values=("Teacher", "Subject", "Edit"))

        # -------- EDIT FUNCTIONALITY --------

        # def on_double_click(event):
        #     item = tree.focus()
        #     if not item:
        #         return

        #     values = tree.item(item, "values")

        #     if values[2] == "Edit":
        #         tree.item(item, values=(values[0], values[1], "Save"))

        #         x1, y1, w1, h1 = tree.bbox(item, "#1")
        #         entry1 = Entry(tree)
        #         entry1.insert(0, values[0])
        #         entry1.place(x=x1, y=y1, width=w1, height=h1)

        #         x2, y2, w2, h2 = tree.bbox(item, "#2")
        #         entry2 = Entry(tree)
        #         entry2.insert(0, values[1])
        #         entry2.place(x=x2, y=y2, width=w2, height=h2)

        #         def save():
        #             tree.item(item, values=(
        #                 entry1.get(),
        #                 entry2.get(),
        #                 "Edit"
        #             ))
        #             entry1.destroy()
        #             entry2.destroy()

        #         entry1.bind("<Return>", lambda e: save())
        #         entry2.bind("<Return>", lambda e: save())

        # tree.bind("<Double-1>", on_double_click)
        
            def on_click(event):
                item = tree.identify_row(event.y)
                column = tree.identify_column(event.x)

                if not item or column != "#3":
                    return

                values = tree.item(item, "values")

                # If currently Edit → switch to Save mode
                if values[2] == "Edit":
                    tree.item(item, values=(values[0], values[1], "Save"))

                    x1, y1, w1, h1 = tree.bbox(item, "#1")
                    entry1 = Entry(tree)
                    entry1.insert(0, values[0])
                    entry1.place(x=x1, y=y1, width=w1, height=h1)

                    x2, y2, w2, h2 = tree.bbox(item, "#2")
                    entry2 = Entry(tree)
                    entry2.insert(0, values[1])
                    entry2.place(x=x2, y=y2, width=w2, height=h2)

                    # Store entries inside tree object
                    tree.edit_entries = (entry1, entry2)

                # If currently Save → save data
                elif values[2] == "Save":
                    entry1, entry2 = tree.edit_entries

                    new_name = entry1.get()
                    new_subject = entry2.get()

                    tree.item(item, values=(new_name, new_subject, "Edit"))

                    entry1.destroy()
                    entry2.destroy()

                    tree.edit_entries = None

            tree.bind("<Button-1>", on_click)



   # Clear previous content
    for widget in instructor_page.winfo_children():
        widget.destroy()

    # ---------- SCROLLABLE AREA ----------
    canvas = Canvas(instructor_page, bg="white")
    scrollbar = Scrollbar(instructor_page, orient=VERTICAL, command=canvas.yview)

    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollable_frame = Frame(canvas, bg="white")

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", on_configure)

    # Make canvas width follow window
    def resize_canvas(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.bind("<Configure>", resize_canvas)

    # Mouse wheel scrolling
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # ---------- CONTENT ----------
    Label(
        scrollable_frame,
        text="Instructor Management",
        font=("Arial", 28, "bold"),
        bg="white"
    ).pack(pady=20)

    create_staff_table(scrollable_frame, "SE STAFF")
    create_staff_table(scrollable_frame, "TE STAFF")
    create_staff_table(scrollable_frame, "BE STAFF")




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