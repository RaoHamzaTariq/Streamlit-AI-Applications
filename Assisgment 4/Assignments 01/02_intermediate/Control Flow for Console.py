import random

NUM_ROUNDS = 5  

def play_high_low():
    """Plays the High-Low game with the user."""

    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    player_score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")

        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {player_number}")

        while True:  
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
            if guess in ("higher", "lower"):
                break
            else:
                print("Please enter either higher or lower:")

        if (guess == "higher" and player_number > computer_number) or \
           (guess == "lower" and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            player_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {player_score}")

    print("\nThanks for playing!")

    if player_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif player_score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

play_high_low()