"""
In Python, the behavior of the operators is defined by special methods
Let's change the behavior of operators with classes defined by the user

Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
"""


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):  # For print the value
        return f"<class 'Rectangle({self.x}, {self.y})'>"

    def __add__(self, other):  # for sum the Rectangles
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Rectangle(new_x, new_y)

    def __lt__(self, other):  # Menor que
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):  # Maior que
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True

        return False


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = r1 + r2
print(r3)
print(r3 > r1)
print(r1 == r3)
