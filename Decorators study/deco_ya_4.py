from functools import wraps


def first_decorator(func):
    @wraps(func)
    def wrapper1():
        """Это декоратор first_decorator."""        
        print(f'Докстринг декорируемой функции: {func.__doc__}')
        print(f'Декорируется функция {func.__name__}')
        return func()        
    return wrapper1

def second_decorator(func):
    @wraps(func)
    def wrapper2():
        """Это декоратор second_decorator."""        
        print(f'Докстринг декорируемой функции: {func.__doc__}')
        print(f'Декорируется функция {func.__name__}')
        return func()        
    return wrapper2

@first_decorator
@second_decorator
def do_nothing():
    """Я ничего не знаю. Я никуда не летаю."""
    ...

do_nothing()

# Ожидаем, что будет дважды выведен один и тот же текст:
# Докстринг декорируемой функции: Я ничего не знаю. Я никуда не летаю.
# Декорируется функция do_nothing
# Докстринг декорируемой функции: Я ничего не знаю. Я никуда не летаю.
# Декорируется функция do_nothing
 
# Но это (неожиданно) не работает. 
# Будет напечатано: 
# Докстринг декорируемой функции: Это декоратор second_decorator.
# Декорируется функция wrapper2
# Докстринг декорируемой функции: Я ничего не знаю. Я никуда не летаю.
# Декорируется функция do_nothing