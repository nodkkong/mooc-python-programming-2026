# Write your solution here
def longest_series_of_neighbours(my_list: list):
    current = 1
    longest = 1
    for i in range(len(my_list) - 1):
        if abs(my_list[i] - my_list[i+1]) == 1:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1
    return longest