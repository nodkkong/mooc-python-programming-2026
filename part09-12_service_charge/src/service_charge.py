# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name: str, account_number: str, balance: float):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    def __service_charge(self):
        if self.__balance > 0:
            self.__balance *= 0.99

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()

    def withdraw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__service_charge()

    @property
    def balance(self):
        return self.__balance