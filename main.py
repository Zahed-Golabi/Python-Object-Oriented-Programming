class Employee:
    salary = 4000  # class variable

    def __init__(self, name, age):
        self.name = name   # object variable
        self.age = age     # object varialbe



# create object
employee1 = Employee("Zanko", 32)


# create object
employee2 = Employee("Mardin", 15)

# print object 1 address
print(employee1)
print(f"Employee 1 name: {employee1.name}, age: {employee1.age}, last: {employee1.salary}")

# print object 2 address
print(employee2)
print(f"Employee 2 name: {employee2.name}, age: {employee2.age}, last: {employee2.salary}")

print("Salary: ", Employee.salary)
Employee.salary = Employee.salary * 3   # change class variable
print("Salar: ", Employee.salary)

print(f"Employee 1 name: {employee1.name}, age: {employee1.age}, last: {employee1.salary}")

employee2.salary = 8000   # change object variable
print(employee2.salary)