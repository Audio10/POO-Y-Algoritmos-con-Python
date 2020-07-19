"""This class is to explain the inheritance"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """Method that returns the area of a figure"""
        return self.height * self.base


class Square(Rectangle):
    """Squere class"""

    def __init__(self, side):
        super().__init__(side, side)


if __name__ == '__main__':
    rectangle = Rectangle(base=3, height=4)
    print(rectangle.area())

    square = Square(side=4)
    print(square.area())
