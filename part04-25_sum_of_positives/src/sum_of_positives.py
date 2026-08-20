# Write your solution here
def sum_of_positives(my_list: list):
    positives = []
    for i in my_list:
        if i > 0:
            positives.append(i)
    return sum(positives)
