class Vector2D():

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Operand must be of type Vector2D")
        if len(self.vector) != 2 or len(other.vector) != 2:
            raise ValueError("Only 2D vectors are supported.")
        first = self.vector[0] + other.vector[0]
        second = self.vector[1] + other.vector[1]
        return Vector2D([first, second])
    
    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Operand must be of type Vector2D")
        if len(self.vector) != 2 or len(other.vector) != 2:
            raise ValueError("Only 2D vectors are supported.")
        first = self.vector[0] - other.vector[0]
        second = self.vector[1] - other.vector[1]
        return Vector2D([first, second])
    

    def __mul__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Operand must be of type Vector2D")
        if len(self.vector) != 2 or len(other.vector) != 2:
            raise ValueError("Only 2D vectors are supported.")
        first = self.vector[0] * other.vector[0]
        second = self.vector[1] * other.vector[1]
        return Vector2D([first, second])
    
    def __str__(self):
        return f"{self.vector}"
    

v1 = Vector2D([2, 3])
v2 = Vector2D([2, 3])

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
