#Program: Demonstration of movie ticket booking using Python Operations
#Topic: Functions and Conditional Statements
movies = {
    "Avengers": 250,
    "Batman": 200,
    "Jawan": 300
}

print("Available Movies:")

for movie in movies:
    print(movie)

movie_name = input("Choose movie: ")
tickets = int(input("Number of tickets: "))

total = movies[movie_name] * tickets

print("Total Cost:", total)
