import random
import string


def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    confusing_chars = ('O', '0', '1', 'l')
    password = ''
    while not len(password) == length:
        char = random.choice(chars)
        if char not in confusing_chars:
            password += char
    return password
