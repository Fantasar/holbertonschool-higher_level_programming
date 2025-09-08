#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    idx = 0
    longeur = len(my_list)
    while idx < longeur:
        if my_list[idx] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        idx += 1
    return new_list
