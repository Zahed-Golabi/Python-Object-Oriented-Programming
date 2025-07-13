print(int.__add__(3, 4))   # + operator
print("1".__mul__(3))      # * operator , overloading
print("hello".__len__())


class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name
    
    
    def __add__(self, other):
        return self.age + other.age
    


emp1 = Employee("Rojhina", 15)
print(emp1)

emp2 = Employee("Mardin", 13)

print(emp1 + emp2)                # is equals to emp1.__add__(emp2)
print(emp1.__add__(emp2))         # is equlas to emp1 + emp2


