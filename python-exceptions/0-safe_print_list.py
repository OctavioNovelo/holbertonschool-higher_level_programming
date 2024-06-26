#!/usr/bin/python3
"""Prints x elements."""


def safe_print_list(my_list=[], x=0):
    """Print elements."""
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        print()
        return count
    print()
    return count
