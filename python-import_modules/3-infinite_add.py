#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    count = len(argv)
    for i in range(1, count):
        total += int(argv[i])
    print("{}".format(total))
