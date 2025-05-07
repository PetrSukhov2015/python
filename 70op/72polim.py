'''Полиморфизм позволяет использовать объекты разных классов через единый интерфейс.
Это означает, что методы с одинаковым именем могут работать по-разному в зависимости от класса объекта.'''
class Bird:
    def fly(self):
        return "Птица летит"

class Airplane:
    def fly(self):
        return "Самолет летит"

def let_it_fly(flying_object):
    print(flying_object.fly())

# Использование
bird = Bird()
airplane = Airplane()

let_it_fly(bird)  # Вывод: Птица летит
let_it_fly(airplane)  # Вывод: Самолет летит