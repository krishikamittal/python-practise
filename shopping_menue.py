#Program: Demonstration of shopping cart using Python Operations
#Topic: menue based program

cart = []

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        cart.append(item)

    elif choice == 2:
        item = input("Enter item to remove: ")

        if item in cart:
            cart.remove(item)

    elif choice == 3:
        print("\nItems in Cart:")
        for item in cart:
            print(item)

    elif choice == 4:
        break
