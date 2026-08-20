# Write your solution here
def grade(exam, exercises):
    exercise_points = exercises // 10
    total_points = exam + exercise_points
    if exam < 10 or total_points < 15:
        return 0
    elif total_points < 18:
        return 1
    elif total_points < 21:
        return 2
    elif total_points < 24:
        return 3
    elif total_points < 28:
        return 4
    else:
        return 5
    
results = []
while True:
    user_input = input("Exam points and exercises completed: ")
    if user_input == "":
        break
    parts = user_input.split()
    exam = int(parts[0])
    exercises = int(parts[1])
    results.append((exam, exercises))

grades = []
for exam, exercises in results:
    grades.append(grade(exam, exercises))

total = sum(exam + (exercises // 10) for exam, exercises in results)
points_average = total / len(results)

passed = 0
for g in grades:
    if g > 0:
        passed += 1
pass_percentage = passed / len(grades) * 100

print("Statistics:")
print(f'Points average: {points_average:.1f}')
print(f'Pass percentage: {pass_percentage:.1f}')
print("Grade distribution:")
for i in range(5, -1, -1):
    star = "*" * grades.count(i)
    print(f'  {i}: {star}')