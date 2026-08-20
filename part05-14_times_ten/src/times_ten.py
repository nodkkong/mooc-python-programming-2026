# Write your solution here
def times_ten(start_index: int, end_index: int):
    my_dict = {}
    for i in range(start_index, end_index + 1):
        my_dict[i] = i * 10
    return my_dict
