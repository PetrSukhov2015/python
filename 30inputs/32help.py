import sys

def show_help():
    print("Использование: python script.py [опции]")
    print("Опции:")
    print("  --help  Показать эту справку")
    print("  --name  Указать имя")

# Обработка аргументов
if "--help" in sys.argv:
    show_help()
elif "--name" in sys.argv:
    name_index = sys.argv.index("--name") + 1
    my_val=len(sys.argv)
    if name_index < len(sys.argv):
        print("Привет,", sys.argv[name_index])
    else:
        print("Ошибка: Не указано имя после --name")
else:
    print("Используйте --help для справки.")