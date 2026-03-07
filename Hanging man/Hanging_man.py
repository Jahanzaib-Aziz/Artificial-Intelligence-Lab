import random

hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]
word_list = ["python", "programming", "computer", "science", "hangman"]

word = random.choice(word_list)
guessed_letters = []
attempts = len(hangman_stages) - 1

print(" Welcome to Hangman Game!")

while attempts > 0:
    print(hangman_stages[len(hangman_stages) - 1 - attempts])

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if "_" not in display_word:
        print(" Congratulations! You guessed the word correctly.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print(" Wrong guess!")

    print(f"Attempts left: {attempts}")

if attempts == 0:
    print(hangman_stages[-1])
    print(" Game Over! The word was:", word)