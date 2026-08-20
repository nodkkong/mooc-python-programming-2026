# Write your solution here
def chessboard(length):
    row = 0
    while row < length:
        col = 0
        while col < length:
            if (row + col) % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
            col += 1
        print()
        row += 1


# Testing the function
if __name__ == "__main__":
    chessboard(3)
