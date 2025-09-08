#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    a = 0
    longeur = len(my_list)
    while a < longeur:
        print("{}".format(my_list[a]))
        a += 1
