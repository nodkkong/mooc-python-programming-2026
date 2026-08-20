# Write your solution here
def list_sum(a, b):
    new_list = []
    for i in range(len(a)):
        new_list.append(a[i] + b[i])
    return new_list