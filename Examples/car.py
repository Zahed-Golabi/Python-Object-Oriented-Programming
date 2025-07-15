class Car:
    
    def __init__(self, make, model, speed=0):
        self.__make = make
        self.__model = model
        if 0 <= speed <= 200:
            self.__speed = speed
        else:
            raise ValueError("Speed must be between 0 and 200")

    def accelerate(self, amount):
        self.__speed += amount
        if self.__speed > 200:
            self.__speed = 200
            return "Speed capped at 200."
        return f"New speed: {self.__speed}"
    
    def brake(self, amount):
        self.__speed -= amount
        if self.__speed < 0:
            self.__speed = 0
            return "Speed reduced to 0."
        return f"New speed: {self.__speed}"

    def get_speed(self):
        return self.__speed

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    

# Creating Objects
car1 = Car(2000, "Tesla", 190)
print(car1.accelerate(5))
print(car1.brake(100))
print(car1.get_speed())

# Creating Objects
car2 = Car(2010, "Tesla", 100)
print(car2.accelerate(101))      # value error
print(car2.brake(1001))            # value error
print(car2.get_speed())
      
