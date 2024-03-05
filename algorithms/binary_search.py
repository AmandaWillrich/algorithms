# Binary Search only works if the array is ordered (On)

def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = int((low + high) / 2)
        guess = array[middle]

        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1

    return None
