class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print("This is start engine!")

    
class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print(f"This is start engine with {self.model}")


class ElectricCar(Car):

    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        print(f"This is a {self.brand}-{self.model} with batter capacity {self.battery_capacity}")



car = ElectricCar("Tesla", 2019, 300)
car.display_info()
