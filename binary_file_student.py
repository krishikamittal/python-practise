#Program: 

import pickle

# Function to create the binary file and add a single student record
def CREATE():
    record = []
    rollno = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    record.append([rollno, name, marks])
    
    with open("result.dat", "wb") as outFile:
        pickle.dump(record, outFile)

# Function to append a new student record to the file
def APPEND():
    try:
        with open("result.dat", "rb") as inFile:
            records = pickle.load(inFile)
    except FileNotFoundError:
        records = []
    
    rollno = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    
    records.append([rollno, name, marks])
    
    with open("result.dat", "wb") as outFile:
        pickle.dump(records, outFile)

# Function to search for a student by roll number
def SEARCH(ROLLNO):
    try:
        with open("result.dat", "rb") as inFile:
            records = pickle.load(inFile)
            for record in records:
                if record[0] == ROLLNO:
                    print("Record Found:", record)
                    return
            print("No record found with Roll Number:", ROLLNO)
    except FileNotFoundError:
        print("File does not exist!")

# Function to delete a student record by roll number
def DELETE(ROLLNO):
    try:
        with open("result.dat", "rb") as inFile:
            records = pickle.load(inFile)
    except FileNotFoundError:
        print("File does not exist!")
        return

    new_records = [record for record in records if record[0] != ROLLNO]

    if len(new_records) == len(records):
        print("No record found with Roll Number:", ROLLNO)
    else:
        with open("result.dat", "wb") as outFile:
            pickle.dump(new_records, outFile)
        print("Record with Roll Number", ROLLNO, "has been deleted.")

# Minimal menu-based execution
def Menu():
    while True:
        print("\n<< STUDENT RECORD MANAGEMENT >>")
        print("1. Create File (First Entry)")
        print("2. Append New Record")
        print("3. Search by Roll Number")
        print("4. Delete by Roll Number")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            CREATE()
        elif choice == 2:
            APPEND()
        elif choice == 3:
            rollno = int(input("Enter Roll Number to Search: "))
            SEARCH(rollno)
        elif choice == 4:
            rollno = int(input("Enter Roll Number to Delete: "))
            DELETE(rollno)
        elif choice == 5:
            print("Exiting Program. Thank You!")
            break
        else:
            print("Invalid Choice! Try Again.")

# Run the menu
Menu()

