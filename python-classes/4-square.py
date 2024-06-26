#!/usr/bin/python3
"""Define a class Square with private instance attribute size."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Return the area of square."""
        return self.__size ** 2

    @property
    def size(self):
        """Get size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of Square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
