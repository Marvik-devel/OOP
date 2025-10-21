class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and 
            course in lecturer.courses_attached and 
            course in self.courses_in_progress and
            1 <= grade <= 10):
            
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def _calculate_average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)
    
    def __str__(self):
        avg_grade = self._calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'
        
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
    
    def _calculate_average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)
    
    def __str__(self):
        avg_grade = self._calculate_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
    
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and 
            course in self.courses_attached and 
            course in student.courses_in_progress):
            
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")

def calculate_average_hw_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

def calculate_average_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0


lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Петр', 'Петров')
reviewer = Reviewer('Сергей', 'Сергеев')
student1 = Student('Ольга', 'Алёхина', 'Ж')
student2 = Student('Алексей', 'Сидоров', 'М')

student1.courses_in_progress = ['Python', 'Git']
student2.courses_in_progress = ['Python', 'Java']
lecturer1.courses_attached = ['Python']
lecturer2.courses_attached = ['Python', 'Java']
reviewer.courses_attached = ['Python']

student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer2, 'Python', 7)

reviewer.rate_hw(student1, 'Python', 10)
reviewer.rate_hw(student1, 'Python', 9)
reviewer.rate_hw(student2, 'Python', 8)

# Test the output
print("Вывод")
print("Лектор 1:", lecturer1, sep='\n')
print("\nСтудент 1:", student1, sep='\n')


# Testing the comparison
print(f"Сравнение")
print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")
print(f"Студент1 > Студент2: {student1 > student2}")

# Testing the average rating functions
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средние оценки")
print(f"Средняя за ДЗ (Python): {calculate_average_hw_grade(students, 'Python'):.1f}")
print(f"Средняя за лекции (Python): {calculate_average_lecture_grade(lecturers, 'Python'):.1f}")
