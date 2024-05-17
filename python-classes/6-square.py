#!/usr/bin/python3
"""
6-square.py - This module initializes a class called 'Square' and provides
documentation for various concepts related to object-oriented programming.
"""


class Square:
    """
    The 'Square' class represents a generic square.

    Attributes:
        __size (int): The size of a square.
        __position (tuple): The position of a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a private instance attribute: 'size' and 'position'.

        Args:
            size (int): The size of a square. Defaults to 0.
            position (tuple): The position of a square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or
            position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or
            position contains negative integers.
        """
        self.size = size  # Use the setter to validate the size
        self.position = position  # Use the setter to validate the position

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Check exception type and value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Check exception type and value for position"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Public instance method: def area(self):
        that returns the current square area.
        """
        return self.__size**2

    def my_print(self):
        """
        Public instance method: def my_print(self):
        that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
            return

        # Print the new lines for the y-coordinate of the position
        for i in range(self.__position[1]):
            print()

        # Print the square
        for i in range(self.__size):
            # Print spaces for the x-coordinate of the position
            print(" " * self.__position[0], end="")
            # Print the # characters for the size of the square
            print("#" * self.__size)


"""
This is the end of the code. The 'Square' class provides functionality
to create and manipulate square objects.
It includes methods to calculate the area
of the square and print the square using the '#' character.
The class also includes getter and setter methods for
the 'size' and 'position' attributes.
"""
