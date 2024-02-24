# Binary Search only works if the list is ordered;
import math

number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
string_array = ['Amanda', 'Bianca', 'Cristiane', 'Dennis', 'Felipe', 'Rafael', 'Kennedy', 'Zayn']


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = math.floor((low + high) / 2)
        guess = list[middle]

        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1

    return None


print(binary_search(string_array, 'Cristiane'))
