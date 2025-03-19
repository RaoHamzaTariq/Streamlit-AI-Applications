# 00_averages

def averages(num1,num2):
    return (num1 + num2) / 2
# print(averages(2,3))

# =====================================================================
# 01_chaotic_counting
import random

DONE_LIKELIHOOD = 0.3

def chaotic_counting():
    for i in range(1, 11):
        if random.random() < DONE_LIKELIHOOD:
            print("I'm done.")
            return
        print(i)
    print("I'm done.")

# chaotic_counting()

# =====================================================================
# 02_count_even

def count_even(list1):
    even_counter=0
    for i in list1:
        if i % 2 == 0:
            even_counter+=1
    print(f"Total numbers of even is {even_counter}")

# count_even([1,2,43,5,2,5,6])

# =====================================================================
# 04_double

def double(num):
    return num * 2

# print(double(3))

# ======================================================================
# 05_get_name

def get_name():
    return "Sophia"
def get_name_main():
    name = get_name() 
    print("Howdy", name, "! 🤠")
# get_name_main()


# ======================================================================
# 06_is_odd
def is_odd(num):
    return num % 2 != 0
# print(is_odd(3))

# =========================================================================
# 07_print_divisors
def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def print_divisors_main():
    num = int(input("Enter a number: "))
    print_divisors(num)
# print_divisors_main()


# =========================================================================
# 08_print_multiple
def print_multiple(num: int, times: int):
    for i in range(times):
        print(num)
def print_multiple_main():
    num = int(input("Enter a number: "))
    times = int(input("Enter how many times to print: "))
    print_multiple(num, times)
# print_multiple_main()


# =========================================================================
# 09_sentence_generator
def make_and_print_sentence():
    word = input("Please type a noun, verb, or adjective: ")
    try:
        part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
        if part_of_speech == 0:
            print(f"I am excited to add this {word} to my vast collection of them!")
        elif part_of_speech == 1:
            print(f"It's so nice outside today it makes me want to {word}!")
        elif part_of_speech == 2:
            print(f"Looking out my window, the sky is big and {word}!")
        else:
            print("Invalid part of speech. Please enter 0, 1, or 2.")
    except ValueError:
        print("Invalid input. Please enter an integer for the part of speech.")

# make_and_print_sentence()


# =========================================================================
# 10_print_ones_digit
def print_ones_digit():
    num = int(input("Enter a number: "))
    print(f"The ones digit is {num % 10}")

# print_ones_digit()

