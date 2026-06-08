#Program: Demonstration of Password Strength Checker using Python Operations

password = input("Enter password: ")

strength = 0

if len(password) >= 8:
    strength += 1

if any(char.isdigit() for char in password):
    strength += 1

if any(char.isupper() for char in password):
    strength += 1

if any(not char.isalnum() for char in password):
    strength += 1

print("Strength Score:", strength, "/4")
