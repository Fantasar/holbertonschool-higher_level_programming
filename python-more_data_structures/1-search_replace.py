#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = my_list.copy()
    for index in range(len(copy_list)):
        if copy_list[index] == search:
            copy_list[index] = replace
    return copy_list
