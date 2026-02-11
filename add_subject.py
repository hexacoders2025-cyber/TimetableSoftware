import sqlite3

conn = sqlite3.connect("timetable.db")
cursor = conn.cursor()

subjects_list = [
    # SE
    ("Data Structures", "SE"),
    ("Digital Logic Design", "SE"),
    ("Computer Organization", "SE"),
    ("Discrete Mathematics", "SE"),
    ("OOP", "SE"),

    # TE
    ("Operating System", "TE"),
    ("Computer Networks", "TE"),
    ("DBMS", "TE"),
    ("Software Engineering", "TE"),
    ("Theory of Computation", "TE"),

    # BE
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

conn.commit()
conn.close()

print("Subjects Added Successfully")
