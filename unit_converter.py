#Program: Demonstration of unit converter program using Python Operations

print("1. KM to M")
print("2. KG to G")
print("3. Celsius to Fahrenheit")

choice = int(input("Enter choice: "))

if choice == 1:
    km = float(input("Enter KM: "))
    print("Meters:", km * 1000)

elif choice == 2:
    kg = float(input("Enter KG: "))
    print("Grams:", kg * 1000)

elif choice == 3:
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)
