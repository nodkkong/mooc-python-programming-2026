# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest_num = None
        for number in new_file:
            num = int(number)
            if largest_num is None or num > largest_num:
                largest_num = num
        return largest_num