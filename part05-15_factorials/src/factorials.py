# Write your solution here
def factorials(n: int):
    my_dict = {}
    for i in range(1, n+1):
        if i == 1:
            my_dict[1] = 1
        else:
            my_dict[i] = i * my_dict[i-1]
    return my_dict
