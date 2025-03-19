# 00_guess_my_number
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

# ===============================================================================
# 01_fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# print(fibonacci(10))

# ===============================================================================
# 02_print_events

def print_events():
    for i in range(20):
        print(i*2)
# print_events()


# =================================================================================
# 03_wholesome_machine
def wholesome_machine():
    affirmation = "I am capable of doing anything I put my mind to."

    while True:
        user_input = input(f"Please type the following affirmation: {affirmation} ")
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation.")
# wholesome_machine()

# ====================================================================================
# 04_liftoff

def liftoff():
    for i in range(10):
        print(10-i)
    print("liftoff")
# liftoff()


# ====================================================================================
# 05_double_it
def double_it():
    num = int(input("Enter a number: "))
    while num < 100:
        print(num)
        num *= 2
    
# double_it()
