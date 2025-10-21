class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture (self, lecturer, course, grade):  # Checking the conditions
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
        
    # Auxiliary method for calculating the average grade
    def calculate_average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)
    
    # Add magic method str
    def __str__(self):
        avg_grade = self.calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses) if self.calculate_average_grade else 'Нет'
        
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')
     
    # Magic method for comparison <  
    def __lt__(self, other):
          if not isinstance(other, Student):
              return NotImplemented
          return self.calculate_average_grade() <= other.calculate_average_grade()
      
    # Magic method for comparison <= 
    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.calculate_average_grade() <= other.calculate_average_grade()
    
    # Magic method for comparison =
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() == other._calculate_average_grade()
        
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    # Add magic method str
    def __str__(self):
        avg_grade = self.calculate_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")
    # Magic method for comparison <  
    def __lt__(self, other):
          if not isinstance(other, Lecturer):
              return NotImplemented
          return self.calculate_average_grade() <= other.calculate_average_grade()
      
    # Magic method for comparison <= 
    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.calculate_average_grade() <= other.calculate_average_grade()
    
    # Magic method for comparison =
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.calculate_average_grade() == other.calculate_average_grade()
        
# Calculating the average grade for lectures
    def calculate_average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)
    
        
# Add your own property a dictionary
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):  # Checking the conditions
        if (isinstance(student, Student) and
            course in self.courses_attached and
            course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    # Add magic method str    
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Петр', 'Петров')
reviewer = Reviewer('Сергей', 'Сергеев')
student1 = Student('Ольга', 'Алёхина', 'Ж')
student2 = Student('Алексей', 'Сидоров', 'М')

student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python', 'Java']

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']
reviewer.courses_attached += ['Python']

student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer1, 'Python', 10)

student2.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 6)

reviewer.rate_hw(student1, 'Python', 9)
reviewer.rate_hw(student1, 'Python', 10)
reviewer.rate_hw(student2, 'Python', 8)
reviewer.rate_hw(student2, 'Python', 7)

print('Эксперт')
print(reviewer)

print('Лектор 1')
print(lecturer1)

print('Лектор 2')
print(lecturer2)

print('Студент 1')
print(student1)

print('Студент 2')
print(student2)

# Compare lecturers by average rating
print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")  # True (9.0 > 6.5)
print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")  # False
print(f"Лектор1 == Лектор2: {lecturer1 == lecturer2}")  # False


# Compare students by average grade
print(f"Студент1 > Студент2: {student1 > student2}")  # True (9.5 > 7.5)
print(f"Студент1 <= Студент2: {student1 <= student2}")  # False



# Checking methods for comparing methods
print(f"Лектор1 >= Лектор2: {lecturer1 >= lecturer2}")  
print(f"Лектор1 != Лектор2: {lecturer1 != lecturer2}")  