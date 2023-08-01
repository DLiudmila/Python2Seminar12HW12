# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
import re


class Student:
    def __init__(self, name, subjects_file):
        self._validate_name(name) # проверка ФИО на первую заглавную букву и наличие только букв
        self.name = name
        self.subjects = self._load_subjects(subjects_file) # загрузка списка предметов из файла CSV
        self.grades = {subject: [] for subject in self.subjects} # словарь для хранения оценок по предметам
        self.test_scores = {subject: [] for subject in self.subjects} # словарь для хранения результатов тестов по предметам

    def _validate_name(self, name):
        if isinstance(name, str) and re.match(r"^(?:[A-Z][a-z]* ){2}[A-Z][a-z]*$", name):
            return True
        else:
            raise ValueError("Неверный формат имени. Имя должно содержать только буквы и пробелы, и каждое слово должно начинаться с заглавной буквы.")


    def _load_subjects(self, subjects_file):
        try:
            with open(subjects_file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                subjects = [row[0] for row in reader]  # прочитать первый столбец (предметы)
                return subjects
        except FileNotFoundError:
            print("Файл с предметами не найден.")

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError("Предмет не существует.")
        if grade < 2 or grade > 5:
            print("Некорректная оценка. Оценка должна быть от 2 до 5.")
        self.grades[subject].append(grade)

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            print("Предмет не существует.")
        if score < 0 or score > 100:
            print("Некорректный результат теста. Результат теста должен быть от 0 до 100.")
        self.test_scores[subject].append(score)

    def get_average_grade(self, subject):
        if subject not in self.subjects:
            print("Предмет не существует.")
        if not self.grades[subject]:
            return None
        return sum(self.grades[subject]) / len(self.grades[subject])

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            print("Предмет не существует.")
        if not self.test_scores[subject]:
            return None
        return sum(self.test_scores[subject]) / len(self.test_scores[subject])

    def get_overall_average_grade(self):
        total_grades = [grade for subject_grades in self.grades.values() for grade in subject_grades]
        if not total_grades:
            return None
        return sum(total_grades) / len(total_grades)

    def get_overall_average_test_score(self):
        total_scores = [score for subject_scores in self.test_scores.values() for score in subject_scores]
        if not total_scores:
            return None
        return sum(total_scores) / len(total_scores)





student = Student("Ivan Ivanovich Ivanoff", "subjects.csv")

print(student.name)

student.add_grade("Математика", 4)
student.add_grade("Математика", 5)
student.add_grade("Физика", 4)
student.add_grade("Физика", 3)

student.add_test_score("Математика", 80)
student.add_test_score("Математика", 75)
student.add_test_score("Физика", 90)
student.add_test_score("Физика", 85)

print(student.get_average_grade("Математика"))  # 4.5
print(student.get_average_grade("Физика"))  # 3.5
print(student.get_average_test_score("Математика"))  # 77.5
print(student.get_average_test_score("Физика"))  # 87.5

print(student.get_overall_average_grade())  # 4.0
print(student.get_overall_average_test_score())  # 82.5