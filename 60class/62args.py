def my_method(a, b):
    print(a, b)

my_method(1, 2)  # Вывод: 1 2


def my_method(a, b):
    print(a, b)

my_method(a=1, b=2)  # Вывод: 1 2


def my_method(*args):
    for arg in args:
        print(arg)

my_method(1, 2, 3)  # Вывод: 1 2 3


def my_method(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_method(a=1, b=2, c=3)  # Вывод: a: 1 b: 2 c: 3


