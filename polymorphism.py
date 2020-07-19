"""This Class is to explain the polymorphism"""


class Person:
    """Person class"""

    def __init__(self, name):
        self.name = name

    def advance(self):
        """Method advance"""
        print("I'm walking")


class Cyclist(Person):
    """Cyclist class"""

    def __init__(self, name):
        super().__init__(name)

    def advance(self):
        print("I'm in my bicycle")


def main():
    """Main method"""

    persona = Person('David')
    persona.advance()

    cyclist = Cyclist('Daniel')
    cyclist.advance()


if __name__ == '__main__':
    main()
