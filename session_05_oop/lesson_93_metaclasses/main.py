"""
In Python all is a OBJECT, including classes.
Metaclasses are the "classes" who create classes.
type is a metaclases
"""

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        # if name == 'A':
        if name == 'C':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_talk' not in namespace:
            print(f'You need to create the b_talk method in {name}')
        else:
            if not callable(namespace['b_talk']):
                print(f'b_talk need to be a method, not a attribute in {name}')

        if 'attr_class' in namespace:
            print(f'{name} try to overwrite attr_class attribute')
            del namespace['attr_class']

        return type.__new__(mcs, name, bases, namespace)

"""
class A(metaclass=Meta):
    def talk(self):
        self.b_talk()


class B(A):
    test = 'value'
    # b_talk = 'Wow'

    def b_talk(self):
        print('Hi')

    def another_fun(self):
        pass
"""

class C(metaclass=Meta):
    attr_class = 'Value C'


class D(C):
    attr_class = 'Value D'

class E(D):
    attr_class = 'Value E'

e = E()
print(e.attr_class)

# F is type F, don't inherit from anywhere, namespace = attr Hello world
F = type(
    'F',
    (),
    {'attr': 'Hello World!'}
)

f = F()
print(f.attr)
print(type(f))
