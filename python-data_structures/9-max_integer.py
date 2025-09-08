#!/usr/bin/python3

def max_integer(my_list=[]):
    longeur = len(my_list)
    if longeur == 0:
        return None
    index = 1
    valeur = my_list[0]

    while index < longeur:
        if my_list[index] > valeur:
            valeur = my_list[index]
        index += 1
    return valeur
