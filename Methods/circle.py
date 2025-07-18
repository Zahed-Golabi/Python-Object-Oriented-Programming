class Circle:

    def __init__(self, radius:int):
        self.radius = radius

    @property
    def diameter(self):
        if not self.radius is None:
            return 2 * self.radius
        else:
            raise ValueError("None .....")
    
    @diameter.setter
    def diameter(self, new_radius:float):
        self.radius = new_radius

    @diameter.deleter
    def diameter(self):
        self.radius = None




circle = Circle(5)
print(circle.diameter)
circle.diameter = 20
print(circle.diameter)
del circle.diameter
print(circle.diameter)