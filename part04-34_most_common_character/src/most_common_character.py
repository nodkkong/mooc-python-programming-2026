# Write your solution here
def most_common_character(my_string: str):
    best_char = my_string[0]
    best_count = 0
    for char in my_string:
        if my_string.count(char) > best_count:
            best_char = char
            best_count = my_string.count(char)
    return best_char