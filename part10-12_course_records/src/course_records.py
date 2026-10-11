# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def set_grade(self, grade: int):
        if grade > self.__grade:
            self.__grade = grade


class CourseRecords:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        else:
            self.__courses[name].set_grade(grade)

    def get_course(self, name: str):
        if name not in self.__courses:
            return None
        return self.__courses[name]

    def all_courses(self):
        return self.__courses


class CourseRecordsApplication:
    def __init__(self):
        self.__courserecords = CourseRecords()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course_name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__courserecords.add_course(course_name, grade, credits)

    def search(self):
        course_name = input("course: ")
        course = self.__courserecords.get_course(course_name)
        if course is None:
            print("no entry for this course")
            return
        print(f"{course_name} ({course.credits()} cr) grade {course.grade()}")

    def stat(self):
        courses = self.__courserecords.all_courses()
        total_courses = len(courses)
        total_credits = sum(course.credits() for course in courses.values())
        total_grade = sum(course.grade() for course in courses.values())
        mean_grade = total_grade / total_courses

        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean_grade:.1f}")
        print("grade distribution")

        g5, g4, g3, g2, g1 = 0, 0, 0, 0, 0
        for course in courses.values():
            grade = course.grade()
            if grade == 5:
                g5 += 1
            elif grade == 4:
                g4 += 1
            elif grade == 3:
                g3 += 1
            elif grade == 2:
                g2 += 1
            elif grade == 1:
                g1 += 1
        print(f"5: {'x'*g5}")
        print(f"4: {'x'*g4}")
        print(f"3: {'x'*g3}")
        print(f"2: {'x'*g2}")
        print(f"1: {'x'*g1}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.search()
            elif command == "3":
                self.stat()
            else:
                self.help()


application = CourseRecordsApplication()
application.execute()