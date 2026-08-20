# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))
row = 1
hashes = "#"
while row <= height:
    print(hashes * width)
    row += 1