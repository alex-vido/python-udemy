"""Documentation of this module

It do nothing, but is a example for you.
Typing - https://docs.python.org/3/library/typing.html
"""
from typing import Union

x: int = 10
y: float = 10.5
z: bool = False


def func(p1: float, p2: str, p3: dict) -> float:
    return 10.10

print(func(10.1, 'str', {}))


def func_2() -> Union[list, dict]:  # Import Union for can return more than one type
    return []
