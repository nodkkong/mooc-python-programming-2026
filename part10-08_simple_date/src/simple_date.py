# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def _total_days(self):
        return self.__day + self.__month * 30 + self.__year * 360

    def __lt__(self, another):
        return self._total_days() < another._total_days()

    def __gt__(self, another):
        return self._total_days() > another._total_days()

    def __eq__(self, another):
        return self._total_days() == another._total_days()

    def __ne__(self, another):
        return self._total_days() != another._total_days()

    def __add__(self, days: int):
        new_day = self.__day + days
        new_month = self.__month
        new_year = self.__year
        while new_day > 30:
            new_day -= 30
            new_month += 1
            if new_month > 12:
                new_month -= 12
                new_year += 1
        return SimpleDate(new_day, new_month, new_year)

    def __sub__(self, another):
        return abs(self._total_days() - another._total_days())