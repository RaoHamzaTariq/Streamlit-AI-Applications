# 00_choosing_returns

def choosing_returns():
    age = int(input("How old is this person?: "))
    if age >= 18:
        print(True)
    else:
        print(False)

# choosing_returns()


# =====================================================================
# 01_greetings

def greetings(name):
    print(f"Greetings {name}!")

def greetings_main():
    name = input("What's your name? ")
    greetings(name)

greetings_main()


# =====================================================================
# 02_in_range

def in_range(n,low,high):
    if low <= n <= high:
        return True
    else:
        return False

# print(in_range(2,23,54))


# =====================================================================
# 03_in_stock

def in_stock(fruit):
    """Returns the number of a given fruit in Sophia's inventory."""
    inventory = {
        "apple": 50,
        "banana": 200,
        "pear": 1000,
        "orange": 75,
    }
    return inventory.get(fruit, 0)

def in_stock_main():
    """Gets fruit input and prints stock information."""
    fruit = input("Enter a fruit: ")
    stock = in_stock(fruit)

    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

in_stock_main()

# =========================================================================================
# 04_multiple_returns

def multiple_returns():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email
    

def multiple_returns():
    """Gets user data and prints it."""
    user_data = multiple_returns()
    print(f"Received the following user data: {user_data}")

# multiple_returns()

# ===========================================================================
# 05_subtract_7

def subtract_7(num):
    return num - 7

def subtract_7_main():
    num = int(input("Enter a number: "))
    result = subtract_7(num)
    print(f"{num} - 7 = {result}")

# subtract_7_main()