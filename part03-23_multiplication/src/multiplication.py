# Write your solution here
limit = int(input("Please type in a number: "))
i = 1
num = 1
while i <= limit:
    while num <= limit:
        print(f'{i} x {num} = {i *num}')
        num += 1
    i += 1
    num = 1

    