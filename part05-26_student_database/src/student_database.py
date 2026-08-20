# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []


def print_student(students: dict, name: str):
    if name not in students:
        print(f'{name}: no such person in the database')
    else:
        print(f'{name}:')
        if not students[name]:
            print(f' no completed courses')
        else:
            print(f' {len(students[name])} completed courses:')
            total = 0
            for course, grade in students[name]:
                print(f'  {course} {grade}')
                total += grade
            print(f' average grade {total / len(students[name])}')


def add_course(students: dict, name: str, course_grade: tuple):
    course, grade = course_grade
    if grade == 0:
        return
    for i in range(len(students[name])):
        if students[name][i][0] == course:
            if grade > students[name][i][1]:
                students[name][i] = course_grade
            return
    students[name].append(course_grade)

def summary(students: dict):
    print(f'students {len(students)}')

    most_course = 0
    most_name = ""
    for name in students:
        if len(students[name]) > most_course:
            most_course = len(students[name])
            most_name = name
    print(f'most courses completed {most_course} {most_name}')

    best_average = 0
    best_name = ""
    for name in students:
        if len(students[name]) > 0:
            total = 0
            for course, grade in students[name]:
                total += grade
            average = total / len(students[name])
            if average > best_average:
                best_average = average
                best_name = name
    print(f'best average grade {best_average} {best_name}')