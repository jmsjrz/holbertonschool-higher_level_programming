#!/usr/bin/python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class representing a geometric shape.

    This class serves as a base for all geometric shapes and
    defines two abstract methods that all subclasses must implement.
    """
    @abstractmethod
    def area(self):
        """ Area method """
        pass

    @abstractmethod
    def perimeter(self):
        """ Perimeter method """
        pass


class Circle(Shape):
    """ Circle class that inherit from Shape class"""
    def __init__(self, radius):
        """ Circle class constructor """
        self.radius = abs(radius)

    def area(self):
        """ Circle area method """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """ Circle perimeter method """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """ Rectangle class that inherit from Shape class"""
    def __init__(self, width, height):
        """ Rectangle class constructor """
        self.width = width
        self.height = height

    def area(self):
        """ Rectangle area method """
        return self.width * self.height

    def perimeter(self):
        """ Rectangle perimeter method """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """ Function to print shape area and perimeter """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
