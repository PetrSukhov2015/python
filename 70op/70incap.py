'''
Инкапсуляция — это механизм, который объединяет данные и методы, работающие с этими данными, в одном объекте,
и ограничивает доступ к данным извне.
В Python инкапсуляция реализуется с помощью модификаторов доступа: public, protected и private.
'''
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner  # public атрибут
        self._balance = balance  # protected атрибут (условно приватный)
        self.__pin = "1234"  # private атрибут (полностью приватный)

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_balance(self) -> float:
        return self._balance

    def __display_pin(self):  # private метод
        print(f"PIN: {self.__pin}")

# Использование
account = BankAccount("Иван", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Вывод: 1300

# Попытка доступа к приватным атрибутам и методам
print(account._balance)  # Работает, но не рекомендуется (protected)
# print(account.__pin)  # Ошибка! (private)
# account.__display_pin()  # Ошибка! (private)