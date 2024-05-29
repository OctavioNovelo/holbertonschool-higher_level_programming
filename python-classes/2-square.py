#!/usr/bin/python3
"""Write a class Square that defines a Square"""


class Square:
    """Represent a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    
    def __init__(self, size=0):
         """Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
        """
         
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        self.__size = size

        try:
            integer = Square()
        except TypeError as e:
            print(e)
            
