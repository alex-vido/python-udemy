"""
https://rszalski.github.io/magicmethods/
"""
class A:
    """
    def __new__(cls, *args, **kwargs):  # Subscribed init

        if not hasattr(cls, '_alreadyExist'):
            cls._alreadyExist = object.__new__(cls)

        return cls._alreadyExist
    """
    def __init__(self):
        print("I'm __init__")

    def __call__(self, *args, **kwds):
        result = 1

        for i in args:
            result *= i

        return result

    def __setattr__(self, name, value):
        if name == 'name':
            self.__dict__[name] = "You can't do that"
        else:
            self.__dict__[name] = value

    def __del__(self):  # Not recomended
        print('Object collected')

    def __str__(self):
        return "<Class 'A'>"

    def __len__(self):
        return 55


a = A()
print(a)
var = a(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(var)
a.name = 'Alex Vido'
print(a.name)
a.anyother = 123
print(a.anyother)
print(len(a))
