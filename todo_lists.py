#Program: Demonstration of to do lists using Python Operations
#Topic: Lists

tasks = []

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == 2:
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)

    elif choice == 3:
        print("\nTasks:")
        for task in tasks:
            print("-", task)

    elif choice == 4:
        break
