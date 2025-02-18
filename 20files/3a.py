# Открываем файл для добавления (если файл не существует, он будет создан)
with open('output.txt', 'a+') as file:
    # Добавляем строку в конец файла
    file.write('\nЭто новая строка.')

    # https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html