from statistics import mean


#готово
# Задание № 1. Наследование
# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов (вы можете взять этот код за основу или написать свой). Студентов пока оставим без изменения, а вот преподаватели бывают разные, поэтому теперь класс Mentor должен стать родительским классом, а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания). Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса. А чем же будут специфичны дочерние классы? Об этом в следующих заданиях.

#готово
# Задание № 2. Атрибуты и взаимодействие классов.
# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания. Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы? Получать оценки за лекции от студентов :) Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок). Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

#готово 
# Задание № 3. Полиморфизм и магические методы
# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:

# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy
# У лекторов:

# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9
# А у студентов так:

# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование


# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
# Задание № 4. Полевые испытания
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:

# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).


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
    
    def rate_lection(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and course in lector.courses_attached
            and course in self.courses_in_progress):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    #вычисление средней оценки за ДЗ
    def average(self):
        return round(mean([mean(grade) for grade in self.grades.values()]),1)
    
# Реализуйте возможность сравнивать (через операторы сравнения) между собой 
# лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Операнд справа должет иметь тип Student")
        # other_average = other.average
        # print(self.average)
        # print(other.average)
        return self.average() < other.average()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Операнд справа должет иметь тип Student")
        # other_average = other.average
        # print(self.average)
        # print(other.average)
        return self.average() == other.average()
    
    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Операнд справа должет иметь тип Student")
        # other_average = other.average
        # print(self.average)
        # print(other.average)
        return self.average() <= other.average()
        




            
    def __str__(self):
        return f"""Имя: {self.name} \nФамилия: {self.surname}
Средняя оценка за домашние задания: {self.average()}
Курсы в процессе изучения: {self.courses_in_progress}
Завершенные курсы: {self.finished_courses}\n"""
 
     
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}\n"
    
    def average(self):
        return round(mean([mean(grade) for grade in self.grades.values()]),1)
    
# Реализуйте возможность сравнивать (через операторы сравнения) между собой 
# лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Операнд справа должет иметь тип Lecturer")
        return self.average() < other.average()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Операнд справа должет иметь тип Lecturer")
        return self.average() == other.average()
    
    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Операнд справа должет иметь тип Lecturer")
        return self.average() <= other.average()


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
        return f"Имя: {self.name} \nФамилия: {self.surname}"


# для подсчета средней оценки за домашние задания по всем студентам в рамках 
# конкретного курса (в качестве аргументов принимаем список студентов и название курса);
def average_corse(students: list, course):
    
    return mean([mean(student.grades.get(course, 'none')) for student in students])

#Объявлениеобъектов классов и их атрибуты
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['SQL']
poor_student = Student('Roma', 'Esin', 'Boy')
poor_student.courses_in_progress += ['Python']
poor_student.courses_in_progress += ['SQL']

cool_mentor = Mentor('Some', 'Buddy')
bad_mentor = Mentor('Nikolay', 'Vushkin')
cool_reviewer = Reviewer('Anton', "Pupkin")
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['SQL']
bad_reviewer = Reviewer('Yana', "Popova")
bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['SQL']
cool_lecture = Lecturer('Vasia', 'Pupkin')
cool_lecture.courses_attached += ['Python']
cool_lecture.courses_attached += ['SQL']
bad_lecture = Lecturer('Ad', 'Konev')
bad_lecture.courses_attached += ['Python']
bad_lecture.courses_attached += ['SQL']

#методы
#выставление оценок
best_student.add_courses('Python с нуля. Разработка бота')
poor_student.add_courses('Python для новичков')
best_student.rate_lection(cool_lecture,'SQL', 10)
best_student.rate_lection(cool_lecture,'SQL', 9)
best_student.rate_lection(bad_lecture,'SQL', 7)
best_student.rate_lection(bad_lecture,'SQL', 7)
best_student.rate_lection(cool_lecture,'Python', 9)
best_student.rate_lection(cool_lecture,'Python', 9)
best_student.rate_lection(bad_lecture,'Python', 8)
best_student.rate_lection(bad_lecture,'Python', 9)

poor_student.rate_lection(cool_lecture,'SQL', 5)
poor_student.rate_lection(cool_lecture,'SQL', 8)
poor_student.rate_lection(bad_lecture,'SQL', 3)
poor_student.rate_lection(bad_lecture,'SQL', 3)
poor_student.rate_lection(cool_lecture,'Python', 8)
poor_student.rate_lection(cool_lecture,'Python', 10)
poor_student.rate_lection(bad_lecture,'Python', 3)
poor_student.rate_lection(bad_lecture,'Python', 4)

cool_reviewer.rate_hw(best_student, 'SQL', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(poor_student, 'SQL', 5)
cool_reviewer.rate_hw(poor_student, 'Python', 6)
cool_reviewer.rate_hw(poor_student, 'Python', 6)
cool_reviewer.rate_hw(poor_student, 'Python', 8)

bad_reviewer.rate_hw(best_student, 'SQL', 10)
bad_reviewer.rate_hw(best_student, 'Python', 10)
bad_reviewer.rate_hw(best_student, 'Python', 10)
bad_reviewer.rate_hw(best_student, 'Python', 8)
bad_reviewer.rate_hw(poor_student, 'SQL', 2)
bad_reviewer.rate_hw(poor_student, 'Python', 3)
bad_reviewer.rate_hw(poor_student, 'Python', 4)
bad_reviewer.rate_hw(poor_student, 'Python', 5)


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

#__str___
print(best_student)
print(poor_student)
print(cool_lecture)
print(bad_lecture)
print(cool_reviewer)
print(bad_reviewer)

grade_avearage_course = average_corse([best_student, poor_student], 'SQL')
print(grade_avearage_course)

print()
print(best_student < poor_student)
print(best_student >= poor_student)
print(best_student == poor_student)

print()
print(cool_lecture < bad_lecture)
print(cool_lecture >= bad_lecture)
print(cool_lecture == bad_lecture)

print()
#print(cool_lecture < best_student) #ошибка
#print(cool_lecture >= best_student)
# print(cool_lecture == best_student)