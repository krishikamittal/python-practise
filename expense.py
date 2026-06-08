#Program: Demonstration of expenses using Python Operations
#Topic: Lists and Function

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        expenses.append((amount, category))

    elif choice == 2:
        for amount, category in expenses:
            print(category, "-", amount)

    elif choice == 3:
        total = sum(amount for amount, category in expenses)
        print("Total Spending:", total)

    elif choice == 4:
        break
