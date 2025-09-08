#!/usr/bin/python3

def print_list_integer(my_list=[]):
    a = 0
    longeur = len(my_list)
    while a < longeur:
        print("{:d}".format(my_list[a]))
        a += 1
