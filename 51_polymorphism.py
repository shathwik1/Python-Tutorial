# Polymorphism = Greek word that means to "have more forms or faces"
#                Poly = Many
#                Morphe = Form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


# circle = Circle()
# square = Square()

shapes = [Circle(2), Square(6), Triangle(6, 7), Pizza("pepperoni", 12)]
for shape in shapes:
    print(f"{shape.area()}cm^2")
