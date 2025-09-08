#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    longeur = len(my_list)
    if idx < 0:
        return None
    elif idx > longeur:
        return None
    else:
        my_list[idx] = element
        return my_list
