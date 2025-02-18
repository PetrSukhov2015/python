# Открываем файл для чтения
with open('output.txt', 'r+') as lines:
    # Читаем файл построчно
    for line in lines:
        print(line.strip())  # Убираем лишние пробелы и переносы строк

