#Program: Demonstration of cafe bill generator using Python Operations
# topic : Functions and Conditional Statements

menu = {
    "Pizza": 200,
    "Burger": 120,
    "Pasta": 180,
    "Cold Drink": 50
}

total_bill = 0

print("------ MENU ------")
for item, price in menu.items():
    print(item, "- ₹", price)

while True:
    item = input("\nEnter item name (or 'done' to finish): ")

    if item.lower() == "done":
        break

    if item in menu:
        total_bill += menu[item]
        print(item, "added.")
    else:
        print("Item not found.")

print("\n------ BILL ------")
print("Total Amount = ₹", total_bill)
