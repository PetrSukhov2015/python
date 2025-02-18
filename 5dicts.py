# Создание списка
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # <class 'list'>

# Доступ к элементам
print(fruits[0])  # apple

# Добавление элемента
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# Удаление элемента
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'orange']





# Создание словаря
person = {"name": "Alice", "age": 25, "city": "New York"}
print(type(person))  # <class 'dict'>

# Доступ к значению по ключу
print(person["name"])  # Alice

# Добавление новой пары ключ-значение
person["email"] = "alice@example.com"
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}

# Удаление элемента
del person["age"]
print(person)  # {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}



