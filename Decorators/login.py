def login_decorator(func):
    def wrapper(*args):
        func(args[0])
        print("Welcome!")
    return wrapper




@login_decorator
def welcome(name):
    print(f"Hi {name}", end="  ")


welcome("Zanko")


