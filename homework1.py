def average(self):
    total_grades = self.values()
    average_grade = []
    for value in total_grades:
        for item in value:
            average_grade.append(item)
    average_grade = sum(average_grade) / len(average_grade)
    return average_grade


def course_average(student, course):
    course_grades = []
    for student in students:
        if course not in student.grades:
            return 'Ошибка'
        else:
            course_grades += student.grades[course]
    count = sum(course_grades) / (len(course_grades))
    return f'Среднее значение по студентам на курсе {course}: {count}'


def course_average_lec(lecturer, course):
    course_grades = []
    for lecturer in lecturers:
        if course not in lecturer.grades:
            return 'Ошибка'
        else:
            course_grades += lecturer.grades[course]
    count = sum(course_grades) / (len(course_grades))
    return f'Среднее значение по лекторам на курсе {course}: {count}'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if grade > 0 and grade <= 10:
            if isinstance(lecturer,
                          Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def __lt__(self, student):
        if isinstance(student, Student):
            return average(self.grades) < average(student.grades)
        else:
            return 'Не студент'

    def __str__(self):
        return f'Имя: {self.name}' '\n' \
               f'Фамилия: {self.surname}' '\n' \
               f'Средняя оценка за задания: {average(self.grades)}' '\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}' '\n' \
               f'Завершенные курсы: {",".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}' '\n' \
               f'Фамилия: {self.surname}' '\n' \
               f'Средняя оценка за лекции: {average(self.grades)}'

    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return average(self.grades) < average(lecturer.grades)
        else:
            return 'Не лектор'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if grade > 0 and grade <= 10:
            if isinstance(student, Student) and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}' '\n' \
               f'Фамилия: {self.surname}'


reviewer = Reviewer('Some', 'Buddy')

student = Student('Ruoy', 'Eman', 'Male')

student.courses_in_progress += ['Python']
student.courses_in_progress += ['GIT']
student.finished_courses += ['Введение в программирование']

student2 = Student('Liza', 'Wom', 'Female')
student2.courses_in_progress += ['GIT']
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Введение в программирование']

lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python']
lecturer.courses_attached += ['GIT']
student.rate_lec(lecturer, 'Python', 8.5)
student.rate_lec(lecturer, 'GIT', 9.5)
student2.rate_lec(lecturer, 'Python', 8)
student2.rate_lec(lecturer, 'GIT', 10)

lecturer2 = Lecturer('Slim', 'Shady')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['GIT']
student.rate_lec(lecturer2, 'Python', 9.0)
student.rate_lec(lecturer2, 'GIT', 7.5)
student2.rate_lec(lecturer2, 'Python', 10)
student2.rate_lec(lecturer2, 'GIT', 8)

reviewer = Reviewer('Sum', 'Buddy')
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'GIT', 5)
reviewer.rate_hw(student2, 'Python', 8)
reviewer.rate_hw(student2, 'GIT', 10)

reviewer2 = Reviewer('Slim', 'Shady')
reviewer2.rate_hw(student, 'Python', 3)
reviewer2.rate_hw(student, 'GIT', 2)
reviewer2.rate_hw(student2, 'Python', 4)
reviewer2.rate_hw(student2, 'GIT', 6)

print(student)

print(student2)

print(lecturer)

print(lecturer2)

print(reviewer)

print(student < student2)

print(lecturer > lecturer2)

students = [student, student2]
lecturers = [lecturer, lecturer2]

print(course_average(students, 'Python'))
print(course_average(students, 'GIT'))
print(course_average(students, 'Введение в программирование'))

print(course_average_lec(lecturers, 'Python'))
print(course_average_lec(lecturers, 'GIT'))
print(course_average_lec(lecturers, 'Введение в программирование'))