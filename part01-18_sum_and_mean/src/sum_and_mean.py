# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))
number4 = int(input("Number 4: "))
numbers = [number1, number2, number3, number4]
mean = sum(numbers) / len(numbers)

print(f'The sum of the numbers is {sum(numbers)} and the mean is {mean:.1f}')