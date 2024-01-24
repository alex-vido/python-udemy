"""
Python don't support charge polymorphism

Polymorphism is the principle who allows that classes derived from the same superclass to have the same method
(of the same signature) but different behaviour.
Same signature = same amount e type of param
"""

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def talk(self, msg):
        pass

class B(A):
    def talk(self, msg):
        print(f'B is talking about {msg}')

class C(A):
    def talk(self, msg):
        print(f'C is talking about {msg}')

b = B()
c = C()
b.talk('coding')
c.talk('math')
