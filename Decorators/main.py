def decor(func):
    def wrapper():
        print("Before....")
        func()
        print("After....")
    return wrapper

@decor
def greetings():
    print("Hello!")


greetings()