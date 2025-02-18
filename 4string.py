text = "Hello, World!"
print(type(text))  # <class 'str'>

# Конкатенация строк
greeting = "Hello" + " " + "World"
print(greeting)  # Hello World

# Многострочная строка
multiline_text = """Это
многострочная
строка"""
print(multiline_text)


# Разделение строки по пробелам
text = "Hello World Python"
words = text.split()
print(words)  # ['Hello', 'World', 'Python']

# Разделение по запятой
data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']


# Приведение к верхнему и нижнему регистру
text = "Hello World"
print(text.upper())  # HELLO WORLD
print(text.lower())  # hello world

# Удаление пробелов с начала и конца строки
text = "   Hello World   "
print(text.strip())  # Hello World

