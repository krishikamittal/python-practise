#Program: Demonstration of attendance tracker using Python Operations
#Topic: Functions and Conditional Statements, Dictionary

attendance = {}

while True:
    print("\n----- Attendance Tracker -----")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Attendance Percentage")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        status = input("Present or Absent (P/A): ")

        if name not in attendance:
            attendance[name] = []

        attendance[name].append(status.upper())

    elif choice == "2":
        for name, records in attendance.items():
            print(name, ":", records)

    elif choice == "3":
        name = input("Enter student name: ")

        if name in attendance:
            total = len(attendance[name])
            present = attendance[name].count("P")

            percentage = (present / total) * 100

            print("Attendance Percentage:", round(percentage, 2), "%")
        else:
            print("Student not found.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
