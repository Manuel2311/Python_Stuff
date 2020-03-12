import random
from time import perf_counter


def random_decorator(func):
    print(random.randint(0,100))
    def wrapper(*args):
        func(*args)

    return wrapper

@random_decorator
def say_hello():
    print("Hello!")  

say_hello=random_decorator(say_hello)

@random_decorator
def say_goodbye(name):
    print("Goodbye "+name)


say_hello()
say_goodbye("Manuel")




def timer(func):
    def wrapper(*args):
        start_time=perf_counter()
        func(*args)
        end_time=perf_counter()
        print(f"Function took {end_time - start_time}s")

    return wrapper



@timer
def quick_function():
    print("This is a quick function!")

@timer
def slow_function():
    print("This is a slow function")
    for _ in range(1000000):
        random.randint(0,100000000000)
    
slow_function=timer(slow_function)


quick_function()
slow_function()









