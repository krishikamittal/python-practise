#Program: Demonstration of movie reccomandation using Python Operations
#Topic: Functions and Conditional Statements

movies = {
    "Action": ["John Wick", "Avengers", "Mission Impossible"],
    "Comedy": ["3 Idiots", "Golmaal", "Bhool Bhulaiyaa"],
    "Horror": ["Conjuring", "Annabelle", "Insidious"]
}

print("Choose a Genre:")
print("1. Action")
print("2. Comedy")
print("3. Horror")

choice = input("Enter choice: ")

if choice == "1":
    genre = "Action"
elif choice == "2":
    genre = "Comedy"
elif choice == "3":
    genre = "Horror"
else:
    print("Invalid Choice")
    exit()

print("\nRecommended Movies:")

for movie in movies[genre]:
    print("-", movie)
