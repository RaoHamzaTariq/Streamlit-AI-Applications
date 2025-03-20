import random

def computer_guesses():
    low = 1
    high = 100
    attempts = 0
    feedback = ""

    print(f"Think of a number between {low} and {high}. The computer will guess it!")

    while feedback != "c":
        guess = random.randint(low, high)
        print(f"Is it {guess}? (h for too high, l for too low, c for correct)")
        feedback = input().lower()
        attempts += 1

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback != "c":
            print("Invalid input! Please enter 'h', 'l', or 'c'.")

    print(f"Computer guessed your number in {attempts} attempts!")

computer_guesses()
