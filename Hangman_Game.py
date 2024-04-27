import random

words = ["python", "hangman", "computer", "programming", "game"]
chosen_word = random.choice(words)
guessed_letters = set()
max_attempts = 6
attempts = 0

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def check_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single letter.")


def display_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     
           |     
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |     
           |     
           |     
           -
        """
    ]
    return stages[attempts]


print("Welcome to Hangman!")

while attempts < max_attempts:
    print("\n" + display_hangman(attempts))
    print("Word: ", display_word(chosen_word, guessed_letters))
    guess = get_guess()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess not in chosen_word:
        attempts += 1
        print("Incorrect guess. Attempts left:", max_attempts - attempts)
    else:
        print("Correct guess!")

    if check_win(chosen_word, guessed_letters):
        print("Congratulations! You've guessed the word:", chosen_word)
        break

else:
    print("\n" + display_hangman(attempts))
    print("Out of attempts! The word was:", chosen_word)
