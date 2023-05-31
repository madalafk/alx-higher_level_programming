#!/usr/bin/python3

"""
This module defines the Square class, which represents a square.
"""

class Square:
    """
    Square class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square with specified size.

        Args:
            size (int): size of square with Defaults to 0.
        """

        self.size = size

    @property
    def size(self):
        """
        int: size square (private attribute).

        Returns:
            int: private size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets value of size attribute. == int

        Args:
            value (int): size of square.

        Raises:
            TypeError: If value == int.
            ValueError: If value < 0.
        """
        if type(value) is not int:
            raise TypeError('size == int')
        elif value < 0:
            raise ValueError('size ==  >= 0')
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of a square.

        Returns:
            int: Area of square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """
        < comparison operator for squares.

        Args:
            other (Square): Another Square object to be compared with.

        Returns:
            bool: True == size of current square < other square's size,else False
        """
        return self.size < other.size

    def __le__(self, other):
        """
        <= comparison operator for squares.

        Args:
            other (Square): Another Square object to be  compared with.

        Returns:
            bool: True == current square <== other square's size,else False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """
        Equality comparison operator for squares.

        Args:
            other (Square): Another Square object to be  compared with.

        Returns:
            bool: True == size of current square == other square's size,else  False
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        != comparison operator for squares.

        Args:
            other (Square): Another Square object to be compared with.

        Returns:
            bool: True == current square != other square's size,else  False
        """
        return self.size != other.size

    def __ge__(self, other):
        """
        >= comparison operator for squares.

        Args:
            other (Square): Another Square object to be compared with.

        Returns:
            bool: True == current square >= other square's size, else false
        """
        return self.size >= other.size
