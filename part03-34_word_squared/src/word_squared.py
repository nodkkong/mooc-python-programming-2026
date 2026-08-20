# Write your solution here
def squared(text, length):
    row = 0
    index = 0
    while row < length:
        col = 0
        while col < length:
            print(text[index % len(text)], end="")
            index += 1
            col += 1
        print()
        row += 1