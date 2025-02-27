import re

text = "Аня - 20, Боря - 35"

# Обычная группа ()
result = re.findall(r"(\w+) - (\d+)", text)
print(result)  # [('Аня', '20'), ('Боря', '35')]

# Именованные группы (?P<name>...)
match = re.search(r"(?P<name>\w+) - (?P<age>\d+)", text)
if match:
    print("Имя:", match.group("name"))  # Аня
    print("Возраст:", match.group("age"))  # 20
