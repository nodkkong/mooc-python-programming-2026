# Write your solution here
from datetime import datetime, timedelta

day_input = int(input("Day: "))
month_input = int(input("Month: "))
year_input = int(input("Year: "))

user_input = datetime(year_input, month_input, day_input)
new_millennium_eve = datetime(1999, 12, 31)
difference = new_millennium_eve - user_input

if user_input < new_millennium_eve:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")