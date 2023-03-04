all_students_list = []
all_lecturers_list = []


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        all_students_list.append(self)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 0 < grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades_student(self) -> object:
        all_grade_student = []
        for grades in self.grades.values():
            for grade in grades:
                all_grade_student.append(grade)
        if len(all_grade_student) > 0:
            return round(sum(all_grade_student) / len(all_grade_student), 1)
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grades_student()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Сравниваемый не является студентом!'
        else:
            var = self.average_grades_student() > other.average_grades_student()
            if True:
                return f'Средняя оценка за домашние задания у {self.name} {self.surname} меньше, чем у {other.name} {other.surname}'
            else:
                return f'Средняя оценка за домашние задания у {self.name} {self.surname} больше, чем у {other.name} {other.surname}'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        all_lecturers_list.append(self)

    def average_grades_lector(self) -> object:
        all_grade_lector = []
        for grades in self.grades.values():
            for grade in grades:
                all_grade_lector.append(grade)
        if len(all_grade_lector) > 0:
            return round(sum(all_grade_lector) / len(all_grade_lector), 1)
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_grades_lector()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Сравниваемый не является лектором!'
        else:
            var = self.average_grades_lector() < other.average_grades_lector()
            if True:
                return f'Средняя оценка за лекции у {self.name} {self.surname} больше, чем у {other.name} {other.surname}'
            else:
                return f'Средняя оценка за лекции у {self.name} {self.surname} меньше, чем у {other.name} {other.surname}'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


def average_grade_all_students_in_course(all_students_list, course):
    all_students_grade = []
    for student in all_students_list:
        if course in student.courses_in_progress:
            for grade in student.grades[course]:
                all_students_grade.append(grade)
        else:
            print(f'{student.name} {student.surname} не получал(а) оценок за этот курс!')
    if len(all_students_grade) > 0:
        return f'Средняя оценка за домашние задания по всем студентам на курсе {course}: {round(sum(all_students_grade) / len(all_students_grade), 1)}'
    else:
        return 'Ошибка'


def average_grade_all_lecturers_in_course(all_lecturers_list, course):
    all_lecturers_grade = []
    for lecturer in all_lecturers_list:
        if course in lecturer.courses_attached:
            for grade in lecturer.grades[course]:
                all_lecturers_grade.append(grade)
        else:
            print(f'{lecturer.name} {lecturer.surname} не получал(а) оценок за лекции на данном курсе!')
    if len(all_lecturers_grade) > 0:
        return f'Средняя оценка за лекции всех лекторов на курсе {course}: {round(sum(all_lecturers_grade) / len(all_lecturers_grade), 1)}'
    else:
        return 'Ошибка'


student_1 = Student('Антон', 'Порешкин', 'мужской')
student_1.courses_in_progress += ['Git', 'Python']
student_1.finished_courses += ['Java', 'Django']

student_2 = Student('Анна', 'Агузарова', 'женский')
student_2.courses_in_progress += ['Java', 'Django', 'Git']
student_2.finished_courses += ['Python']

lecturer_1 = Lecturer('Федор', 'Сифлонов')
lecturer_1.courses_attached += ['Python', 'Django']

lecturer_2 = Lecturer('Герман', 'Фрауз')
lecturer_2.courses_attached += ['Git', 'Java', 'Python']

student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Django', 7)
student_1.rate_lecture(lecturer_2, 'Git', 9)
student_1.rate_lecture(lecturer_2, 'Java', 9)
student_1.rate_lecture(lecturer_2, 'Python', 6)

student_2.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_1, 'Django', 5)
student_2.rate_lecture(lecturer_2, 'Git', 10)
student_2.rate_lecture(lecturer_2, 'Java', 8)
student_2.rate_lecture(lecturer_2, 'Python', 5)

reviewer_1 = Reviewer('Альберт', 'Браунг')
reviewer_1.courses_attached += ['Python', 'Java']
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Django', 6)
reviewer_1.rate_hw(student_1, 'Java', 6)
reviewer_1.rate_hw(student_2, 'Git', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Django', 8)
reviewer_1.rate_hw(student_2, 'Java', 9)

reviewer_2 = Reviewer('Лариса', 'Долина')
reviewer_2.courses_attached += ['Git', 'Django']
reviewer_2.rate_hw(student_1, 'Git', 6)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Django', 5)
reviewer_2.rate_hw(student_1, 'Java', 6)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Django', 7)
reviewer_2.rate_hw(student_2, 'Java', 8)

print(student_1)
print('--------------------------------------')
print(student_2)
print('--------------------------------------')
print(lecturer_1)
print('--------------------------------------')
print(lecturer_2)
print('--------------------------------------')
print(student_1.__gt__(student_2))
print(lecturer_2.__lt__(lecturer_1))
print('--------------------------------------')
print(average_grade_all_students_in_course(all_students_list, 'Git'))
print('--------------------------------------')
print(average_grade_all_lecturers_in_course(all_lecturers_list, 'Python'))
