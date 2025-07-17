from time import time


def timer_func(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Function {func.__name__!r} executed in {(end - start):.3f}s")
        return result
    return wrapper


@timer_func
def long_time(n):
    for i in range(n):
        for j in range(n):
            i * j

    return i*j



p = long_time(5)
print(p)
