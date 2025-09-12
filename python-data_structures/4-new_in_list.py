#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    longeur = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= longeur:
        return my_list.copy()
    else:
        copy_my_list = my_list.copy()
        copy_my_list[idx] = element
        return copy_my_list
