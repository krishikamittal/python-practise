#Program: Demonstration of employee salary using Python Operations
#Topic: Functions and Conditional Statements, Dictionary

employees = {}

while True:
    print("\n----- Employee Salary Calculator -----")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Calculate Salary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        basic_salary = float(input("Enter basic salary: "))

        employees[name] = basic_salary

        print("Employee added successfully!")

    elif choice == "2":

        if len(employees) == 0:
            print("No employees found.")

        else:
            print("\nEmployee Records:")
            for name, salary in employees.items():
                print(name, "- ₹", salary)

    elif choice == "3":

        name = input("Enter employee name: ")

        if name in employees:

            basic = employees[name]

            hra = basic * 0.20
            da = basic * 0.10

            total_salary = basic + hra + da

            print("\nSalary Details")
            print("Basic Salary:", basic)
            print("HRA:", hra)
            print("DA:", da)
            print("Total Salary:", total_salary)

        else:
            print("Employee not found.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
