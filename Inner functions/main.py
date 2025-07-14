'''This is a sample Python script.
 Press Shift+F10 to execute it or replace it with your code.
 Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
 See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''


def outer_func(who):
    def inner_func():
        print(f"Hello, {who}!")
    inner_func()


def increment(number):
    def inner_increment():
        return number + 1
    return inner_increment()


def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power


def generate_closure(hi):
    def inner(hoy):
        print(f"outer:{hi} inner:{hoy}")
    return inner


def has_permission(page):
    def permission(username):
        if username.lower() == "admin":
            return f"'{username}' has access to {page}."
        else:
            return f"'{username}' doesn't have access to {page}."
    return permission


def add_messages(func):
    def _add_messages():
        print("This is my first decorator")
        func()
        print("Bye!")

    return _add_messages


@add_messages
def greeting():
    print("Hello, World!")


def debug(func):
    def _debug(*args, **kwargs):
        result = func(*args, **kwargs)
        print(
            f"{func.__name__}(args: {args}, kwargs: {kwargs}) -> {result}"
        )
        return result

    return _debug


@debug
def add(a, b):
    return a + b


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def generate_power2(exponent):
    def power(func):
        def inner_power(*args):
            base = func(*args)
            return base ** exponent

        return inner_power

    return power


@generate_power2(2)
def raise_two(n):
    return n


@generate_power2(3)
def raise_three(n):
    return n


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    outer_func("PyCharm")
    print(increment(101))

    raise_two = generate_power(2)
    raise_three = generate_power(3)
    print(raise_three(2))

    greet = generate_closure("I am outer")
    greet("I am inner")

    check_admin_page_permision = has_permission("Admin Page")
    print(check_admin_page_permision("admin"))
    print(check_admin_page_permision("john"))

    greeting()

    add(9, 99)

    print(raise_three(5))
    print(raise_two(7))
    #something
