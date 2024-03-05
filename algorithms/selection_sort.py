# Selection sort orders a list from lowest to highest (Onlogn)


def selection_sort(array):
    ordered_array = []

    for i in range(len(array)):
        lowest_index = search_lowest_index(array)
        ordered_array.append(array.pop(lowest_index))

    return ordered_array


def search_lowest_index(array):
    lowest_value = array[0]
    lowest_index = 0

    for i in range(1, len(array)):
        if array[i] < lowest_value:
            lowest_value = array[i]
            lowest_index = i
    return lowest_index
