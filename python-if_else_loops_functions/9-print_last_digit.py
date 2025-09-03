#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        values = (number % 10)
    else:
        values = (number * -1) % 10
    print("{}".format(values), end="")
    return (values)
