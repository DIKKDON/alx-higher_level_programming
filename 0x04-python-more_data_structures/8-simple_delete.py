#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not key or key not in a_dictionary:
        return a_dictionary
    a_dictionary.pop(key)
    return a_dictionary 
