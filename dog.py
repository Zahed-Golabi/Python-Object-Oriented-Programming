class Dog:
    quantity = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.quantity += 1

    def __str__(self):
        return f"Hi, It is {self.name}, It is {self.age}"

    

class UserInput:

    def __init__(self):
        self.user_input = str(input("Please Enter Your Name: "))

    def get_name(self):
        return self.user_input.upper()
    

# class Dog
dog1 = Dog("Haski", 3)
dog2 = Dog("Sharlie", 2)
print(Dog.quantity)


# class UserInput
userinput = UserInput()
print(userinput.get_name())
