# Write your solution here
def dict_of_numbers():
    new_dict = {}
    ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    for n in range(100):
        if n <= 19:
            new_dict[n] = ones[n]
        elif n % 10 == 0:
            new_dict[n] = tens[n // 10]
        else:
            new_dict[n] = f'{tens[n // 10]}-{ones[n % 10]}'
    return new_dict