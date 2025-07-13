# Person 
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
     

# Employee, Simple Inheritance
class Employee(Person):

    salary = 4000

    def __init__(self, first_name, last_name, position):
        # self.first_name = first_name
        # self.last_name = last_name
        super().__init__(first_name, last_name)
        # Person.__init__(self, first_name, last_name)

        self.position = position

    def job(self):
        return f"I am {self.first_name} {self.last_name}, {self.position}"


 # Intern
class Intern(Employee):
    salary = 1000
    def job(self):
        return "Learning Programming"
    

# Manager
class Manager:
    def authority(self):
        return "can fire employess"


# CTO, Multiple Inheritance 
class CTO(Employee, Manager):
    salary = 5000

    def job(self):
        return f"I am {self.first_name} {self.last_name}, CTO"
    

emp1 = Employee("Zanko", "Martian", "Programmer")
print(emp1.job())
print(emp1.salary)

emp2 = CTO("Mardin", "Solin", "Data Engineer")
print(emp2.job())
print(emp2.salary)
print(emp2.authority())

emp3 = Intern("Mardin", "Solin", "Data Engineer")
print(emp3.job())
print(emp3.salary)
