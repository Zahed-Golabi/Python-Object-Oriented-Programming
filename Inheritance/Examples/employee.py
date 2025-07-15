class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        return f"This is {self.name} with id {self.id}"


class Manager(Employee):

    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def display(self):
        base_info = super().display()
        return f"{base_info} at department {self.department}"

    

manager = Manager("Zanko", 234555, "IT")
print(manager.display())