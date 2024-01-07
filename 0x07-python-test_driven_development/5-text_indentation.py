#!/usr/bin/python3
"""
function text_indentation
"""


def text_indentation(text):
    """
    function that print the text with indentation

    Args:
        text (str): the text to print
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    else:
        i = 0
        for char in text:
            if i == 0:
                if char == " ":
                    continue
                else:
                    i = 1
            if i == 1:
                if char in [".", "?", ":"]:
                    print(char + "\n")
                    i = 0
                else:
                    print(char, end="")
