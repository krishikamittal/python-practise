#Program: Demonstration of atm system using Python Operations
#Topic: Functions and Conditional Statements

balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        balance += amount
        print("Amount deposited.")

    elif choice == 3:
        amount = float(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    elif choice == 4:
        break
