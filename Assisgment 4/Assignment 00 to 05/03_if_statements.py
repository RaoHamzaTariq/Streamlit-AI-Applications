# 01_print_events

def print_events():
    for i in range(20):
        print(i*2)
# print_events()

# ===========================================================
# 02_international_voting_age

def international_voting_age():
    user_input = int(input("Enter your age: "))
    if user_input >= 16:
        print("You can vote in Peturksbouipo ")
    else:
        print("You can't vote in Peturksbouipo ")

    if user_input >=25 :
        print("You can vote in Stanlau  ")
    else:
        print("You can't vote in Stanlau ")

    if user_input >=48 :
        print("You can vote in Mayengua   ")
    else:
        print("You can't vote in Mayengua ")

# international_voting_age()


# =========================================================
# 03_leap_year

def leap_year():
    year = int(input("Enter a year: "))
    if year % 4==0 and year % 100 == 0 and year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
# leap_year()


# =============================================================
# 04_tall_enough_to_ride


def tall_enough_to_ride():
    MINIMUM_HEIGHT = 50
    while True:
        height_input = input("How tall are you? (Enter nothing to quit) ")
        if not height_input:
            break
        try:
            height = int(height_input)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Invalid input. Please enter a number.")

# tall_enough_to_ride()


# =============================================================
# 05_random_numbers
import random
def random_numbers():
    for i in range(10):
        print(f"{i+1}: {random.randint(1, 100)}")
# random_numbers()