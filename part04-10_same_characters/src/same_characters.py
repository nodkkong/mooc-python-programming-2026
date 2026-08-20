# Write your solution here
def same_chars(text, a, b):
    if 0 <= a < len(text) and 0 <= b < len(text):
        return text[a] == text[b]
    return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))