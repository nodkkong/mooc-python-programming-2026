# Write your solution here
def shortest(my_list: list):
    result = my_list[0]
    for item in my_list:
        if len(item) < len(result):
            result = item
    return result 