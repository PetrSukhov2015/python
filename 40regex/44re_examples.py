import re
text = "Пишите на email@example.com или support@domain.org."
result = re.findall(r"[\w\.-]+@[\w\.-]+", text)  # Ищем email-адреса
print(result)  # ['email@example.com', 'support@domain.org']

text = "Цена: 100$, цена: 200$"
result = re.sub(r"\d+\$", "XXX$", text)  # Заменяем все цены на "XXX$"
print(result)  # Цена: XXX$, цена: XXX$

def validate_phone(number):
    pattern = r"^\+7 \d{3} \d{3}-\d{2}-\d{2}$"  # Формат: +7 999 999-99-99
    return bool(re.match(pattern, number))

def validate_phone2(number):
    pattern = r"^\+7 \d{3} \d{3}-\d{2}-\d{2}$"  # Формат: +7 999 999-99-99
    result = re.match(pattern, number)
    if None != result:
        return True
    else:
        return False


print(validate_phone2("+7 999 123-45-67"))  # True
print(validate_phone2("8 999 123-45-67"))   # False

a=5
a+=1
print(a)


