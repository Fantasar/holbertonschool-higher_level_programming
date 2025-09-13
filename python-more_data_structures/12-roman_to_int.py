#!/usr/bin/python3
def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    new_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    values = 0
    idx = 0

    while idx < len(roman_string):
        prev = new_dict.get(roman_string[idx], 0)

        if idx + 1 < len(roman_string):
            next_value = new_dict.get(roman_string[idx + 1], 0)

            if prev < next_value:
                values += next_value - prev
                idx += 2
                continue

        values += prev
        idx += 1

    return values
