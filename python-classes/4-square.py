#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        self.size = size


    def area(self):
        """Calculate the area of the square.

        Returns:
               int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
         """Get the size of the square.
        
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Initialize a new Square.                                                                                                                                                  
                                                                                                                                                                                     
        Args:                                                                                                                                                                        
            size (int): The size of the new square. It must be a non-negative integer.                                                                                               
                                                                                                                                                                                     
        Raises:                                                                                                                                                                      
            TypeError: If size is not an integer.                                                                                                                                    
            ValueError: If size is less than 0.                                                                                                                                      
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
