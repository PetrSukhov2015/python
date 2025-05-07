from concurrent.futures import ThreadPoolExecutor
import time

# Метод, который будет выполняться в потоках
def task(name):
    print(f"Задача {name} начата")
    time.sleep(2)  # Имитация долгой операции
    print(f"Задача {name} завершена")
    return f"Результат задачи {name}"

# Создание пула потоков
with ThreadPoolExecutor(max_workers=3) as executor:
    # Запуск задач с передачей метода и аргументов
    futures = [executor.submit(task, f"Поток {i}") for i in range(5)]

    # Получение результатов выполнения задач
    for future in futures:
        print(future.result())

print("Все задачи завершены!")