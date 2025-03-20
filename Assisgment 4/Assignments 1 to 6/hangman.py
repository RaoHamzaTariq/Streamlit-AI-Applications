import random

def choose_word():
    """Chooses a random word from a list."""
    words = ["python", "hangman", "programming", "computer", "algorithm", "developer", "software", "keyboard"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    """Plays the hangman game."""
    word = choose_word()
    guessed_letters = []
    attempts = 6  

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You guessed the word!")
            break

    if attempts == 0:
        print(f"You ran out of attempts. The word was: {word}")

if __name__ == "__main__":
    hangman()