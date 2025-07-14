def fizzbuzz(number):
    """
    Returns 'fizz' for multiples of 3, 'buzz' for multiples of 5, and 'fizz buzz' for multiples of 15.
    If the number is not a multiple of 3, 5, or 15, it returns the number itself.

    >>> fizzbuzz(3)
    'fizz'

    >>> fizzbuzz(5)
    'buzz'

    >>> fizzbuzz(15)
    'fizz buzz'

    >>> fizzbuzz(7)
    7
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number


if __name__ == "__main__":
    import doctest
    doctest.testmod()
