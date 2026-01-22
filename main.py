from database import connect_db
from student import add_student, view_students

connect_db()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
