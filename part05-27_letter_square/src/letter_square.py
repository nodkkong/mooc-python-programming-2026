# Write your solution here
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
layers = int(input("Layers: "))
n = layers * 2 - 1

for row in range(n):
    for col in range(n):
        distance = min(row, col, n - 1 - row, n - 1 - col)
        print(alphabet[layers - 1 - distance], end="")
    print()
