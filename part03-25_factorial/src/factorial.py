# Write your solution here
while True:
    num = int(input("Please type in a number: "))
    i = 1
    factorial = 1
    if num <= 0:
        print("Thanks and bye!")
        break
    while i <= num:
        factorial *= i
        i += 1
    print(f'The factorial of the number {num} is {factorial}')