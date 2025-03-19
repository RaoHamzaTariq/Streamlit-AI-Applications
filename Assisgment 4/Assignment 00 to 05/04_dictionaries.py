# 00_count_nums

def count_nums():
    counts = {}
    while True:
        try:
            num = int(input("Enter a number: "))
            counts[num] = counts.get(num, 0) + 1
        except ValueError:
            break

    for num, count in counts.items():
        print(f"{num} appears {count} times.")

# count_nums()


# ========================================================
# 01_phonebook

def phonebook():
    phonebooks= {}

    while True:
        phone_num = input("Enter the Phone Number: ")
        name = input("Enter the Name: ")
        if phone_num and name != "":
            phonebooks[phone_num] = name
        elif phone_num == "":
            print("Phone Number is required")
        elif name == "":
            print("Name is required")
        else:
            print("Both Phone Number and Name are required")
        
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != "yes":
            break
    
    for phone_num, name in phonebooks.items():
        print(f"{name} : {phone_num}")

# phonebook()


# =======================================================================
# 02_pop_up_shop

def pop_up_shop():
    fruit_prices = {"apple": 1.5,"durian": 50,"jackfruit": 20,"kiwi": 2,"rambutan": 3,"mango": 8,
    }
    total_cost = 0

    for fruit, price in fruit_prices.items():
        try:
            quantity = int(input(f"How many ({fruit}) do you want?: "))
            total_cost += quantity * price
        except ValueError:
            print("Invalid input. Quantity must be a number. Skipping this fruit.")

    print(f"Your total is ${total_cost}")

# pop_up_shop()


# ======================================================================
# 03_powerful_passwords

import hashlib

def hashlib_login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email or password != "":
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
    else:
        print("Email and password are required")


    stored_logins = {
    "user1@example.com": hashlib.sha256("password123".encode()).hexdigest(),
    "user2@example.com": hashlib.sha256("securepass".encode()).hexdigest(),
    }

    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    isCorrect =  email in stored_logins and stored_logins[email] == hash_password(password)
    print(f"The user {email} is {isCorrect}")

# print(hashlib_login())


        
        
    


