#!/usr/bin/python3
"""
function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    function that print the full name

    Args:
        first_name (str): the first name
        last_name (str): the last name. Defaults to "".
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
