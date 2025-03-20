def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(len(fruit_list))

    fruit_list.append('mango')
    print(fruit_list)

    my_list = [10, "hello", 3.14, "world", 5]

    def access_element(lst, index):
        if 0 <= index < len(lst):
            return lst[index]
        else:
            return "Index out of range."

    def modify_element(lst, index, new_value):
        if 0 <= index < len(lst):
            lst[index] = new_value
            return "Element modified."
        else:
            return "Index out of range."

    def slice_list(lst, start, end):
        if 0 <= start <= end <= len(lst):
            return lst[start:end]
        else:
            return "Indices out of range."

    while True:
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            index = int(input("Enter index: "))
            result = access_element(my_list, index)
            print(result)
            print("Current List: ", my_list)

        elif choice == "2":
            index = int(input("Enter index: "))
            new_value = input("Enter new value: ")
            result = modify_element(my_list, index, new_value)
            print(result)
            print("Current List: ", my_list)

        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print(result)
            print("Current List: ", my_list)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()