# Write your solution here
def length_of_longest(my_list: list):
    best = 0
    for item in my_list:
        if len(item) > best:
            best = len(item)
    return best
