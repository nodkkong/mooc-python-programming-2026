# Write your solution here
import csv
from datetime import datetime, timedelta

def final_points():
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
            task = line[1]
            points = line[2]
            time = line[3]
            if name not in handin_times:
                handin_times[name] = []
            handin_times[name].append((task, points, time))
        
    scores = {}
    for name, submissions in handin_times.items():
        start = datetime.strptime(start_times[name], "%H:%M")
        for task, points, time in submissions:
            submit = datetime.strptime(time, "%H:%M")
            if submit - start > timedelta(hours=3):
                continue

            points = int(points)
            if name not in scores:
                scores[name] = {}
            if task not in scores[name] or points > scores[name][task]:
                scores[name][task] = points

    result = {}
    for name, tasks in scores.items():
        result[name] = sum(tasks.values())

    return result