# Write your solution here
def no_shouting(my_list: list):
    new_list = []
    for item in my_list:
        if not item.isupper():
            new_list.append(item)
    return new_list