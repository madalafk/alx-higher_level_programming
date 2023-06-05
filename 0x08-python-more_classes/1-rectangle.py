#!/usr/bin/python3
""" This Empty class Rectangle defines a rectangle
"""


class Rectangle:
    """ Class rectangle"""
    def __init__(self, width=0,#!/usr/bin/python3
""" an  Empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ Class rectangle"""
    def __init__(self, width=0, height=0):
        """class allows for creating instances with optional width and height values"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
 height=0):
        """ Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

