import random
from pprint import pprint


def foo(arr: list[str]) -> str:
    p = arr[0]
    for t in arr[1:]:
        while not t.startswith(p):
            p = p[:-1]
    return p


def bar(data: set, total: int) -> set:
    return set(sorted(data)[total:-total]) if total else data


if __name__ == '__main__':
    some_array = set([random.randint(1, 99) for _ in range(11)])
    pprint(some_array)
    sorted = bar(some_array, 5)
    pprint(sorted)

