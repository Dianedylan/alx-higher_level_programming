#!/usr/bin/python3
"""
10-square.py
class Square
imports and inherits class Rectangle
which inherits class BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle
    """
    def __init__(self, size):
        """
        size must be validated and is privately set here
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
