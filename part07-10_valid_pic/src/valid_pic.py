# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    try:
        if len(pic) != 11:
            return False
        day = int(pic[0:2])
        month = int(pic[2:4])
        year = int(pic[4:6])
        century = pic[6]
        if century == "+":
            year += 1800
        elif century == "-":
            year += 1900
        elif century == "A":
            year += 2000
        else:
            return False
        valid_date = datetime(year, month, day)
        number = int(pic[0:6] + pic[7:10])
        remainder = number % 31
        control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
        if pic[10] == control_chars[remainder]:
            return True
        return False

    except ValueError:
        return False