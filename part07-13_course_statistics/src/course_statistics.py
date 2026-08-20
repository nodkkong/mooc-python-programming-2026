# Write your solution here
import urllib.request
import json

def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urllib.request.urlopen(address)
    data = json.loads(response.read())

    result = []
    for course in data:
        if course["enabled"]:
            name = course["fullName"]
            course_name = course["name"]
            year = course["year"]
            total_exercises = sum(course["exercises"])
            result.append((name, course_name, year, total_exercises))
    return result

def retrieve_course(course_name: str):
    address = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    response = urllib.request.urlopen(address)
    data = json.loads(response.read())

    weeks = len(data)
    students = 0
    hours = 0
    exercises = 0

    for week, info in data.items():
        if info["students"] > students:
            students = info["students"]
        hours += info["hour_total"]
        exercises += info["exercise_total"]

    hours_average = hours // students
    exercises_average = exercises // students

    return {
        "weeks": weeks,
        "students": students,
        "hours": hours,
        "hours_average": hours_average,
        "exercises": exercises,
        "exercises_average": exercises_average
    }
