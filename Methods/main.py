class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):              # now it is a like a property, not callable
        return f"I am {self.first_name} {self.last_name}"
    
    @full_name.setter
    def full_name(self, new_name):
        self.first_name, self.last_name = new_name.split(" ")
    
    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None



p1 = Person("Zanko", "Golabi")
print(p1.full_name)
p1.full_name = "Mardin Soling"
print(p1.full_name)
del p1.full_name
print(p1.full_name)