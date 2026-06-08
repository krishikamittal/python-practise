#Program: Demonstration of exam result analyser using Python Operations
#Topic: Functions and Conditional Statements,Lists

marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 40:
        passed += 1

print("\n----- Result Analysis -----")
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Students Passed:", passed)
print("Students Failed:", n - passed)
