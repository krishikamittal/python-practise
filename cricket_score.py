#Program: Demonstration of cricket score menue using Python Operations
#Topic: Functions and Conditional Statements

runs = 0
wickets = 0

while True:

    print("\n1. Add Runs")
    print("2. Add Wicket")
    print("3. Show Score")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        run = int(input("Runs scored: "))
        runs += run

    elif choice == 2:
        wickets += 1

    elif choice == 3:
        print("Score:", runs, "/", wickets)

    elif choice == 4:
        break
