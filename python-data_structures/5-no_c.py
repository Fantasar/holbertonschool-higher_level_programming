#!/usr/bin/python3

def no_c(my_string):
    copy_my_string = my_string.translate(str.maketrans("", "", "cC"))
    return copy_my_string
