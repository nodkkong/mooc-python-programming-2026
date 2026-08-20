# Write your solution here
def spruce(size):
    print("a spruce!")
    i = 1
    while i <= size:
        lines = ("*" * (i*2 - 1)).center(size*2 - 1)
        print(lines)
        i += 1
    print("*".center(size*2 - 1))


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)