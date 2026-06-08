#Program: Demonstration of student details using Python Operations
#Topic: Dictionary

students = {}

while True:
    print("\n----- Student Database -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No records found.")
        else:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(name, "-", marks)

    elif choice == "3":
        if len(students) == 0:
            print("No records available.")
        else:
            topper = max(students, key=students.get)
            print("Topper:", topper)
            print("Marks:", students[topper])

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")
