# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, winning_numbers: list):
        self.__week = week
        self.__winning_numbers = winning_numbers

    def number_of_hits(self, numbers: list):
        return sum([1 for number in numbers if number in self.__winning_numbers])

    def hits_in_place(self, numbers: list):
        return [number if number in self.__winning_numbers else -1 for number in numbers]