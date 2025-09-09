#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for clé in sorted(a_dictionary):
        print("{}: {}".format(clé, a_dictionary[clé]))
