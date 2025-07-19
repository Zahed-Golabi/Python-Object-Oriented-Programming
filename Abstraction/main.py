from abc import ABC

class Vehicle(ABC):
    pass


class Mustange(Vehicle):

    def start(self):
        return "Starting..."
    

Mustange()