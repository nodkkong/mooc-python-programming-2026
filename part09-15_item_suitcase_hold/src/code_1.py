# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def weight(self):
        total = 0
        for i in self.__items:
            total += i.weight()
        return total

    def add_item(self, item: Item):
        if item.weight() + self.weight() <= self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        for i in self.__items:
            print(i)

    def heaviest_item(self):
        if not self.__items:
            return None
        heaviest = self.__items[0]
        for i in self.__items:
            if i.weight() > heaviest.weight():
                heaviest = i
        return heaviest

    def __str__(self):
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({self.weight()} kg)"
        return f"{len(self.__items)} items ({self.weight()} kg)"


class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def weight(self):
        total = 0
        for s in self.__suitcases:
            total += s.weight()
        return total

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() + self.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        if len(self.__suitcases) == 1:
            return f"{len(self.__suitcases)} suitcase, space for {self.__max_weight - self.weight()} kg"    
        return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.weight()} kg"