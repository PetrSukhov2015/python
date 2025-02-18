# Открываем файл для чтения
with open('output.txt', 'r+') as file:
    # Читаем все содержимое файла
    content = file.read()
    print(content)