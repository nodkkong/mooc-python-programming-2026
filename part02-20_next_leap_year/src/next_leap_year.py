# Write your solution here
year = int(input("Year: "))
next_year = year + 1
while True:
    leap_year = next_year + (4 - (next_year % 4)) % 4
    if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
        break
    else:
        next_year += 4
print(f'The next leap year after {year} is {leap_year}')

