# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def _total_cents(self):
        return self.__euros * 100 + self.__cents

    def __eq__(self, another):
        return self._total_cents() == another._total_cents()

    def __lt__(self, another):
        return self._total_cents() < another._total_cents()

    def __gt__(self, another):
        return self._total_cents() > another._total_cents()

    def __ne__(self, another):
        return self._total_cents() != another._total_cents()

    def __add__(self, another):
        total = self._total_cents() + another._total_cents()
        new_euros = total // 100
        new_cents = total % 100
        return Money(new_euros, new_cents)

    def __sub__(self, another):
        if self._total_cents() < another._total_cents():
            raise ValueError("a negative result is not allowed")
        total = self._total_cents() - another._total_cents()
        new_euros = total // 100
        new_cents = total % 100
        return Money(new_euros, new_cents)

