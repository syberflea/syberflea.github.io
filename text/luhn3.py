def luhn(value):
    digits = list(map(int,str(value))
    oddSum = sum(digits[-1::-2])
    evnSum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (oddSum + evnSum) % 10 == 0