# Пример программы
a=5
def process_data(data):
    # Разделяем строку по запятым
    items = data.split(",")

    # Создаем словарь для подсчета элементов
    count_dict = {}

    # Перебираем элементы
    for item in items:
        item = item.strip().lower()  # Убираем пробелы и приводим к нижнему регистру
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    # Выводим результат
    for key, value in count_dict.items():
        print(f"{key}: {value}")


# Входные данные
input_data = "apple, banana, apple, orange, banana, apple"
process_data(input_data)