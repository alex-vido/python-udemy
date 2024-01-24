import math

PI = math.pi


def double_list(lst):
    return [x * 2 for x in lst]


def multiply(lst):
    r = 1
    for i in lst:
        r *= i
    return r

if __name__ == '__main__':
    lst = [12, 2, 3, 4, 48, 12]
    print(double_list(lst))
    print(multiply(lst))
    print(PI)
