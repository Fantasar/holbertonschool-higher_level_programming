#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    tuple_b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    if len(tuple_a) > 2:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return new_tuple
    elif len(tuple_a) < 2:
        new_tuple = (new_tuple_a[0] + tuple_b[0], new_tuple_a[1] + tuple_b[1])
        return new_tuple
    else:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return new_tuple
