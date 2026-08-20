# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
starting_date = input("Starting date: ")
days = int(input("How many days: "))

print("Please type in screen time in minutes on each day (TV computer mobile):")

date = datetime.strptime(starting_date, "%d.%m.%Y")
entries = []
for i in range(days):
    screen_time = input(f"Screen time {date.strftime('%d.%m.%Y')}: ")
    entries.append((date, screen_time))
    date += timedelta(days=1)

total = 0
for d, screen_time in entries:
    parts = screen_time.split()
    total += sum(int(p) for p in parts)

start = entries[0][0].strftime("%d.%m.%Y")
end = entries[-1][0].strftime("%d.%m.%Y")

with open(filename, "w") as f:
    f.write(f"Time period: {start}-{end}\n")
    f.write(f"Total minutes: {total}\n")
    f.write(f"Average minutes: {total / days}\n")
    for d, screen_time in entries:
        parts = screen_time.split()
        f.write(f"{d.strftime('%d.%m.%Y')}: {'/'.join(parts)}\n")

print(f"Data stored in file {filename}")