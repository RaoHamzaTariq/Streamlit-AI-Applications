# 00_joke_bot

def joke_bot():
    prompt_message= "What do you want? "
    joke_message = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
    sorry_message = "Sorry I only tell jokes."

    user_input = input("Enter the message: ")
    
    if "joke" in user_input.lower():
        print(joke_message)
    else:
        print(sorry_message)

# joke_bot()


# ====================================================================================
# 01_double_it

def double_it():
    user_input = int(input("Enter a number: "))

    while user_input <100:
        print(user_input)
        user_input = user_input * 2

# double_it()

# ====================================================================================
# 02_liftoff

def liftoff():
    for i in range(10):
        print(10-i)
    print("liftoff")
# liftoff()


# ====================================================================================
# 03_guess_my_number

import random
def guess_my_number():
    real_num = random.randint(0, 99)
    while True:
        try:
            user_number = int(input("Guess a number between 0 and 99: "))
            if user_number == real_num:
                print("Congratulations, you guessed the number correctly!")
                break
            elif user_number < real_num:
                print("Your guess is too low. Try again!")
            else:
                print("Your guess is too high. Try again!")
        except ValueError:
            print("Invalid input. Please enter a number.")
            break

# guess_my_number()


# =================================================================================
# 04_random_numbers

def random_numbers():
    for i in range(10):
        print(random.randint(0, 100))
# random_numbers()
