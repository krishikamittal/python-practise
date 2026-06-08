#Program: Demonstration of quiz using Python Operations
# Topic: Dictionaries and Loops

questions = {
    "What is the capital of India?": "Delhi",
    "Which language is used for AI?": "Python",
    "How many days are there in a week?": "7"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")

    if user_answer.lower() == answer.lower():
        score += 1

print("\nFinal Score:", score)
print("Out of", len(questions))
