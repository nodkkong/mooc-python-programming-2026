# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        counts = {}
        for item in my_list:
            if item not in counts:
                counts[item] = 0
            counts[item] += 1
        most_common = None
        highest_count = 0
        for item, count in counts.items():
            if count > highest_count:
                highest_count = count
                most_common = item
        return most_common

    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for item in my_list:
            if item not in counts:
                counts[item] = 0
            counts[item] += 1
        double_count = 0
        for item in counts:
            if counts[item] >= 2:
                double_count += 1
        return double_count