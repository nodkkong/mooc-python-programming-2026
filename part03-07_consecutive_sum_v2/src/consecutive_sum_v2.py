# Write your solution here
limit = int(input("Limit: "))
total = 0
num = 1
words = "The consecutive sum: "
while total < limit:
    total += num
    words += f'{num}'
    num += 1
    if total < limit:
        words += " + "
print(words + f' = {total}')
