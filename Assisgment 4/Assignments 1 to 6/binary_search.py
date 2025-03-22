import random
import time

def naive_search(list1,target):
    for i in range(len(list1)):
        if list1[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    length=10000
    sorted_list=set()
    while len(sorted_list)<length:
        sorted_list.add(random.randint(-3*length,3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end =time.time()

    print(f"Naive Search time: {(end - start)/10000} seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end =time.time()

    print(f"Binary Search time: {(end - start)/10000} seconds")