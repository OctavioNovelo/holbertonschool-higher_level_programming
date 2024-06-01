#!/usr/bin/python3
"""Creates class Square with private instance attribute size"""


class Square:
     """defines class and
     instantiates private instance attribute size with validation."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
