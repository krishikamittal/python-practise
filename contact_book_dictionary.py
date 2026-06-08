#Program: Demonstration of contact book using Python Operations
# Topic: Dictionary

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. View Contacts")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number

    elif choice == 2:
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found")

    elif choice == 3:
        print(contacts)

    elif choice == 4:
        break
