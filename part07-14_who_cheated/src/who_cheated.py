# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():
    start_times = {}
    with open("start_times.csv") as f:
        for line in csv.reader(f, delimiter=";"):
            name = line[0]
            time = line[1]
            start_times[name] = time

    handin_times = {}
    with open("submissions.csv") as j:
        for line in csv.reader(j, delimiter=";"):
            name = line[0]
            time = line[3]
            if name not in handin_times:
                handin_times[name] = []
            handin_times[name].append(time)
    
    cheater_list = []
    for name, time in handin_times.items():
        start = datetime.strptime(start_times[name], "%H:%M")
        for t in time:
            submit = datetime.strptime(t, "%H:%M")
            if submit - start > timedelta(hours=3):
                cheater_list.append(name)
                break

    return cheater_list