'''
Наследование позволяет создавать новый класс на основе существующего. Новый класс (дочерний)
наследует атрибуты и методы родительского класса и может расширять или изменять их.
'''

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        raise NotImplementedError("Дочерние классы должны реализовать этот метод")

class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит Гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит Мяу!"

# Использование
dog = Dog("Бобик")
cat = Cat("Мурка")

print(dog.speak())  # Вывод: Бобик говорит Гав!
print(cat.speak())  # Вывод: Мурка говорит Мяу!