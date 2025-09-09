#!/usr/bin/python3
def common_elements(set_1, set_2):
    identique = set_1.copy()
    identique.intersection_update(set_2)
    return identique
