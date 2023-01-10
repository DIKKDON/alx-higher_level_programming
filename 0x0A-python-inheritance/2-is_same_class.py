#!/usr/bin/python3
"""
    2-is_same_class module
    Get if a object is exactly an instance of the \
    specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Function that returns True if the object is\
       exactly an instance of the specified class \
       ; otherwise False"""
    if isinstance(a_class(), type(obj)):
        return True
    return False
