# Copy here code of line function from previous exercise and use it in your solution
def line(num, text):
    if not text:
        print("*" * num)
    else:
        print(text[0] * num)

def shape(width, char1, height, char2):
    x = 1
    y = 1
    while x <= width:
        line(x, char1)
        x += 1
    while y <= height:
        line(width, char2)
        y += 1
    



# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")