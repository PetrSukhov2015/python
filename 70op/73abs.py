'''
Абстракция позволяет скрыть сложную реализацию и показать только необходимые детали.
В Python абстракция реализуется с помощью абстрактных классов и методов.
'''
from abc import ABC, abstractmethod

class Shape(ABC):  # Абстрактный класс
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Использование
circle = Circle(5)
square = Square(4)

print(f"Площадь круга: {circle.area()}")  # Вывод: Площадь круга: 78.5
print(f"Периметр квадрата: {square.perimeter()}")  # Вывод: Периметр квадрата: 16