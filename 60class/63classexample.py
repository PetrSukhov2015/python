class MyClass:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def display_args(self):
        print("Позиционные аргументы:", self.args)

    def display_kwargs(self):
        print("Именованные аргументы:", self.kwargs)

    @staticmethod
    def static_method():
        print("Это статический метод")

    def dynamic_method(self):
        print("Это динамический метод")

# Создание объекта с передачей аргументов
obj = MyClass(1, 2, 3, a=4, b=5)

# Вызов методов
obj.display_args()  # Вывод: Позиционные аргументы: (1, 2, 3)
obj.display_kwargs()  # Вывод: Именованные аргументы: {'a': 4, 'b': 5}
obj.static_method()  # Вывод: Это статический метод
obj.dynamic_method()  # Вывод: Это динамический метод