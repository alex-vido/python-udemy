from time import time
from time import sleep

def master(function):  # Decorator function
    def slave(*args, **kwargs):
        print("I'm decorated")
        function(*args, **kwargs)
    return slave

@master  # Decorator
def speak_hi():
    print('Hi')


# speak_hi = master(speak_hi)
speak_hi()

@master
def another_func(msg):
    print(msg)


another_func('Hello')


def speed(func):
    def intern(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        exec_time = (end_time - start_time) * 1000
        print(f'\nThe function {func.__name__} '
              f'took {exec_time:.2f}ms to be executed')
        return result
    return intern


@speed
def lazy():
    for i in range(10):
        print(i, end='')


lazy()
