# 01_add_many_number

list_of_numbers = [1,2,3,4,5]
def add_many_number(list):
    return sum(list)

# print(add_many_number(list_of_numbers))


# ===========================================================
# 02_double_list

def double_list(list):
    return [i*2 for i in list]

# print(double_list([1,2,3,4,5]))

# ==============================================================
# 04_flowing_with_data_structures

def flowing_with_data_structures():
    list1=[]
    name = "Hamza"
    for i in range(3):
        list1.append(name)
    print(list1)

# flowing_with_data_structures()


# ==============================================================
# 05_get_first_element

def get_first_element(list):
    print(list[0])
# get_first_element([1,2,3,4,5,6])


# ==============================================================
# 05_get_last_element

def get_last_element(list):
    print(list[-1])
# get_last_element([1,2,3,4,5,6])


# ==============================================================
# 07_get_list   

def get_list():
    list = []
    while True:
        user_input = input("Enter the value: ")
        if user_input == "":
            print(list)
            break
        else:
            list.append(user_input)
# get_list()

# ==============================================================
# 08_shorten

max_length = 3
def shorten_and_print(lst):
    """Removes elements from the end of lst until it reaches MAX_LENGTH and prints them."""
    while len(lst) > max_length:
        print(lst.pop())
    print("Shortened list:", lst)

# Example usage:
my_list = input("Enter a list of items separated by spaces: ").split()
shorten_and_print(my_list)