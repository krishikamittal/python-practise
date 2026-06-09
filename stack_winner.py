#Program: Demonstration of Winner list using STACK Menu Based Program and using Python Operations
#Topic: Stack, Python Operations

# Function to create and return the CUSTOMERS list
def CREATE():
    CUSTOMERS = []  
    N = int(input("Enter the number of customers: "))  
    for _ in range(N):
        name = input("Enter customer name: ")  
        amount = int(input("Enter purchased amount: "))  
        CUSTOMERS.append((name, amount))  
    return CUSTOMERS  

# Function to push eligible customers (Amount >= 5000) into WINNER stack
def PUSH(CUSTOMERS, WINNER):
    for customer in CUSTOMERS:
        if customer[1] >= 5000:  # Only customers with amount 5000 or more are pushed
            WINNER.append(customer)  
    print("Eligible customers added to the stack.")
    return WINNER  

# Function to pop customers from the stack WINNER
def POP(WINNER):
    if not WINNER:  
        print("Stack is empty! No customers to pop.")
    else:
        while WINNER:
            customer = WINNER.pop()  # Removes the last customer (LIFO)
            print(f"Popped Customer: {customer[0]}, Amount: {customer[1]}")

# Function to display customers in the stack WINNER
def DISPLAY(WINNER):
    if not WINNER:  
        print("Stack is empty!")
    else:
        print("Customers in stack (Last added displayed first):")
        for customer in reversed(WINNER):  # Display in LIFO order
            print(f"{customer[0]}, Amount: {customer[1]}")

# Main menu
WINNER = []  # Stack to store customers with amount >= 5000
CUSTOMERS = []  # List to store all customer details

while True:
    print("\nMenu:")
    print("1. Create Customer List")
    print("2. Push Customers to Stack")
    print("3. Pop Customers from Stack")
    print("4. Display Stack")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        CUSTOMERS = CREATE()
    elif choice == "2":
        WINNER = PUSH(CUSTOMERS, WINNER)
    elif choice == "3":
        POP(WINNER)
    elif choice == "4":
        DISPLAY(WINNER)
    elif choice == "5":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
