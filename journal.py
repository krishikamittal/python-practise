#Program: Demonstration of journal manager using Python Operations
#Topic: Functions and Conditional Statements

while True:
    print("\n----- Journal Manager -----")
    print("1. Write Entry")
    print("2. View Entries")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        entry = input("Write your journal entry:\n")

        file = open("journal.txt", "a")
        file.write(entry + "\n")
        file.close()

        print("Entry Saved!")

    elif choice == "2":

        try:
            file = open("journal.txt", "r")
            print("\njournal Entries:\n")
            print(file.read())
            file.close()

        except FileNotFoundError:
            print("No journal entries found.")

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
