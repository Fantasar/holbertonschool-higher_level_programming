#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if length > 0:
        new_tuple = (length, first)
    else:
        return None
    
    return new_tuple
