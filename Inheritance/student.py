class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"I am {self.name}, I am {self.age} years old."
        


class Student(Person):

    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def displayStudent(self):
        return f"I am {self.name}, I am {self.age} years old. My major is {self.major}"
    



student1 = Student("Mardin", 15, "Math")
print(student1.display())
print(student1.displayStudent())
