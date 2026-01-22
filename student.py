import sqlite3

def add_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter course name: ")

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()
    print("✅ Student added successfully")


def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("❌ No students found")

    conn.close()
