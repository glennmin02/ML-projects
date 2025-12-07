questions = ("How many continents are there on Earth?",
            "Which of the following is the largest planet in our solar system?",
            "What is the chemical symbol for water?",
            "Who wrote 'Romeo and Juliet'?",
            "What is the capital city of France?")

options = (("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
           ("A. H2O", "B. CO2", "C. O2", "D. NaCl"),
           ("A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"),
           ("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"))

answer = ("C", "B", "A", "C", "C")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answer[question_number]:
        score += 1
        print(f"Correct!")
    else:
        print(f"Incorrect!")
        print(f"{answer[question_number]} is the correct answer.")
    question_number += 1


print("-------------------------")
print("Quiz Completed!")
print(f"Your final score is: {score}")
print(f"answers: ", end="")
for ans in answer:
    print(ans, end=" ")
print()
print(f"guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
