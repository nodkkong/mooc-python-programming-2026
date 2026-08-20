# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")

else:
    student_info = "student1.csv"
    exercise_data = "exercises1.csv"

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

for id, name in names.items():
    if id in exercises:
        exercise = exercises[id]
        print(f'{name} {sum(exercise)}')