# 01_dicesimulator
import random
def roll_dice():
    total_slides=6
    dice1 = random.randint(1,total_slides)
    dice2 = random.randint(1,total_slides)
    print(dice1+dice2)

def roll_stimulator():
    roll_dice()
    roll_dice()
# roll_stimulator()

# ======================================
# 02_e=mc2

def einstein_formula():
    m = float(input("Enter the mass in kg:"))
    return m*((3*10**6)**2)
# print(einstein_formula())

# ================================================
# 03_feet_to_inches

def feet_to_inches():
    user_input= float(input("Enter the length in feets: "))
    return user_input * 12

# print(feet_to_inches())


# ==============================================================
# 04_pythagorean_theorem

import math  

def pythagorean_theorem():
    base = float(input("Enter the length of base: "))
    perpendicular = float(input("Enter the length of perpendicular: "))
    return math.sqrt((perpendicular**2) * (base**2))

# print(pythagorean_theorem())


# ==============================================================
# 05_remainder_division

def remainder_division():
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend // divisor  
    remainder: int = dividend % divisor  
    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))
# remainder_division()


# ==================================================
# 06_rolldice
def rolldice():
    total_sides = 6
    dice1= random.randint(1,total_sides)
    dice2= random.randint(1,total_sides)
    total = dice1+dice2

    print(f"Dice 1 : {dice1}")
    print(f"Dice 2 : {dice2}")
    print(f"Total : {total}")

# rolldice()


# ======================================================================
# 06_seconds_in_year

def seconds_in_year():
    seconds_in_year = 60 * 60 * 24 * 365.25
    print(f"There are {seconds_in_year} seconds in a year")

# seconds_in_year()


# =======================================================================
# 07_tiny_mad_lib

def tiny_mad_lib():
    sentence_starting = "Life is filled with sunshines and darknights and every"
    adjective = input("Please enter an adjective: ")
    noun = input("Please enter a noun: ")
    verb = input("Please enter a verb: ")
    print(f"{sentence_starting} {adjective} {noun} {verb}!")

# tiny_mad_lib()

