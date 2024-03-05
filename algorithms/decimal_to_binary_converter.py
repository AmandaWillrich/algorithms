# Converts decimal to binary

def convert_to_binary(decimal_number):

    stored_number = decimal_number
    binary_number = ''
    multiplier = _find_starting_multiplier(decimal_number)

    while multiplier > 0:

        if not stored_number and multiplier:
            binary_number = binary_number + '0'
            multiplier = multiplier / 2 if not multiplier == 1 else 0
            continue
        if multiplier > stored_number:
            binary_number = binary_number + '0'
            multiplier = multiplier / 2 if not multiplier == 1 else 0
            continue
        if multiplier <= stored_number:
            stored_number -= multiplier
            binary_number = binary_number + '1'
            multiplier = multiplier / 2 if not multiplier == 1 else 0
            continue
        if stored_number == 0:
            return binary_number

    return binary_number


def _find_starting_multiplier(decimal_number):
    # it starts with 2^1 and it doubles
    # so 1, 2, 4, 8, 16, 32 and so on
    multiplier = 1

    while multiplier < decimal_number:

        if multiplier * 2 > decimal_number:
            break
        multiplier *= 2

    return multiplier
