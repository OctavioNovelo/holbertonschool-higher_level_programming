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
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Retur the rectangle perimeter."""
        if height == 0 or width == 0:
            self.__perimeter = 0
            return self.__perimeter
        else:
            self.__perimeter = (self.__width * 2) + (self.__height * 2)
        return self.__perimeter
