import threading
import time

# Функция, которая будет выполняться в первом потоке
def print_numbers():
    for i in range(5):
        print(f"Число: {i}")
        time.sleep(1)  # Имитация долгой операции

# Функция, которая будет выполняться во втором потоке
def print_letters():
    for letter in "ABCDE":
        print(f"Буква: {letter}")
        time.sleep(1)  # Имитация долгой операции

# Создание потоков
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Запуск потоков
thread1.start()
thread2.start()

# Ожидание завершения потоков
thread1.join()
thread2.join()

print("Все потоки завершены!")