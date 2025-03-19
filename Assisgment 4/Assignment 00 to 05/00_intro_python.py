#  01_add_two_numbers

def sum():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1+num2
# print(sum())

# =====================================================

# 02_agreement_bot 

def agreement_bot():
    user_input=input("What's your favourite animal? : ")
    print(f"My favourite animal is {user_input}")
# agreement_bot()

# =====================================================
# 03_fahrenheit_to_celsius

def fahrenheit_to_celsius():
    user_input=int(input("Enter temperature in celsius: "))
    return ((user_input - 32) * 5/9)
# print(fahrenheit_to_celsius())


# =====================================================
# 04_how_old_are_they

def how_old_are_they():
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = anton+chen
    ethan = chen

    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

# how_old_are_they()


# =====================================================
# 05_triangle_perimeter

def triangle_perimeter():
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    print("The perimeter of the triangle is " + str(side1 + side2 + side3))

# triangle_perimeter()


# =====================================================
# 06_square_number

def square_number():
    user_input : int = int(input("Enter numbers to squared: "))
    print(user_input**2)

# square_number()
