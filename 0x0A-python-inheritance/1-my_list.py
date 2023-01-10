#!/usr/bin/python3
"""
   1-my_list module
   Class MyList that inherits from list that contain \
   Public instance method: def print_sorted(self): that \
   prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """Print the list, but sorted (ascending sort)"""
        print(sorted(self))
