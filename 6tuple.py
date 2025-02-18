# Создание кортежа
person = ("Alice", 30, "New York")

# Доступ к элементам кортежа
print("Имя:", person[0])
print("Возраст:", person[1])
print("Город:", person[2])




tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
tuple3 = (1, 2, 3)

print("tuple1 == tuple2:", tuple1 == tuple2)  # False
print("tuple1 == tuple3:", tuple1 == tuple3)  # True
print("tuple1 < tuple2:", tuple1 < tuple2)    # True




tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Объединение кортежей
combined_tuple = tuple1 + tuple2
print("Объединенный кортеж:", combined_tuple)