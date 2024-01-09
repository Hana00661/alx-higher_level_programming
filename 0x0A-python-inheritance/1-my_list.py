#!/usr/bin/python3
"""the print_sorted function"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """that prints the list (sorted)"""
        print(sorted(self))
