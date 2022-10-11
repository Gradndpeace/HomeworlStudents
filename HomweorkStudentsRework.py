class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lc(self, lecturer, course, grade_lecturer):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grade_lecturer:
                lecturer.grade_lecturer[course] += [grade_lecturer]
            else:
                lecturer.grade_lecturer[course] = [grade_lecturer]
        else:
            return 'Ошибка'

    def average_grade_counter(self):
        self.average_grade = 0
        for values in self.grades.values():
            self.average_grade = round(sum(values) / len(values), 1)
        return self.average_grade

    def __str__(self):
        val = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average_grade_counter()}\nКурсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}\n'
        return val

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка!'
        return self.average_grade < other.average_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_lecturer = {}

    def average_grade_counter(self):
        self.average_grade = 0
        for values in self.grade_lecturer.values():
            self.average_grade = round(sum(values)/len(values), 1)
        return self.average_grade

    def __str__(self):
        val = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade_counter()}\n'
        return val

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка!'
        return self.average_grade < other.average_grade

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
        val = f'Имя: {self.name}\nФамилия: {self.surname}\n'

        return val

best_student1 = Student('William', 'Shakehands', 'male')
best_student1.courses_in_progress += ['Python']
best_student2 = Student('Rauf', 'Babaev', 'male')
best_student2.courses_in_progress += ['Python']
class_number_1 = [best_student1, best_student2]


cool_lecturer1 = Lecturer('Jake', "Gyllenhoopaloop")
cool_lecturer1.courses_attached += ['Python']
cool_lecturer2 = Lecturer('Vitaly', 'Volochay')
cool_lecturer2.courses_attached += ['Python']
lecturer_group = [cool_lecturer1, cool_lecturer2]

cool_reviewer1 = Reviewer('John', 'Lenin')
cool_reviewer1.courses_attached += ['Python']
cool_reviewer2 = Reviewer('Dart', 'Vedro')
cool_reviewer2.courses_attached += ['Python']

cool_reviewer1.rate_hw(best_student1, 'Python', 10)
cool_reviewer1.rate_hw(best_student1, 'Python', 7)
cool_reviewer2.rate_hw(best_student1, 'Python', 7)
cool_reviewer1.rate_hw(best_student2, 'Python', 7)
cool_reviewer1.rate_hw(best_student2, 'Python', 9)
cool_reviewer2.rate_hw(best_student2, 'Python', 4)

best_student1.rate_lc(cool_lecturer1, 'Python', 5)
best_student1.rate_lc(cool_lecturer1, 'Python', 8)
best_student1.rate_lc(cool_lecturer1, 'Python', 10)
best_student2.rate_lc(cool_lecturer2, 'Python', 6)
best_student2.rate_lc(cool_lecturer2, 'Python', 9)
best_student2.rate_lc(cool_lecturer2, 'Python', 10)

print(cool_lecturer1.grade_lecturer)
print(best_student1.grades)

print(cool_reviewer1)
print(cool_lecturer1)
print(best_student1)
print(cool_reviewer2)
print(cool_lecturer2)
print(best_student2)

def avrg_std_grade(course, class_number_1):
    sum = 0
    count = 0
    for std in class_number_1:
         for grade in std.grades[course]:
            sum += grade
            count += 1
    return f'Средняя оценка в группе равна {sum / count}'

print(avrg_std_grade('Python', class_number_1))

def avrg_lc_grade(course, lecturer_group):
    sum = 0
    counter = 0
    for lc in lecturer_group:
         for grade in lc.grade_lecturer[course]:
            sum += grade
            counter += 1
    return f'Средняя оценка лекторов равна {sum / counter}'

print(avrg_lc_grade('Python', lecturer_group))
print(best_student1 < best_student2)
print(cool_lecturer1 < cool_lecturer2)