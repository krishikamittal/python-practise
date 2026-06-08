#Program: Demonstration of library management using Python Operations
#Topic: Functions and Conditional Statements, List

books = []

while True:
    print("\n----- Library Management -----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in books:
                print("-", book)

    elif choice == "3":
        book = input("Enter book name to issue: ")

        if book in books:
            books.remove(book)
            print("Book issued successfully!")
        else:
            print("Book not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
