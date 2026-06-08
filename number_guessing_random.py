#Program: Demonstration of number guessing game using Python Operations
# Topic: Random Module

import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed it.")
        break
