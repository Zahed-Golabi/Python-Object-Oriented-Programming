class Rectangle:

    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height

    @property
    def area(self):
        if self.width is None or self.height is None:
            raise ValueError("Cannot compute area. Width or Heigh is None.")
        return self.width * self.height
    
    @area.deleter
    def area(self):
        self.width = None
        self.height = None

    
    @property
    def perimeter(self):
        if self.width is None or self.height is None:
            raise ValueError("Cannot compute perimeter. Width or Heigh is None.")
        return 2 * (self.width + self.height)
    
    @perimeter.deleter
    def perimeter(self):
        self.width = None
        self.height = None

    @area.setter
    def area(self, value):
        if self.width is None or self.height is None:
            raise ValueError("Cannot set area when width or height is None.")
        ratio = self.width / self.height
        self.height = (value / ratio) ** 0.5
        self.width = ratio * self.height
    

r = Rectangle(4, 2)
print(r.area)
print(r.perimeter)

r.area = 18
print(r.width)
print(r.height)

del r.area
print(r.width)
print(r.area)