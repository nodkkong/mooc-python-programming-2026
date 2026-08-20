# tee ratkaisu tänne
# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_info = input("Course information: ")
    print("Results written to files results.txt and results.csv")

else:
    student_info = "student1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_info = "course1.txt"

names = {}
with open(student_info) as f:
    for line in f:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1] + " " + parts[2]

exercises = {}
with open(exercise_data) as g:
    for line in g:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        nums = []
        for num in parts[1:]:
            nums.append(int(num))
        exercises[parts[0]] = nums

points = {}
with open(exam_points) as h:
    for line in h:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        nums = []
        for num in parts[1:]:
            nums.append(int(num))
        points[parts[0]] = nums

with open(course_info) as i:
    lines = []
    for line in i:
        lines.append(line.strip())
course_name = lines[0].split(": ")[1]
credits = lines[1].split(": ")[1]


def grade(total):
    if total < 15:
        return 0
    elif total < 18:
        return 1
    elif total < 21:
        return 2
    elif total < 24:
        return 3
    elif total < 28:
        return 4
    else:
        return 5

with open("results.txt", "w") as txt, open("results.csv", "w") as csv:
    header = f"{course_name}, {credits} credits"
    txt.write(header + "\n")
    txt.write("=" * len(header) + "\n")
    txt.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
    for id, name in names.items():
        if id in exercises and id in points:
            exercise = exercises[id]
            point = points[id]
            total = sum(exercise) // 4 + sum(point)
            grades = grade(total)
            txt.write(f'{name:30}{sum(exercise):<10}{sum(exercise)//4:<10}{sum(point):<10}{total:<10}{grades:<10}\n')
            csv.write(f"{id};{name};{grades}\n")
