# Define questions, options, and correct answers for the quiz
questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("C", "D", "A", "A", "B")  # Correct answers for each question
guesses = []  # Store user's guesses
score = 0  # Initialize the score counter
question_num = 0  # Initialize the question number counter

# Iterate through each question
for question in questions:
    print("----------------------")
    print(question)
    # Display options for the current question
    for option in options[question_num]:
        print(option)

    # Prompt the user to enter their guess and convert to uppercase
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)  # Store the user's guess

    # Check if the guess is correct
    if guess == answers[question_num]:
        score += 1  # Increment score for correct guess
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1  # Move to the next question

# Display quiz results
print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Calculate and display final score as a percentage
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
