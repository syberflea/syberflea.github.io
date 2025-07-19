import time
from functools import wraps


def time_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции {func.__name__}: {execution_time} с.')
        return result

    return wrapper


def cache_args(func):
    cache = {}
    @wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
        return cache[cache_key]

    return wrapper_cache


def memoize(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


@time_check
@cache_args
def long_heavy(num):
    time.sleep(1)
    return num * 2


def wrapper_cache(*args, **kwargs):
    cache_key = args
    print(type(cache_key))


print(long_heavy(1))
# Время выполнения функции long_heavy: 1.0 с.
# 2
print(long_heavy(1))
# Время выполнения функции long_heavy: 0.0 с.
# 2
print(long_heavy(2))
# Время выполнения функции long_heavy: 1.0 с.
# 4
print(long_heavy(2))
# Время выполнения функции long_heavy: 0.0 с.
# 4
print(long_heavy(2))
# Время выполнения функции long_heavy: 0.0 с.
# 4