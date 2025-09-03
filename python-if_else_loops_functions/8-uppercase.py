#!/usr/bin/python3
def uppercase(str):
    for count in str:
        val = ord(count)
        if 'a' <= count <= 'z':
            valeur = val - 32
            print("{}".format(chr(valeur)), end="")
        else:
            print("{}".format(count), end="")
    print()
