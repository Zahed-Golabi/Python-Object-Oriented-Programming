class Employee:
    salary = 3000
    total_employee = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def raise_salary(cls, new_salary):
        if isinstance(new_salary, int):
            cls.salary = new_salary
        else:
            raise ValueError("Salary must be integer!")
        
    @classmethod                  # as constructor
    def create_from_string(cls, full_info):
        if isinstance(full_info, str):
            first_name = full_info.split("-")[0]
            last_name = full_info.split("-")[1]
            age = full_info.split("-")[2]
            return cls(first_name, last_name, age)
        else:
            raise ValueError("ful_info must be string!")
        

emp1 = Employee("Zanko", "Golabi", 32)
emp2 = Employee("Mardin", "Vafa", 13)

print("Before...")
print(emp1.full_name(), f" {emp1.salary}")
print(emp2.full_name(), f" {emp2.salary}")

print("After.....")
Employee.raise_salary(4500)
print(emp1.full_name(), f" {emp1.salary}")
print(emp2.full_name(), f" {emp2.salary}")

emp3 = Employee.create_from_string("Rojhina-Golabi-14")
print(emp3.full_name())