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

class Lecturer(Mentor):
        def __init__(self, name, surname):
        super().__init__(name, surname)
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
    
    def __le__(self, other):

        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() <= other._calculate_average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() == other._calculate_average_grade()
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
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
    """
    Функция для подсчета средней оценки за домашние задания 
    по всем студентам в рамках конкретного курса
    """
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    
    if not total_grades:
        return 0  # если нет оценок
    
    return sum(total_grades) / len(total_grades)

def calculate_average_lecture_grade(lecturers, course):
    """
    Функция для подсчета средней оценки за лекции 
    всех лекторов в рамках курса
    """
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    
    if not total_grades:
        return 0  # если нет оценок
    
    return sum(total_grades) / len(total_grades)



# Создаем по 2 экземпляра каждого класса
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Петр', 'Петров')

reviewer1 = Reviewer('Сергей', 'Сергеев')
reviewer2 = Reviewer('Анна', 'Аннова')

student1 = Student('Ольга', 'Алёхина', 'Ж')
student2 = Student('Алексей', 'Сидоров', 'М')

print("Созданы все объекты")

# Студенты изучают курсы
student1.courses_in_progress += ['Python', 'Git', 'Java']
student1.finished_courses += ['Введение в программирование']

student2.courses_in_progress += ['Python', 'Java', 'C++']
student2.finished_courses += ['Алгоритмы']

# Лекторы прикреплены к курсам
lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['Python', 'Java', 'C++']

# Эксперты прикреплены к курсам
reviewer1.courses_attached += ['Python', 'Git']
reviewer2.courses_attached += ['Java', 'C++']

print("Курсы настроены")

print("\n=== ТЕСТИРУЕМ МЕТОД rate_lecture ===")

# Студенты оценивают лекции
print("Студент1 оценивает лектора1 по Python:", student1.rate_lecture(lecturer1, 'Python', 9))
print("Студент1 оценивает лектора1 по Python:", student1.rate_lecture(lecturer1, 'Python', 8))
print("Студент1 оценивает лектора1 по Git:", student1.rate_lecture(lecturer1, 'Git', 10))

print("Студент2 оценивает лектора1 по Python:", student2.rate_lecture(lecturer1, 'Python', 7))
print("Студент2 оценивает лектора2 по Java:", student2.rate_lecture(lecturer2, 'Java', 6))
print("Студент2 оценивает лектора2 по C++:", student2.rate_lecture(lecturer2, 'C++', 8))

# Тестируем ошибки
print("Ошибка - курс не изучается:", student1.rate_lecture(lecturer2, 'C++', 5))
print("Ошибка - не лектор:", student1.rate_lecture(reviewer1, 'Python', 5))

print("\n=== ТЕСТИРУЕМ МЕТОД rate_hw ===")

# Эксперты оценивают домашние задания
print("Эксперт1 оценивает студента1 по Python:", reviewer1.rate_hw(student1, 'Python', 9))
print("Эксперт1 оценивает студента1 по Python:", reviewer1.rate_hw(student1, 'Python', 10))
print("Эксперт1 оценивает студента1 по Git:", reviewer1.rate_hw(student1, 'Git', 8))

print("Эксперт2 оценивает студента2 по Java:", reviewer2.rate_hw(student2, 'Java', 7))
print("Эксперт2 оценивает студента2 по C++:", reviewer2.rate_hw(student2, 'C++', 6))

# Тестируем ошибки
print("Ошибка - курс не прикреплен:", reviewer1.rate_hw(student1, 'Java', 5))
print("Ошибка - не студент:", reviewer1.rate_hw(lecturer1, 'Python', 5))

print("\n=== ТЕСТИРУЕМ __str__ МЕТОДЫ ===")

print("\n--- ЭКСПЕРТЫ ---")
print("Эксперт1:")
print(reviewer1)
print("\nЭксперт2:")
print(reviewer2)

print("\n--- ЛЕКТОРЫ ---")
print("Лектор1:")
print(lecturer1)
print("\nЛектор2:")
print(lecturer2)

print("\n--- СТУДЕНТЫ ---")
print("Студент1:")
print(student1)
print("\nСтудент2:")
print(student2)


print("\n=== ТЕСТИРУЕМ СРАВНЕНИЕ ===")

print("Лектор1 > Лектор2:", lecturer1 > lecturer2)
print("Лектор1 < Лектор2:", lecturer1 < lecturer2)
print("Лектор1 == Лектор2:", lecturer1 == lecturer2)

print("Студент1 > Студент2:", student1 > student2)
print("Студент1 < Студент2:", student1 < student2)
print("Студент1 == Студент2:", student1 == student2)

print("\n=== ТЕСТИРУЕМ ФУНКЦИИ СРЕДНИХ ОЦЕНОК ===")

# Создаем списки для функций
all_students = [student1, student2]
all_lecturers = [lecturer1, lecturer2]

# Подсчитываем средние оценки по курсам
python_avg_hw = calculate_average_hw_grade(all_students, 'Python')
java_avg_hw = calculate_average_hw_grade(all_students, 'Java')
csharp_avg_hw = calculate_average_hw