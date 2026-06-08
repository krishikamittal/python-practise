# Program: Banking System

accounts = {}

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. View Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter account holder name: ")
        accounts[name] = 0
        print("Account created.")

    elif choice == 2:
        name = input("Enter account holder name: ")

        if name in accounts:
            amount = float(input("Enter amount: "))
            accounts[name] += amount

    elif choice == 3:
        name = input("Enter account holder name: ")

        if name in accounts:
            print("Balance:", accounts[name])

    elif choice == 4:
        break
