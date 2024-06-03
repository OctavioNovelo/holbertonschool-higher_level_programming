#!/usr/bin/python3
"""Rectangle."""


class Rectangle:
    """Represent Rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width."""
        return (self.width)

    @width.setter
    def width(self, value):
        """Set width."""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return (self.height)

    @height.setter
    def height(self, value):
        """Set height."""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
