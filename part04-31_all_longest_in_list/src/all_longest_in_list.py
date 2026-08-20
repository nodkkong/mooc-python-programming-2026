# Write your solution here
def all_the_longest(my_list: list):
    new_list = []
    longest = my_list[0]
    for item in my_list:
        if len(item) > len(longest):
            longest = item
            new_list.clear()
            new_list.append(longest)
        elif len(item) == len(longest):
            new_list.append(item)
    return new_list