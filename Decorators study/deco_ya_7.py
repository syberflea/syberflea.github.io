from functools import wraps


def cache3(func):
    cache_result = {}
    def wrapper():
        wrapper.func_call += 1
        if wrapper.func_call == 1:
            cache_result[wrapper.func_call] = func()
        elif wrapper.func_call > 3:
            cache_result.clear()
            wrapper.func_call = 1
            cache_result[wrapper.func_call] = func()
        return cache_result[1]
    wrapper.func_call = 0
    return wrapper


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1
