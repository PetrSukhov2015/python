#. — соответствует любому символу, кроме новой строки (\n).
# https://docs.python.org/3/library/re.html
# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/
import re

text = "cat, bat, rat, hat"
result = re.findall(r"c.t", text)  # Ищем "c", любой символ, затем "t"
print(result)  # ['cat']


#\d — соответствует любой цифре (эквивалентно [0-9]).

text = "Мой номер телефона: 123-456-7890."
result = re.findall(r"\d+", text)  # Ищем последовательности цифр
print(result)  # ['123', '456', '7890']

#\w — соответствует любой букве (латиница или кириллица), цифре или символу подчёркивания (_).
#[a-zA-Z] — только латинские буквы.
#[а-яА-Я] — только кириллица.
text = "Hello, Привет, 123_"
result = re.findall(r"\w+", text)  # Ищем слова
print(result)  # ['Hello', 'Привет', '123_']
