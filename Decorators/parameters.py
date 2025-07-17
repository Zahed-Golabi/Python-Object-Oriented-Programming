def decorator(like):
    print("Inside decorator...")

    def inner(func):
        print("Inside inner function....")
        print("I like ", like)

        def wrapper():
            func()

        return wrapper
    return inner


@decorator(like="CodeGene")
def my_func():
    print("Inside actual function..")


my_func()
