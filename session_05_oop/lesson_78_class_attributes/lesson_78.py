
class A:
    v = 123  # Var class

    def __init__(self):  # Instance class
        self.v = 321


a1 = A()
a2 = A()

# a1.v = 321

# print(a1.__dict__)
# print(a2.__dict__)
# print(A.__dict__)

print()

print(a1.v)
print(a2.v)
print(A.v)
