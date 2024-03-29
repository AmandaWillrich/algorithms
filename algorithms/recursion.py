# DIVIDE AND CONQUER + RECURSION

# Find the base case (the simplest one);
# Divide or diminish the problem until it becomes the base case.


# Sum the values of an array using recursion
def sum_numbers(array, sum=0):
    if len(array) == 0:
        return sum

    sum += array.pop(0)
    return sum_numbers(array, sum)


def sum_numbers_alternative(array):
    if array == []:
        return 0
    return array[0] + sum_numbers_alternative(array[1:])


###########################################################
# Write a recursive function that counts the amount of items in an array
def sum_number_of_items(array, amount_of_items=0):
    if len(array) == 0:
        return amount_of_items

    amount_of_items += 1
    return sum_number_of_items(array[0:-1], amount_of_items)


def sum_number_of_items_alternative(array):
    if array == []:
        return 0
    return 1 + sum_number_of_items_alternative(array[1:])


###########################################################
# Find the highest value of a list
def find_highest_value(array, highest_value=0):
    if len(array) == 0:
        return highest_value
    curr_highest_value = highest_value if highest_value > array[-1] \
        else array[-1]
    return find_highest_value(array[0:-1], curr_highest_value)


def find_highest_value_alternative(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = find_highest_value_alternative(array[1:])
    return array[0] if array[0] > sub_max else sub_max
