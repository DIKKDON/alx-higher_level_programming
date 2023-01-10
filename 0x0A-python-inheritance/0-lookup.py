#!/usr/bin/python3
"""
    0-lookup module
    Search available attributes and methods of an object
"""


def lookup(obj):
    """Function that returns the list of available attributes \
       and methods of an object"""
    return [method_name for method_name in dir(obj)]
