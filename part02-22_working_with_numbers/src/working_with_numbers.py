# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
nums = []
positive_nums = 0
negative_nums = 0

while True:
    num = int(input("Number: "))
    if num == 0:
        break
    if num < 0:
        negative_nums += 1
    elif num > 0:
        positive_nums += 1
    nums.append(num)
total = sum(nums)
print(f'Numbers typed in {len(nums)}')
print(f'The sum of the numbers is {total}')
print(f'The mean of the numbers is {total / len(nums)}')
print(f'Positive numbers {positive_nums}')
print(f'Negative numbers {negative_nums}')
