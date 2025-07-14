from math import pi, sqrt
from itertools import groupby


def foo(num: int) -> int:
    return (9, num % 9)[bool(num % 9) | (not num)]


def bar(*args):
    match len(args):
        case 1:
            res = pi * args[0] ** 2 / 4
        case 2:
            res = args[0] * args[1]
        case 3:
            a, b, c = args
            res = sqrt((a + b + c) * (a + b - c) * (a + c - b) * (b + c - a)) / 4
    return round(res, 2)


def checkio(A):
    a, b = A
    for _ in range(a):
        b = b * (b / b + 1 / b)
    return round(b)


def group_digits(digits: str) -> str:
    return "".join(str(len(list(counter))) + current for current, counter in groupby(digits))


if __name__ == '__main__':
    print(group_digits('098877665544332211'))
    for current, counter in groupby('098765432109'):
        print(f'{current=} {counter=} {list(counter)}')
