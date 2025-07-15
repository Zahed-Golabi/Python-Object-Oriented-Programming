class Student:

    def __init__(self, name, grades=None):
        self.__name = name
        self.__grades = grades if grades is not None else []

        # Type check goes here
        if not isinstance(self.__grades, list):
            raise ValueError("Grades must be a list.")

    def add_grade(self, grade):
        if 0.0 <= grade <= 4.0:
            self.__grades.append(grade)
        else:
            print("Invalid grade. Must be between 0.0 and 4.0.")

    def get_average(self):
        if not self.__grades:
            return 0.0
        return round(sum(self.__grades) / len(self.__grades), 2)

    def get_name(self):
        return self.__name

    

# Creating Objects
student1 = Student("Mardin", [3, 2, 4, 4, 3])
print(student1.get_average())
print(student1.get_name())
print(student1.add_grade(5))
print(student1.add_grade(3.8))
print(student1.get_average())

# Another Object
student2 = Student("Rojhina", 3)
print(student2.get_average())
print(student2.get_name())
print(student2.add_grade(5))
print(student2.add_grade(3.8))
print(student2.get_average())
