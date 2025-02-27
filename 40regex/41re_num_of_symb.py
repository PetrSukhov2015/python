#{n} — ровно n повторений.
#{n, m} — от n до m повторений.
import re
text = "xxy, xyy, xyyyy, xy"
result = re.findall(r"xy{2}", text)  # Ищем "x", затем ровно два "y"
print(result)  # ['xyy']

#Один или более (+), ноль или более (*)
#+ — одно или более повторений.
#* — ноль или более повторений
text = "x, xy, xyy, xyyyy"
result = re.findall(r"xy+", text)  # Ищем "x", затем одно или более "y"
print(result)  # ['xy', 'xyy', 'xyyyy']

#Ноль или одно (?)
#? — ноль или одно повторение.
text = "color, colour"
result = re.findall(r"colou?r", text)  # Ищем "color" или "colour"
print(result)  # ['color', 'colour']

