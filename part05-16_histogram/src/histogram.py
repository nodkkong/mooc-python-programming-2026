# Write your solution here
def histogram(my_string: str):
    my_dict = {}
    for char in my_string:
        if char not in my_dict:
            my_dict[char] = my_string.count(char)
    
    for char, count in my_dict.items():
        print(f"{char} {'*' * count}")