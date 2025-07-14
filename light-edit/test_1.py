def exponentiation(x):
    return x ** 2


def get_numbers(x):
    numbers = []
    for i in range(x):
        numbers.append(i)
    return numbers


def exp_numbers(x):
    numbers = get_numbers(x)
    for number in numbers:
        print(exponentiation(number))


exp_numbers(4)
