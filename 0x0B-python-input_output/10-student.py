#!/usr/bin/python3
"""This module contains Student
that defines a student by:
"""


class Student:
    """This class defines a student"""
    def __init__(self, first_name, last_name, age):
        """Arguments:
            firs_name - first name of the student
            last_name - last name of the student
            age - age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves a dictionary representation of a Student instance
        """
        new_dict = {}
        if type(attrs) is list:
            if all(type(i) is str for i in attrs):
                for i in attrs:
                    if hasattr(self, i):
                        new_dict[i] = getattr(self, i)
                return new_dict

        return self.
