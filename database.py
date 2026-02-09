import sqlite3

conn = sqlite3.connect("timetable.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM instructor")
print(cursor.fetchall())
# Instructor table
cursor.execute("""
CREATE TABLE IF NOT EXISTS instructor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name TEXT NOT NULL,
    subject TEXT NOT NULL,
    division TEXT NOT NULL,
    timeslot TEXT NOT NULL,
    available INTEGER NOT NULL
)
""")

# Room table
cursor.execute("""
CREATE TABLE IF NOT EXISTS room(
id INTEGER PRIMARY KEY AUTOINCREMENT,
number TEXT,
capacity INTEGER
)
""")

# Course table
cursor.execute("""
CREATE TABLE IF NOT EXISTS course(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
max_students INTEGER,
is_lab INTEGER
)
""")

# Meeting Time table
cursor.execute("""
CREATE TABLE IF NOT EXISTS meeting_time(
id INTEGER PRIMARY KEY AUTOINCREMENT,
day TEXT,
period INTEGER
)
""")

conn.commit()
conn.close()
print("Database Ready")
