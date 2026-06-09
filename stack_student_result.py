# Function to create and return the RESULT list
def CREATE():
    RESULT = []  
    N = int(input("Enter the number of students: "))  
    for _ in range(N):
        name = input("Enter student name: ")  
        marks = int(input("Enter Computer Science marks: "))  
        RESULT.append((name, marks))  
    return RESULT  

# Function to push eligible students (Marks >= 33) into PASS stack
def PUSH(RESULT, PASS):
    for student in RESULT:
        if student[1] >= 33:  # Only students with marks 33 or above are pushed
            PASS.append(student)  
    print("Eligible students added to the stack.")
    return PASS  

# Function to pop students from the stack PASS
def POP(PASS):
    if not PASS:  
        print("Stack is empty! No students to pop.")
    else:
        student = PASS.pop()  # Removes the last student (LIFO)
        print(f"Popped Student: {student[0]}, Marks: {student[1]}")

# Function to display students in the stack PASS
def DISPLAY(PASS):
    if not PASS:  
        print("Stack is empty!")
    else:
        print("Students in stack (Last added displayed first):")
        for student in reversed(PASS):  # Display in LIFO order
            print(f"{student[0]}, Marks: {student[1]}")

# Main menu
PASS = []  # Stack to store students with marks >= 33
RESULT = []  # List to store all student details

while True:
    print("\nMenu:")
    print("1. Create Student List")
    print("2. Push Students to Stack")
    print("3. Pop a Student from Stack")
    print("4. Display Stack")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        RESULT = CREATE()
    elif choice == "2":
        PASS = PUSH(RESULT, PASS)
    elif choice == "3":
        POP(PASS)
    elif choice == "4":
        DISPLAY(PASS)
    elif choice == "5":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")


