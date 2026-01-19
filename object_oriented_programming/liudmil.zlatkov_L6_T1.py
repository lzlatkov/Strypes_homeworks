class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = {}

    def getSalary(self):
        return self.salary

    def addCourse(self, signature,  course):
        self.courses[signature] = course

    def getCourses(self):
        for key, value in self.courses.items():
            print(f"{key} {value}")


class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}

    def attendCourse(self, course, year):
        if course not in self.courses:
            self.courses[course] = {'grades': [], 'year': [year]}

    def addGrade(self, course, grade):
        if course in self.courses:
            self.courses[course]['grades'].append(grade)

    def getCourses(self):
        for key, value in self.courses.items():
            print(f"{key} {value}")

    def getAvgGrade(self, course):
        if course in self.courses:
            grades = self.courses[course]["grades"]
            return sum(grades) / len(grades)

