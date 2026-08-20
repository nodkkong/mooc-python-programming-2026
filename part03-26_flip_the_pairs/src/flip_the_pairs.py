# Write your solution here
num = int(input("Please type in a number: "))
i = 2
while i <= num + 1:
    if i > num:
        print(i-1)
    else:
        print(i)
        print(i-1)
    i += 2