#Program: Demonstration of Student Report Card using Python Operations
#Topic: Conditional Statement

name = input("Enter student name: ")

m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

print("\nStudent:", name)
print("Percentage:", percentage)
print("Grade:", grade)
