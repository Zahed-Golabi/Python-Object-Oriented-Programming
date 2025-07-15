class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"Woof! I am a dog and my name is {self.name}")


# objects
dog = Dog("Haski")
dog.speak()