# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number:int):
        self.numbers += number
        self.count += 1

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.numbers

    def average(self):
        if self.count == 0:
            return 0
        return self.numbers / self.count

all_numbers = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()

print("Please type in integer numbers:")
while True:
    number = int(input())
    if number == -1:
        break
    if number % 2 == 0:
        even_numbers.add_number(number)
    else:
        odd_numbers.add_number(number)
    all_numbers.add_number(number)

print("Sum of numbers:", all_numbers.get_sum())
print("Mean of numbers:", all_numbers.average())
print("Sum of even numbers:", even_numbers.get_sum())
print("Sum of odd numbers:", odd_numbers.get_sum())