import sqlite3
import random
conn = sqlite3.connect("timetable.db")
cursor = conn.cursor()

# ================= STAFF TABLE =================
cursor.execute("""
CREATE TABLE IF NOT EXISTS staff (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

# ================= SUBJECT TABLE =================
cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL,
    year TEXT NOT NULL
)
""")

# ================= STAFF-SUBJECT MAPPING =================
cursor.execute("""
CREATE TABLE IF NOT EXISTS staff_subject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_id INTEGER,
    subject_id INTEGER,
    FOREIGN KEY(staff_id) REFERENCES staff(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
)
""")

# ================= ROOM TABLE =================
cursor.execute("""
CREATE TABLE IF NOT EXISTS room(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    capacity INTEGER
)
""")

# ================= COURSE TABLE =================
cursor.execute("""
CREATE TABLE IF NOT EXISTS course(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    max_students INTEGER,
    is_lab INTEGER
)
""")

# ================= MEETING TIME TABLE =================
cursor.execute("""
CREATE TABLE IF NOT EXISTS meeting_time(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT,
    period INTEGER
)
""")

conn.commit()

# ================= SHOW DATA =================
print("STAFF DATA:")
cursor.execute("SELECT * FROM staff")
print(cursor.fetchall())

print("SUBJECT DATA:")
cursor.execute("SELECT * FROM subjects")
print(cursor.fetchall())

for i in range(1, 31):
    cursor.execute("INSERT INTO staff (name) VALUES (?)", (f"Staff{i}",))

    # Insert random subjects
subjects_list = [
    # SE Subjects
    ("Data Structures", "SE"),
    ("Digital Logic Design", "SE"),
    ("Computer Organization", "SE"),
    ("Discrete Mathematics", "SE"),
    ("OOP", "SE"),

    # TE Subjects
    ("Operating System", "TE"),
    ("Computer Networks", "TE"),
    ("DBMS", "TE"),
    ("Software Engineering", "TE"),
    ("Theory of Computation", "TE"),

    # BE Subjects
    ("Machine Learning", "BE"),
    ("Cloud Computing", "BE"),
    ("Cyber Security", "BE"),
    ("Big Data", "BE"),
    ("Artificial Intelligence", "BE"),
]

cursor.executemany(
    "INSERT INTO subjects (subject_name, year) VALUES (?, ?)",
    subjects_list
)

print("Subjects Added Successfully")
cursor.execute("SELECT * FROM subjects")
print(cursor.fetchall())
for sub in subjects_list:
    cursor.execute("INSERT INTO subjects (subject_name, year) VALUES (?, ?)", sub)

# ================= RANDOM MAPPING =================

cursor.execute("SELECT id FROM staff")
staff_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM subjects")
subject_ids = [row[0] for row in cursor.fetchall()]

for staff_id in staff_ids:
    subject_id = random.choice(subject_ids)
    cursor.execute(
        "INSERT INTO staff_subject (staff_id, subject_id) VALUES (?, ?)",
        (staff_id, subject_id)
    )

print("Staff-Subject Mapping Done")

conn.commit()
conn.close()

conn.commit()    
conn.close()

print("Database Ready")
