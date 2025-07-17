# Decorator Function
def star_decorator(func):
    def wrapper(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("=" * 10)
    return wrapper


def say_hello(name):
    print(f"Hello {name}")

@star_decorator
def say_bye(name):
    print(f"Bye {name}")

say_hello = star_decorator(say_hello)
say_hello("Zanko")
say_bye("Martian")